-- MySQL dump 10.13  Distrib 5.5.28, for debian-linux-gnu (i686)
--
-- Host: localhost    Database: propiet_db
-- ------------------------------------------------------
-- Server version	5.5.28-0ubuntu0.12.04.3

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (2,'ROLE_ADMIN'),(3,'ROLE_AGENT'),(6,'ROLE_CLIENT'),(4,'ROLE_COMPANY'),(5,'ROLE_SUPER_ADMIN'),(1,'ROLE_USER'),(7,'ROLE_USER_SEARCH');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add log entry',7,'add_logentry'),(20,'Can change log entry',7,'change_logentry'),(21,'Can delete log entry',7,'delete_logentry'),(22,'Can add User Profile',8,'add_userprofile'),(23,'Can change User Profile',8,'change_userprofile'),(24,'Can delete User Profile',8,'delete_userprofile'),(25,'Can add Feature',9,'add_feature'),(26,'Can change Feature',9,'change_feature'),(27,'Can delete Feature',9,'delete_feature'),(28,'Can add Operation',10,'add_operation'),(29,'Can change Operation',10,'change_operation'),(30,'Can delete Operation',10,'delete_operation'),(31,'Can add Currency',11,'add_currency'),(32,'Can change Currency',11,'change_currency'),(33,'Can delete Currency',11,'delete_currency'),(34,'Can add Service',12,'add_service'),(35,'Can change Service',12,'change_service'),(36,'Can delete Service',12,'delete_service'),(37,'Can add Category',13,'add_category'),(38,'Can change Category',13,'change_category'),(39,'Can delete Category',13,'delete_category'),(40,'Can add Subcategory',14,'add_subcategory'),(41,'Can change Subcategory',14,'change_subcategory'),(42,'Can delete Subcategory',14,'delete_subcategory'),(43,'Can add Ambience',15,'add_ambience'),(44,'Can change Ambience',15,'change_ambience'),(45,'Can delete Ambience',15,'delete_ambience'),(46,'Can add Location',16,'add_location'),(47,'Can change Location',16,'change_location'),(48,'Can delete Location',16,'delete_location'),(49,'Can add Property',17,'add_property'),(50,'Can change Property',17,'change_property'),(51,'Can delete Property',17,'delete_property'),(52,'Can add Post',18,'add_post'),(53,'Can change Post',18,'change_post'),(54,'Can delete Post',18,'delete_post'),(55,'Can add Photo',19,'add_postphoto'),(56,'Can change Photo',19,'change_postphoto'),(57,'Can delete Photo',19,'delete_postphoto'),(58,'Can add Saved Query',20,'add_savedquery'),(59,'Can change Saved Query',20,'change_savedquery'),(60,'Can delete Saved Query',20,'delete_savedquery'),(61,'Can add Alert',21,'add_alert'),(62,'Can change Alert',21,'change_alert'),(63,'Can delete Alert',21,'delete_alert'),(64,'Can add api access',22,'add_apiaccess'),(65,'Can change api access',22,'change_apiaccess'),(66,'Can delete api access',22,'delete_apiaccess'),(67,'Can add api key',23,'add_apikey'),(68,'Can change api key',23,'change_apikey'),(69,'Can delete api key',23,'delete_apikey'),(70,'Can add country',24,'add_country'),(71,'Can change country',24,'change_country'),(72,'Can delete country',24,'delete_country'),(73,'Can add region/state',25,'add_region'),(74,'Can change region/state',25,'change_region'),(75,'Can delete region/state',25,'delete_region'),(76,'Can add city',26,'add_city'),(77,'Can change city',26,'change_city'),(78,'Can delete city',26,'delete_city'),(79,'Can add migration history',27,'add_migrationhistory'),(80,'Can change migration history',27,'change_migrationhistory'),(81,'Can delete migration history',27,'delete_migrationhistory');
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
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$12000$9KFvkuMWhI6j$qMqA3KyThel/rC+PkHgIZLYkAzVosS75LFKfnnv+ERc=','2014-04-05 18:10:08',1,'propiet@propiet.com','Admin','Admin','propiet@propiet.com',1,1,'2014-04-05 15:36:44'),(2,'pbkdf2_sha256$12000$oodBRfqeFF0P$ZcluzvY37o/aH7/cFoIG7VWSVVxQV2ECnldSNRaS3b0=','2014-04-05 18:17:23',0,'agente@propiet.com','Agente','Prueba','agente@propiet.com',0,1,'2014-04-05 18:17:06');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (3,1,1),(4,1,2),(5,2,3);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_city`
--

