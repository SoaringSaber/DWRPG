package terminal;

// TODO: Create javadoc on this class.
public class Colors {
	
	// Original colors																// Color aliases
	public static final String white			= "`\033[38;2;255;255;255m";		public static final String shade10		= white;
	public static final String shade9			= "`\033[38;2;219;219;219m";
	public static final String lightGray		= "`\033[38;2;196;196;196m";		public static final String shade8		= lightGray;
	public static final String shade7			= "`\033[38;2;173;173;173m";
	public static final String shade6			= "`\033[38;2;150;150;150m";
	public static final String gray				= "`\033[38;2;128;128;128m";		public static final String shade5		= gray;
	public static final String shade4			= "`\033[38;2;105;105;105m";
	public static final String shade3			= "`\033[38;2;82;82;82m";
	public static final String darkGray			= "`\033[38;2;59;59;59m"; 			public static final String shade2		= darkGray;
	public static final String shade1			= "`\033[38;2;36;36;36m";
	public static final String black			= "`\033[38;2;0;0;0m";				public static final String shade0		= black;



	public static final String darkRed			= "`\033[38;2;163;0;0m";
	public static final String red				= "`\033[38;2;255;0;0m";
	public static final String lightRed			= "`\033[38;2;255;92;92m";

	public static final String darkOrange		= "`\033[38;2;117;76;0m";
	public static final String dullOrange		= "`\033[38;2;150;75;0m";			public static final String brown		= dullOrange;
    public static final String orange			= "`\033[38;2;255;165;0m";
    public static final String vibrantOrange	= "`\033[38;2;255;102;0m";
    public static final String lightOrange		= "`\033[38;2;255;214;138m";

    public static final String darkYellow		= "`\033[38;2;117;117;0m";
    public static final String yellow			= "`\033[38;2;255;255;0m";
    public static final String lightYellow		= "`\033[38;2;255;255;138m";

    public static final String darkGreen		= "`\033[38;2;0;117;0m";
    public static final String green			= "`\033[38;2;0;255;0m";
    public static final String lightGreen		= "`\033[38;2;138;255;138m";		public static final String mint			= lightGreen;

    public static final String darkBlue			= "`\033[38;2;0;0;117m";
    public static final String teal				= "`\033[38;2;0;128;128m";			public static final String dullBlue		= teal;
    public static final String blue				= "`\033[38;2;0;0;255m";
    public static final String cyan				= "`\033[38;2;0;255;255m";			public static final String vibrantBlue	= cyan;
    public static final String lightBlue		= "`\033[38;2;138;138;235m";
    public static final String lightCyan		= "`\033[38;2;138;255;255m";

    public static final String darkPurple		= "`\033[38;2;117;0;117m";
    public static final String dullPurple		= "`\033[38;2;209;0;209m";
    public static final String purple			= "`\033[38;2;255;46;255m";
    public static final String vibrantPink		= "`\033[38;2;255;78;137m";
    public static final String lightPurple		= "`\033[38;2;255;138;255m";		public static final String pink			= lightPurple;
    public static final String lightPink		= "`\033[38;2;255;209;220m";
    
    
    
    public static final String bg_white			= "`\033[48;2;255;255;255m";		public static final String bg_shade10	= bg_white;
	public static final String bg_shade9		= "`\033[48;2;219;219;219m";
	public static final String bg_lightGray		= "`\033[48;2;196;196;196m";		public static final String bg_shade8	= bg_lightGray;
	public static final String bg_shade7		= "`\033[48;2;173;173;173m";
	public static final String bg_shade6		= "`\033[48;2;150;150;150m";
	public static final String bg_gray			= "`\033[48;2;128;128;128m";		public static final String bg_shade5	= bg_gray;
	public static final String bg_shade4		= "`\033[48;2;105;105;105m";
	public static final String bg_shade3		= "`\033[48;2;82;82;82m";
	public static final String bg_darkGray		= "`\033[48;2;59;59;59m"; 			public static final String bg_shade2	= bg_darkGray;
	public static final String bg_shade1		= "`\033[48;2;36;36;36m";
	public static final String bg_black			= "`\033[48;2;0;0;0m";				public static final String bg_shade0	= bg_black;



	public static final String bg_darkRed		= "`\033[48;2;163;0;0m";
	public static final String bg_red			= "`\033[48;2;255;0;0m";
	public static final String bg_lightRed		= "`\033[48;2;255;92;92m";

