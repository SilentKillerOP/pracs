import java.io.*;
import java.net.*;

public class TCPServer
{
    public static void main(String[] args) throws Exception
    {
        ServerSocket server = new ServerSocket(1160);
        System.out.println("Connecting...");
        Socket ss = server.accept();
        System.out.println("Connected");
        DataInputStream din = new DataInputStream(ss.getInputStream());
        DataOutputStream dout = new DataOutputStream(ss.getOutputStream());
        String str = "";
        int sum = 0;
        System.out.println("Receiving integers from client...");
        while(true)
        {
            str = din.readUTF();
            if (str.equals("stop"))
            {
                System.out.println("Sum of integers received from client: " + sum);
                dout.writeUTF(""+sum);
                dout.flush();
                break;
            }
            sum += Integer.parseInt(str);
        }
        din.close();
        dout.close();
        ss.close();
        server.close();
    }
}
