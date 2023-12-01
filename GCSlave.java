import java.io.*;
import java.net.*;

public class GCSlave {
    public static void main(String[] args) throws Exception{
        Socket client = new Socket("127.0.0.1", 1250);
        DataInputStream din = new DataInputStream(client.getInputStream());
        System.out.println("Connected as Slave");
        String recv = "";
        do
        {
            recv = din.readUTF();
            System.out.println("Master Message: " + recv);
        }while(!recv.equals("stop"));
        din.close();
        client.close();
    }
}