DROP TABLE IF EXISTS `cities_light_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `search_names` longtext NOT NULL,
  `latitude` decimal(8,5) DEFAULT NULL,
  `longitude` decimal(8,5) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  UNIQUE KEY `region_id` (`region_id`,`name`),
  KEY `cities_light_city_37ed44f1` (`name_ascii`),
  KEY `cities_light_city_f52cfca0` (`slug`),
  KEY `cities_light_city_4da47e07` (`name`),
  KEY `cities_light_city_55a4ce96` (`region_id`),
  KEY `cities_light_city_d860be3c` (`country_id`),
  CONSTRAINT `country_id_refs_id_f2111876` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `region_id_refs_id_f574ff13` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_city`
--

LOCK TABLES `cities_light_city` WRITE;
/*!40000 ALTER TABLE `cities_light_city` DISABLE KEYS */;
INSERT INTO `cities_light_city` VALUES (1,'','',NULL,NULL,'Abasto','','',NULL,NULL,1,1),(2,'','',NULL,NULL,'Agronomía','','',NULL,NULL,1,1),(3,'','',NULL,NULL,'Almagro','','',NULL,NULL,1,1),(4,'','',NULL,NULL,'Balvanera','','',NULL,NULL,1,1),(5,'','',NULL,NULL,'Barracas','','',NULL,NULL,1,1),(6,'','',NULL,NULL,'Barrio Norte','','',NULL,NULL,1,1),(7,'','',NULL,NULL,'Belgrano','','',NULL,NULL,1,1),(8,'','',NULL,NULL,'Boca','','',NULL,NULL,1,1),(9,'','',NULL,NULL,'Boedo','','',NULL,NULL,1,1),(10,'','',NULL,NULL,'Caballito','','',NULL,NULL,1,1),(11,'','',NULL,NULL,'Catalinas','','',NULL,NULL,1,1),(12,'','',NULL,NULL,'Microcentro','','',NULL,NULL,1,1),(13,'','',NULL,NULL,'Chacarita','','',NULL,NULL,1,1),(14,'','',NULL,NULL,'Coghlan','','',NULL,NULL,1,1),(15,'','',NULL,NULL,'Colegiales','','',NULL,NULL,1,1),(16,'','',NULL,NULL,'Congreso','','',NULL,NULL,1,1),(17,'','',NULL,NULL,'Constitución','','',NULL,NULL,1,1),(18,'','',NULL,NULL,'Flores','','',NULL,NULL,1,1),(19,'','',NULL,NULL,'Floresta','','',NULL,NULL,1,1),(20,'','',NULL,NULL,'Las Cañitas','','',NULL,NULL,1,1),(21,'','',NULL,NULL,'Liniers','','',NULL,NULL,1,1),(22,'','',NULL,NULL,'Mataderos','','',NULL,NULL,1,1),(23,'','',NULL,NULL,'Monserrat','','',NULL,NULL,1,1),(24,'','',NULL,NULL,'Monte Castro','','',NULL,NULL,1,1),(25,'','',NULL,NULL,'Nuñez','','',NULL,NULL,1,1),(26,'','',NULL,NULL,'Once','','',NULL,NULL,1,1),(27,'','',NULL,NULL,'Palermo','','',NULL,NULL,1,1),(28,'','',NULL,NULL,'Parque Avellaneda','','',NULL,NULL,1,1),(29,'','',NULL,NULL,'Parque Centenario','','',NULL,NULL,1,1),(30,'','',NULL,NULL,'Parque Chacabuco','','',NULL,NULL,1,1),(31,'','',NULL,NULL,'Parque Chas','','',NULL,NULL,1,1),(32,'','',NULL,NULL,'Parque Patricios','','',NULL,NULL,1,1),(33,'','',NULL,NULL,'Paternal','','',NULL,NULL,1,1),(34,'','',NULL,NULL,'Pompeya','','',NULL,NULL,1,1),(35,'','',NULL,NULL,'Puerto Madero','','',NULL,NULL,1,1),(36,'','',NULL,NULL,'Recoleta','','',NULL,NULL,1,1),(37,'','',NULL,NULL,'Retiro','','',NULL,NULL,1,1),(38,'','',NULL,NULL,'Saavedra','','',NULL,NULL,1,1),(39,'','',NULL,NULL,'San Cristobal','','',NULL,NULL,1,1),(40,'','',NULL,NULL,'San Nicolás','','',NULL,NULL,1,1),(41,'','',NULL,NULL,'San Telmo','','',NULL,NULL,1,1),(42,'','',NULL,NULL,'Tribunales','','',NULL,NULL,1,1),(43,'','',NULL,NULL,'Velez Sarsfield','','',NULL,NULL,1,1),(44,'','',NULL,NULL,'Versalles','','',NULL,NULL,1,1),(45,'','',NULL,NULL,'Villa Crespo','','',NULL,NULL,1,1),(46,'','',NULL,NULL,'Villa Devoto','','',NULL,NULL,1,1),(47,'','',NULL,NULL,'Villa General Mitre','','',NULL,NULL,1,1),(48,'','',NULL,NULL,'Villa Lugano','','',NULL,NULL,1,1),(49,'','',NULL,NULL,'Villa Luro','','',NULL,NULL,1,1),(50,'','',NULL,NULL,'Villa Ortuzar','','',NULL,NULL,1,1),(51,'','',NULL,NULL,'Villa Pueyrredón','','',NULL,NULL,1,1),(52,'','',NULL,NULL,'Villa Real','','',NULL,NULL,1,1),(53,'','',NULL,NULL,'Villa Riachuelo','','',NULL,NULL,1,1),(54,'','',NULL,NULL,'Villa Santa Rita','','',NULL,NULL,1,1),(55,'','',NULL,NULL,'Villa Soldati','','',NULL,NULL,1,1),(56,'','',NULL,NULL,'Villa Urquiza','','',NULL,NULL,1,1),(57,'','',NULL,NULL,'Villa del Parque','','',NULL,NULL,1,1);
/*!40000 ALTER TABLE `cities_light_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_country`
--

DROP TABLE IF EXISTS `cities_light_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_country` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `code2` varchar(2) DEFAULT NULL,
  `code3` varchar(3) DEFAULT NULL,
  `continent` varchar(2) NOT NULL,
  `tld` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  UNIQUE KEY `code2` (`code2`),
  UNIQUE KEY `code3` (`code3`),
  KEY `cities_light_country_37ed44f1` (`name_ascii`),
  KEY `cities_light_country_f52cfca0` (`slug`),
  KEY `cities_light_country_72f4141b` (`continent`),
  KEY `cities_light_country_df69a71f` (`tld`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_country`
--

LOCK TABLES `cities_light_country` WRITE;
/*!40000 ALTER TABLE `cities_light_country` DISABLE KEYS */;
INSERT INTO `cities_light_country` VALUES (1,'Argentina','argentina',NULL,'AR','Argentina',NULL,NULL,'SA','');
/*!40000 ALTER TABLE `cities_light_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cities_light_region`
--

DROP TABLE IF EXISTS `cities_light_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities_light_region` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  `name` varchar(200) NOT NULL,
  `display_name` varchar(200) NOT NULL,
  `geoname_code` varchar(50) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_id` (`country_id`,`name`),
  UNIQUE KEY `geoname_id` (`geoname_id`),
  KEY `cities_light_region_37ed44f1` (`name_ascii`),
  KEY `cities_light_region_f52cfca0` (`slug`),
  KEY `cities_light_region_4da47e07` (`name`),
  KEY `cities_light_region_c86134f1` (`geoname_code`),
  KEY `cities_light_region_d860be3c` (`country_id`),
  CONSTRAINT `country_id_refs_id_6e35ae55` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_region`
--

LOCK TABLES `cities_light_region` WRITE;
/*!40000 ALTER TABLE `cities_light_region` DISABLE KEYS */;
INSERT INTO `cities_light_region` VALUES (1,'Capital Federal','capital-federal',NULL,'CABA','Capital Federal','Capital Federal, Argentina',NULL,1);
/*!40000 ALTER TABLE `cities_light_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_alert`
--

DROP TABLE IF EXISTS `core_alert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_alert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `query_id` int(11) NOT NULL,
  `alert_type` int(11) NOT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `query_id` (`query_id`),
  KEY `core_alert_6340c63c` (`user_id`),
  CONSTRAINT `query_id_refs_id_6e52ed5c` FOREIGN KEY (`query_id`) REFERENCES `core_saved_query` (`id`),
  CONSTRAINT `user_id_refs_id_dbe6deea` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_alert`
--

LOCK TABLES `core_alert` WRITE;
/*!40000 ALTER TABLE `core_alert` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_alert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_ambience`
--

DROP TABLE IF EXISTS `core_ambience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_ambience` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_ambience`
--

LOCK TABLES `core_ambience` WRITE;
/*!40000 ALTER TABLE `core_ambience` DISABLE KEYS */;
INSERT INTO `core_ambience` VALUES (1,'Altillo'),(2,'Balcón'),(3,'Baulera'),(4,'Cocina'),(5,'Hall'),(6,'Jardín'),(7,'Patio'),(8,'Sótano'),(9,'Terraza'),(10,'Toilette'),(11,'Comedor'),(12,'Comedor de diario'),(13,'Dependencia de servicio'),(14,'Dormitorio en suite'),(15,'Escritorio'),(16,'Hall'),(17,'Lavadero'),(18,'Living'),(19,'Living comedor'),(20,'Terraza'),(21,'Vestidor');
/*!40000 ALTER TABLE `core_ambience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_category`
--

DROP TABLE IF EXISTS `core_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_category`
--

LOCK TABLES `core_category` WRITE;
/*!40000 ALTER TABLE `core_category` DISABLE KEYS */;
INSERT INTO `core_category` VALUES (1,'Departamentos'),(2,'Casas'),(3,'PH'),(4,'Countries y Barrios cerrados'),(5,'Quintas'),(6,'Terrenos y Lotes'),(7,'Campos y chacras'),(8,'Galpones, depósitos y edificios industriales'),(9,'Locales comerciales'),(10,'Oficinas'),(11,'Consultorios'),(12,'Cocheras');
/*!40000 ALTER TABLE `core_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_currency`
--

DROP TABLE IF EXISTS `core_currency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_currency` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `symbol` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_currency`
--

LOCK TABLES `core_currency` WRITE;
/*!40000 ALTER TABLE `core_currency` DISABLE KEYS */;
INSERT INTO `core_currency` VALUES (1,'ARS$','Pesos'),(2,'US$','Dólares');
/*!40000 ALTER TABLE `core_currency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_feature`
--

DROP TABLE IF EXISTS `core_feature`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_feature` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_feature`
--

LOCK TABLES `core_feature` WRITE;
/*!40000 ALTER TABLE `core_feature` DISABLE KEYS */;
INSERT INTO `core_feature` VALUES (1,'Aire acondicionado'),(2,'Alarma'),(3,'Amoblado'),(4,'Calefacción'),(5,'Cancha deportes'),(6,'Gimnasio'),(7,'Hidromasaje'),(8,'Laundry'),(9,'Parrilla'),(10,'Piscina'),(11,'Quincho'),(12,'Sala de juegos'),(13,'Sauna'),(14,'Solarium'),(15,'SUM'),(16,'Vigilancia');
/*!40000 ALTER TABLE `core_feature` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_location`
--

DROP TABLE IF EXISTS `core_location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(500) NOT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_location_d860be3c` (`country_id`),
  KEY `core_location_55a4ce96` (`region_id`),
  KEY `core_location_b376980e` (`city_id`),
  CONSTRAINT `city_id_refs_id_2bbf48de` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `country_id_refs_id_3cde47e3` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `region_id_refs_id_88552e4b` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_location`
--

LOCK TABLES `core_location` WRITE;
/*!40000 ALTER TABLE `core_location` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_operation`
--

DROP TABLE IF EXISTS `core_operation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_operation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `operation` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_operation`
--

LOCK TABLES `core_operation` WRITE;
/*!40000 ALTER TABLE `core_operation` DISABLE KEYS */;
INSERT INTO `core_operation` VALUES (1,'Venta'),(2,'Alquiler'),(3,'Emprendimiento');
/*!40000 ALTER TABLE `core_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_post`
--

DROP TABLE IF EXISTS `core_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `agent_id` int(11) DEFAULT NULL,
  `category_id` int(11) NOT NULL,
  `operation_id` int(11) NOT NULL,
  `price` double NOT NULL,
  `currency_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `status` smallint(5) unsigned NOT NULL,
  `featured` tinyint(1) NOT NULL,
  `video_url` varchar(500) DEFAULT NULL,
  `map_image_url` varchar(500) DEFAULT NULL,
  `plane_url` varchar(500) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_post_8d69009c` (`property_id`),
  KEY `core_post_6340c63c` (`user_id`),
  KEY `core_post_44625c0c` (`agent_id`),
  KEY `core_post_6f33f001` (`category_id`),
  KEY `core_post_ba874c5c` (`operation_id`),
  KEY `core_post_b2321453` (`currency_id`),
  KEY `core_post_55a4ce96` (`region_id`),
  KEY `core_post_b376980e` (`city_id`),
  CONSTRAINT `agent_id_refs_id_7c48a680` FOREIGN KEY (`agent_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `category_id_refs_id_a9827efd` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`),
  CONSTRAINT `city_id_refs_id_91d5351f` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `currency_id_refs_id_fea7d77c` FOREIGN KEY (`currency_id`) REFERENCES `core_currency` (`id`),
  CONSTRAINT `operation_id_refs_id_adb0cc33` FOREIGN KEY (`operation_id`) REFERENCES `core_operation` (`id`),
  CONSTRAINT `property_id_refs_id_76b8fd6c` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `region_id_refs_id_7b7b129f` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`),
  CONSTRAINT `user_id_refs_id_7c48a680` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_post`
--

LOCK TABLES `core_post` WRITE;
/*!40000 ALTER TABLE `core_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_post_photo`
--

DROP TABLE IF EXISTS `core_post_photo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_post_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) NOT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_post_photo_87a49a9a` (`post_id`),
  CONSTRAINT `post_id_refs_id_c2eacd87` FOREIGN KEY (`post_id`) REFERENCES `core_post` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_post_photo`
--

LOCK TABLES `core_post_photo` WRITE;
/*!40000 ALTER TABLE `core_post_photo` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_post_photo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property`
--

DROP TABLE IF EXISTS `core_property`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `subcategory_id` int(11) DEFAULT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `antiqueness` smallint(5) unsigned NOT NULL,
  `square_meters` double,
  `total_meters` double,
  `total_uncovered_meters` double DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  `lightness` smallint(5) unsigned NOT NULL,
  `orientation` smallint(5) unsigned NOT NULL,
  `disposition` smallint(5) unsigned NOT NULL,
  `quantityAmbiences` smallint(5) unsigned NOT NULL,
  `quantityBathrooms` smallint(5) unsigned NOT NULL,
  `quantityBedrooms` smallint(5) unsigned NOT NULL,
  `quantityGarages` smallint(5) unsigned NOT NULL,
  `garageCoverage` smallint(5) unsigned DEFAULT NULL,
  `buildingType` smallint(5) unsigned NOT NULL,
  `buildingCondition` smallint(5) unsigned NOT NULL,
  `buildingStatus` smallint(5) unsigned NOT NULL,
  `buildingCategory` smallint(5) unsigned NOT NULL,
  `apartmentsPerFloor` smallint(5) unsigned DEFAULT NULL,
  `quantityBuildingFloors` smallint(5) unsigned DEFAULT NULL,
  `floorNumber` smallint(5) unsigned DEFAULT NULL,
  `quantityElevators` smallint(5) unsigned NOT NULL,
  `expenses` double DEFAULT NULL,
  `roofType` smallint(5) unsigned NOT NULL,
  `industrialRoofType` smallint(5) unsigned NOT NULL,
  `roofHeight` double DEFAULT NULL,
  `gateType` smallint(5) unsigned NOT NULL,
  `frontGround` double DEFAULT NULL,
  `largeGround` double DEFAULT NULL,
  `hectares` double DEFAULT NULL,
  `fot` double DEFAULT NULL,
  `fos` double DEFAULT NULL,
  `suitableProfessional` smallint(5) unsigned NOT NULL,
  `commercialUsage` smallint(5) unsigned NOT NULL,
  `suitableCredit` smallint(5) unsigned DEFAULT NULL,
  `providesFunding` smallint(5) unsigned DEFAULT NULL,
  `stage` smallint(5) unsigned NOT NULL,
  `deliveryYear` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `location_id` (`location_id`),
  KEY `core_property_6340c63c` (`user_id`),
  KEY `core_property_6f33f001` (`category_id`),
  KEY `core_property_790ef9fb` (`subcategory_id`),
  CONSTRAINT `category_id_refs_id_e90c3736` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`),
  CONSTRAINT `location_id_refs_id_e3603458` FOREIGN KEY (`location_id`) REFERENCES `core_location` (`id`),
  CONSTRAINT `subcategory_id_refs_id_b4c82e44` FOREIGN KEY (`subcategory_id`) REFERENCES `core_sub_category` (`id`),
  CONSTRAINT `user_id_refs_id_2d3884e0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property`
--

LOCK TABLES `core_property` WRITE;
/*!40000 ALTER TABLE `core_property` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_ambiences`
--

DROP TABLE IF EXISTS `core_property_ambiences`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_ambiences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `ambience_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id` (`property_id`,`ambience_id`),
  KEY `core_property_ambiences_8d69009c` (`property_id`),
  KEY `core_property_ambiences_0bde50ee` (`ambience_id`),
  CONSTRAINT `property_id_refs_id_292e9fae` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `ambience_id_refs_id_2ae7c702` FOREIGN KEY (`ambience_id`) REFERENCES `core_ambience` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_ambiences`
--

LOCK TABLES `core_property_ambiences` WRITE;
/*!40000 ALTER TABLE `core_property_ambiences` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_ambiences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_features`
--

DROP TABLE IF EXISTS `core_property_features`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_features` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `feature_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id` (`property_id`,`feature_id`),
  KEY `core_property_features_8d69009c` (`property_id`),
  KEY `core_property_features_27b2b2cf` (`feature_id`),
  CONSTRAINT `property_id_refs_id_51188b7c` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `feature_id_refs_id_a40968c0` FOREIGN KEY (`feature_id`) REFERENCES `core_feature` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_features`
--

LOCK TABLES `core_property_features` WRITE;
/*!40000 ALTER TABLE `core_property_features` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_services`
--

DROP TABLE IF EXISTS `core_property_services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_services` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `property_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id` (`property_id`,`service_id`),
  KEY `core_property_services_8d69009c` (`property_id`),
  KEY `core_property_services_91a0ac17` (`service_id`),
  CONSTRAINT `property_id_refs_id_ef4b95ff` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `service_id_refs_id_e1f4d5aa` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_services`
--

LOCK TABLES `core_property_services` WRITE;
/*!40000 ALTER TABLE `core_property_services` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_saved_query`
--

DROP TABLE IF EXISTS `core_saved_query`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_saved_query` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `query` longtext NOT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_saved_query_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_bb5a5e1c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_saved_query`
--

LOCK TABLES `core_saved_query` WRITE;
/*!40000 ALTER TABLE `core_saved_query` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_saved_query` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_service`
--

DROP TABLE IF EXISTS `core_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_service`
--

LOCK TABLES `core_service` WRITE;
/*!40000 ALTER TABLE `core_service` DISABLE KEYS */;
INSERT INTO `core_service` VALUES (1,'Agua corriente'),(2,'Desagüe cloacal'),(3,'Gas natural'),(4,'Internet'),(5,'Luz'),(6,'Pavimento'),(7,'Teléfono'),(8,'Video cable');
/*!40000 ALTER TABLE `core_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_sub_category`
--

DROP TABLE IF EXISTS `core_sub_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_sub_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_sub_category_6f33f001` (`category_id`),
  CONSTRAINT `category_id_refs_id_97180265` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sub_category`
--

LOCK TABLES `core_sub_category` WRITE;
/*!40000 ALTER TABLE `core_sub_category` DISABLE KEYS */;
INSERT INTO `core_sub_category` VALUES (1,1,'Dúplex'),(2,1,'Triplex'),(3,1,'Loft'),(4,1,'Piso'),(5,1,'Semipiso'),(6,1,'Penthouse'),(7,1,'Departamento'),(8,2,'Dúplex'),(9,2,'Triplex'),(10,2,'Chalet'),(11,2,'Cabaña'),(12,2,'Casa'),(13,3,'PH'),(14,4,'Casa'),(15,4,'Departamento'),(16,4,'Terreno'),(17,5,'Quintas'),(18,6,'Terrenos y Lotes'),(19,7,'Campos y chacras'),(20,8,'Galpones'),(21,8,'Depósitos'),(22,8,'Edificios industriales'),(23,9,'Locales comerciales'),(24,10,'Oficinas'),(25,11,'Consultorios'),(26,12,'Cocheras');
/*!40000 ALTER TABLE `core_sub_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_user_profile`
--

DROP TABLE IF EXISTS `core_user_profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_user_profile` (
  `user_id` int(11) NOT NULL,
  `phone` longtext NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `user_id_refs_id_88ba6cc8` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_profile`
--

LOCK TABLES `core_user_profile` WRITE;
/*!40000 ALTER TABLE `core_user_profile` DISABLE KEYS */;
INSERT INTO `core_user_profile` VALUES (1,'1550452536'),(2,'541150452536');
/*!40000 ALTER TABLE `core_user_profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-04-05 15:55:55',1,24,'1','Argentina',1,''),(2,'2014-04-05 15:56:17',1,25,'1','Capital Federal, Argentina',1,''),(3,'2014-04-05 16:32:20',1,16,'1','Pergamino 650 > Capital Federal-Saavedra',1,''),(4,'2014-04-05 16:32:30',1,17,'1','Casas-Pergamino 650',1,''),(5,'2014-04-05 16:33:27',1,18,'1','titulo 1',1,''),(6,'2014-04-05 16:50:57',1,2,'1','ROLE_USER',1,''),(7,'2014-04-05 16:51:05',1,2,'2','ROLE_ADMIN',1,''),(8,'2014-04-05 16:51:14',1,2,'3','ROLE_AGENT',1,''),(9,'2014-04-05 16:51:29',1,2,'4','ROLE_COMPANY',1,''),(10,'2014-04-05 16:51:42',1,2,'5','ROLE_SUPER_ADMIN',1,''),(11,'2014-04-05 16:52:31',1,2,'6','ROLE_CLIENT',1,''),(12,'2014-04-05 16:52:40',1,2,'7','ROLE_USER_SEARCH',1,''),(13,'2014-04-05 16:52:56',1,3,'1','propiet@propiet.com',2,'No ha modificado ningún campo.'),(14,'2014-04-05 17:55:56',1,3,'1','propiet@propiet.com',2,'Modifica first_name y last_name.'),(15,'2014-04-05 17:56:18',1,3,'1','propiet@propiet.com',2,'Modifica groups.'),(16,'2014-04-05 18:09:36',1,3,'1','propiet@propiet.com',2,'Se agregó Perfíl de usuario \"propiet@propiet.com\".'),(17,'2014-04-05 18:26:22',1,18,'1','titulo 1',3,''),(18,'2014-04-05 18:35:39',1,18,'3','titulo 1',1,''),(19,'2014-04-06 03:00:59',1,18,'3','titulo 1',3,''),(20,'2014-04-06 03:07:40',1,15,'1','Altillo',1,''),(21,'2014-04-06 03:07:51',1,15,'2','Balcón',1,''),(22,'2014-04-06 03:07:59',1,15,'3','Baulera',1,''),(23,'2014-04-06 03:08:07',1,15,'4','Cocina',1,''),(24,'2014-04-06 03:08:14',1,15,'5','Hall',1,''),(25,'2014-04-06 03:08:23',1,15,'6','Jardín',1,''),(26,'2014-04-06 03:08:31',1,15,'7','Patio',1,''),(27,'2014-04-06 03:08:39',1,15,'8','Sótano',1,''),(28,'2014-04-06 03:08:46',1,15,'9','Terraza',1,''),(29,'2014-04-06 03:08:53',1,15,'10','Toilette',1,''),(30,'2014-04-06 03:10:23',1,15,'11','Comedor',1,''),(31,'2014-04-06 03:10:32',1,15,'12','Comedor de diario',1,''),(32,'2014-04-06 03:10:44',1,15,'13','Dependencia de servicio',1,''),(33,'2014-04-06 03:10:52',1,15,'14','Dormitorio en suite',1,''),(34,'2014-04-06 03:11:00',1,15,'15','Escritorio',1,''),(35,'2014-04-06 03:11:07',1,15,'16','Hall',1,''),(36,'2014-04-06 03:11:15',1,15,'17','Lavadero',1,''),(37,'2014-04-06 03:11:20',1,15,'18','Living',1,''),(38,'2014-04-06 03:11:27',1,15,'19','Living comedor',1,''),(39,'2014-04-06 03:11:36',1,15,'20','Terraza',1,''),(40,'2014-04-06 03:11:42',1,15,'21','Vestidor',1,''),(41,'2014-04-06 03:17:45',1,16,'5','Pergamino 650 > Capital Federal-Boca',3,''),(42,'2014-04-06 03:17:45',1,16,'4','Pergamino 650 > Capital Federal-Boca',3,''),(43,'2014-04-06 03:39:32',1,17,'2','Cocheras-Pergamino 650',1,''),(44,'2014-04-06 03:40:01',1,17,'3','Casas-Pergamino 650',1,''),(45,'2014-04-06 03:42:12',1,17,'3','Casas-Pergamino 650',3,''),(46,'2014-04-06 03:42:12',1,17,'2','Cocheras-Pergamino 650',3,''),(47,'2014-04-06 03:42:25',1,16,'8','Pergamino 650 > Capital Federal-Boca',3,''),(48,'2014-04-06 03:42:25',1,16,'7','Pergamino 650 > Capital Federal-Caballito',3,''),(49,'2014-04-06 03:42:25',1,16,'6','Pergamino 650 > Capital Federal-Barracas',3,''),(50,'2014-04-06 03:44:26',1,16,'9','Pergamino 650 > Capital Federal-Boca',3,''),(51,'2014-04-06 03:46:35',1,17,'4','Cocheras-Pergamino 650',1,''),(52,'2014-04-06 04:15:30',1,17,'4','Cocheras-Pergamino 650',3,''),(53,'2014-04-06 04:26:08',1,17,'5','Cocheras-Pergamino 650',3,''),(54,'2014-04-06 10:11:57',1,18,'5','Casa en venta en la calle Baker Street 221B, Barrio Norte',2,'Se agregó Foto \"4\".'),(55,'2014-04-06 10:40:36',1,18,'5','Casa en venta en la calle Baker Street 221B, Barrio Norte',2,'Se eliminó Foto \"None\". Se eliminó Foto \"None\". Se eliminó Foto \"None\". Se eliminó Foto \"None\".'),(56,'2014-04-06 11:20:00',1,18,'7','Pergamino 650',3,''),(57,'2014-04-06 11:20:00',1,18,'6','Pergamino 650',3,''),(58,'2014-04-06 11:20:23',1,16,'24','Pergamino 650 > Capital Federal-Abasto',3,''),(59,'2014-04-06 11:20:23',1,16,'23','Pergamino 650 > Capital Federal-Abasto',3,''),(60,'2014-04-06 11:20:23',1,16,'22','Baker street 221B > Capital Federal-Barrio Norte',3,''),(61,'2014-04-06 11:20:23',1,16,'21','Baker street 221B > Capital Federal-Abasto',3,''),(62,'2014-04-06 11:20:23',1,16,'20','Baker street 221B > Capital Federal-Abasto',3,''),(63,'2014-04-06 11:20:23',1,16,'19','Baker street 221B > Capital Federal-Barrio Norte',3,''),(64,'2014-04-06 11:20:23',1,16,'18','Pergamino 650 > Capital Federal-Abasto',3,''),(65,'2014-04-06 11:20:23',1,16,'17','Pergamino 650 > Capital Federal-Abasto',3,''),(66,'2014-04-06 11:20:23',1,16,'16','Pergamino 650 > Capital Federal-Abasto',3,''),(67,'2014-04-06 11:20:23',1,16,'15','Pergamino 650 > Capital Federal-Abasto',3,''),(68,'2014-04-06 11:20:23',1,16,'14','Pergamino 650 > Capital Federal-Agronomía',3,''),(69,'2014-04-06 11:20:23',1,16,'13','Pergamino 650 > Capital Federal-Abasto',3,''),(70,'2014-04-06 11:20:23',1,16,'12','Pergamino 650 > Capital Federal-Abasto',3,''),(71,'2014-04-06 11:20:23',1,16,'11','Pergamino 650 > Capital Federal-Abasto',3,''),(72,'2014-04-06 11:20:23',1,16,'10','Pergamino 650 > Capital Federal-Abasto',3,''),(73,'2014-04-06 11:47:44',1,16,'26','Pergamino 650 > Capital Federal-Abasto',3,''),(74,'2014-04-06 12:45:04',1,16,'31','Pergamino 650 > Capital Federal-Abasto',3,''),(75,'2014-04-06 12:45:04',1,16,'30','Pergamino 650 > Capital Federal-Boca',3,''),(76,'2014-04-06 12:45:04',1,16,'29','Pergamino 650 > Capital Federal-Abasto',3,''),(77,'2014-04-06 12:45:04',1,16,'28','Pergamino 650 > Capital Federal-Abasto',3,''),(78,'2014-04-06 12:45:04',1,16,'27','Pergamino 650 > Capital Federal-Abasto',3,''),(79,'2014-04-06 12:45:04',1,16,'25','Pergamino 650 > Capital Federal-Boca',3,'');
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
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'log entry','admin','logentry'),(8,'User Profile','core','userprofile'),(9,'Feature','core','feature'),(10,'Operation','core','operation'),(11,'Currency','core','currency'),(12,'Service','core','service'),(13,'Category','core','category'),(14,'Subcategory','core','subcategory'),(15,'Ambience','core','ambience'),(16,'Location','core','location'),(17,'Property','core','property'),(18,'Post','core','post'),(19,'Photo','core','postphoto'),(20,'Saved Query','core','savedquery'),(21,'Alert','core','alert'),(22,'api access','tastypie','apiaccess'),(23,'api key','tastypie','apikey'),(24,'country','cities_light','country'),(25,'region/state','cities_light','region'),(26,'city','cities_light','city'),(27,'migration history','south','migrationhistory');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
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
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0i3xwmhhwkcfdqxw8wklwtnvqcpob6ix','OWM0NGZjN2RlNmZkMDZjOTI4MGE0ZDA1YTZhMjc2NWFhMDM0OGExNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-04-19 18:09:49'),('j1mzt22hwvwnjm0qkj4d62hye1yfv3r0','OWM0NGZjN2RlNmZkMDZjOTI4MGE0ZDA1YTZhMjc2NWFhMDM0OGExNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-04-19 15:55:38'),('mog4t8pgoj7onoctwwn6qsth94s4wbbp','OWM0NGZjN2RlNmZkMDZjOTI4MGE0ZDA1YTZhMjc2NWFhMDM0OGExNTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=','2014-04-19 18:10:08'),('msdj9be4dbrkjev9r9p7ywpyv8fslpfv','YWY5MzUxNDNmZjMzNDQ3YTM1ZGZiOTBjYTgyY2UzYjIzZDdlYmExZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-04-19 18:17:23');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'core','0002_auto__add_field_property_stage__add_field_property_deliveryYear','2014-04-06 03:06:06'),(2,'core','0003_auto__chg_field_property_total_meters__chg_field_property_square_meter','2014-04-06 03:35:43');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apiaccess`
--

DROP TABLE IF EXISTS `tastypie_apiaccess`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apiaccess` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `identifier` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `request_method` varchar(10) NOT NULL,
  `accessed` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apiaccess`
--

LOCK TABLES `tastypie_apiaccess` WRITE;
/*!40000 ALTER TABLE `tastypie_apiaccess` DISABLE KEYS */;
/*!40000 ALTER TABLE `tastypie_apiaccess` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tastypie_apikey`
--

DROP TABLE IF EXISTS `tastypie_apikey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tastypie_apikey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `key` varchar(128) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `tastypie_apikey_c0d4be93` (`key`),
  CONSTRAINT `user_id_refs_id_990aee10` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apikey`
--

LOCK TABLES `tastypie_apikey` WRITE;
/*!40000 ALTER TABLE `tastypie_apikey` DISABLE KEYS */;
INSERT INTO `tastypie_apikey` VALUES (1,1,'323318c1292865b6888979636b25f5ba501779df','2014-04-05 15:53:03'),(2,2,'f0fe4094bccaea09c954a1fa8b7f5eeda084e89c','2014-04-05 18:17:06');
/*!40000 ALTER TABLE `tastypie_apikey` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-04-06 14:45:50
