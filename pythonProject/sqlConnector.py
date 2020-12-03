import mysql.connector
import datetime
from mysql.connector import Error
#instanciate db connection
class sql_Connector:

  def __init__(self):
    self.mydb = mysql.connector.connect(
      host="localhost",
      user="cakephpuser",
      password="c@k3_Us3r_p@ssw0rd",
      database="cakephp"
    )
    # instanciate the cursor
    self.mycursor = self.mydb.cursor()

  def insert_scan(self,descr,comand,file):
    try:
      sql = "INSERT INTO scan ( Data, Hora, Descricao, comandline, file) VALUES (%s, %s, %s, %s,%s)"
      data=datetime.date.today()
      hora=datetime.datetime.now()
      val = (data, hora, descr, comand,file)
      self.mycursor.execute(sql, val)
      print(self.mycursor.rowcount, "was inserted.")
      self.mydb.commit()
    except mysql.connector.Error as error:
      print("Failed inserting BLOB data into MySQL table {}".format(error))
    return 1

  def insert_hosts(self,scanid,vals):
    try:
      sql = "INSERT INTO host (idscan, host, opsystem, kernel, ports) VALUES (%d, %s, %s, %s, %s)"
      if (len(vals)==1):
        vals=[vals[0],'','','']
      val2 = (scanid,vals[0],vals[1],vals[2],vals[3])
      print(val2)
      self.mycursor.execute(sql, val2)
      print(self.mycursor.rowcount, "record inserted.")
      self.mydb.commit()
    except mysql.connector.Error as error:
      print("Error: {}".format(error))
    return 1

  def insert_ports(self,scanid,hostid,vals):
    try:
      sql = "INSERT INTO port (idscan, hostid, number, state, service, version, info) VALUES (%d,%d,%s,%s,%s,%s,%s)"
      val2 = (scanid,hostid,vals[0],vals[1],vals[2],vals[3],vals[4])
      print(val2)
      self.mycursor.execute(sql, val2)
      print(self.mycursor.rowcount, "record inserted.")
      self.mydb.commit()
    except mysql.connector.Error as error:
      print("Error: {}".format(error))
