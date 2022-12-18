#Server

import socket
def ServerSoc():
    host = "127.0.0.1"
    port = 8000
    print("Server is running!")
    msg = "PREPARE"
    log = msg
    over = 0
    s_soc = socket.socket()
    s_soc.bind((host,port))
    s_soc.listen(2)
    while(1):
        replies = []
        print(f"Coordinator : {msg.upper()}")
        for i in range(3):
            conn,add = s_soc.accept()
            conn.send(msg.encode())
            data = conn.recv(1024).decode()
            replies.append(data.upper())
            print(f"Subordinator {i} {add} : {data.upper()}")
        if over == 1:
            break
        if ("ABORT" in replies) or (len(replies)<3) :
            msg = "ABORT"
            print("TRANSACTION ABORTED!\nThe final log is: ", log+" "+msg)
            over = 1
        elif "SUCCESS" in replies:
            msg = "COMPLETE"
            print("TRANSACTION COMPLETED!\nThe final log is: ", log+" "+msg)
            over = 1
        else:
            msg = "COMMIT"
            log += " "+msg
ServerSoc()

#Client

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
            if rec_data.upper() == "ABORT":
                msg = "OK"
                print("TRANSACTION ABORTED!")
                over = 1
            elif rec_data.upper() == "SUCCESS":
                msg = "OK"
                print("TRANSACTION COMPLETED!")
                over = 1
            else:
                msg = input("System Status: ").upper()
                log += " "+msg
                s_soc.send(msg.encode())
            if over == 1:
                break
            s_soc.close()
        except:
            print("END OF TRANSACTION\n final log is: ",log+" "+rec_data.upper())
            break
ClientSoc()