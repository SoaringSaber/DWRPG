package terminal;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Insets;
import java.awt.event.KeyListener;
import java.awt.event.MouseWheelListener;
import java.net.URL;

import javax.swing.BorderFactory;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JLayeredPane;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JScrollPane;
import javax.swing.JTextPane;
import javax.swing.ScrollPaneConstants;
import javax.swing.SwingConstants;
import javax.swing.Timer;
import javax.swing.text.BadLocationException;
import javax.swing.text.Style;
import javax.swing.text.StyleConstants;
import javax.swing.text.StyledDocument;

import main.SettingHandler;

// TODO: Create javadoc for class.
public class TermWindow extends JFrame {
	private static final long serialVersionUID = -8334368252504536164L;	// I don't know why I need this, but whatever.
	
	private JTextPane display;
	
	private JPanel notifyPanel;
	private JLabel notifyLabel;
	private Timer notifyTimer;
	private JProgressBar notifyProgress;
	private long notifyStartTime;
	private int currentNotifyWidth = 250; // Track width for repositioning
	
	private int bg_r = 20, bg_g = 20, bg_b = 20;
	
	private Color currentAnsiFg = Color.WHITE;
	private Color currentAnsiBg = new Color(bg_r, bg_g, bg_b);
	private boolean isBold = false, isItalic = false, isInverse = false;

	
	public TermWindow(String title, int width, int height) {
        setTitle(title);
        setSize(width, height);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setLocationRelativeTo(null);
        setFocusable(true);
        
        try {
        	URL iconURL = getClass().getResource("/assets/game-icon.png");
            if (iconURL != null) {
                ImageIcon icon = new ImageIcon(iconURL);
                setIconImage(icon.getImage());
            }
        } catch (Exception e) {
            System.out.println("Icon not found, using default.");
        }
        
        // // Psuedo-Terminal properties
        display = new JTextPane();									// Text goes here.
        display.setBackground(new Color(bg_r, bg_g, bg_b));			// The background of the text box.
        display.setEditable(false);									// Is the textbox editable? HECK NO!
        display.setFocusable(false);								// Is the textbox focusable? Nah, don't need it to be.
        display.setFont(new Font("Monospaced", Font.PLAIN, 15));	// The font of the text in the box.
        display.setMargin(new Insets(0, 0, 0, 0));					// The space between the window border and box.
        
        // // Border and scroll pane removal
        JScrollPane scrollPane = new JScrollPane(display);											// Lets us edit the scrolling stuffs and stuff.
        scrollPane.setBorder(BorderFactory.createEmptyBorder());									// Removes border.
        scrollPane.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_NEVER);		// Removes scroll bar.
        scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);	// Removes scroll bar.
        for (MouseWheelListener mwl : scrollPane.getMouseWheelListeners()) {						// Removes mouse scroll wheel function.
            scrollPane.removeMouseWheelListener(mwl);
        }
        
        add(scrollPane);																			// Adds the psuedo-console to the window.

        // // Notifications
        // The panel
        notifyPanel = new JPanel(new BorderLayout());
        notifyPanel.setBackground(new Color(30, 30, 30, 230));
        notifyPanel.setBorder(BorderFactory.createLineBorder(Color.CYAN, 1));
        notifyPanel.setVisible(false);
        // The panel text
        notifyLabel = new JLabel("", SwingConstants.CENTER);
        notifyLabel.setForeground(Color.CYAN);
        notifyLabel.setBorder(BorderFactory.createEmptyBorder(10, 15, 10, 15));
        // The progress bar
        notifyProgress = new JProgressBar(0, 100);
        notifyProgress.setPreferredSize(new Dimension(0, 4));
        notifyProgress.setBackground(new Color(50, 50, 50));
        notifyProgress.setForeground(Color.CYAN);
        notifyProgress.setBorderPainted(false);
        // Layering and positions
        notifyPanel.add(notifyLabel, BorderLayout.CENTER);
        notifyPanel.add(notifyProgress, BorderLayout.SOUTH);
        getLayeredPane().add(notifyPanel, JLayeredPane.POPUP_LAYER);

        // Reposition logic (Handles window resizing)
        this.addComponentListener(new java.awt.event.ComponentAdapter() {
            public void componentResized(java.awt.event.ComponentEvent e) {
                updateNotifyBounds();
            }
        });

        setVisible(true);
        toFront();
    }
	
	// TODO: Create javadoc for keylistener.
	// This allows your Game class to pass its own KeyListener
    public void addGameInput(KeyListener listener) {
        this.addKeyListener(listener);
    }
	
	// TODO: Create javadoc for wait methods.
	public void wait(int seconds) {
		try {
			Thread.sleep(seconds * 1000);
		} catch (InterruptedException e) {
			System.out.println("..!");
		}
	}
	public void wait(double seconds) {
		try {
			Thread.sleep((int)(seconds * 1000));
		} catch (InterruptedException e) {
			System.out.println("..!");
		}
	}
	
