import java.awt.*;
import javax.swing.*;

public class LayoutManagerDemo {
    public static void main(String args[]) {
        JFrame f = new JFrame("Layout");
        f.setSize(300, 300);
        f.setLayout(new GridLayout(2, 2));

        f.add(new JButton("1"));
        f.add(new JButton("2"));
        f.add(new JButton("3"));
        f.add(new JButton("4"));

        f.setVisible(true);
    }
}
