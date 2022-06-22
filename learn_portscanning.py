import socket
import threading
import os
from queue import Queue

open_ports = []
target = ""
queue = Queue()
def scanning_one_port():
    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            return True
        except:
            return False

    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            if port_scan(port):
                open_ports.append(str(port))

    port_list = input("Please enter port")
    os.system("cls")
    fill_queue(port_list)

    thread_list = []

    for t in range(500):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    if open_ports:

        print()
        print("  The scanned port is Open")
        print()
        print("*****************")
    else:
        print("*****************")
        print()
        print("  The scanned port is Closed")
        print()
        print("*****************")
        cmd = input("Press ENTER")
        if cmd == True or cmd == False:
            choose_ip()


def start_important():
    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            return True
        except:
            return False

    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            if port_scan(port):
                open_ports.append(str(port))

    port_list = (21, 22, 23, 25, 53, 110, 135, 137, 138, 139, 443, 1433, 1434)
    fill_queue(port_list)

    thread_list = []

    for t in range(1):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("*****************")
    print(f"  total ports scanned : {len(port_list)}")
    print(f"  there are currently {len(open_ports)} open ports")
    print()
    print(f"    -To list all the open ports press '1'.")
    print()
    print(f"    -To quit press 'q'.")
    print("*****************")

    def choose_start_full():
        cmd = input("CMD>>")
        if cmd == "q":
            beginning()
        elif cmd == "1":
            os.system("cls")
            print("*****************")
            print(f"  All open ports:")
            print()
            print(open_ports)
            cfm = input("Press ENTER")
            if cfm == True or cfm == False:
                os.system("cls")
                choose_ip()
        else:
            os.system("cls")
            choose_start_full()

    choose_start_full()


def start_full():
    def port_scan(port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            return True
        except:
            return False

    def fill_queue(port_list):
        for port in port_list:
            queue.put(port)

    def worker():
        while not queue.empty():
            port = queue.get()
            if port_scan(port):
                open_ports.append(str(port))

    port_list = range(1, 65535 + 1)
    fill_queue(port_list)

    print("Scanning has begun. Please wait ")

    thread_list = []

    for t in range(500):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
    os.system("cls")
    print("*****************")
    print(f"  total ports scanned: {len(port_list)}")
    print(f"  there are currently {len(open_ports)} open ports!")
    print()
    print(f"    -For all open ports press 1.")
    print()
    print(f"    -To quit press q.")
    print("*****************")

    def choose_start_full():
        cmd = input("CMD>>")
        if cmd == "q":
            beginning()
        elif cmd == "1":
            os.system("cls")
            print("*****************")
            print(f"  All open ports:")
            print()
            print(open_ports)
            cfm = input("Press ENTER")
            if cfm == True or cfm == False:
                os.system("cls")
                choose_ip()
        else:
            os.system("cls")
            choose_start_full()

    choose_start_full()


def choose_ip():
    print("*****************")
    print(" type '1' to begin typing the ip address")
    print("*****************")
    input_ip = input("CMD>>").lower()
    if input_ip == "help":
        os.system("cls")
        print("*****************")
        print(
            "   type 127.0.0.1 to scan computer else type 1 ")
        print()
        print(
            "  To scan router type r.")
        print("*****************")
        print("*****************")
        cdm = input("CMD>>")
        if cdm == "1":
            choose_ip()
        elif cdm == "r":
            os.system("cls")
            ip = os.system("ipconfig")
            print(ip)
            choose_ip()
        else:
            os.system("cls")
            choose_ip()
    elif input_ip == "1":
        target_ip = input(" Type ip ")
        global target
        target = target_ip
        os.system("cls")
        beginning()
    else:
        os.system("cls")
        choose_ip()


def beginning():
    os.system("cls")
    print("*****************")
    print("  Type of port-scan ?")
    print()
    print("    -for a full port scan press '1'")
    print()
    print("    -for only scanning the dangerous ports press '2'")
    print()
    print("    -for only scanning a specific port press '3'")
    print()
    print("    -To quit press q")
    print("*****************")
    start_cmd = input("CMD>>").lower()

    if start_cmd == "1":
        print(
            "  Port-scan is running. Please wait")
        os.system("cls")
        start_full()
    elif start_cmd == "2":
        print(
            "  Port-scan for important ports is running. Please wait")
        os.system("cls")
        start_important()
    elif start_cmd == "3":
        os.system("cls")
        scanning_one_port()
    elif start_cmd == "q":
        os.system("cls")
        quit()
    else:
        os.system("cls")
        beginning()


print()
print("Welcome to the 'Port-scanning' project")
cmd = input("Press ENTER")
text = input("type in enter")  
if text == "":
    print("you pressed enter")
    choose_ip()
else:
    print("you typed some text before pressing enter")
