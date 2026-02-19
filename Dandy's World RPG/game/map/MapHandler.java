package map;

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
		System.out.println(" - Help Guide for Mapmaking -");
		for(int y = 0; y < mapSizeY; y++) {
			map.add(new ArrayList<>());
			for(int x = 0; x < mapSizeX; x++) {
				map.get(y).add(x, null);
			}
		}
		
		while(true) {
			String toPrint 		= getTileString(cameraPosX, cameraPosY, "top") 	+ "\n"
								+ getTileString(cameraPosX, cameraPosY, "bottom")	+ "\n";
			console.print(toPrint);
			createTile(0, 0);
			getTile(0, 0).setToBlock();
			kh.getNextKey();
			console.println("!");
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
	
	public static String getTileString(int x, int y) {
		if(x >= 0 && x < mapSizeX && y >= 0 && y < mapSizeY) {
			Tile tile = map.get(y).get(x);
			if(tile != null) {
				return tile.getTop() + tile.getBottom();
			} else {
				return " - - - -";
			}
		} else {
			return " - - - -";
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
				return " - -";
			}
		} else {
			return " - -";
		}
	}
	
	public static void loadMap() {
		
	}
	public static void unloadMap() {
		
	}
}
