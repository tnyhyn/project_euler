package problem7;

public class Prime10001st {

public static void main(String[] args){

	primer(10001);
	
	}

	public static long primer(long i){
		
		boolean yep = true;
		long counter = 1;
		long number = 1;
		
		while(yep == true){
			
			if(counter == i) yep = false;	
			number = number + 2;	
			if(isPrime(number) == true){
				counter++;
			}		
		}
		System.out.println(number);
		return number;
	}
	
	
	public static boolean isPrime(long n) {
	    for(long i=2;2*i<n;i++) {
	        if(n%i==0)
	            return false;
	    }
	    return true;
	}
	
	
}
