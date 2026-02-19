package terminal;

public class Menu {
	private static TermWindow console = null;
	private static KeyHandler kh = null;
	public static void getTerminal(TermWindow c, KeyHandler k) {
		console = c;
		kh = k;
	}
	
	// private final int menuType;
	// 0/1 - Simple
	// 2   - Advanced
	// 3   - Battle
	
	// The list that the user selects from.
	private String[] options;
	
	// What is currently selected in the menu.
	// Cannot be below 0 or above the size of options.
	private int selected;
	private boolean confirmed;
	
	public Menu() {
		// menuType = 1;
		String[] error = {"Error! Default menu options!"};
		options = error;
		selected = 0;
		confirmed = false;
	}
	public Menu(int menuType, String[] options) {
		// this.menuType = menuType;
		this.options = options;
		
		selected = 0;
		confirmed = false;
	}
	
	public String getOption(int option) {
			if(options[option].startsWith("~") && option == selected) {
				return " ► " + options[option].substring(1);
			} else if(options[option].startsWith("~")) {
				return "   " + options[option].substring(1);
			}
			if(option == selected) {
				return " ► " + options[option];
			} else{
				return "   " + options[option];
			}
	}
	public String toString() {
		String toReturn = "";
		for(int i = 0; i < options.length; i++) {
			toReturn += getOption(i) + "\n";
		}
		return toReturn;
	}
	public int getSelected() {
		return selected;
	}
	public boolean getConfirmed() {
		return confirmed;
	}
	
	public void interactWith() {
		boolean validInput = false;
		while(!validInput) {
			// Get key input
			String option = kh.menuSelect();
			if(option == "up") {
				if(!(selected - 1 < 0)) {
					selected--;
					validInput = true;
				}
			}
			if(option == "down") {
				if(!(selected + 1 > options.length - 1)) {
					selected++;
					validInput = true;
				}
			}
			if(option == "select" && !(options[selected].startsWith("~"))) {
				confirmed = true;
				validInput = true;
			} else if(option == "select" && options[selected].startsWith("~")) {
				console.alert("This option isn't available.", 2000);
			}
		}
	}
	
	public int interactUntilConfirmed() {
		while(!this.getConfirmed()) {
			String printBuffer = "";
			// printBuffer = header + "\n";
			printBuffer += this.toString();
			console.clear();
			console.println(printBuffer);
			this.interactWith();
		}
		return selected;
	}
	public int interactUntilConfirmed(String header) {
		while(!this.getConfirmed()) {
			String printBuffer = header + "\n";
			// printBuffer = header + "\n";
			printBuffer += this.toString();
			console.clear();
			console.println(printBuffer);
			this.interactWith();
		}
		return selected;
	}
}
