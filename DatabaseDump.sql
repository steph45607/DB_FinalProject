-- MySQL dump 10.13  Distrib 8.0.31, for macos12 (x86_64)
--
-- Host: 35.238.148.78    Database: LibraryDB
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `author_details`
--

DROP TABLE IF EXISTS `author_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `author_details` (
  `id` int NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author_details`
--

LOCK TABLES `author_details` WRITE;
/*!40000 ALTER TABLE `author_details` DISABLE KEYS */;
INSERT INTO `author_details` VALUES (1112,'Colleen','Hoover'),(3939,'Donald','Knuth'),(4321,'Richard','Johnsonbaugh'),(4422,'Silvanus','Thompson'),(5550,'Jon','Bentley'),(6767,'Rachel','Carson'),(7171,'Robert','Martin'),(8888,'Junji','Ito'),(9933,'Marc','Hill');
/*!40000 ALTER TABLE `author_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_details`
--

DROP TABLE IF EXISTS `book_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_details` (
  `id` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `author_id` int NOT NULL,
  `pub_id` int NOT NULL,
  `isbn` bigint NOT NULL,
  `group_id` int NOT NULL,
  `status_id` int NOT NULL,
  `damages_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `author_id` (`author_id`),
  KEY `pub_id` (`pub_id`),
  KEY `status_id` (`status_id`),
  KEY `damages_id` (`damages_id`),
  KEY `group_id` (`group_id`),
  CONSTRAINT `book_details_ibfk_1` FOREIGN KEY (`author_id`) REFERENCES `author_details` (`id`),
  CONSTRAINT `book_details_ibfk_2` FOREIGN KEY (`pub_id`) REFERENCES `publisher_details` (`id`),
  CONSTRAINT `book_details_ibfk_3` FOREIGN KEY (`status_id`) REFERENCES `status_details` (`id`),
  CONSTRAINT `book_details_ibfk_4` FOREIGN KEY (`damages_id`) REFERENCES `damages_details` (`id`),
  CONSTRAINT `book_details_ibfk_5` FOREIGN KEY (`group_id`) REFERENCES `group_details` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_details`
--

LOCK TABLES `book_details` WRITE;
/*!40000 ALTER TABLE `book_details` DISABLE KEYS */;
INSERT INTO `book_details` VALUES (1234,'It Ends with Us',1112,1818,9781501110368,1,1,0),(2345,'Verity',1112,2299,9781408726600,1,0,1),(3456,'Tomie',8888,3848,1421590565,1,1,0),(4567,'Discrete Mathematics',4321,9999,9780131277670,2,0,2),(5432,'Silent Spring',6767,2882,9780141184944,4,0,0),(5678,'Calculus Made Easy',4422,1133,9780312114107,2,0,3),(6543,'Nobody',9933,1818,9781501124969,4,0,0),(6789,'Concrete Mathematics',3939,4849,9787111105763,2,1,0),(7654,'Clean Code',7171,9999,9780132350884,3,0,0),(7890,'Mathematical Writing',3939,1001,9780883850633,2,1,0),(8765,'Algorithms',4321,9999,9780023606922,3,1,0),(9876,'Programming Pearls',5550,4849,9787115151711,3,0,4);
/*!40000 ALTER TABLE `book_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `damages_details`
--

DROP TABLE IF EXISTS `damages_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `damages_details` (
  `id` int NOT NULL,
  `detail` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `damages_details`
--

LOCK TABLES `damages_details` WRITE;
/*!40000 ALTER TABLE `damages_details` DISABLE KEYS */;
INSERT INTO `damages_details` VALUES (0,'No Damage'),(1,'Cover Tear'),(2,'Chipped'),(3,'Dampened'),(4,'Mold');
/*!40000 ALTER TABLE `damages_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `group_details`
--

DROP TABLE IF EXISTS `group_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `group_details` (
  `id` int NOT NULL,
  `group_name` varchar(255) NOT NULL,
  `location` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `group_details`
--

LOCK TABLES `group_details` WRITE;
/*!40000 ALTER TABLE `group_details` DISABLE KEYS */;
INSERT INTO `group_details` VALUES (1,'Fiction','Shelf F'),(2,'Mathematics','Shelf A'),(3,'Programming','Shelf D'),(4,'Nonfiction','Shelf C');
/*!40000 ALTER TABLE `group_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `publisher_details`
--

DROP TABLE IF EXISTS `publisher_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `publisher_details` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `publisher_details`
--

LOCK TABLES `publisher_details` WRITE;
/*!40000 ALTER TABLE `publisher_details` DISABLE KEYS */;
INSERT INTO `publisher_details` VALUES (1001,'The Mathematical Association of America','tmaofa@gmail.com'),(1133,'St. Martins Press','stmartinspress@gmail.com'),(1818,'Atria Books','atria@gmail.com'),(2299,'Grand Central Publishing','gcp@gmail.com'),(2882,'Mariner Books','marinerbooks@gmail.com'),(3848,'ComicsOne','comicsone@gmail.com'),(4849,'Addison Wesley','addisonwesley@gmail.com'),(9999,'Pearson','pearson@gmail.com');
/*!40000 ALTER TABLE `publisher_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_details`
--

DROP TABLE IF EXISTS `role_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_details` (
  `id` int NOT NULL,
  `role_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_details`
--

LOCK TABLES `role_details` WRITE;
/*!40000 ALTER TABLE `role_details` DISABLE KEYS */;
INSERT INTO `role_details` VALUES (1,'student'),(2,'teacher'),(3,'staff');
/*!40000 ALTER TABLE `role_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_details`
--

DROP TABLE IF EXISTS `status_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_details` (
  `id` int NOT NULL,
  `detail` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_details`
--

LOCK TABLES `status_details` WRITE;
/*!40000 ALTER TABLE `status_details` DISABLE KEYS */;
INSERT INTO `status_details` VALUES (0,'unavailable'),(1,'available');
/*!40000 ALTER TABLE `status_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactionStatus_details`
--

DROP TABLE IF EXISTS `transactionStatus_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transactionStatus_details` (
  `id` int NOT NULL,
  `detail` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactionStatus_details`
--

LOCK TABLES `transactionStatus_details` WRITE;
/*!40000 ALTER TABLE `transactionStatus_details` DISABLE KEYS */;
INSERT INTO `transactionStatus_details` VALUES (0,'active'),(1,'returned'),(2,'overdue');
/*!40000 ALTER TABLE `transactionStatus_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_details`
--

DROP TABLE IF EXISTS `transaction_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_details` (
  `transaction_id` int NOT NULL,
  `book_id` int NOT NULL,
  `borrower_id` varchar(255) NOT NULL,
  `borrow_date` date DEFAULT NULL,
  `due_date` date DEFAULT NULL,
  `borrow_status` int NOT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `borrower_id` (`borrower_id`),
  KEY `book_id` (`book_id`),
  KEY `borrow_status` (`borrow_status`),
  CONSTRAINT `transaction_details_ibfk_1` FOREIGN KEY (`borrower_id`) REFERENCES `user_details` (`id`),
  CONSTRAINT `transaction_details_ibfk_2` FOREIGN KEY (`book_id`) REFERENCES `book_details` (`id`),
  CONSTRAINT `transaction_details_ibfk_3` FOREIGN KEY (`borrow_status`) REFERENCES `transactionStatus_details` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_details`
--

LOCK TABLES `transaction_details` WRITE;
/*!40000 ALTER TABLE `transaction_details` DISABLE KEYS */;
INSERT INTO `transaction_details` VALUES (1005,4567,'S1234','2023-01-09','2023-01-16',0),(1550,9876,'ST7878','2022-12-23','2022-12-30',2),(1939,7890,'T8989','2022-12-03','2022-12-10',2),(2662,6789,'S2510','2023-01-02','2023-01-09',2),(3435,5678,'T6767','2023-01-02','2023-01-09',1),(6363,1234,'S1234','2023-01-11','2023-01-18',0),(7274,2345,'S3344','2022-12-29','2023-01-05',2),(7879,3456,'ST1293','2023-01-09','2023-01-16',1),(8844,7654,'T4848','2023-01-08','2023-01-15',1),(8845,6543,'S1234','2023-01-11','2023-01-25',1),(8846,6789,'T6767','2023-01-11','2023-01-25',0),(8847,3456,'S3344','2023-01-11','2023-01-25',1),(8848,1234,'S2510','2023-01-11','2023-01-25',0);
/*!40000 ALTER TABLE `transaction_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_details` (
  `id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_details_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role_details` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_details`
--

LOCK TABLES `user_details` WRITE;
/*!40000 ALTER TABLE `user_details` DISABLE KEYS */;
INSERT INTO `user_details` VALUES ('S1234','Stephanie Staniswinata','stephs@gmail.com',1),('S2510','Maria Clarin','mariac@gmail.com',1),('S3344','Rachel Anastasia','rachana@gmail.com',1),('ST1293','Cindy Jung','cindyju@gmail.com',3),('ST6726','John William','johnw@gmail.com',3),('ST7878','Jane Stevens','janes@gmail.com',3),('ST9922','Michael Owen','michowen@gmail.com',3),('T4848','Raymond Bahana','rbahana@gmail.com',2),('T6767','Nunung Nurul','nnurul@gmail.com',2),('T8989','Ida Bagus','ibagus@gmail.com',2),('T9090','Jude Lamug','judelm@gmail.com',2);
/*!40000 ALTER TABLE `user_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-11 22:54:44
