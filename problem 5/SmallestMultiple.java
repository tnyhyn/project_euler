package problem5;

public class SmallestMultiple {

	public static void main(String[] args) {

		boolean cont = false;
		int sum = 20;
		int res = 0;
		
		while(cont == false){
			
			if(sum % 2 == 0 &&
					sum % 3 == 0 &&
					sum % 4 == 0 &&
					sum % 5 == 0 &&
					sum % 6 == 0 &&
					sum % 7 == 0 &&
					sum % 8 == 0 &&
					sum % 9 == 0 &&
					sum % 10 == 0 &&
					sum % 11 == 0 &&
					sum % 12 == 0 &&
					sum % 13 == 0 &&
					sum % 14 == 0 &&
					sum % 15 == 0 &&
					sum % 16 == 0 &&
					sum % 17 == 0 &&
					sum % 18 == 0 &&
					sum % 19 == 0 &&
					sum % 20 == 0
					){
				res = sum;
				cont = true;
			}
			
			sum = sum + 1;
		
		}
		
		System.out.println(res);
		
	}

}
