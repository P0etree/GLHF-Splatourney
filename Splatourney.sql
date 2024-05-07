-- MariaDB dump 10.19  Distrib 10.4.32-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: Splatourney
-- ------------------------------------------------------
-- Server version	10.4.32-MariaDB

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add team',7,'add_team'),(26,'Can change team',7,'change_team'),(27,'Can delete team',7,'delete_team'),(28,'Can view team',7,'view_team'),(29,'Can add moderator',8,'add_moderator'),(30,'Can change moderator',8,'change_moderator'),(31,'Can delete moderator',8,'delete_moderator'),(32,'Can view moderator',8,'view_moderator'),(33,'Can add player',9,'add_player'),(34,'Can change player',9,'change_player'),(35,'Can delete player',9,'delete_player'),(36,'Can view player',9,'view_player'),(37,'Can add player role',10,'add_playerrole'),(38,'Can change player role',10,'change_playerrole'),(39,'Can delete player role',10,'delete_playerrole'),(40,'Can view player role',10,'view_playerrole'),(41,'Can add tournament',11,'add_tournament'),(42,'Can change tournament',11,'change_tournament'),(43,'Can delete tournament',11,'delete_tournament'),(44,'Can view tournament',11,'view_tournament'),(45,'Can add bracket',12,'add_bracket'),(46,'Can change bracket',12,'change_bracket'),(47,'Can delete bracket',12,'delete_bracket'),(48,'Can view bracket',12,'view_bracket'),(49,'Can add bracket column',13,'add_bracketcolumn'),(50,'Can change bracket column',13,'change_bracketcolumn'),(51,'Can delete bracket column',13,'delete_bracketcolumn'),(52,'Can view bracket column',13,'view_bracketcolumn'),(53,'Can add pairing',14,'add_pairing'),(54,'Can change pairing',14,'change_pairing'),(55,'Can delete pairing',14,'delete_pairing'),(56,'Can view pairing',14,'view_pairing'),(57,'Can add game entry',15,'add_gameentry'),(58,'Can change game entry',15,'change_gameentry'),(59,'Can delete game entry',15,'delete_gameentry'),(60,'Can view game entry',15,'view_gameentry'),(61,'Can add schedule',16,'add_schedule'),(62,'Can change schedule',16,'change_schedule'),(63,'Can delete schedule',16,'delete_schedule'),(64,'Can view schedule',16,'view_schedule');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(12,'SplatourneyApp','bracket'),(13,'SplatourneyApp','bracketcolumn'),(15,'SplatourneyApp','gameentry'),(8,'SplatourneyApp','moderator'),(14,'SplatourneyApp','pairing'),(9,'SplatourneyApp','player'),(10,'SplatourneyApp','playerrole'),(16,'SplatourneyApp','schedule'),(7,'SplatourneyApp','team'),(11,'SplatourneyApp','tournament');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'SplatourneyApp','0001_initial','2024-05-07 10:14:59.649370'),(2,'contenttypes','0001_initial','2024-05-07 10:14:59.681037'),(3,'auth','0001_initial','2024-05-07 10:14:59.868815'),(4,'admin','0001_initial','2024-05-07 10:14:59.919748'),(5,'admin','0002_logentry_remove_auto_add','2024-05-07 10:14:59.925748'),(6,'admin','0003_logentry_add_action_flag_choices','2024-05-07 10:14:59.930266'),(7,'contenttypes','0002_remove_content_type_name','2024-05-07 10:14:59.968863'),(8,'auth','0002_alter_permission_name_max_length','2024-05-07 10:15:00.009430'),(9,'auth','0003_alter_user_email_max_length','2024-05-07 10:15:00.028150'),(10,'auth','0004_alter_user_username_opts','2024-05-07 10:15:00.035671'),(11,'auth','0005_alter_user_last_login_null','2024-05-07 10:15:00.061710'),(12,'auth','0006_require_contenttypes_0002','2024-05-07 10:15:00.063709'),(13,'auth','0007_alter_validators_add_error_messages','2024-05-07 10:15:00.069859'),(14,'auth','0008_alter_user_username_max_length','2024-05-07 10:15:00.082892'),(15,'auth','0009_alter_user_last_name_max_length','2024-05-07 10:15:00.096437'),(16,'auth','0010_alter_group_name_max_length','2024-05-07 10:15:00.111620'),(17,'auth','0011_update_proxy_permissions','2024-05-07 10:15:00.125254'),(18,'auth','0012_alter_user_first_name_max_length','2024-05-07 10:15:00.140313'),(19,'sessions','0001_initial','2024-05-07 10:15:00.160393'),(20,'SplatourneyApp','0002_alter_team_team_rank','2024-05-07 10:29:40.874405'),(21,'SplatourneyApp','0003_alter_player_team_id','2024-05-07 11:29:39.308248');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_bracket`
--

