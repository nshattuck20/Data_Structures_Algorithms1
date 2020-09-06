public class FizzBuzz {
//This little program is the classic fizz buzz problem. 
    public static void main (String [] args){

        int num;

        for(int i = 0; i < 100; i ++){
            if (i % 3 == 0 ){
                System.out.println(i + " : "+ " fizz");
            }
           else if (i % 5 == 0){
                System.out.println(i +" : " + " buzz");
            }
        }
    }
}
