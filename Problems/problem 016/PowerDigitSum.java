package problem016;

import java.math.BigInteger;

public class PowerDigitSum {

	public static void main(String[] args) {

		long startTime = System.currentTimeMillis();
	
		BigInteger power, base;
		int exponent = 1000;
		int sum = 0;
		
		base = new BigInteger("2");
		power = base.pow(exponent);
		
		String powerS = power.toString();		
		String[] list = powerS.split("");
		
		for(int i = 0; i < list.length; i++){	
			int element = Integer.parseInt(list[i]);
			sum = sum + element;
		}
		
		System.out.println(sum);
		
		long endTime = System.currentTimeMillis();
		timer(startTime,endTime);
		
		/** 1366
		 *  Runtime: 0.004s
		 */
	}
	
	
	public static void timer(long start, long end){
		
		double totalTime = end - start;
		System.out.println("Runtime: " + totalTime/1000 +"s");
		
	}
}