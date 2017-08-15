-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: db_quiz
-- ------------------------------------------------------
-- Server version	5.7.18-log

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
-- Table structure for table `tblcategories`
--

DROP TABLE IF EXISTS `tblcategories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblcategories` (
  `IDcategory` int(11) NOT NULL AUTO_INCREMENT,
  `Description` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IDcategory`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblcategories`
--

LOCK TABLES `tblcategories` WRITE;
/*!40000 ALTER TABLE `tblcategories` DISABLE KEYS */;
INSERT INTO `tblcategories` VALUES (1,'Anime'),(2,'Books'),(3,'Games'),(4,'Movies');
/*!40000 ALTER TABLE `tblcategories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblgames`
--

DROP TABLE IF EXISTS `tblgames`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblgames` (
  `IDgame` int(11) NOT NULL AUTO_INCREMENT,
  `IDuser` int(11) DEFAULT NULL,
  `IDcategory` int(11) DEFAULT NULL,
  `correct` int(11) DEFAULT NULL,
  PRIMARY KEY (`IDgame`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblgames`
--

LOCK TABLES `tblgames` WRITE;
/*!40000 ALTER TABLE `tblgames` DISABLE KEYS */;
INSERT INTO `tblgames` VALUES (1,3,2,3),(2,3,1,1),(3,3,3,3),(4,3,4,4),(5,3,1,2),(6,3,2,2),(7,1,4,1),(8,1,2,1),(9,2,1,0),(10,1,2,3),(11,1,3,0),(12,1,4,0),(13,4,3,3),(14,1,2,3),(15,1,1,4),(16,1,2,2),(17,1,3,3),(18,1,1,3),(19,2,2,1),(20,2,2,5),(21,2,1,2),(22,7,4,3);
/*!40000 ALTER TABLE `tblgames` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblquestions`
--

DROP TABLE IF EXISTS `tblquestions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblquestions` (
  `IDquestion` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(200) DEFAULT NULL,
  `option1` varchar(75) DEFAULT NULL,
  `option2` varchar(75) DEFAULT NULL,
  `option3` varchar(75) DEFAULT NULL,
  `option4` varchar(75) DEFAULT NULL,
  `trivia` varchar(200) DEFAULT NULL,
  `IDcategory` int(11) NOT NULL,
  PRIMARY KEY (`IDquestion`,`IDcategory`),
  KEY `fk_tblQuestions_tblCategories_idx` (`IDcategory`),
  CONSTRAINT `fk_tblQuestions_tblCategories` FOREIGN KEY (`IDcategory`) REFERENCES `tblcategories` (`IDcategory`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblquestions`
--

LOCK TABLES `tblquestions` WRITE;
/*!40000 ALTER TABLE `tblquestions` DISABLE KEYS */;
INSERT INTO `tblquestions` VALUES (1,'What are the enemies in Gravity Rush called?','Ne\'vi,True','Na\'vi,False','No\'vi,False','Nu\'vi,False','The Nevi are a strange race of monsters that act are generally colored red and black.',3),(2,'Who is the protagonist of the original Crysis game?','Nomad,True','Alcatraz,False','Prophet,False','Psycho,False','Known as Nomad, Jake Dunn is a member of the Raptor Team that descends on Lingshan islands.',3),(3,'In what city does Infamous Second Son take place?','Seattle,True','Empire City,False','New Marais,False','Boston,False','Sucker Punch choose its own town as a stage so they could draw from personal experience.',3),(4,'What is the current console generation?','8,True','9,False','7,False','6,False','As PS4 Pro and Scorpio are iterations on existing architecture, the current generation is the 8th.',3),(5,'Who is the manufacturer of the SoC used in the PS4 and XB1?','AMD,True','Intel,False','Nvidia,False','Snapdragon,False','Despite offers from Nvidia, both Sony and MS went with similar architectures made by AMD.',3),(6,'What is the name of Geralt\'s horse in Witcher 3?','Roach,True','Epona,False','Shadowmere,False','Agro,False','Roach is how geralt calls all of his mares, with the original polish name being diminutive and female.',3),(7,'How much different Battlefield games are there?','15,True','14,False','12,False','13,False','1942, Vietnam, 2, Modern Combat, 2142, Bad Company, Heroes, 1943, Bad Company 2, Online, Play4Free, 3, 4, Hardline, 1',3),(8,'What is the highest grossing game in the world?','Wii Sports,True','Grand Theft Auto V,False','World of Warcraft,False','Minecraft,False','With a total of 82.78 million it is a milestone not many games even come close to.',3),(9,'Adjusted for inflation, what is the highest grossing video game?','Space Invaders,True','Pac-Man,False','League of Legends,False','Candy Crush Saga,False','Causing a coin-shortage in Japan when it released in arcades, it\'s easy to understand why it\'s #1.',3),(10,'Without adjusting for inflation, what is the highest grossing video game?','World of Warcraft,True','League of Legends,False','Lineage,False','CrossFire,False','In pure numbers, WoW is king, making Blizzard a whopping $9,268,000,000 at the end of 2015. ',3),(11,'What is the currency used in the Legend of Zelda?','Rupees,True','Gems,False','Coins,False','Gil,False','Whether the spelling is with a p or b is debatable, but you\'ll be getting it regardless.',3),(12,'What mobile avian-related game rose to popularity in 2013?','Flappy Bird,True','Angry Birds,False','Mr Flap,False','Birds,False','Flappy Bird is a mobile game developed in 2013 by Vietnamese programmer Dong Nguyen',3),(13,'What is the name of Peter\'s father in Guardians of the Galaxy Vol. 2?','Ego,True','Yondu,False','Tullk,False','Drax,False','Spoiler Alert: Starlord is 50% human, 50% celestial, and 100% awesome!',4),(14,'Who does Cipher threaten to get Dom on her side in F&F8?','Elena,True','Letty,False','Mia,False','Brian,False','Spoiler Alert: Elena has a kid. It\'s Dom\'s. ',4),(15,'Which studio made Princess Swan?','Crest Animation,True','Disney,False','Pixar,False','Dreamworks,False','Your whole childhood has been a lie, wasn\'t it? You thought Disney, didn\'t you?',4),(16,'Who directed the first Narnia movie?','Andrew Adamson,True','James Cameron,False','Michael Apted,False','Joe Johnston,False','It\'s an AA movie. Nice alliteration though.',4),(17,'Who owns the rights to the X-men?','20th Century Fox,True','Marvel,False','Universal,False','Sony Pictures,False','Marvel sold it a while ago to 20th Century in return for more liberties with other rights.',4),(18,'\"Believe it!\" was a famous catchprase of which character?','Naruto,True','Lelouch,False','Ichigo,False','Luffy,False','Not liked by his peers, Naruto often uses this phrase to incite trust from his comrades.',1),(19,'What is the family name of Cornelia, in Code Geass?','li Britannia,True','zi Britannia,False','vi Britannia,False','el Britannia,False','An important side-character in the show, Cornelia li Britannia is Lulu\'s half-sister.',1),(20,'What was the name of the submarine in Full Metal Panic?','Tuatha de Danaan,True','Blue No.6,False','Submarine 707,False','VF-1 Valkyrie,False','I mean, what else is a 16year old gonna name a submarine?',1),(21,'Who is Naruto Uzumaki\'s father?','Minato Namikaze,True','Arashi Kazama,False','Sarutobi Hizuren,False','Nagato Uzumaki,False','The fourth hokage, Minato Namikaze sealed the Kyuubi in his own son.',1),(22,'Who killed Masaki Kurosaki?','Grand Fisher,True','Aizen Sousuke,False','Ywach,False','Kisuke Urahara,False','While Aizen and Ywach orchestrated it, the actual culpit is Grand Fisher.',1),(23,'Who wrote The Silmarillion?','J. R. R. Tolkiën,True','J. K. Rowling,False','C.S. Lewis,False','Mark Twain,False','The prequel to \"The Hobbit\" and \"LotR\" this book sets the scene on Middle Earth.',2),(24,'Which characters discovers the closet that houses Narnia?','Lucy,True','Edmund,False','Susan,False','Peter,False','Lucy discovers the country while playing hide and seek with her siblings.',2),(25,'Who wrote Harry Potter?','J.K. Rowling,True','Stephen King,False','G. R.R. Martin,False','Kate Bernheister,False','Rowling is the first billionair to loose her status due to charity.',2),(26,'What is excalibur known as in Welsh?','Caledfwlch,True','Kaledvoulc\'h,False','Cleddyf,False','Addewid,False','The sword of promised victory my ass.',2),(27,'What book is George Orwell most known for?','1984,True','Animal Farm,False','Homage to Catalonia,False','The Road to Wigan Pier,False','A dystopian future we appear to slowly transitioning to.',2);
/*!40000 ALTER TABLE `tblquestions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblscores`
--

DROP TABLE IF EXISTS `tblscores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblscores` (
  `IDscore` int(11) NOT NULL AUTO_INCREMENT,
  `IDuser` int(11) DEFAULT NULL,
  `IDcategory` int(11) DEFAULT NULL,
  `IDquestion` int(11) DEFAULT NULL,
  `answer` int(1) DEFAULT NULL,
  `datetime` datetime DEFAULT NULL,
  PRIMARY KEY (`IDscore`)
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblscores`
--

LOCK TABLES `tblscores` WRITE;
/*!40000 ALTER TABLE `tblscores` DISABLE KEYS */;
INSERT INTO `tblscores` VALUES (15,3,2,23,1,'2017-08-14 14:00:27'),(16,3,2,24,1,'2017-08-14 14:00:29'),(17,3,2,25,1,'2017-08-14 14:00:32'),(18,3,2,26,0,'2017-08-14 14:00:36'),(19,3,2,27,0,'2017-08-14 14:00:38'),(20,3,1,18,1,'2017-08-14 14:15:52'),(21,3,1,19,0,'2017-08-14 14:15:54'),(22,3,1,20,0,'2017-08-14 14:15:55'),(23,3,1,21,0,'2017-08-14 14:15:57'),(24,3,1,22,0,'2017-08-14 14:15:59'),(25,3,3,1,1,'2017-08-14 14:16:04'),(26,3,3,2,0,'2017-08-14 14:16:06'),(27,3,3,3,1,'2017-08-14 14:16:09'),(28,3,3,4,1,'2017-08-14 14:16:11'),(29,3,3,5,0,'2017-08-14 14:16:13'),(30,3,4,13,0,'2017-08-14 14:16:17'),(31,3,4,14,1,'2017-08-14 14:16:19'),(32,3,4,15,1,'2017-08-14 14:16:21'),(33,3,4,16,1,'2017-08-14 14:16:23'),(34,3,4,17,1,'2017-08-14 14:16:25'),(35,3,1,18,0,'2017-08-14 14:16:31'),(36,3,1,19,1,'2017-08-14 14:16:32'),(37,3,1,20,1,'2017-08-14 14:16:34'),(38,3,1,21,0,'2017-08-14 14:16:35'),(39,3,1,22,0,'2017-08-14 14:16:37'),(40,3,2,23,0,'2017-08-14 14:16:41'),(41,3,2,24,0,'2017-08-14 14:16:43'),(42,3,2,25,0,'2017-08-14 14:16:44'),(43,3,2,26,1,'2017-08-14 14:16:47'),(44,3,2,27,1,'2017-08-14 14:16:48'),(45,1,1,18,0,'2017-08-14 14:17:19'),(46,1,1,19,0,'2017-08-14 14:17:21'),(47,1,1,20,0,'2017-08-14 14:17:23'),(48,1,1,21,1,'2017-08-14 14:17:26'),(49,1,1,22,0,'2017-08-14 14:17:28'),(50,1,2,23,0,'2017-08-14 14:20:16'),(51,1,2,24,0,'2017-08-14 14:20:17'),(52,1,2,25,0,'2017-08-14 14:20:18'),(53,1,2,26,1,'2017-08-14 14:20:20'),(54,1,2,27,0,'2017-08-14 14:20:22'),(55,2,1,18,0,'2017-08-14 14:20:33'),(56,2,1,19,0,'2017-08-14 14:20:36'),(57,2,1,20,0,'2017-08-14 14:20:37'),(58,2,1,21,0,'2017-08-14 14:20:38'),(59,2,1,22,0,'2017-08-14 14:20:40'),(60,2,3,1,1,'2017-08-14 14:21:46'),(61,2,4,13,1,'2017-08-14 15:16:27'),(62,2,4,13,0,'2017-08-14 15:17:08'),(63,2,4,13,0,'2017-08-14 15:17:15'),(64,2,4,13,1,'2017-08-14 15:24:11'),(65,2,4,13,1,'2017-08-14 15:24:18'),(66,2,1,18,0,'2017-08-14 15:26:26'),(67,2,2,23,1,'2017-08-14 15:26:36'),(68,2,2,23,1,'2017-08-14 15:28:08'),(69,2,2,23,1,'2017-08-14 15:28:18'),(70,2,2,23,1,'2017-08-14 15:31:01'),(71,2,2,23,0,'2017-08-14 15:31:28'),(72,2,1,18,1,'2017-08-14 15:32:27'),(73,2,2,23,0,'2017-08-14 15:33:03'),(74,2,3,1,0,'2017-08-14 15:34:14'),(75,2,1,18,1,'2017-08-14 15:34:34'),(76,2,3,1,1,'2017-08-14 15:35:48'),(77,2,3,2,0,'2017-08-14 15:35:51'),(78,2,3,3,0,'2017-08-14 15:37:31'),(79,1,1,18,1,'2017-08-14 15:46:17'),(80,1,1,19,0,'2017-08-14 15:46:22'),(81,1,1,20,1,'2017-08-14 15:46:29'),(82,1,1,21,0,'2017-08-14 15:46:31'),(83,1,1,22,1,'2017-08-14 15:46:34'),(84,1,3,1,0,'2017-08-14 16:25:54'),(85,1,3,2,0,'2017-08-14 16:25:55'),(86,1,3,3,0,'2017-08-14 16:25:57'),(87,1,3,4,0,'2017-08-14 16:25:58'),(88,1,3,5,0,'2017-08-14 16:26:00'),(89,1,4,13,1,'2017-08-14 16:26:05'),(90,1,4,14,1,'2017-08-14 16:26:06'),(91,1,4,15,1,'2017-08-14 16:26:07'),(92,1,4,16,1,'2017-08-14 16:26:09'),(93,1,4,17,0,'2017-08-14 16:28:41'),(94,1,1,18,1,'2017-08-14 18:38:35'),(95,1,1,18,1,'2017-08-14 18:38:50'),(96,1,2,23,1,'2017-08-14 18:39:32'),(97,1,1,18,1,'2017-08-14 19:37:18'),(98,1,1,18,1,'2017-08-14 20:29:09'),(99,1,1,18,0,'2017-08-14 21:11:59'),(100,4,3,1,1,'2017-08-14 21:24:19'),(101,4,3,2,0,'2017-08-14 21:24:21'),(102,4,3,3,0,'2017-08-14 21:24:23'),(103,4,3,4,1,'2017-08-14 21:24:25'),(104,4,3,5,1,'2017-08-14 21:24:27'),(105,1,2,23,1,'2017-08-14 23:36:26'),(106,1,2,24,1,'2017-08-14 23:36:31'),(107,1,2,25,1,'2017-08-14 23:36:37'),(108,1,2,26,0,'2017-08-14 23:36:38'),(109,1,2,27,0,'2017-08-14 23:36:41'),(110,1,1,18,1,'2017-08-15 20:50:04'),(111,1,1,19,1,'2017-08-15 20:50:07'),(112,1,1,20,0,'2017-08-15 20:50:13'),(113,1,1,21,1,'2017-08-15 20:50:16'),(114,1,1,22,1,'2017-08-15 20:50:19'),(115,1,4,13,0,'2017-08-15 20:50:25'),(116,1,4,14,0,'2017-08-15 20:51:15'),(117,1,2,23,0,'2017-08-15 21:18:26'),(118,1,2,24,0,'2017-08-15 21:18:28'),(119,1,2,25,1,'2017-08-15 21:18:30'),(120,1,2,26,1,'2017-08-15 21:18:32'),(121,1,2,27,0,'2017-08-15 21:18:34'),(122,1,4,13,1,'2017-08-15 21:35:55'),(123,1,4,14,0,'2017-08-15 21:35:57'),(124,1,4,15,1,'2017-08-15 21:35:59'),(125,1,4,16,1,'2017-08-15 21:36:01'),(126,1,4,17,0,'2017-08-15 21:36:04'),(127,1,4,13,0,'2017-08-15 21:43:06'),(128,1,4,14,1,'2017-08-15 21:43:08'),(129,1,4,15,1,'2017-08-15 21:43:10'),(130,1,4,16,0,'2017-08-15 21:43:11'),(131,1,4,17,1,'2017-08-15 21:43:13'),(132,2,2,23,0,'2017-08-15 23:08:31'),(133,2,2,24,0,'2017-08-15 23:08:33'),(134,2,2,25,0,'2017-08-15 23:08:34'),(135,2,2,26,1,'2017-08-15 23:08:35'),(136,2,2,27,0,'2017-08-15 23:08:36'),(137,2,2,23,1,'2017-08-15 23:09:42'),(138,2,2,24,1,'2017-08-15 23:09:44'),(139,2,2,25,1,'2017-08-15 23:09:46'),(140,2,2,26,1,'2017-08-15 23:09:49'),(141,2,2,27,1,'2017-08-15 23:09:51'),(142,2,1,18,1,'2017-08-15 23:10:13'),(143,2,1,19,0,'2017-08-15 23:10:15'),(144,2,1,20,1,'2017-08-15 23:10:16'),(145,2,1,21,0,'2017-08-15 23:10:17'),(146,2,1,22,0,'2017-08-15 23:10:18'),(147,7,4,13,1,'2017-08-16 00:06:33'),(148,7,4,14,0,'2017-08-16 00:06:35'),(149,7,4,15,0,'2017-08-16 00:06:36'),(150,7,4,16,1,'2017-08-16 00:06:38'),(151,7,4,17,1,'2017-08-16 00:06:39');
/*!40000 ALTER TABLE `tblscores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblusers`
--

DROP TABLE IF EXISTS `tblusers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tblusers` (
  `IDuser` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`IDuser`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblusers`
--

LOCK TABLES `tblusers` WRITE;
/*!40000 ALTER TABLE `tblusers` DISABLE KEYS */;
INSERT INTO `tblusers` VALUES (1,'andrei','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(2,'bart','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(3,'nanook','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(4,'thomas','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(5,'jonas','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(6,'admin','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033'),(7,'lara','1d2d189b13bb74c9c4c9b9764c1791a9635702885e531309d7d449dc82563033');
/*!40000 ALTER TABLE `tblusers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-16  0:09:11
