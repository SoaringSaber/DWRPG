package map;

import java.awt.event.KeyEvent;
import java.util.ArrayList;
import java.util.List;

import terminal.KeyHandler;
import terminal.TermWindow;

public class MapHandler {
	private static TermWindow console = null;
	private static KeyHandler kh = null;
	
	private static List<List<Tile>> map = new ArrayList<>();
	
	private static int mapSizeX = 5;
	private static int mapSizeY = 5;
	
	private static int cameraPosX = 0;
	private static int cameraPosY = 0;
	
	public static void getTerminal(TermWindow c, KeyHandler k) {
		console = c;
		kh = k;
	}
	public static void devTest() {
		
		mapMaker();
		
	}
	public static void mapMaker() {
		for(int y = 0; y < mapSizeY; y++) {
			map.add(new ArrayList<>());
			for(int x = 0; x < mapSizeX; x++) {
				map.get(y).add(x, null);
			}
		}
		
		createTile(0, 0);
		createTile(1, 0);
		getTile(0, 0).setToBlock();
		
		while(true) {
			String toPrint 		= getMapLine(cameraPosX-13, cameraPosY-11, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-11, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-10, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-10, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-9, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-9, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-8, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-8, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-7, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-7, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-6, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-6, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-5, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-5, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-4, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-4, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-3, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-3, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-2, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-2, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-1, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY-1, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY, 13, "top") 		+ " ┌─┐" + getMapLine(cameraPosX+1, cameraPosY, 13, "top") + "\n"
								+ getMapLine(cameraPosX-13, cameraPosY, 13, "bottom") 	+ " └─┘" + getMapLine(cameraPosX+1, cameraPosY, 13, "bottom") + "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+1, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+1, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+2, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+2, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+3, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+3, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+4, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+4, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+5, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+5, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+6, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+6, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+7, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+7, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+8, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+8, 26, "bottom") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+9, 26, "top") 	+ "\n"
								+ getMapLine(cameraPosX-13, cameraPosY+9, 26, "bottom") 	+ "\n";
			console.println(toPrint, true);
			String input = kh.mapMakerKeys();
			if(input.equals("up")) {
				cameraPosY--;
			}
			if(input.equals("left")) {
				cameraPosX--;
			}
			if(input.equals("down")) {
				cameraPosY++;
			}
			if(input.equals("right")) {
				cameraPosX++;
			}
			// Shortcut keys for setting blocks to be _____.
			if(input.equals("air")) {
				
			}
			if(input.equals("wall")) {
				
			}
			if(input.equals("objective")) {
				
			}
			if(input.equals("interactable")) {
				
			}
			if(input.equals("trigger")) {
				
			}
			if(input.equals("forcedMachine")) {
				
			}
			if(input.equals("potentialMachine")) {
				
			}
			
			System.out.println(cameraPosX + ", " + cameraPosY);
			console.clear();
		}
	}
	
	public static void addX() {
		for(int y = 0; y < mapSizeY; y++) {
			map.get(y).add(mapSizeX - 1, null);
		}
	}
	public static void addY() {
		map.add(new ArrayList<>());
		for(int x = 0; x < mapSizeX; x++) {
			map.get(map.size() - 1).add(x, null);
		}
		mapSizeY++;
	}
	
	public static void createTile(int x, int y) {
		if(x >= 0 && x < mapSizeX && y >= 0 && y < mapSizeY) {
			Tile t = new Tile();
			map.get(y).set(x, t);
		}
	}
	
	public static Tile getTile(int x, int y) {
		return map.get(y).get(x);
	}
	
	public static String getMapLine(int x, int y, int length, String side) {
		String returning = ""; 
		for(int i = 0; i < length; i++) {
			 returning += getTileString(x + i, y, side);
		}
		return returning;
	}
	
	public static String getTileString(int x, int y) {
		if(x >= 0 && x < mapSizeX && y >= 0 && y < mapSizeY) {
			Tile tile = map.get(y).get(x);
			if(tile != null) {
				return tile.getTop() + tile.getBottom();
			} else {
				// Tile is null
				return " - - - -";
			}
		} else {
			// Tile is out of bounds
			return "\033[38;2;36;36;36m - - - -";
		}
	}
	public static String getTileString(int x, int y, String side) {
		if(x >= 0 && x < mapSizeX && y >= 0 && y < mapSizeY) {
			Tile tile =  map.get(y).get(x);
			if(tile != null) {
				if(side.equals("top")) {
					return tile.getTop();
				} else if(side.equals("bottom")) {
					return tile.getBottom();
				}
				return "err: side invalid";
			} else {
				// Tile is null
				return " - -";
			}
		} else {
			// Tile is out of bounds
			return "\033[38;2;36;36;36m - -\033[0m";
		}
	}
	
	public static void loadMap() {
		
	}
	public static void unloadMap() {
		
	}
}
