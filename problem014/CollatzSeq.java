package problem014;

public class CollatzSeq {

	public static void main(String[] args) {
		
		long startTime = System.currentTimeMillis();

		
		long maxTerm = 0;
		long maxNum = 0;
		
		for(long i = 2; i < 1000000; i++){
			
			long term = 1;
			long number = i;
			long numberX = i;
			
			while(number != 1){
				
				if(number%2 == 0){
					number = even(number);
				}
				else{
					number = odd(number);
				}
				term++;
			}
			if(term > maxTerm) {
				maxTerm = term;
				maxNum = numberX;
			}
		}
		
		long endTime   = System.currentTimeMillis();
		double totalTime = endTime - startTime;

		
		System.out.println(maxNum);
		System.out.println(maxTerm);
		System.out.println("Runtime: " + totalTime/1000 +"s");

	}
	
	public static long even(long i){
		
		return i/2;
	}
	
	public static long odd(long i ){
		
		return 3*i + 1;
	}

}