// Printing methods
// TODO: Create javadoc for printing methods
//
	public void print(String text) {
        parseAndAppend(text);
    }
	public void print(int number) {
        parseAndAppend(number + "");
    }
	public void print(double number) {
        parseAndAppend(number + "");
    }
	public void println() {
        appendText("\n");
    }
	public void println(String text) {
        parseAndAppend(text);
        appendText("\n");
    }
	public void println(String text, boolean moveWindow) {
        parseAndAppend(text);
        appendTextStaticPosition("\n");
    }
	public void println(int number) {
        parseAndAppend(number + "");
        appendText("\n");
    }
	public void println(double number) {
        parseAndAppend(number + "");
        appendText("\n");
    }
	public void type(String text) {
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
		} else {
			this.print(text);
		}
	}
	public void type(int number) {
		String text = number + "";
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
		} else {
			this.print(text);
		}
	}
	public void type(double number) {
		String text = number + "";
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
		} else {
			this.print(text);
		}
	}
	public void typeln(String text) {
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
			this.println("");
		} else {
			this.println(text);
		}
	}
	public void typeln(int number) {
		String text = number + "";
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
			this.println("");
		} else {
			this.println(text);
		}
	}
	public void typeln(double number) {
		String text = number + "";
		if(SettingHandler.typeOut) {
			boolean coloring = false;
			String getColor = null;
			for(int i = 0; i < text.length(); i++) {
				String s = String.valueOf(text.charAt(i));
				if(s.equals("`") || coloring) {
					coloring = true;
					if(s.equals("`")) {
						getColor = "";
					} else {
						getColor += s;
					}
	                if(s.equals("m")) {
	                	coloring = false;
	                	this.print(getColor);
	                	getColor = null;
	                }
				} else {
					if(s.equals(".") || s.equals("!") || s.equals("?")){
						System.out.print(s);
						wait(SettingHandler.typeSpeed * 6);
					} else if (s.equals(",")) {
						this.print(s);
						wait(SettingHandler.typeSpeed * 3);
					} else if(s.equals(" ")) {
						this.print(s);
					} else {
						this.print(s);
						wait(SettingHandler.typeSpeed);
					}
				}
			}
			this.println("");
		} else {
			this.println(text);
		}
	}

	public void notify(String text, int durationMs) {
		Color panelBorder = new Color(0, 91, 209);
		Color panelBackground = new Color(0, 51, 117);
		Color panelText = new Color(138, 189, 255);
		notifyPanel.setBackground(panelBackground);
		notifyPanel.setBorder(BorderFactory.createLineBorder(panelBorder, 1));
	    notifyLabel.setForeground(panelText);
	    notifyProgress.setBackground(panelBackground);
        notifyProgress.setForeground(panelText);
	    createNotification(text, durationMs);
	}
	public void alert(String text, int durationMs) {
		Color panelBorder = new Color(255, 57, 51);
		Color panelBackground = new Color(71, 2, 0);
		Color panelText = new Color(255, 186, 184);
		notifyPanel.setBackground(panelBackground);
		notifyPanel.setBorder(BorderFactory.createLineBorder(panelBorder, 1));
	    notifyLabel.setForeground(panelText);
	    notifyProgress.setBackground(panelBackground);
        notifyProgress.setForeground(panelText);
	    createNotification(text, durationMs);
	}
	
	private void createNotification(String text, int durationMs) {
		notifyLabel.setText(text);
		int textWidth = notifyLabel.getFontMetrics(notifyLabel.getFont()).stringWidth(text);
	    currentNotifyWidth = textWidth + 60;
	    updateNotifyBounds();
	    
	    notifyPanel.setVisible(true);
	    notifyProgress.setValue(100);
	    
	    if (notifyTimer != null) notifyTimer.stop();

	    notifyStartTime = System.currentTimeMillis();
	    
	    notifyTimer = new javax.swing.Timer(8, e -> {
	        long elapsed = System.currentTimeMillis() - notifyStartTime;
	        
	        float progress = 1.0f - ((float) elapsed / durationMs);

	        if (progress <= 0) {
	            notifyPanel.setVisible(false);
	            ((javax.swing.Timer)e.getSource()).stop();
	        } else {
	            notifyProgress.setMaximum(1000);
	            notifyProgress.setValue((int) (progress * 1000));
	        }
	    });
	    notifyTimer.start();
	}
	
	private void updateNotifyBounds() {
	    int padding = 25;
	    int h = notifyPanel.getPreferredSize().height;
	    notifyPanel.setBounds(getWidth() - currentNotifyWidth - padding, 
	                         getHeight() - h - padding - 45, 
	                         currentNotifyWidth, h);
	}

