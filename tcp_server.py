import socket
import threading
from functools import partial
from time import sleep
from tkinter import *
from tkinter import ttk
from threading import Thread


class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title("Welcome to M&S app")
        self.geometry('750x750')

    def create_label(self, s: str, col, row):
        lbl = Label(self, text=s)
        lbl.grid(column=col, row=row)
        lbl.config(bg="red", fg="white")

    # Define a function to close the window
    def close(self):
        # win.destroy()
        self.quit()


def win(filename, root):
    bg = PhotoImage(file="coding.png")
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)
    action_with_arg1 = partial(UpdateAppend_The_File, filename, root)
    action_with_arg2 = partial(RemoveFromTheFile, filename, root)
    action_with_arg3 = partial(Clear_File, root)
    btn1 = Button(root, text="UPDATE", bg='#54FA9B', command=action_with_arg1)
    btn2 = Button(root, text="REMOVE", bg='red', command=action_with_arg2)
    btn3 = Button(root, text="CLEAR", bg='#A877BA', command=action_with_arg3)
    btn4 = Button(root, text="QUIT", bg='black',font=("Calibri", 14, "bold"), command=root.quit)

    btn1.grid(column=6, row=25)
    btn2.grid(column=6, row=75)
    btn3.grid(column=6, row=125)
    btn4.grid(column=0, row=175)

    root.mainloop()


IP = socket.gethostbyname(socket.gethostname())
PORT = 20382
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
files = ["yto.txt", "pro.txt", "numbers.txt"]
path = "/Users/mohanadsafi/PycharmProjects/FinalProject/Files"


def UpdateAppend_The_File(filename, root):
    root.create_label("Click your update", 1, 2)

    mystring = StringVar()

    # define the function that the signup button will do
    def getvalue():
        global strp
        strp = mystring.get()
        print(strp)
        try:
            with open(path + "/" + filename, 'a') as f:
                f.write(strp)
        except FileExistsError:
            msg = "Sorry, the file" + filename + "not work..."
            print(msg)

    Entry(root, textvariable=mystring).grid(row=3, column=1)  # entry textbox
    Button(root, text="print text", command=getvalue).grid(row=4, column=1)


def RemoveFromTheFile(filename, root):
    root.create_label("Please choose line to remove in range ({},{})".format(1, 8), 2, 2)

    mystring = StringVar()
    try:
        with open(path + "/" + filename, 'r') as f:
            num_lines = sum(1 for line in f)
            # print("Total lines {}".format(num_lines))
    except FileExistsError:
        msg = "Sorry, the file" + filename + "not work..."
        print(msg)

    def getvalue():
        global num
        num = mystring.get()
        print(num)
        num = int(num)

        try:
            with open(path + "/" + filename, 'r+') as f:

                lines = f.readlines()
                f.seek(0)
                f.truncate()

                for number, line in enumerate(lines):

                    if number + 1 != num:
                        f.write(line)
        except FileExistsError:
            msg = "Sorry, the file" + filename + "not work..."
            print(msg)

    Entry(root, textvariable=mystring).grid(row=3, column=2)  # entry textbox
    Button(root, text="print number", command=getvalue).grid(row=4, column=2)


def Clear_File(root):
    root.create_label("Please choose the file you want to clear", 2, 6)
    mystring = StringVar()

    def getvalue():
        global num
        num = mystring.get()
        num = int(num)
        filename = files[num - 1]
        print(filename)

        try:
            with open(path + "/" + filename, 'w'):
                pass
        except FileExistsError:
            msg = "Sorry, the file" + filename + "not work..."
            print(msg)

    Entry(root, textvariable=mystring).grid(row=7, column=2)  # entry textbox
    Button(root, text="get file", command=getvalue).grid(row=8, column=2)


def tcp_prog(root):
    print("[STARTING] Server is starting.")
    """ Staring a TCP socket. """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    root.create_label("Server: (IP: {},PORT: {})".format(IP, PORT), 0, 0)

    """ Bind the IP and PORT to the server. """
    server.bind(ADDR)

    """ Server is listening, i.e., server is now waiting for the client to connected. """
    server.listen()
    print("[LISTENING] Server is listening.")

    while True:
        try:
            """ Server has accepted the connection from the client. """
            client_socket, client_address = server.accept()
            print(f"[NEW CONNECTION] {client_address} connected.")

            request_client = client_socket.recv(SIZE).decode(FORMAT)
            arr_req = request_client
            print(f"[RECV] Receiving the filename.")
            filename = files[int(arr_req) - 1]
            print(filename)

            if not request_client:
                print("The request is empty!!!")
                break
            else:
                win(filename, root)


        except KeyboardInterrupt:
            print("Shutting down...")
            break


if __name__ == "__main__":
    gui = GUI()
    tcp_prog(gui)
