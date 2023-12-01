import java.util.*;
import java.io.*;
import java.net.*;

public class GCServer {
    static ArrayList<ClientHandler> clients = new ArrayList<ClientHandler>();

    public static void main(String[] args) throws Exception {
        ServerSocket server = new ServerSocket(1250);
        Message msg = new Message();
        int count = 0;
        while (true) {
            Socket ss = server.accept();
            DataInputStream din = new DataInputStream(ss.getInputStream());
            DataOutputStream dout = new DataOutputStream(ss.getOutputStream());
            ClientHandler chlr = new ClientHandler(ss, din, dout, msg);
            clients.add(chlr);
            chlr.start();
            count++;
        }
    }
}

class Message
{
    String msg;
    public void setMsg(String msg)
    {
        this.msg = msg;
    }
    public void getMsg()
    {
        System.out.println("\nNEW GROUP MESSAGE: " + this.msg);
        for(int i=0;i<GCServer.clients.size();i++)
        {
            try
            {
                System.out.println("Client: " + GCServer.clients.get(i).ip + "; ");
                GCServer.clients.get(i).out.writeUTF(this.msg);
                GCServer.clients.get(i).out.flush();
            }
            catch(Exception e)
            {
                System.out.println(e);
            }
        }
    }
}

class ClientHandler extends Thread
{
    DataInputStream in;
    DataOutputStream out;
    Socket socket;
    int sum;
    float res;
    boolean conn;
    Message msg;
    String ip;

    public ClientHandler(Socket s, DataInputStream din, DataOutputStream dout, Message msg)
    {
        this.socket = s;
        this.in = din;
        this.out = dout;
        this.msg = msg;
        this.conn = true;
        this.ip = (((InetSocketAddress) s.getRemoteSocketAddress()).getAddress()).toString().replace("/", "");
    }

    public void run()
    {
        while(conn == true)
        {
            try
            {
                String input = this.in.readUTF();
                this.msg.setMsg(input);
                this.msg.getMsg();
            }
            catch(Exception e)
            {
                conn = false;
                System.out.println(e);
            }
        }
        closeConn();
    }

    public void closeConn()
    {
        try
        {
            this.in.close();
            this.out.close();
            this.socket.close();
        }
        catch(Exception e)
        {
            System.out.println(e);
        }
    }
}


