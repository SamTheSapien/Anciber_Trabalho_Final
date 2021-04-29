#!/usr/bin/python
import ipaddress
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

def myIP():
    file = os.getcwd() + '/' + 'ip.txt'
    os.system('ifconfig > %s' % (file))
    f = open(file, 'r')
    contents = f.readlines()
    return contents

def show_file(file):
    f = open(file, 'r')
    contents = f.readlines()
    #lbl3.delete(1.0)
    for text in contents:
        lbl3.insert(END,text)

if __name__ == '__main__':
    scandir = '/' + 'scans'
    if not os.path.exists(scandir):
        os.makedirs(scandir)
    filecounter=scan.last_id()
    print("Scans já efetuados: ",filecounter)

window = Tk()
window.title("The SCANER")
window.geometry('1200x600')
lbl = Label(window, text="My Ip")
lbl.grid(column=0, row=0)
txt = Entry(window,width=30)
txt.grid(column=1, row=0)
lbl2 = Label(window, text="WorkBench:")
lbl2.grid(column=0, row=2)
lbl3 = Text(window)
lbl3.grid(column=1,row=2)
lbl4 = Label(window, text="Description of Scan:")
lbl4.grid(column=0, row=3)
txtDesc = Entry(window,width=80)
txtDesc.grid(column=1, row=3)

def clicked():
    network=txt.get()
    try:
        ipaddress.ip_network(network)
    except:
        messagebox.showerror('Enter your ip!', 'Enter a correct IP!')
        return
    if network==None or network == '' :
        messagebox.showerror('No Ip given', 'Enter your ip!')
    else:
        output=myNetwork(network)
        for text in output:
            lbl3.insert(END,text)

def protect_Description(desc):
    bad_chars = [';', '\'', '"', "-"]
    escape=['\'','\\','\n','\r','\t','\b','\f']
    size=15
    if len(desc) > size:
        messagebox.showerror('Description Error', 'Choose a description  15 characters!')
        return False
    for char in bad_chars:
        if desc.find(char)>-1:
            messagebox.showerror('Description Error', 'Remove strange characters please!')
            return False
    for char in escape:
        if desc.find(char)>-1:
            messagebox.showerror('Description Error', 'Remove strange characters please!')
            return False
    return True


def clickedMyIP():
    output=myIP()
    for text in output:
        lbl3.insert(END,text)

def fastScan():
    global filecounter
    description = txtDesc.get()
    if not protect_Description(description):
        return
    filename = '{0}-scan.txt'.format(str(filecounter))
    print(filename)
    ip=txt2.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fastScanComputer(ip,filename,description)
                filecounter += 1
                messagebox.showinfo("Done", "Scan Finished with sucess!")
                show_file(filename)
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a IP!')
            return


def fastScanAllPorts():
    global filecounter
    description = txtDesc.get()
    if not protect_Description(description):
        return
    filename = '{0}-scan.txt'.format(str(filecounter))
    print(filename)
    ip = txt3.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fullScanComputer(ip, filename,description)
                filecounter += 1
                messagebox.showinfo("Done", "Scan Finished with sucess!")
                show_file(filename)
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a IP!')
            return

def scanAllNetwork():
    global filecounter
    description = txtDesc.get()
    if not protect_Description(description):
        return
    filename = '{0}-scan.txt'.format(str(filecounter))
    print(filename)
    ip = txt4.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s'% ip)
    if (res==True):
        if(ip!=''):
            if (description != ''):
                scan.fastScanNetwork(ip, filename,description)
                filecounter += 1
                messagebox.showinfo("Done", "Scan Finished with sucess!")
                show_file(filename)
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a Network Address IP!')
            return


def scaAllNetowrkAllPorts():
    description = txtDesc.get()
    if not protect_Description(description):
        return
    ip = txt5.get()
    res = messagebox.askyesno('SCAN', 'Are you sure you want to scan the IP: %s' % ip)
    if (res == True):
        if (ip != ''):
            if (description != ''):
                scan.fullSpeedScanNetwork(ip)
                messagebox.showinfo("Done", "This is a hacker feature! Check your terminal with the results!")
            else:
                messagebox.showerror('Description error', 'Enter a description for the scan!')
                return
        else:
            messagebox.showerror('IP error', 'Enter a Network Address IP!')
            return

btn = Button(window, text="Search Network Details by Ip", command=clicked)
btn.grid(column=2, row=0)
txt6 = Entry(window,width=30)
txt6.grid(column=0, row=4)
btn6 = Button(window, text="Search My Ip", command=clickedMyIP)
btn6.grid(column=2, row=1)
txt2 = Entry(window,width=30)
txt2.grid(column=0, row=4)
btn2 = Button(window, text="SCAN IP", command=fastScan)
btn2.grid(column=0, row=5)
#btn7 = Button(window, text="Clear", command=clear)
#btn7.grid(column=2, row=2)
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
