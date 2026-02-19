package terminal;

import java.awt.event.*;
import java.util.concurrent.LinkedBlockingQueue;

public class KeyHandler extends KeyAdapter {
	private final LinkedBlockingQueue<Integer> keyQueue = new LinkedBlockingQueue<>();

	@Override
    public void keyPressed(KeyEvent e) {
        keyQueue.offer(e.getKeyCode());
    }
    
	@Override
    public void keyReleased(KeyEvent e) {
    	// Does nothing right now.
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
}
