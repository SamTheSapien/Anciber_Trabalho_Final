USE cakephp;
CREATE TABLE scan (
  id int(11) NOT NULL AUTO_INCREMENT,
  Data date DEFAULT NULL,
  Hora timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  Descricao varchar(300) DEFAULT 'No Description',
  comandline varchar(300) DEFAULT 'Unknow',
  file mediumblob NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
CREATE TABLE host (
  id int(11) NOT NULL AUTO_INCREMENT,
  idscan int(11) NOT NULL,
  host varchar(100) NOT NULL,
  opsystem varchar(100) DEFAULT 'Unknow',
  kernel varchar(100) DEFAULT 'Unknow',
  ports varchar(500) DEFAULT 'Unknow',
  PRIMARY KEY (id),
  KEY idscan (idscan),
  CONSTRAINT host_ibfk_1 FOREIGN KEY (idscan) REFERENCES scan (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;
CREATE TABLE port (
  id int(11) NOT NULL AUTO_INCREMENT,
  idscan int(11) NOT NULL,
  hostid int(11) NOT NULL,
  number varchar(10) NOT NULL,
  state varchar(100) DEFAULT 'Unknow',
  service varchar(100) DEFAULT 'Unknow',
  version varchar(100) DEFAULT 'Unknow',
  info varchar(100) DEFAULT 'Unknow',
  PRIMARY KEY (id),
  KEY idscan (idscan),
  KEY hostid (hostid),
  CONSTRAINT port_ibfk_1 FOREIGN KEY (idscan) REFERENCES scan (id),
  CONSTRAINT port_ibfk_2 FOREIGN KEY (hostid) REFERENCES host (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;

