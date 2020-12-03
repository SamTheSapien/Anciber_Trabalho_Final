import nmap # import nmap.py module
import threading
import collections
import sqlConnector as conn
import os

nm = nmap.PortScanner() # instantiate nmap.PortScanner object
nmY = nmap.PortScannerYield() #Continuo
sql = conn.sql_Connector()

def create_file(name):
    f = open(name, "w")
    return f

def end_file(f):
    f.close()

#for progressive_result in nmY.scan('192.168.1.0/24', '22-25'):
#for progressive_result in nmY.scan('192.168.1.0/24',arguments='-sn -T5'):
#   print(progressive_result)
# nm.scan('127.0.0.1', '22-443') # scan host 127.0.0.1, ports from 22 to 443
# nm.command_line() # get command line used for the scan : nmap -oX - -p 22-443 127.0.0.1
# nm.scaninfo() # get nmap scan informations {'tcp': {'services': '22-443', 'method': 'connect'}}
# nm.all_hosts() # get all hosts that were scanned

def convertToBinaryData(name):
    with open(name, 'r') as file:
        binaryData = file.read()
    return binaryData

def fastScanComputer(ip,name,desc):
    nm.scan(ip,arguments=' -sV -sC -O -T5')
    comandline="Command Line: %s\n" % nm.command_line()
    saveCSV(nm)
    print(comandline)
    f = create_file(name)
    f.write(comandline)
    hosts,ports = complet_report(nm,f)
    end_file(f)
    descricao = desc
    filepath=os.getcwd()+'/'+name
    strings = convertToBinaryData(filepath)
    scanid = sql.insert_scan(descricao,nm.command_line(),strings)
    i=0
    hostid=[]
    for i in range(len(hosts)):
        host=hosts[i]
        print(host)
        hid=sql.insert_hosts(scanid,host)
        print(hid)
        hostid.append(hid)
        currentport=ports[i]
        for j in currentport:
            sql.insert_ports(scanid,hostid[i],j)
        i=i+1

def fullScanComputer(ip,name,desc):
    nm.scan(ip,arguments='-sV -sC -O -p- -T5')
    saveCSV(nm)
    comandline = "Command Line: %s\n" % nm.command_line()
    print(comandline)
    f = create_file(name)
    f.write(comandline)
    hosts,ports = complet_report(nm,f)
    end_file(f)
    descricao = desc
    filepath = os.getcwd() + '/' + name
    strings = convertToBinaryData(filepath)
    scanid = sql.insert_scan(descricao, nm.command_line(), strings)
    i = 0
    hostid = []
    for i in range(len(hosts)):
        host = hosts[i]
        print(host)
        hid = sql.insert_hosts(scanid, host)
        print(hid)
        hostid.append(hid)
        currentport = ports[i]
        for j in currentport:
            sql.insert_ports(scanid, hostid[i], j)
        i = i + 1

def fastScanNetwork(ip,name,desc):
    hosts=[]
    nm.scan(ip,arguments='-sn -T5')
    saveCSV(nm)
    comandline = "Command Line: %s\n" % nm.command_line()
    print(comandline)
    f = create_file(name)
    f.write(comandline)
    hosts = fast_report_network(nm,f)
    end_file(f)
    descricao = desc
    filepath = os.getcwd() + '/' + name
    strings = convertToBinaryData(filepath)
    scanid = sql.insert_scan(descricao, nm.command_line(), strings)
    for i in range(len(hosts)):
        host = hosts[i]
        print(host)
        hid = sql.insert_hosts(scanid, host)

def fullSpeedScanNetwork(ip):
    result=[]
    i=0
    total=0
    for progressive_result in nmY.scan(ip,arguments='-sn -T5'):
        result.append({'Ip':progressive_result[0],'Up':progressive_result[1]['nmap']['scanstats']['uphosts']})
        print(result[i])
        if (int(result[i]['Up']) == 1):
            print('----------------------------------------------------')
            currentIp = result[i]['Ip']
            print('Found Ip up: %s ' % currentIp)
            thread1 = myThread(total, "Thread-"+str(total), currentIp,' -sV -sC -O -T5')
            thread1.start()
            total=total+1
        i=i+1

