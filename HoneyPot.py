from socket import *
from datetime import date, datetime
import nmap
import os, sys

log_name = "./log/"

def main():
    ip_add = "0.0.0.0"
    port = 8080
    print("[+] ========== HoneyPot_Lite Activated ==========")

    try:
        get_socket_con = socket(AF_INET, SOCK_STREAM)
        get_socket_con.bind((ip_add, port))
        get_socket_con.listen(10)
        while True:
            client_con, client_addr = get_socket_con.accept()
            print("Visitor Found! - [{}]".format(client_addr[0]))
            scan_visitor(client_addr[0])
            client_con.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>You Have Been Hacked!</h1>")
            data = client_con.recv(2048)
            print(data.decode("utf-8"))
            client_con.close() #newly added
    except error as identifier:
        print("[+] Unspecified Error [{}]".format(identifier))
    except KeyboardInterrupt as kbi:
        print("[-] Process Stopped!")
    except OSError as ose:
        print("[+] OSError Error [{}]".format(ose))
        get_socket_con.close()
    finally:
        get_socket_con.close()
    get_socket_con.close()

def scan_visitor(visitor_ip_address):
    today_date = date.today()
    datetime_now = datetime.now()
    dir_name = today_date.strftime("%d_%m_%Y")
    file_log_path = os.path.join(log_name, dir_name)

    isExist = os.path.exists(file_log_path)

    if not isExist:
        os.mkdir(file_log_path)
    
    file_log_name = "/"  visitor_ip_address.replace(".","_") + " " + datetime.strftime(datetime_now, "%d_%m_%Y") + ".log"

    isFile_Exist = os.path.isfile(file_log_path + file_log_name)

    if not isFile_Exist:
        is_write_or_append = "w"
    else:
        is_write_or_append = "a"
    
    with open(file_log_path + file_log_name, is_write_or_append) as fp:
        get_port_details = get_port_information(visitor_ip_address)

        fp.write("\n")
        for disp in range(len(get_port_details)-1):
            fp.write(str(get_port_details[disp]) + "\n")
        fp.write("\n")
        fp.close()

    print("[+] Visitor scanning ! {} complete ...".format(file_log_path + file_log_name))

def get_port_information(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=ip_address)
    ip_status = scanner[ip_address].state()
    print("[+] Scanning Visitor Inprogress ...")
    sc = {}
    for host in scanner.all_hosts():
        details_info = []
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            sc = scanner[host][proto]
            for port in lport:
                a = "port: " + str(port) + "  Service Name: " + sc[port]['name'] + "  Product Name: " + sc[port]['product'] + "  Version Name: " + sc[port]['version'] + "  Status: " + sc[port]['status']
                details_info.append(a)
    return details_info

if __name__ == "__main__":
    main()