import java.util.*;

public class Bully
{
    static int n;
    static int pro[] = new int[100];
    static int sta[] = new int[100];
    static int co;
    public static void main(String args[])
    {
        System.out.print("Enter the number of process: ");
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int i, j, c, cl = 1;
        for (i = 0; i< n; i++)
        {
            sta[i] = 1;
            pro[i] = i;
        }
        boolean choice = true;
        int ch;
        do
        {
            System.out.println("Enter Your Choice");
            System.out.println("1. Crash Process");
            System.out.println("2. Recover Process");
            System.out.println("3. Exit");
            System.out.print("> ");
            ch = sc.nextInt();
            switch (ch)
            {
                case 1:
                System.out.print("Enter the process number: ");
                c = sc.nextInt();
                sta[c - 1] = 0;
                cl = 1;
                break;
                case 2:
                System.out.print("Enter the process number: ");
                c = sc.nextInt();
                sta[c - 1] = 1;
                cl = 1;
                break;
                case 3:
                choice = false;
                cl = 0;
                break;
            }
            if (cl == 1)
            {
                System.out.print("Which process will initiate election? = ");
                int ele = sc.nextInt();
                elect(ele);
            }
            System.out.println("Final coordinator is " + co);
        } while (choice);
    }

    static void elect(int ele)
    {
        ele = ele - 1;
        co = ele + 1;
        for (int i = 0; i< n; i++)
        {
            if (pro[ele] < pro[i])
            {
                System.out.println("Election message is sent from " + (ele + 1) + " to " + (i + 1));
                if (sta[i] == 1)
                System.out.println("Ok message is sent from " + (i + 1) + " to " + (ele + 1));
                if (sta[i] == 1)
                elect(i + 1);
            }
        }
    }
}