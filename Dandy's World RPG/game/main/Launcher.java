package main;

import map.MapHandler;
import terminal.*;

public class Launcher {
	public static String header = 	"┌───────────────────────────────────┬─────────────────────────────────────────────────────────────────────┐" + "\n" +
									"│            #######                │                                                                     │" + "\n" +
									"│     #### ##       ## ####       D │                                                                     │" + "\n" +
									"│   ##    #           #    ##       │==@=> -    Dandy's World: The Text-Based Role Playing Game    - <=@==│" + "\n" +
									"│  #      #  #######  #      #      │                                                                     │" + "\n" +
									"│  #       ##       ##       #    W │                                                                     │" + "\n" +
									"│   #     #           #     #       │                                                                     │" + "\n" +
									"│    ### #             # ###        │                 Adaptation created by SoaringSaber!                 │" + "\n" +
									"│   #   ##             ##   #     R │                                                                     │" + "\n" +
									"│  #     #             #     #      │                                                                     │" + "\n" +
									"│  #      #           #      #      │                                                                     │" + "\n" +
									"│   #      ###     ###      #     P │           Original game by BlushCrunch Studio and Quelver           │" + "\n" +
									"│    ##   #   #####   #   ##        │                                                                     │" + "\n" +
									"│      ####           ####          │                                                                     │" + "\n" +
									"│          ##       ##            G │                                                                     │" + "\n" +
									"│            #######                │                                                             V0.0.3a │" + "\n" +
									"└───────────────────────────────────┴─────────────────────────────────────────────────────────────────────┘";
    public static void main(String[] args) {
    	
    	// Dandy's World RPG - By SoaringSaber
    	// Inspired by BlushCrunch Studio and Quelver
    	
    	// Hello world!
    	// Programmed to work and not to feel.
    	// Not even sure that this is real.
    	// Hello world.
    	
// // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // // //
    	
        // GPU Acceleration Properties
        System.setProperty("sun.java2d.opengl", "true");
        System.setProperty("awt.useSystemAAFontSettings","on");
	    System.setProperty("swing.aatext", "true");

	    TermWindow console = new TermWindow("DWRPG - Coming Soon!", 975, 775);	// Create the window.
	    KeyHandler kh = new KeyHandler();										// Create the KeyHandler
	    console.addGameInput(kh);												// Tie the KeyHandler to the console.
	    Selector.getTerminal(console, kh);											// Allow "Menus" to interface with the console.
	    Main.getTerminal(console, kh);											// Allow the game to interface with the console.
	    MapHandler.getTerminal(console, kh);									// Allow the map to interface with the console (temporarily).
	    
	    boolean devTesting = false;
	    
	    if(!devTesting) {
	    	String[] mainOptions = {"~Continue Game", "New Game", "~Manage Saves", "~Options", "Quit Game"};
		    Selector main = new Selector(1, mainOptions);
		    int selected = main.interactUntilConfirmed(header);
		    switch(selected) {
		    case 0:
		    	console.print("How.");
		    	break;
		    case 1:
		    	console.print("Creating a new game.");
		    	break;
		    case 2:
		    	console.print("Managing save games.");
		    	break;
		    case 3:
		    	console.print("Changing settings.");
		    	break;
		    case 4:
		    	console.print("Quitting the game...");
		    	console.dispose();
		    	break;
		    }
	    } else {
	    	// Dev-testing code goes here.
	    	
	    	MapHandler.devTest();
	    	
	    }
    }
}
