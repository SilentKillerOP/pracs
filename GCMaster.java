import java.util.*;
import java.io.*;
import java.net.*;

public class GCMaster {
    public static void main(String[] args) throws Exception{
        Socket client = new Socket("127.0.0.1", 1250);
        DataInputStream din = new DataInputStream(client.getInputStream());
        DataOutputStream dout = new DataOutputStream(client.getOutputStream());
        System.out.println("Connected as Master");
        Scanner sc = new Scanner(System.in);
        String send = "";
        do
        {
            System.out.print("Enter message: ");
            send = sc.nextLine();
            dout.writeUTF(send);
            dout.flush();
        }while(!send.equals("stop"));
        sc.close();
        dout.close();
        din.close();
        client.close();
    }
}