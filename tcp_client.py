import socket
from functools import partial
from tkinter import *
from tkinter import ttk
from threading import Thread
from tcp_server import GUI
from tcp_server import *

IP = socket.gethostbyname(socket.gethostname())

PORT = 20382
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024
files = ["yto.txt", "pro.txt", "numbers.txt"]
options = ["Update the file", "remove line the data from the file", "Clear the file"]


def work():
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    # GUI.create_label()
    # lbl = Label(gui, text="Client: (IP: {},PORT: {})".format(IP, PORT))
    # lbl.grid(column=5, row=5)
    # lbl.config(bg="red", fg="white")

    """ Opening and reading the file data. """
    print("Please get your choose(Number), with which file would you work:- ")
    for number, file in enumerate(files):
        print("{}.{}".format(number + 1, file))

    print()
    file_name = input()
    print("Your choose is:- " + file_name)

    print("Please get your choose(Number), What do you want to do with this :- ")
    for number, option in enumerate(options):
        print("{}.{}".format(number + 1, option))

    print()

    request = file_name

    print()

    """ Sending the filename and the option work to the server. """
    client.send(request.encode(FORMAT))
    msg = client.recv(SIZE).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    work()
