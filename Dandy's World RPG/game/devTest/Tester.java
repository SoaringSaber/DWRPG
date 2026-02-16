package devTest;

import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

import terminal.*;

public class Tester {

	public static void main(String[] args) {
		
		// Enable Hardware Acceleration
	    System.setProperty("sun.java2d.opengl", "true");
	    
	    // Smooth text rendering
	    System.setProperty("awt.useSystemAAFontSettings","on");
	    System.setProperty("swing.aatext", "true");
		TermWindow console = new TermWindow("DWRPG - Coming Soon!", 975, 750);
		
		testCustomTerminalFormatting(console);
		testCustomTerminalText(console);
		console.wait(5);
		console.notify("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 5000);
		
//		console.println("hello world, i am in coding purgatory");
//		console.println("this is totally not a cry for help...");
//		console.println(Colors.red + "...yep! Not a cry for help!");
//		console.println("");
//		console.println(" | # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # |");
	}
	
	@SuppressWarnings("static-access")
	public static void testCustomTerminalFormatting(TermWindow console) {
		Colors.printColors(console);
		console.wait(3);		
		console.setBackground(255, 255, 255);
		console.reset();
		console.wait(1);
		console.setBackground(255, 0, 0);
		console.reset();
		console.wait(1);
		console.setBackground(0, 255, 0);
		console.reset();
		console.wait(1);
		console.setBackground(0, 0, 255);
		console.reset();
		console.wait(3);
		console.setBackground(20, 20, 20);
		console.reset();
		console.notify("Test complete.", 5000);
	}
	
	static String header = 	"/ - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - \\" + "\n" +
							"|            #######                |                                                                     |" + "\n" +
							"|     #### ##       ## ####       D |==@=> -    Dandy's World: The Text-Based Role Playing Game    - <=@==|" + "\n" +
							"|   ##    #           #    ##       |                                                                     |" + "\n" +
							"|  #      #  #######  #      #      |                                                                     |" + "\n" +
							"|  #       ##       ##       #    W |                                                                     |" + "\n" +
							"|   #     #           #     #       |                                                                     |" + "\n" +
							"|    ### #             # ###        |                 Adaptation created by SoaringSaber!                 |" + "\n" +
							"|   #   ##             ##   #     R |                                                                     |" + "\n" +
							"|  #     #             #     #      |                                                                     |" + "\n" +
							"|  #      #           #      #      |                                                                     |" + "\n" +
							"|   #      ###     ###      #     P |           Original game by BlushCrunch Studio and Quelver           |" + "\n" +
							"|    ##   #   #####   #   ##        |                                                                     |" + "\n" +
							"|      ####           ####          |                                                                     |" + "\n" +
							"|          ##       ##            G |                                                                     |" + "\n" +
							"|            #######                |                                                                     |" + "\n" +
							"| - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - > < - |";
	
	public static void testCustomTerminalText(TermWindow console) {
		console.println(header);
		console.notify("Test complete.", 5000);
	}
	
	public static void testSelection() {
		System.out.println("Selection test:");
		boolean selecting = true;
		while(selecting) {
			
		}
	}
	
}
