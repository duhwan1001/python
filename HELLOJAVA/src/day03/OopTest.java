package day03;

public class OopTest {
	
	public static void main(String[] args) {
		
		/*
		 * Animal ani = new Animal();
		 * 
		 * System.out.println(ani.fullness); ani.eat(); System.out.println("eat 1ȸ : " +
		 * ani.fullness); ani.mantang(); System.out.println("mantang : " +
		 * ani.fullness);
		 */
		
		Human hum = new Human();
		
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
		hum.mantang();
		hum.goHakwon();
		System.out.println(hum.fullness);
		System.out.println(hum.flag_cook);
		
	}
	
	
}
