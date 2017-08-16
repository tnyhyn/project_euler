package problem6;

public class SumSquareDifference {

	public static void main(String[] args){
		
		int sumofsquare = 0;
		int squareofsum = 0;
		int result;
		
		for(int i = 0; i < 101; i++){
			
			sumofsquare += i*i;
			squareofsum += i;
			
		}
		
		squareofsum = squareofsum * squareofsum;
		
		result = squareofsum - sumofsquare;
		
		System.out.println(result);
		
		
	}
	
	
}
