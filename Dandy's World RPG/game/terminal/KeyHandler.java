package terminal;

import java.awt.event.*;
import java.util.concurrent.LinkedBlockingQueue;

public class KeyHandler extends KeyAdapter {
	private final LinkedBlockingQueue<Integer> keyQueue = new LinkedBlockingQueue<>();
	
	private boolean canMove = true;

	@Override
    public void keyPressed(KeyEvent e) {
        keyQueue.offer(e.getKeyCode());
    }
    
	@Override
    public void keyReleased(KeyEvent e) {
    	canMove = true;
    }

    // This runs on your Main Thread
    public Integer getNextKey() {
        try {
        	return keyQueue.take();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		return 0;
    }
    
    public String menuSelect() {
		while(true) {
			Integer input = this.getNextKey(); 
			if(input == KeyEvent.VK_UP || input == KeyEvent.VK_LEFT) {
				return "up";
			}
			if(input == KeyEvent.VK_DOWN || input == KeyEvent.VK_RIGHT) {
				return "down";
			}
			if(input == KeyEvent.VK_Z || input == KeyEvent.VK_ENTER) {
				return "select";
			}
			if(input == KeyEvent.VK_X) {
				return "back";
			}
			if(input == KeyEvent.VK_C) {
				return "menu";
			}
		}
	}
    public String advancedMenuSelect() {
		while(true) {
			Integer input = this.getNextKey(); 
			if(input == KeyEvent.VK_UP) {
				return "up";
			}
			if(input == KeyEvent.VK_LEFT) {
				return "left";
			}
			if(input == KeyEvent.VK_DOWN) {
				return "down";
			}
			if(input == KeyEvent.VK_RIGHT) {
				return "right";
			}
			if(input == KeyEvent.VK_Z || input == KeyEvent.VK_ENTER) {
				return "select";
			}
			if(input == KeyEvent.VK_X) {
				return "back";
			}
			if(input == KeyEvent.VK_C) {
				return "menu";
			}
		}
	}
    public String mapMakerKeys() {
    	while(true) {
			Integer input = this.getNextKey(); 
			if(canMove) {
				if(input == KeyEvent.VK_UP) {
					canMove = false;
					return "up";
				}
				if(input == KeyEvent.VK_LEFT) {
					canMove = false;
					return "left";
				}
				if(input == KeyEvent.VK_DOWN) {
					canMove = false;
					return "down";
				}
				if(input == KeyEvent.VK_RIGHT) {
					canMove = false;
					return "right";
				}
				if(input == KeyEvent.VK_1) {
					return "air";
				}
				if(input == KeyEvent.VK_2) {
					return "wall";
				}
				if(input == KeyEvent.VK_3) {
					return "objective";
				}
				if(input == KeyEvent.VK_4) {
					return "interactable";
				}
				if(input == KeyEvent.VK_5) {
					return "trigger";
				}
				if(input == KeyEvent.VK_6) {
					return "forcedMachine";
				}
				if(input == KeyEvent.VK_7) {
					return "potentialMachine";
				}
				if(input == KeyEvent.VK_C) {
					return "traversable";
				}
				if(input == KeyEvent.VK_F1) {
					return "toggleView";		// Does nothing right now.
				}
				if(input == KeyEvent.VK_Z || input == KeyEvent.VK_ENTER) {
					return "info";
				}
			}
		}
    }
}
