-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: 127.0.0.1    Database: seedschool
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `absent_request`
--

DROP TABLE IF EXISTS `absent_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `absent_request` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `child_id` varchar(8) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `absent_request_children_id_fk` (`child_id`),
  CONSTRAINT `absent_request_children_id_fk` FOREIGN KEY (`child_id`) REFERENCES `children` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `absent_request`
--

LOCK TABLES `absent_request` WRITE;
/*!40000 ALTER TABLE `absent_request` DISABLE KEYS */;
INSERT INTO `absent_request` (`id`, `child_id`, `time`) VALUES (4,'20231823','2023-08-21 01:55:43');
/*!40000 ALTER TABLE `absent_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attendance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `child_id` varchar(8) NOT NULL,
  `img_name` varchar(50) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `checkin_children_id_fk` (`child_id`),
  CONSTRAINT `checkin_children_id_fk` FOREIGN KEY (`child_id`) REFERENCES `children` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` (`id`, `child_id`, `img_name`, `time`) VALUES (1,'20231823','20231823 img','2023-08-20 05:48:34'),(2,'20231823','20231823 img4','2023-08-20 05:48:34');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `children`
--

DROP TABLE IF EXISTS `children`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `children` (
  `id` varchar(8) NOT NULL DEFAULT concat(year(current_timestamp()),substr('0123456789',floor(rand() * 9 + 1),1),substr('0123456789',floor(rand() * 9 + 1),1),substr('0123456789',floor(rand() * 9 + 1),1),substr('0123456789',floor(rand() * 9 + 1),1)),
  `name` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `class_id` int(11) NOT NULL,
  `parent_id` varchar(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `student_class_id_fk` (`class_id`),
  KEY `children_parent_id_fk` (`parent_id`),
  CONSTRAINT `children_parent_id_fk` FOREIGN KEY (`parent_id`) REFERENCES `parent` (`id`),
  CONSTRAINT `student_class_id_fk` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `children`
--

LOCK TABLES `children` WRITE;
/*!40000 ALTER TABLE `children` DISABLE KEYS */;
INSERT INTO `children` (`id`, `name`, `DOB`, `class_id`, `parent_id`) VALUES ('20231823','c1','2023-08-08',1,'230001');
/*!40000 ALTER TABLE `children` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `class`
--

DROP TABLE IF EXISTS `class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `class` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `class`
--

