package chr;

import java.util.ArrayList;

public class Toon {
	
	public static int numToonsCreated;

	private String name;
	
	private boolean isActive;
	private boolean isAlive;
	
	// Original Material's Statistics
	private int hearts;
	private int skillStars;
	private int speedStars;
	private int staminaStars;
	private int stealthStars;
	private int extractStars;
	
	// DWRPG Statistics
	private int health;
	private int maxHealth;
	private int skill;
	private int skillModifier;
	private int speed;
	private int speedModifier;
	private int stamina;
	private int staminaStatMax;	
	private int stealth;
	private int stealthModifier;
	private int strength;
	private int strengthModifier;
	
	public Toon() {
		name = "Toon";
		isActive = false;
		isAlive = false;
		hearts = 0;
		skillStars = 0;
		speedStars = 0;
		staminaStars = 0;
		stealthStars = 0;
		extractStars = 0;
		
		convertAllStats();
	}
	public Toon(String name, int hearts, int skillStars, int speedStars, int staminaStars, int stealthStars, int extractStars) {
		this.name = name;
		isActive = false;
		isAlive = false;
		this.hearts = hearts;
		this.skillStars = skillStars;
		this.speedStars = speedStars;
		this.staminaStars = staminaStars;
		this.stealthStars = stealthStars;
		this.extractStars = extractStars;
		
		convertAllStats();
	}
	public void convertAllStats() {
		health = convertHealth();
		maxHealth = convertHealth();
		skill = convertSkill();
		skillModifier = 0;
		speed = convertSpeed();
		speedModifier = 0;
		stamina = convertStamina();
		staminaStatMax = 0;
		stealth = convertStealth();
		stealthModifier = 0;
		strength = convertStrength();
		strengthModifier = 0;
	}
	public int convertHealth() {
		return hearts * 50;
	}
	public int convertSkill() {
		return skillStars * 3;
	}
	public int convertSpeed() {
		return speedStars * 2;
	}
	public int convertStamina() {
		return Math.max(25, 50 * staminaStars - 50);
	}
	public int convertStealth() {
		return stealthStars * 2;
	}
	// TODO: Figure out how strength alters combat.
	public int convertStrength() {
		return 0;
	}
}
