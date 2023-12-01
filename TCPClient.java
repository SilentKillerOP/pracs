import java.io.*;
import java.net.*;
import java.util.*;

public class TCPClient {
    public static void main(String[] args) throws Exception {
        System.out.println("Connecting...");
        Socket s = new Socket("localhost",1160);
        System.out.println("Connected");
        DataInputStream din = new DataInputStream(s.getInputStream());
        DataOutputStream dout = new DataOutputStream(s.getOutputStream());
        Scanner sc = new Scanner(System.in);
        String str = "";
        while(true) {
            str = sc.nextLine();
            dout.writeUTF(str);
            dout.flush();
            if (str.equals("stop")) {
                System.out.println("Sum of integers received from server: " + din.readUTF());
                break;
            }
        }
        din.close();
        dout.close();
        s.close();
        sc.close();
    }
}