LOCK TABLES `class` WRITE;
/*!40000 ALTER TABLE `class` DISABLE KEYS */;
INSERT INTO `class` (`id`, `name`) VALUES (1,'L1');
/*!40000 ALTER TABLE `class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  `child_id` varchar(8) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_teacher_id_fk` (`teacher_id`),
  KEY `feedback_children_id_fk` (`child_id`),
  CONSTRAINT `feedback_children_id_fk` FOREIGN KEY (`child_id`) REFERENCES `children` (`id`),
  CONSTRAINT `feedback_teacher_id_fk` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` (`id`, `content`, `teacher_id`, `time`, `child_id`) VALUES (2,'bruh',1,'2023-08-19 01:02:26','20231823'),(3,'bruh',1,'2023-08-19 06:27:27','20231823'),(4,'bruh',1,'2023-08-20 00:22:51','20231823'),(6,'hehe',1,'2023-08-21 00:20:26','20231823');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_reply_parent`
--

DROP TABLE IF EXISTS `feedback_reply_parent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_reply_parent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) NOT NULL,
  `parent_id` varchar(6) NOT NULL,
  `feedback_id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_reply_parent_feedback_id_fk` (`feedback_id`),
  KEY `feedback_reply_parent_parent_id_fk` (`parent_id`),
  CONSTRAINT `feedback_reply_parent_feedback_id_fk` FOREIGN KEY (`feedback_id`) REFERENCES `feedback` (`id`),
  CONSTRAINT `feedback_reply_parent_parent_id_fk` FOREIGN KEY (`parent_id`) REFERENCES `parent` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_reply_parent`
--

LOCK TABLES `feedback_reply_parent` WRITE;
/*!40000 ALTER TABLE `feedback_reply_parent` DISABLE KEYS */;
INSERT INTO `feedback_reply_parent` (`id`, `content`, `parent_id`, `feedback_id`, `time`) VALUES (2,'p cmt 1','230001',2,'2023-08-09 01:33:04'),(3,'p cmt 2','230001',2,'2023-08-14 01:33:04'),(4,'bruh','230001',2,'2023-08-19 04:25:01'),(5,'hehehehehe','230001',2,'2023-08-19 04:25:49'),(6,'hehehehehedasdasdas','230001',2,'2023-08-19 04:26:14');
/*!40000 ALTER TABLE `feedback_reply_parent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback_reply_teacher`
--

DROP TABLE IF EXISTS `feedback_reply_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback_reply_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` varchar(500) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  `feedback_id` int(11) NOT NULL,
  `time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `feedback_reply_teacher_teacher_id_fk` (`teacher_id`),
  KEY `feedback_reply_teacher_feedback_id_fk` (`feedback_id`),
  CONSTRAINT `feedback_reply_teacher_feedback_id_fk` FOREIGN KEY (`feedback_id`) REFERENCES `feedback` (`id`),
  CONSTRAINT `feedback_reply_teacher_teacher_id_fk` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback_reply_teacher`
--

LOCK TABLES `feedback_reply_teacher` WRITE;
/*!40000 ALTER TABLE `feedback_reply_teacher` DISABLE KEYS */;
INSERT INTO `feedback_reply_teacher` (`id`, `content`, `teacher_id`, `feedback_id`, `time`) VALUES (1,'t cmt 1',1,2,'2023-08-10 01:34:34'),(2,'t cmt 2',1,2,'2023-08-22 01:34:34'),(3,'hee he',1,4,'2023-08-20 01:04:39'),(4,'bruh',1,4,'2023-08-20 01:04:56'),(5,'hello',1,6,'2023-08-21 00:23:16'),(6,'hello',1,6,'2023-08-21 00:23:20'),(7,'hello',1,6,'2023-08-21 00:23:20'),(8,'hello',1,6,'2023-08-21 00:23:21');
/*!40000 ALTER TABLE `feedback_reply_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parent`
--

DROP TABLE IF EXISTS `parent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parent` (
  `id` varchar(6) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parent`
--

LOCK TABLES `parent` WRITE;
/*!40000 ALTER TABLE `parent` DISABLE KEYS */;
INSERT INTO `parent` (`id`, `name`, `email`, `phone`, `password`) VALUES ('230001','Nguyen Van A','email1@gmail.com','0123456789','$2b$12$Qcsm8lmONsdJOvJoLFWyFecdYH90OimGDmoQgc6hfnDVAQ1dqGAPi');
/*!40000 ALTER TABLE `parent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `phone` int(11) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `class_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  KEY `teacher_class_id_fk` (`class_id`),
  CONSTRAINT `teacher_class_id_fk` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` (`id`, `email`, `phone`, `password`, `name`, `class_id`) VALUES (1,'a@a.a',90123456,'$2b$12$Qcsm8lmONsdJOvJoLFWyFecdYH90OimGDmoQgc6hfnDVAQ1dqGAPi','co giao A',1);
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable`
--

DROP TABLE IF EXISTS `timetable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timetable` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `class_id` int(11) NOT NULL,
  `activity` varchar(100) NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `timetable_class_id_fk` (`class_id`),
  CONSTRAINT `timetable_class_id_fk` FOREIGN KEY (`class_id`) REFERENCES `class` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable`
--

LOCK TABLES `timetable` WRITE;
/*!40000 ALTER TABLE `timetable` DISABLE KEYS */;
/*!40000 ALTER TABLE `timetable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-08-21  1:56:55