def allPortsAllNetworkAtFullSpeed(ip):
    result = []
    i = 0
    total = 0
    for progressive_result in nmY.scan(ip, arguments='-sn -T5'):
        result.append({'Ip': progressive_result[0], 'Up': progressive_result[1]['nmap']['scanstats']['uphosts']})
        #print(result[i])
        if (int(result[i]['Up']) == 1):
            print('----------------------------------------------------')
            currentIp = result[i]['Ip']
            print('Found Ip up: %s ' % currentIp)
            thread1 = myThread(total, "Thread-" + str(total), currentIp, ' -sV -sC -O -p- -T5')
            thread1.start()
            total = total + 1
        i = i + 1

#Print a report to terminal, save to file and return two arrays to save in db
def complet_report(nm,f):
    hosts=[]
    portsArray=[]
    portsArray2 = []
    for host in nm.all_hosts():
        sep='----------------------------------------------------\n'
        print(sep)
        f.write(sep)
        line1='Host : %s (%s)\n' % (host, nm[host].hostname())
        print(line1)
        f.write(line1)
        line2='State : %s\n' % nm[host].state()
        print(line2)
        f.write(line2)
        #print(nm[host])
        #print(nm[host]['osmatch'])
        #print(nm[host]['osmatch'][0]['name'])
        #Atencao as filtered ports
        try:
            opsystem= nm[host]['osmatch'][0]['name']
            line3='Operative System : %s\n' % nm[host]['osmatch'][0]['name']
            print(line3)
            f.write(line3)
            kernel=nm[host]['osmatch'][0]['osclass'][0]['cpe'][0]
            line4='Kernel : %s\n' % nm[host]['osmatch'][0]['osclass'][0]['cpe'][0]
            print(line4)
            f.write(line4)
        except:
            opsystem='Unknow'
            line3='Operative System : Unknow\n'
            print(line3)
            f.write(line3)
            kernel='Unknow'
            line4='Kernel : Unknow\n'
            print(line4)
            f.write(line4)
        finally:
            for proto in nm[host].all_protocols():
                sep2='----------\n'
                print(sep2)
                f.write(sep2)
                line5='Protocol : %s\n' % proto
                print(line5)
                f.write(line5)
                #print(ports)
                portsInfo=nm[host][proto].items()
                orderedPorts = collections.OrderedDict(sorted(portsInfo))
                ports = ''
                #print(orderedPorts)
                for port in orderedPorts:
                    line6='port : %s\t|\tstate : %s\t|\tservice : %s\t|\tproduct : %s\t|\tversion : %s\t|\textra info : %s\n' % (port, nm[host][proto][port]['state'],nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version'],nm[host][proto][port]['extrainfo'])
                    print(line6)
                    f.write(line6)
                    portsToDb=(str(port), nm[host][proto][port]['state'],nm[host][proto][port]['name'],nm[host][proto][port]['product'],nm[host][proto][port]['version'],nm[host][proto][port]['extrainfo'])
                    if(ports!=''):
                        ports=ports+', '+str(port)
                    else: ports=str(port)
                    portsArray.append(portsToDb)
        hosts.append([host,opsystem,kernel,ports])
        portsArray2.append(portsArray)
    sep3='----------------------------------------------------\n'
    print(hosts)
    print(sep3)
    f.write(sep3)
    return hosts,portsArray2

def fast_report_network(nm,f):
    hosts=[]
    str(nm.all_hosts())
    print(sorted(nm.all_hosts()))
    #portsInfo = nm[host].items()
    #orderedHosts = collections.OrderedDict(sorted(portsInfo))
    sep1='----------------------------------------------------\n'
    print(sep1)
    f.write(sep1)
    line1='Found a total of %i hosts up\n' % len(nm.all_hosts())
    print(line1)
    f.write(line1)
    for host in nm.all_hosts():
        sep2='----------------------------------------------------\n'
        print(sep2)
        f.write(sep2)
        line2='Host : %s (%s)\n' % (host, nm[host].hostname())
        print(line2)
        f.write(line2)
        line3='State : %s\n' % nm[host].state()
        print(line3)
        f.write(line3)
        hosts.append([host])
    sep3='----------------------------------------------------\n'
    print(sep3)
    f.write(sep3)
    return hosts

def saveCSV(nm):
    print('----------------------------------------------------')
    print(nm.csv())
    with open('output.csv', 'w') as output:
        output.write(nm.csv())

class myThread (threading.Thread):
   def __init__(self, threadID, name, ip,args):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.ip = ip
      self.args = args
   def run(self):
      print("Starting " + self.name)
      sc = nmap.PortScanner()
      sc.scan(self.ip, arguments=self.args)
      #threading.Lock()
      f=create_file('a.txt')
      complet_report(sc,f)
      print("Exiting " + self.name)

