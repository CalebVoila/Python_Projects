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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-04-19 13:07:04.291354'),(2,'auth','0001_initial','2024-04-19 13:07:05.127996'),(3,'admin','0001_initial','2024-04-19 13:07:05.318116'),(4,'admin','0002_logentry_remove_auto_add','2024-04-19 13:07:05.328147'),(5,'admin','0003_logentry_add_action_flag_choices','2024-04-19 13:07:05.341822'),(6,'contenttypes','0002_remove_content_type_name','2024-04-19 13:07:05.453770'),(7,'auth','0002_alter_permission_name_max_length','2024-04-19 13:07:05.541357'),(8,'auth','0003_alter_user_email_max_length','2024-04-19 13:07:05.582651'),(9,'auth','0004_alter_user_username_opts','2024-04-19 13:07:05.592654'),(10,'auth','0005_alter_user_last_login_null','2024-04-19 13:07:05.664284'),(11,'auth','0006_require_contenttypes_0002','2024-04-19 13:07:05.669256'),(12,'auth','0007_alter_validators_add_error_messages','2024-04-19 13:07:05.678582'),(13,'auth','0008_alter_user_username_max_length','2024-04-19 13:07:05.770129'),(14,'auth','0009_alter_user_last_name_max_length','2024-04-19 13:07:05.852229'),(15,'auth','0010_alter_group_name_max_length','2024-04-19 13:07:05.882004'),(16,'auth','0011_update_proxy_permissions','2024-04-19 13:07:05.893779'),(17,'auth','0012_alter_user_first_name_max_length','2024-04-19 13:07:05.978607'),(18,'sessions','0001_initial','2024-04-19 13:07:06.029136'),(19,'myapp','0001_initial','2024-04-19 13:37:38.263865'),(20,'myapp','0002_local_news','2024-04-20 18:13:36.630388'),(21,'myapp','0003_alter_local_news_image','2024-04-20 18:27:35.032556'),(22,'myapp','0004_alter_local_news_image','2024-04-20 18:36:24.571352'),(23,'myapp','0005_remove_destination_offer_remove_destination_price','2024-04-21 05:06:42.217152'),(24,'myapp','0006_destination_image','2024-04-21 05:19:40.354177'),(25,'myapp','0007_alter_destination_image_alter_local_news_image','2024-04-21 05:30:18.844356'),(26,'myapp','0008_alter_destination_image','2024-04-21 05:50:38.009318'),(27,'myapp','0009_alter_destination_image','2024-04-21 05:52:55.591875'),(28,'myapp','0010_alter_destination_image','2024-04-21 05:54:23.098054'),(29,'myapp','0011_alter_destination_image','2024-04-21 06:02:34.626391'),(30,'myapp','0012_alter_local_news_image','2024-04-21 06:36:16.774785'),(31,'myapp','0013_international_news_national_news','2024-04-22 18:10:38.031839'),(32,'myapp','0014_kdrama_movies_shows','2024-04-25 15:34:38.351480'),(33,'myapp','0015_anime_car_mov_desi_car','2024-04-26 02:39:03.410668'),(34,'myapp','0016_destination_link','2024-04-28 16:53:12.973256'),(35,'myapp','0017_anime_link_car_mov_link_desi_car_link_and_more','2024-04-28 17:05:21.257799');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-30 15:43:00
