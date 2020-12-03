#!/usr/bin/python
import os
from tkinter import messagebox
import scansDefinitions as scan
from tkinter import *

def myNetwork(ip):
    file=os.getcwd()+'/'+'network.txt'
    os.system('ipcalc %s > %s'% (ip,file))
    f = open(file,'r')
    contents = f.readlines()
    return contents

def show_file(file):
    f = open(file, 'r')
    contents = f.readlines()
    #lbl3.delete(1.0)
    for text in contents:
        lbl3.insert(END,text)

if __name__ == '__main__':
    filecounter = 0

window = Tk()
window.title("The SCANER")
window.geometry('1200x600')
lbl = Label(window, text="My Ip")
lbl.grid(column=0, row=0)
txt = Entry(window,width=30)
txt.grid(column=1, row=0)
lbl2 = Label(window, text="Network details:")
lbl2.grid(column=0, row=2)
lbl3 = Text(window)
lbl3.grid(column=1,row=2)
lbl4 = Label(window, text="Description of Scan:")
lbl4.grid(column=0, row=3)
txtDesc = Entry(window,width=80)
txtDesc.grid(column=1, row=3)

def clicked():
    output=myNetwork(txt.get())
    for text in output:
        lbl3.insert(END,text)

def fastScan():
    description = txtDesc.get()
    filename = str(filecounter) + '-scan.txt'
    print(filename)
    ip=txt2.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fastScanComputer(ip,filename,description)
                filecounter + 1
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a IP!')
            return
    messagebox.showinfo("Done", "Scan Finished with sucess!")
    show_file(filename)
def fastScanAllPorts():
    description = txtDesc.get()
    filename = str(filecounter) + '-scan.txt'
    print(filename)
    ip = txt3.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fullScanComputer(ip, filename,description)
                filecounter + 1
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a IP!')
            return
    messagebox.showinfo("Done", "Scan Finished with sucess!")
    show_file(filename)
def scanAllNetwork():
    description = txtDesc.get()
    filename = str(filecounter) + '-scan.txt'
    print(filename)
    ip = txt4.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s'% ip)
    if (res==True):
        if(ip!=''):
            if (description != ''):
                scan.fastScanNetwork(ip, filename,description)
                filecounter + 1
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a Network Address IP!')
            return
    messagebox.showinfo("Done", "Scan Finished with sucess!")
    show_file(filename)

def scaAllNetowrkAllPorts():
    description = txtDesc.get()
    ip = txt5.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fullSpeedScanNetwork(ip)
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a Network Address IP!')
            return
    messagebox.showinfo("Done","Scan Finished with sucess!")

btn = Button(window, text="Search Ip Network", command=clicked)
btn.grid(column=2, row=0)
txt2 = Entry(window,width=30)
txt2.grid(column=0, row=4)
btn2 = Button(window, text="SCAN IP", command=fastScan)
btn2.grid(column=0, row=5)
txt3 = Entry(window,width=30)
txt3.grid(column=1, row=4)
btn3 = Button(window, text="SCAN ALL PORTS IP", command=fastScanAllPorts)
btn3.grid(column=1, row=5)
txt4 = Entry(window,width=30)
txt4.grid(column=0, row=6)
btn4 = Button(window, text="SCAN ALL NETWORK", command=scanAllNetwork)
btn4.grid(column=0, row=7)
txt5 = Entry(window,width=30)
txt5.grid(column=1, row=6)
btn5 = Button(window, text="SCAN ALL PORTS ALL NETWORK", command=scaAllNetowrkAllPorts)
btn5.grid(column=1, row=7)


window.mainloop()

#scan.fullScanComputer('127.0.0.1',filename)
#fastScanNetwork('192.168.1.0/24')
#fullSpeedScanNetwork('192.168.1.0/24')
#allPortsAllNetworkAtFullSpeed('192.168.1.0/24')
#sql.create_table()
#sql.insert_scan()
#sql.insert_ips()