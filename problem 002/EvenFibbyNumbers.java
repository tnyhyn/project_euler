package problem2;

public class EvenFibbyNumbers {

	public static void main(String[] args) {
	
		int sum = 2;
		
		int back = 1;
		int front = 2;
		int temp = 0;
		
		for(int i = 0; front < 4000000; i++){
			
			temp = back + front;
			if(temp%2 == 0){
				sum = sum + temp;
			}
					
			back = front;
			front = temp;
			
		}
		
		System.out.println(sum);
		
		
		

	}

}
