USE cakephp;
CREATE TABLE `host` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `host` varchar(100) NOT NULL,
  `opsystem` varchar(100) DEFAULT 'Unknow',
  `kernel` varchar(100) DEFAULT 'Unknow',
  `ports` varchar(500) DEFAULT 'Unknow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `port` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` varchar(10) NOT NULL,
  `state` varchar(100) DEFAULT 'Unknow',
  `service` varchar(100) DEFAULT 'Unknow',
  `version` varchar(100) DEFAULT 'Unknow',
  `info` varchar(100) DEFAULT 'Unknow',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `scan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Data` date DEFAULT NULL,
  `Hora` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `Descricao` varchar(300) DEFAULT 'No Description',
  `comandline` varchar(300) DEFAULT 'Unknow',
  `file` mediumblob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

