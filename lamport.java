import java.util.*;
import javax.swing.*;
import java.awt.*;
import java.awt.geom.AffineTransform;

public class lamport
{
    int e[][] = new int[10][10];
    int en[][] = new int[10][10];
    int ev[] = new int[10];
    int i,p,j,k;
    HashMap<Integer,Integer> hm = new HashMap<Integer, Integer>();
    int xpoints[] = new int[5];
    int ypoints[] = new int[5];

    class draw extends JFrame{
        private final int ARR_SIZE = 4;

        void drawArrow(Graphics g1,int x1, int y1, int x2, int y2)
        {
            Graphics2D g = (Graphics2D) g1.create();
            double dx = x2 -x1, dy = y2 - y1;
            double angle = Math.atan2(dy, dx);
            int len = (int) Math.sqrt(dx*dx + dy*dy);
            AffineTransform at = AffineTransform.getTranslateInstance(x1, y1);
            at.concatenate(AffineTransform.getRotateInstance(angle));
            g.transform(at);
            //Draw horizontal arrow starting in (0,0)
            g.drawLine(0,0,len,0);
            g.fillPolygon(new int[] {len,len-ARR_SIZE,len-ARR_SIZE, len},
            new int[] {0, -ARR_SIZE, ARR_SIZE,0},4);
        }

        public void paintComponent(Graphics g)
        {
            for(int x=15;x<200;x+=16)
            {
                drawArrow(g, x, x, x, 150);
                drawArrow(g, 30, 300, 300, 190);
            }
        }

        public void paint(Graphics g){
            int h1,h11,h12;
            Graphics2D go=(Graphics2D) g;
            go.setPaint(Color.black);

            for(i=1;i<=p;i++)
            {
                go.drawLine(50,100*i, 450, 100*i);
            }

            for(int i=1;i<=p;i++)
            {
                for(j=1; j<=ev[i]; j++){
                    k=i*10+j;
                    go.setPaint(Color.blue);
                    go.fillOval(50*j, 100*i-3, 5, 5);
                    go.drawString("e"+i+j+"("+en[i][j]+")", 50*j, 100*i-5);
                    h1=hm.get(k);
                    if(h1!=0){
                        h11 = h1/10;
                        h12 = h1%10;
                        go.setPaint(Color.red);
                        drawArrow(go,50*h12+2,100*h11,50*j+2,100*i);
                    }
                }
            }
        }
    }

    public void calc()
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of process: ");
        p=sc.nextInt();
        System.out.println("Enter the number of events per process: ");
        for(i=1;i<=p;i++)
        {
            ev[i]=sc.nextInt();
        }
        System.out.println("Enter the relationship: ");
        for(i=1;i<=p;i++)
        {
            System.out.println("For process: "+i);
            for(j=1;j<=ev[i];j++){
                System.out.println("For event: "+(j));
                int input=sc.nextInt();
                k=i*10+j;
                hm.put(k, input);
                if(j==1){
                    en[i][j]=1;
                }
            }
        }
        for(i=1;i<=p;i++)
        {
            for(j=2;j<=ev[i];j++)
            {
                k=i*10+j;
                if(hm.get(k) == 0)
                {
                    en[i][j]=en[i][j-1]+1;
                }
                else{
                    int a=hm.get(k);
                    int p1=a/10;
                    int e1=a%10;
                    if(en[p1][e1]>en[i][j-1]){
                        en[i][j] = en[p1][e1] + 1;
                    }
                    else{
                        en[i][j] = en[i][j-1]+1;
                    }
                }
            }

            for(i=1;i<=p;i++){
                for(j=1;j<=ev[i];j++)
                {
                    System.out.println(en[i][j]);
                }
            }
            JFrame jf = new draw();
            jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            jf.setSize(500, 500);
            jf.setVisible(true);
            sc.close();
        }
    }

    public static void main(String[] args)
    {
        lamport lam = new lamport();
        lam.calc();
    }

    
}
