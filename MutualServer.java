import java.io.*;
import java.net.*;

public class MutualServer implements Runnable
{
    Socket socket = null;
    static ServerSocket ss;

    MutualServer(Socket newSocket)
    {
        this.socket = newSocket;
    }

    public static void main(String[] args) throws IOException
    {
        ss = new ServerSocket(7000);
        System.out.println("Server Started...");
        while(true)
        {
            Socket s = ss.accept();
            System.out.println("New client connected...");
            MutualServer es = new MutualServer(s);
            Thread t = new Thread(es);
            t.start();
        }
    }

    public void run()
    {
        try
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            while(true)
            {
                String str = br.readLine();
                System.out.println("Client: " + str);
            }
        }
        catch(Exception e)
        {
            System.out.println("Exception: " + e);
        }
    }
}