	public static final String bg_darkOrange	= "`\033[48;2;117;76;0m";
	public static final String bg_dullOrange	= "`\033[48;2;150;75;0m";			public static final String bg_brown		= bg_dullOrange;
    public static final String bg_orange		= "`\033[48;2;255;165;0m";
    public static final String bg_vibrantOrange	= "`\033[48;2;255;102;0m";
    public static final String bg_lightOrange	= "`\033[48;2;255;214;138m";

    public static final String bg_darkYellow	= "`\033[48;2;117;117;0m";
    public static final String bg_yellow		= "`\033[48;2;255;255;0m";
    public static final String bg_lightYellow	= "`\033[48;2;255;255;138m";

    public static final String bg_darkGreen		= "`\033[48;2;0;117;0m";
    public static final String bg_green			= "`\033[48;2;0;255;0m";
    public static final String bg_lightGreen	= "`\033[48;2;138;255;138m";		public static final String bg_mint		= bg_lightGreen;

    public static final String bg_darkBlue		= "`\033[48;2;0;0;117m";
    public static final String bg_teal			= "`\033[48;2;0;128;128m";			public static final String bg_dullBlue	= bg_teal;
    public static final String bg_blue			= "`\033[48;2;0;0;255m";
    public static final String bg_cyan			= "`\033[48;2;0;255;255m";			public static final String bg_vibrantBlue=bg_cyan;
    public static final String bg_lightBlue		= "`\033[48;2;138;138;235m";
    public static final String bg_lightCyan		= "`\033[48;2;138;255;255m";

    public static final String bg_darkPurple	= "`\033[48;2;117;0;117m";
    public static final String bg_dullPurple	= "`\033[48;2;209;0;209m";
    public static final String bg_purple		= "`\033[48;2;255;46;255m";
    public static final String bg_vibrantPink	= "`\033[48;2;255;78;137m";
    public static final String bg_lightPurple	= "`\033[48;2;255;138;255m";		public static final String bg_pink		= bg_lightPurple;
    public static final String bg_lightPink		= "`\033[48;2;255;209;220m";
    
    public static final String bold				= "`\033[1m";
    public static final String unbold			= "`\033[22m";
    public static final String italic			= "`\033[3m";
    public static final String unitalic			= "`\033[23m";
	// public static final String ul			= "`\033[4m";
	public static final String inverse			= "`\033[7m";
	public static final String uninverse		= "`\033[27m";
	public static final String reset			= "`\033[0m";
	
    public static String noBT(String color) {
		return color.substring(1);
	}
	
