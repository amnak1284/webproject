// Chapter 17 Question 8

import java.awt.Container;
import java.awt.Font;
import java.awt.Dimension;
import java.awt.GridLayout;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.border.EmptyBorder;

public class Keypad extends JPanel
{
  private DigitalDisplay display;

  public Keypad(int width)
  {
    display = new DigitalDisplay();
    display.setPreferredSize(new Dimension(width - 20, width/8));
    display.setFont(new Font("monospaced", Font.BOLD, width / 12));
    display.setBorder(new EmptyBorder(0, 5, 0, 5));
                        // top, left, bottom, right

    JPanel buttons = new JPanel();
    buttons.setPreferredSize(new Dimension(width - 10, width + 5));
    buttons.setLayout(new GridLayout(4, 3, 5, 5));

    JButton b;
    for (int d = 0; d <= 9; d++)
    {
      b = new JButton(String.valueOf(d));
      b.addActionListener(display);
      buttons.add(b);
    }
    b = new JButton(".");
    b.addActionListener(display);
    buttons.add(b);
    b = new JButton("C");
    b.addActionListener(display);
    buttons.add(b);

    add(display);
    add(buttons);
  }

  public static void main(String[] args)
  {
    int width = 240, height = 320;
    JFrame window = new JFrame("Keypad test");
    window.setBounds(100, 100, width, height);
    window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    Container c = window.getContentPane();
    c.add(new Keypad(width));

    window.setVisible(true);
  }
}
