from socket import *

def main():
    ip_add = "10.1.220.190"
    port = 8080
    print("[+] ========== HoneyPot_Lite Activated ==========")

    try:
        get_socket_con = socket(AF_INET, SOCK_STREAM)
        get_socket_con.bind((ip_add, port))
        get_socket_con.listen(10)
        while True:
            client_con, client_addr = get_socket_con.accept()
            print("Visitor Found! - [{}]".format(client_addr[0]))
            http_response = b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>You Have Been Hacked!</h1>"
            client_con.send(http_response)
            data = client_con.recv(2048)
            print(data.decode("utf-8"))
            client_con.close()
    except error as identifier:
        print("[+] Unspecified Error [{}]".format(identifier))
    except KeyboardInterrupt as kbi:
        print("[-] Process Stopped!")
    except OSError as identifier:
        print("[+] OSError Error [{}]".format(identifier))
        get_socket_con.close()
    finally:
        get_socket_con.close()
    get_socket_con.close()

if __name__ == "__main__":
    main()