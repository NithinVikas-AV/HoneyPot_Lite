from socket import *
from datetime import date, datetime
import nmap
import os, sys

log_name = "./log/"

def main():
    ip_add = "192.168.188.97"
    port = 85
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
            client_con.close()
    except error as identifier:
        print("[+] Unspecified Error [{}]".format(identifier))
    except KeyboardInterrupt:
        print("[-] Process Stopped!")
    except OSError as ose:
        print("[+] OSError Error [{}]".format(ose))
    finally:
        get_socket_con.close()

def scan_visitor(visitor_ip_address):
    today_date = date.today()
    datetime_now = datetime.now()
    dir_name = today_date.strftime("%d_%m_%Y")
    file_log_path = os.path.join(log_name, dir_name)

    # Ensure log directory exists
    if not os.path.exists(file_log_path):
        os.makedirs(file_log_path, exist_ok=True)

    # Proper log file name
    file_log_name = visitor_ip_address.replace(".", "_") + "_" + datetime.strftime(datetime_now, "%d_%m_%Y") + ".log"
    log_file_path = os.path.join(file_log_path, file_log_name)

    # Determine write mode
    if os.path.isfile(log_file_path):
        is_write_or_append = "a" 
    else:
        is_write_or_append = "w"

    with open(log_file_path, is_write_or_append) as fp:
        get_port_details = get_port_information(visitor_ip_address)
        fp.write("\n")
        for disp in get_port_details:
            fp.write(str(disp) + "\n")
        fp.write("\n")

    print(f"[+] Visitor scanning ! {log_file_path} complete ...")

def get_port_information(ip_address):
    scanner = nmap.PortScanner()
    scanner.scan(hosts=ip_address)
    ip_status = scanner[ip_address].state()
    print("[+] Scanning Visitor In Progress ...")
    details_info = []

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            lport = scanner[host][proto].keys()
            sc = scanner[host][proto]
            for port in lport:
                a = f"port: {port}  Service Name: {sc[port].get('name')}  Product Name: {sc[port].get('product')}  Version Name: {sc[port].get('version')}  Status: {sc[port].get('state')}"
                details_info.append(a)

    return details_info

if __name__ == "__main__":
    main()