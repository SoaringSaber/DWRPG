package map;

public class Tile {
	private boolean isTraversable;
	private String plotType;
	// List of plot types:
	// "wall"			- Self explanatory.
	// "floor"			- Self explanatory.
	// "objective"		- The "quest marker" that the player must reach.
	// "machine"		- A machine (forced). No top/bottom Strings need to be assigned.
	// "pMachine"		- A machine marker, however, it is recommended to assign top/bottom Strings.
	// "interactable"	- Something the player can interact with.
	// "trigger"		- When walked over, trigger "actionOnInteract".
	
	private String top;
	private String bottom;
	// Identifiers for each type of plot:
	// # - Wall
	// _ - Floor (will be invisible when rendering through getTop/getBottom)
	// $ - Decoration (identifying only)
	// % - Counter/Window (identifying only)
	// Any other String value will be displayed as-is on the map.
	// Also, having a wall doesn't determine if the plot can be passed through. This is "isTraversable"'s job.
	
	private String defaultFloorColor;
	private String defaultWallColor;
	
	private int machineTurns;
	
	private int actionOnInteract;
	
	public Tile() {
		isTraversable = true;
		plotType = "floor";
		
		top		= "____";
		bottom	= "____";
		
		defaultFloorColor = "";
		defaultWallColor = "";
		
		machineTurns = 0;
		
		actionOnInteract = -1;
	}
	
	public Tile(boolean isTraversable, String plotType, String topString, String bottomString) {
		this.isTraversable = isTraversable;
		this.plotType = plotType;
		
		top		= "____";
		bottom	= "____";
		
		defaultFloorColor = "";
		defaultWallColor = "";
		
		machineTurns = 0;
		
		actionOnInteract = -1;
	}
	
	public void setString(String str) {
		if(str.length() == 4) {
			this.top = str.substring(0, 2);
			this.bottom = str.substring(2, 4);
		} else if(str.length() == 6) {
			this.top = str.substring(0, 3);
			this.bottom = str.substring(3, 6);
		} else if(str.length() == 8) {
					this.top = str.substring(0, 4);
					this.bottom = str.substring(4, 8);
		} else {
			System.out.println("Error: Cannot set a string value with an argument other than a String with a length of 4, 6, or 8 characters.");
		}
	}
	
	public String getTop() {
		if(top.length() == 2) {
			return " " + parseAir(top.substring(0, 1)) + " " + parseAir(top.substring(1, 2));
		} else if(top.length() == 3) {
			return " " + parseAir(top);
		} else if(top.length() == 4) {
			return parseAir(top);
		}
		return "No";
	}
	
	public String getBottom() {
		if(bottom.length() == 2) {
			return " " + parseAir(bottom.substring(0, 1)) + " " + parseAir(bottom.substring(1, 2));
		} else if(bottom.length() == 3) {
			return " " + parseAir(bottom);
		} else if(bottom.length() == 4) {
			return parseAir(bottom);
		}
		return "No";
	}
	
	private String parseAir(String str) {
		String parsedString = "";
		for(int i = 0; i < str.length(); i++) {
			String toParse = str.substring(i, i+1);
			if(toParse.equals("_")) {
				parsedString += " ";
			} else {
				parsedString += toParse;
			}
		}
		return parsedString;
	}
	
	public void setToAir() {
		
	}
	
	public void setToBlock() {
		this.setString("####");
	}
	
}
