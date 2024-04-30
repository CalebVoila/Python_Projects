CREATE DATABASE  IF NOT EXISTS `my_bot` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `my_bot`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: my_bot
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add destination',7,'add_destination'),(26,'Can change destination',7,'change_destination'),(27,'Can delete destination',7,'delete_destination'),(28,'Can view destination',7,'view_destination'),(29,'Can add local_news',8,'add_local_news'),(30,'Can change local_news',8,'change_local_news'),(31,'Can delete local_news',8,'delete_local_news'),(32,'Can view local_news',8,'view_local_news'),(33,'Can add international_news',9,'add_international_news'),(34,'Can change international_news',9,'change_international_news'),(35,'Can delete international_news',9,'delete_international_news'),(36,'Can view international_news',9,'view_international_news'),(37,'Can add national_news',10,'add_national_news'),(38,'Can change national_news',10,'change_national_news'),(39,'Can delete national_news',10,'delete_national_news'),(40,'Can view national_news',10,'view_national_news'),(41,'Can add kdrama',11,'add_kdrama'),(42,'Can change kdrama',11,'change_kdrama'),(43,'Can delete kdrama',11,'delete_kdrama'),(44,'Can view kdrama',11,'view_kdrama'),(45,'Can add movies',12,'add_movies'),(46,'Can change movies',12,'change_movies'),(47,'Can delete movies',12,'delete_movies'),(48,'Can view movies',12,'view_movies'),(49,'Can add shows',13,'add_shows'),(50,'Can change shows',13,'change_shows'),(51,'Can delete shows',13,'delete_shows'),(52,'Can view shows',13,'view_shows'),(53,'Can add anime',14,'add_anime'),(54,'Can change anime',14,'change_anime'),(55,'Can delete anime',14,'delete_anime'),(56,'Can view anime',14,'view_anime'),(57,'Can add car_mov',15,'add_car_mov'),(58,'Can change car_mov',15,'change_car_mov'),(59,'Can delete car_mov',15,'delete_car_mov'),(60,'Can view car_mov',15,'view_car_mov'),(61,'Can add desi_car',16,'add_desi_car'),(62,'Can change desi_car',16,'change_desi_car'),(63,'Can delete desi_car',16,'delete_desi_car'),(64,'Can view desi_car',16,'view_desi_car');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 15:42:57
