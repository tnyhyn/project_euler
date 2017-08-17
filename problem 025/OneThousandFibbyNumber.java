package problem25;

import java.math.BigInteger;

public class OneThousandFibbyNumber {

	public static void main(String[] args) {

		int index = 3;
		BigInteger sum = new BigInteger("2");
		BigInteger back = new BigInteger("1");
		BigInteger front = new BigInteger("1");
		BigInteger temp = new BigInteger("2");

		int digitContain = 0;

		while(digitContain < 1000){
			
			index = index + 1;
			temp = sum;
			sum = sum.add(front);
			back = front;
			front = temp;

			digitContain = sum.toString().length();
	
		}
		System.out.println(index);
	}
}
