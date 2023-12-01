import java.util.*;

public class LoadBalance {

    static void printLoad(int server, int processes){
        int each = processes / server;
        int extra = processes % server;
        int total = 0;
        int i = 0;
        for(i = 0; i < extra; i++){
            System.out.println("Server " + (i+1) + " has " + (each+1) + " processes");
        }
        for(; i < server; i++){
            System.out.println("Server " + (i+1) + " has " + each + " processes");
        }
    }

    public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the number of servers: ");
            int servers = sc.nextInt();
            System.out.println("Enter the number of processes: ");
            int processes = sc.nextInt();
            while(true){
                printLoad(servers, processes);
                System.out.println("\n1.Add Servers 2.Remove Servers 3.Add Processes 4.Remove Processes 5.Exit ");
                System.out.print("> ");
                switch(sc.nextInt()){
                    case 1:
                        System.out.println("Enter the number of servers to add: ");
                        servers += sc.nextInt();
                        break;
                    case 2:
                        System.out.println("Enter the number of servers to remove: ");
                        servers -= sc.nextInt();
                        break;
                    case 3:
                        System.out.println("Enter the number of processes to add: ");
                        processes += sc.nextInt();
                        break;
                    case 4:
                        System.out.println("Enter the number of processes to remove: ");
                        processes -= sc.nextInt();
                        break;
                    case 5:
                        System.exit(0);
                    default:
                        System.out.println("Invalid choice");
                }
            }
    }
}