DROP TABLE IF EXISTS `splatourneyapp_bracket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_bracket` (
  `bracket_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `bracket_Name` varchar(20) NOT NULL,
  `tournament_title_id` varchar(60) NOT NULL,
  PRIMARY KEY (`bracket_ID`),
  KEY `SplatourneyApp_brack_tournament_title_id_563deefe_fk_Splatourn` (`tournament_title_id`),
  CONSTRAINT `SplatourneyApp_brack_tournament_title_id_563deefe_fk_Splatourn` FOREIGN KEY (`tournament_title_id`) REFERENCES `splatourneyapp_tournament` (`tournament_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_bracket`
--

LOCK TABLES `splatourneyapp_bracket` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_bracket` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_bracket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_bracketcolumn`
--

DROP TABLE IF EXISTS `splatourneyapp_bracketcolumn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_bracketcolumn` (
  `bracketColumn_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `bracketColumn_Name` varchar(20) NOT NULL,
  `bracketColumn_Limit` int(11) NOT NULL,
  `bracket_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`bracketColumn_ID`),
  KEY `SplatourneyApp_brack_bracket_ID_id_e5148c81_fk_Splatourn` (`bracket_ID_id`),
  CONSTRAINT `SplatourneyApp_brack_bracket_ID_id_e5148c81_fk_Splatourn` FOREIGN KEY (`bracket_ID_id`) REFERENCES `splatourneyapp_bracket` (`bracket_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_bracketcolumn`
--

LOCK TABLES `splatourneyapp_bracketcolumn` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_bracketcolumn` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_bracketcolumn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_gameentry`
--

DROP TABLE IF EXISTS `splatourneyapp_gameentry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_gameentry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_Check_in_Status` varchar(11) NOT NULL,
  `game_Result` varchar(4) NOT NULL,
  `pairing_ID_id` bigint(20) NOT NULL,
  `team_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SplatourneyApp_gamee_pairing_ID_id_1d6e6fd5_fk_Splatourn` (`pairing_ID_id`),
  KEY `SplatourneyApp_gamee_team_ID_id_d3eb55d6_fk_Splatourn` (`team_ID_id`),
  CONSTRAINT `SplatourneyApp_gamee_pairing_ID_id_1d6e6fd5_fk_Splatourn` FOREIGN KEY (`pairing_ID_id`) REFERENCES `splatourneyapp_pairing` (`pairing_ID`),
  CONSTRAINT `SplatourneyApp_gamee_team_ID_id_d3eb55d6_fk_Splatourn` FOREIGN KEY (`team_ID_id`) REFERENCES `splatourneyapp_team` (`team_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_gameentry`
--

LOCK TABLES `splatourneyapp_gameentry` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_gameentry` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_gameentry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_moderator`
--

DROP TABLE IF EXISTS `splatourneyapp_moderator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_moderator` (
  `moderator_username` varchar(20) NOT NULL,
  `moderator_password` varchar(20) NOT NULL,
  PRIMARY KEY (`moderator_username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_moderator`
--

LOCK TABLES `splatourneyapp_moderator` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_moderator` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_moderator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_pairing`
--

DROP TABLE IF EXISTS `splatourneyapp_pairing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_pairing` (
  `pairing_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `pairing_Name` varchar(20) NOT NULL,
  `pairing_Status` varchar(11) NOT NULL,
  `bracketColumn_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`pairing_ID`),
  KEY `SplatourneyApp_pairi_bracketColumn_ID_id_e2d354d6_fk_Splatourn` (`bracketColumn_ID_id`),
  CONSTRAINT `SplatourneyApp_pairi_bracketColumn_ID_id_e2d354d6_fk_Splatourn` FOREIGN KEY (`bracketColumn_ID_id`) REFERENCES `splatourneyapp_bracketcolumn` (`bracketColumn_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_pairing`
--

LOCK TABLES `splatourneyapp_pairing` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_pairing` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_pairing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_player`
--

DROP TABLE IF EXISTS `splatourneyapp_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_player` (
  `player_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `player_in_game_name` varchar(20) NOT NULL,
  `player_fname` varchar(20) NOT NULL,
  `player_lname` varchar(20) NOT NULL,
  `player_dc_id` varchar(15) NOT NULL,
  `player_fc` varchar(14) NOT NULL,
  `player_rank` varchar(5) NOT NULL,
  `player_role` varchar(10) NOT NULL,
  `player_type` varchar(10) NOT NULL,
  `player_checkin_status` varchar(20) NOT NULL,
  `Team_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`player_ID`),
  KEY `SplatourneyApp_playe_Team_ID_id_d0265263_fk_Splatourn` (`Team_ID_id`),
  CONSTRAINT `SplatourneyApp_playe_Team_ID_id_d0265263_fk_Splatourn` FOREIGN KEY (`Team_ID_id`) REFERENCES `splatourneyapp_team` (`team_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_player`
--

LOCK TABLES `splatourneyapp_player` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_player` DISABLE KEYS */;
INSERT INTO `splatourneyapp_player` VALUES (1,'a','a','a','a','a','1','Slayer','member','',1);
/*!40000 ALTER TABLE `splatourneyapp_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_playerrole`
--

DROP TABLE IF EXISTS `splatourneyapp_playerrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_playerrole` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `player_role` varchar(20) NOT NULL,
  `player_ID_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `SplatourneyApp_playe_player_ID_id_0edec464_fk_Splatourn` (`player_ID_id`),
  CONSTRAINT `SplatourneyApp_playe_player_ID_id_0edec464_fk_Splatourn` FOREIGN KEY (`player_ID_id`) REFERENCES `splatourneyapp_player` (`player_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_playerrole`
--

LOCK TABLES `splatourneyapp_playerrole` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_playerrole` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_playerrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_schedule`
--

DROP TABLE IF EXISTS `splatourneyapp_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_schedule` (
  `schedule_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `time_Start` time(6) NOT NULL,
  `time_End` time(6) NOT NULL,
  PRIMARY KEY (`schedule_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_schedule`
--

LOCK TABLES `splatourneyapp_schedule` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_schedule` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_team`
--

DROP TABLE IF EXISTS `splatourneyapp_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_team` (
  `team_ID` bigint(20) NOT NULL AUTO_INCREMENT,
  `team_Name` varchar(30) NOT NULL,
  `wins` int(11) NOT NULL,
  `losses` int(11) NOT NULL,
  `team_Rank` int(11) DEFAULT NULL,
  PRIMARY KEY (`team_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_team`
--

LOCK TABLES `splatourneyapp_team` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_team` DISABLE KEYS */;
INSERT INTO `splatourneyapp_team` VALUES (1,'a',0,0,8),(2,'a',0,0,8);
/*!40000 ALTER TABLE `splatourneyapp_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `splatourneyapp_tournament`
--

DROP TABLE IF EXISTS `splatourneyapp_tournament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `splatourneyapp_tournament` (
  `tournament_title` varchar(60) NOT NULL,
  `tournament_description` varchar(300) NOT NULL,
  `tournament_mode` varchar(6) NOT NULL,
  `registration_status` varchar(18) NOT NULL,
  `tournament_status` varchar(12) NOT NULL,
  PRIMARY KEY (`tournament_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `splatourneyapp_tournament`
--

LOCK TABLES `splatourneyapp_tournament` WRITE;
/*!40000 ALTER TABLE `splatourneyapp_tournament` DISABLE KEYS */;
/*!40000 ALTER TABLE `splatourneyapp_tournament` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-07 19:43:03
