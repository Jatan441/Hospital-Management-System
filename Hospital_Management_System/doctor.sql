-- MySQL dump 10.10
--
-- Host: 127.0.0.1    Database: hospital
-- ------------------------------------------------------
-- Server version	5.0.24-community-nt

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
CREATE TABLE `appointment` (
  `pname` varchar(20) default NULL,
  `dname` varchar(20) default NULL,
  `datetime` varchar(20) NOT NULL,
  PRIMARY KEY  USING BTREE (`datetime`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment`
--


/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
LOCK TABLES `appointment` WRITE;
INSERT INTO `appointment` VALUES ('Jatan441','Dr. Jatan','1/8/21 12:00 PM'),('Jatan441','Dr. Jatan','1/8/21 2:00 PM'),('Jatan441','Dr. Jatan','1/8/21 4:00 PM');
UNLOCK TABLES;
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
CREATE TABLE `doctor` (
  `ID` varchar(20) NOT NULL default '',
  `Name` varchar(20) default NULL,
  `specialize` varchar(20) default NULL,
  `cont` varchar(20) default NULL,
  PRIMARY KEY  USING BTREE (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `doctor`
--


/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
LOCK TABLES `doctor` WRITE;
INSERT INTO `doctor` VALUES ('1','Jatan','cardiologist','123456'),('123','Jatan','cardio','123'),('2','Jat','s','2'),('3','jatan','cardio','123'),('4','Jack','cardio','123456'),('5','jc','ca','1232'),('6','jata','gh','7989');
UNLOCK TABLES;
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
CREATE TABLE `patient` (
  `id` varchar(20) NOT NULL,
  `name` varchar(20) default NULL,
  `address` varchar(20) default NULL,
  `cont` varchar(20) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `patient`
--


/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
LOCK TABLES `patient` WRITE;
INSERT INTO `patient` VALUES ('1','Jatan Choudhary','khandwa MP','123456'),('2','Jatan','Khandwa','12345');
UNLOCK TABLES;
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