    public static void printColors(TermWindow terminal) {
    	terminal.typeln(shade0		+ "Black / Shade 0" + reset);
    	terminal.typeln(shade1		+ "Shade 1" + reset);
    	terminal.typeln(shade2		+ "Dark Gray / Shade 2" + reset);
    	terminal.typeln(shade3		+ "Shade 3" + reset);
    	terminal.typeln(shade4		+ "Shade 4" + reset);
    	terminal.typeln(shade5		+ "Gray / Shade 5" + reset);
    	terminal.typeln(shade6		+ "Shade 6" + reset);
    	terminal.typeln(shade7		+ "Shade 7" + reset);
    	terminal.typeln(shade8		+ "Light Gray / Shade 8" + reset);
    	terminal.typeln(shade9		+ "Shade 9" + reset);
    	terminal.typeln(shade10		+ "White / Shade 10" + reset);
    	terminal.println("");
    	terminal.typeln(darkRed 	+ "Dark Red" + reset);
    	terminal.typeln(red 		+ "Red" + reset);
    	terminal.typeln(lightRed 	+ "Light Red" + reset);
    	terminal.println("");
    	terminal.typeln(darkOrange	+ "Dark Orange" + reset);
    	terminal.typeln(dullOrange	+ "Dull Orange / Brown" + reset);
    	terminal.typeln(orange 		+ "Orange" + reset);
    	terminal.typeln(vibrantOrange+"Vibrant Orange" + reset);
    	terminal.typeln(lightOrange	+ "Light Orange" + reset);
    	terminal.println("");
    	terminal.typeln(darkYellow	+ "Dark Yellow" + reset);
    	terminal.typeln(yellow 		+ "Yellow" + reset);
    	terminal.typeln(lightYellow	+ "Light Yellow" + reset);
    	terminal.println("");
    	terminal.typeln(darkGreen	+ "Dark Green" + reset);
    	terminal.typeln(green 		+ "Green" + reset);
    	terminal.typeln(lightGreen	+ "Light Green / Mint" + reset);
    	terminal.println("");
    	terminal.typeln(darkBlue 	+ "Dark Blue" + reset);
    	terminal.typeln(teal	 	+ "Teal / Dull Blue" + reset);
    	terminal.typeln(blue 		+ "Blue" + reset);
    	terminal.typeln(cyan	 	+ "Cyan / Vibrant Blue" + reset);
    	terminal.typeln(lightBlue 	+ "Light Blue" + reset);
    	terminal.typeln(lightCyan 	+ "Light Cyan" + reset);
    	terminal.println("");
    	terminal.typeln(darkPurple	+ "Dark Purple" + reset);
    	terminal.typeln(dullPurple	+ "Dull Purple" + reset);
    	terminal.typeln(purple 		+ "Purple" + reset);
    	terminal.typeln(vibrantPink + "Vibrant Pink" + reset);
    	terminal.typeln(lightPurple + "Light Purple / Pink" + reset);
    	terminal.typeln(lightPink	+ "Light Pink" + reset);
    	terminal.println();
    	terminal.println();
    	terminal.println();
    	terminal.typeln(bg_shade0		+ "Black / Shade 0" + reset);
    	terminal.typeln(bg_shade1		+ "Shade 1" + reset);
    	terminal.typeln(bg_shade2		+ "Dark Gray / Shade 2" + reset);
    	terminal.typeln(bg_shade3		+ "Shade 3" + reset);
    	terminal.typeln(bg_shade4		+ "Shade 4" + reset);
    	terminal.typeln(bg_shade5		+ "Gray / Shade 5" + reset);
    	terminal.typeln(bg_shade6		+ "Shade 6" + reset);
    	terminal.typeln(bg_shade7		+ "Shade 7" + reset);
    	terminal.typeln(bg_shade8		+ "Light Gray / Shade 8" + reset);
    	terminal.typeln(bg_shade9		+ "Shade 9" + reset);
    	terminal.typeln(bg_shade10		+ "White / Shade 10" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkRed 		+ "Dark Red" + reset);
    	terminal.typeln(bg_red 			+ "Red" + reset);
    	terminal.typeln(bg_lightRed 	+ "Light Red" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkOrange	+ "Dark Orange" + reset);
    	terminal.typeln(bg_dullOrange	+ "Dull Orange / Brown" + reset);
    	terminal.typeln(bg_orange 		+ "Orange" + reset);
    	terminal.typeln(bg_vibrantOrange+ "Vibrant Orange" + reset);
    	terminal.typeln(bg_lightOrange	+ "Light Orange" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkYellow	+ "Dark Yellow" + reset);
    	terminal.typeln(bg_yellow 		+ "Yellow" + reset);
    	terminal.typeln(bg_lightYellow	+ "Light Yellow" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkGreen	+ "Dark Green" + reset);
    	terminal.typeln(bg_green 		+ "Green" + reset);
    	terminal.typeln(bg_lightGreen	+ "Light Green / Mint" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkBlue 	+ "Dark Blue" + reset);
    	terminal.typeln(bg_teal	 		+ "Teal / Dull Blue" + reset);
    	terminal.typeln(bg_blue 		+ "Blue" + reset);
    	terminal.typeln(bg_cyan	 		+ "Cyan / Vibrant Blue" + reset);
    	terminal.typeln(bg_lightBlue 	+ "Light Blue" + reset);
    	terminal.typeln(bg_lightCyan 	+ "Light Cyan" + reset);
    	terminal.println("");
    	terminal.typeln(bg_darkPurple	+ "Dark Purple" + reset);
    	terminal.typeln(bg_dullPurple	+ "Dull Purple" + reset);
    	terminal.typeln(bg_purple 		+ "Purple" + reset);
    	terminal.typeln(bg_vibrantPink	+ "Vibrant Pink" + reset);
    	terminal.typeln(bg_lightPurple	+ "Light Purple / Pink" + reset);
    	terminal.typeln(bg_lightPink	+ "Light Pink" + reset);
    	terminal.println();
    	terminal.println();
    	terminal.println();
    	terminal.typeln("Normal Text");
    	terminal.typeln(bold			+ "Bolded Text" + reset);
    	terminal.typeln(italic			+ "Italicized Text" + reset);
    	terminal.typeln(inverse			+ "Inversed Text" + reset);
    }
}
