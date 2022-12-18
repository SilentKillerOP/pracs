import socket
def ClientSoc():
    host = "127.0.0.1"
    port = 8000
    log = ""
    over = 0
    while(1):
        try:
            s_soc = socket.socket()
            s_soc.connect((host,port))
            rec_data = s_soc.recv(1024).decode()
            print("Coordinator: ", rec_data.upper())
            if rec_data.upper() == "FINAL ABORT":
                msg = "OK"
                print("TRANSACTION ABORTED!")
                over = 1
            elif rec_data.upper() == "SUCCESS":
                msg = "OK"
                print("TRANSACTION COMPLETED!")
                over = 1
            else:
                msg = input("System Status: ").upper()
                log += " "+rec_data.upper()
                s_soc.send(msg.encode())
            if over == 1:
                break
            s_soc.close()
        except:
            print("END OF TRANSACTION\n final log is: ",log+" "+rec_data.upper())
            break
ClientSoc()