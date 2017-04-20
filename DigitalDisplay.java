// Chapter 17 Question 8

import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JButton;
import javax.swing.JTextField;

public class DigitalDisplay extends JTextField
    implements ActionListener
{
  public DigitalDisplay()
  { //setting for the screen
    setBackground(new Color(50, 200, 50));
        //this is manually setting the color RGB format
    setForeground(Color.WHITE);
    setHorizontalAlignment(RIGHT);
    setEditable(false);
  }

  public void actionPerformed(ActionEvent e)
  {
    JButton b = (JButton)e.getSource();
    String str = b.getText();
    if ("C".equals(str))
    {
      setText("");
    }
    else
    {
      setText(getText() + str);
    }
  }
}
