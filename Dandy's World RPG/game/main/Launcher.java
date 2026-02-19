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
									"│            #######                │                                                             V0.0.2a │" + "\n" +
									"└───────────────────────────────────┴─────────────────────────────────────────────────────────────────────┘";
    public static void main(String[] args) {
        // GPU Acceleration Properties
        System.setProperty("sun.java2d.opengl", "true");
        System.setProperty("awt.useSystemAAFontSettings","on");
	    System.setProperty("swing.aatext", "true");

	    TermWindow console = new TermWindow("DWRPG - Coming Soon!", 975, 750);	// Create the window.
	    KeyHandler kh = new KeyHandler();										// Create the KeyHandler
	    console.addGameInput(kh);												// Tie the KeyHandler to the console.
	    Menu.getTerminal(console, kh);											// Allow "Menus" to interface with the console.
	    Main.getTerminal(console, kh);											// Allow the game to interface with the console.
	    MapHandler.getTerminal(console, kh);									// Allow the map to interface with the console (temporarily).
	    
	    boolean devTesting = true;
	    
	    if(!devTesting) {
	    	String[] mainOptions = {"~Continue Game", "New Game", "~Manage Saves", "~Options", "Quit Game"};
		    Menu main = new Menu(1, mainOptions);
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