// Text parsing methods
	private void parseAndAppend(String text) {
        String[] parts = text.split("\u001b");
        for (String part : parts) {
            if (part.isEmpty()) continue;
            if (part.startsWith("[")) {
                int mIndex = part.indexOf("m");
                if (mIndex != -1) {
                    updateAnsiStyle(part.substring(1, mIndex));
                    appendText(part.substring(mIndex + 1));
                    continue;
                }
            }
            appendText(part);
        }
    }
	private void updateAnsiStyle(String code) {
		if (code.equals("0")) { // Full Reset
			currentAnsiFg = Color.WHITE;
			currentAnsiBg = new Color(20, 20, 20);
			isBold = isItalic = isInverse = false;
		} else if (code.equals("1"))  isBold = true;
		else if (code.equals("22")) isBold = false;
		else if (code.equals("3"))  isItalic = true;
		else if (code.equals("23")) isItalic = false;
		else if (code.equals("7"))  isInverse = true;
		else if (code.equals("27")) isInverse = false;
		else if (code.startsWith("38;2;")) {
			currentAnsiFg = parseRGB(code);
		} else if (code.startsWith("48;2;")) {
			currentAnsiBg = parseRGB(code);
		}
	}
	private Color parseRGB(String code) {
	    try {
	        String[] rgb = code.split(";");
	        return new Color(Integer.parseInt(rgb[2]), Integer.parseInt(rgb[3]), Integer.parseInt(rgb[4]));
	    } catch (Exception e) { return Color.WHITE; }
	}
	private void appendText(String msg) {
	    StyledDocument doc = display.getStyledDocument();
	    Style style = display.addStyle("CurrentStyle", null);
	    
	    // Determine final colors based on Inverse state
	    Color finalFg = isInverse ? currentAnsiBg : currentAnsiFg;
	    Color finalBg = isInverse ? currentAnsiFg : currentAnsiBg;

	    StyleConstants.setForeground(style, finalFg);
	    StyleConstants.setBackground(style, finalBg);
	    StyleConstants.setBold(style, isBold);
	    StyleConstants.setItalic(style, isItalic);

	    try {
	        doc.insertString(doc.getLength(), msg, style);
	    } catch (BadLocationException e) { e.printStackTrace(); }
	    display.setCaretPosition(doc.getLength());
	}
	private void appendTextStaticPosition(String msg) {
	    StyledDocument doc = display.getStyledDocument();
	    Style style = display.addStyle("CurrentStyle", null);
	    
	    // Determine final colors based on Inverse state
	    Color finalFg = isInverse ? currentAnsiBg : currentAnsiFg;
	    Color finalBg = isInverse ? currentAnsiFg : currentAnsiBg;

	    StyleConstants.setForeground(style, finalFg);
	    StyleConstants.setBackground(style, finalBg);
	    StyleConstants.setBold(style, isBold);
	    StyleConstants.setItalic(style, isItalic);

	    try {
	        doc.insertString(doc.getLength(), msg, style);
	    } catch (BadLocationException e) { e.printStackTrace(); }
	    display.setCaretPosition(0);
	}
	
	public void clear() {
		display.setText("");
	}
	public void reset() {
	    display.setText("");
	    currentAnsiFg = Color.WHITE;
	    currentAnsiBg = new Color(20, 20, 20);
	    isBold = false;
	    isItalic = false;
	    isInverse = false;
	    display.setCaretPosition(0);
	}
	
	public void setBackground(int r, int g, int b) {
		bg_r = r; bg_g = g; bg_b = b;
		display.setBackground(new Color(bg_r, bg_g, bg_b));
		currentAnsiBg = new Color(bg_r, bg_g, bg_b);
	}
	public void setTextColor(Color col) {
		currentAnsiFg = col;
	}
	
	public String getTextInput(String text) {
		return JOptionPane.showInputDialog(null, text);
	}
	public boolean getYesNo(String text) {
		int choice = JOptionPane.showConfirmDialog(null, text, "", JOptionPane.YES_NO_OPTION);
	    return choice == JOptionPane.YES_OPTION;
	}
	
}
