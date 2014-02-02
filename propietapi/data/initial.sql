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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'AGENCY'),(2,'AGENT'),(3,'CLIENT'),(4,'USER_DEFAULT'),(5,'USER_SAVED_SEARCH');
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
  KEY `permission_id_refs_id_5886d21f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_5886d21f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
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
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add user profile',4,'add_userprofile'),(11,'Can change user profile',4,'change_userprofile'),(12,'Can delete user profile',4,'delete_userprofile'),(13,'Can add feature',5,'add_feature'),(14,'Can change feature',5,'change_feature'),(15,'Can delete feature',5,'delete_feature'),(16,'Can add operation',6,'add_operation'),(17,'Can change operation',6,'change_operation'),(18,'Can delete operation',6,'delete_operation'),(19,'Can add currency',7,'add_currency'),(20,'Can change currency',7,'change_currency'),(21,'Can delete currency',7,'delete_currency'),(22,'Can add service',8,'add_service'),(23,'Can change service',8,'change_service'),(24,'Can delete service',8,'delete_service'),(25,'Can add category',9,'add_category'),(26,'Can change category',9,'change_category'),(27,'Can delete category',9,'delete_category'),(28,'Can add ambience',10,'add_ambience'),(29,'Can change ambience',10,'change_ambience'),(30,'Can delete ambience',10,'delete_ambience'),(31,'Can add location',11,'add_location'),(32,'Can change location',11,'change_location'),(33,'Can delete location',11,'delete_location'),(34,'Can add property',12,'add_property'),(35,'Can change property',12,'change_property'),(36,'Can delete property',12,'delete_property'),(37,'Can add post',13,'add_post'),(38,'Can change post',13,'change_post'),(39,'Can delete post',13,'delete_post'),(40,'Can add consulting room',14,'add_consultingroom'),(41,'Can change consulting room',14,'change_consultingroom'),(42,'Can delete consulting room',14,'delete_consultingroom'),(43,'Can add country house',15,'add_countryhouse'),(44,'Can change country house',15,'change_countryhouse'),(45,'Can delete country house',15,'delete_countryhouse'),(46,'Can add department',16,'add_department'),(47,'Can change department',16,'change_department'),(48,'Can delete department',16,'delete_department'),(49,'Can add field',17,'add_field'),(50,'Can change field',17,'change_field'),(51,'Can delete field',17,'delete_field'),(52,'Can add garage',18,'add_garage'),(53,'Can change garage',18,'change_garage'),(54,'Can delete garage',18,'delete_garage'),(55,'Can add house',19,'add_house'),(56,'Can change house',19,'change_house'),(57,'Can delete house',19,'delete_house'),(58,'Can add industrial building',20,'add_industrialbuilding'),(59,'Can change industrial building',20,'change_industrialbuilding'),(60,'Can delete industrial building',20,'delete_industrialbuilding'),(61,'Can add land',21,'add_land'),(62,'Can change land',21,'change_land'),(63,'Can delete land',21,'delete_land'),(64,'Can add local',22,'add_local'),(65,'Can change local',22,'change_local'),(66,'Can delete local',22,'delete_local'),(67,'Can add office',23,'add_office'),(68,'Can change office',23,'change_office'),(69,'Can delete office',23,'delete_office'),(70,'Can add ph',24,'add_ph'),(71,'Can change ph',24,'change_ph'),(72,'Can delete ph',24,'delete_ph'),(73,'Can add shed',25,'add_shed'),(74,'Can change shed',25,'change_shed'),(75,'Can delete shed',25,'delete_shed'),(76,'Can add storage',26,'add_storage'),(77,'Can change storage',26,'change_storage'),(78,'Can delete storage',26,'delete_storage'),(79,'Can add saved query',27,'add_savedquery'),(80,'Can change saved query',27,'change_savedquery'),(81,'Can delete saved query',27,'delete_savedquery'),(82,'Can add alert',28,'add_alert'),(83,'Can change alert',28,'change_alert'),(84,'Can delete alert',28,'delete_alert'),(85,'Can add api access',29,'add_apiaccess'),(86,'Can change api access',29,'change_apiaccess'),(87,'Can delete api access',29,'delete_apiaccess'),(88,'Can add api key',30,'add_apikey'),(89,'Can change api key',30,'change_apikey'),(90,'Can delete api key',30,'delete_apikey'),(91,'Can add country',31,'add_country'),(92,'Can change country',31,'change_country'),(93,'Can delete country',31,'delete_country'),(94,'Can add region/state',32,'add_region'),(95,'Can change region/state',32,'change_region'),(96,'Can delete region/state',32,'delete_region'),(97,'Can add city',33,'add_city'),(98,'Can change city',33,'change_city'),(99,'Can delete city',33,'delete_city'),(100,'Can add content type',34,'add_contenttype'),(101,'Can change content type',34,'change_contenttype'),(102,'Can delete content type',34,'delete_contenttype'),(103,'Can add session',35,'add_session'),(104,'Can change session',35,'change_session'),(105,'Can delete session',35,'delete_session'),(106,'Can add site',36,'add_site'),(107,'Can change site',36,'change_site'),(108,'Can delete site',36,'delete_site'),(109,'Can add log entry',37,'add_logentry'),(110,'Can change log entry',37,'change_logentry'),(111,'Can delete log entry',37,'delete_logentry'),(112,'Can add migration history',38,'add_migrationhistory'),(113,'Can change migration history',38,'change_migrationhistory'),(114,'Can delete migration history',38,'delete_migrationhistory'),(115,'Can add sub category',39,'add_subcategory'),(116,'Can change sub category',39,'change_subcategory'),(117,'Can delete sub category',39,'delete_subcategory'),(118,'Can add picture',40,'add_picture'),(119,'Can change picture',40,'change_picture'),(120,'Can delete picture',40,'delete_picture');
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
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
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
INSERT INTO `auth_user` VALUES (2,'propiet','','','propiet@propiet.com','pbkdf2_sha256$10000$Xh8DdR8nRKvN$6g+Cy/+kuiSJsq/nlugkfgXzEIDo4x003yKO6tDa4iQ=',1,1,1,'2014-02-02 12:16:53','2014-01-29 22:44:14');
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
  KEY `group_id_refs_id_f116770` (`group_id`),
  CONSTRAINT `group_id_refs_id_f116770` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_7ceef80f` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,4);
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
  KEY `permission_id_refs_id_67e79cb` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_dfbab7d` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  `name` varchar(200) NOT NULL,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  `latitude` decimal(8,5),
  `longitude` decimal(8,5),
  `search_names` longtext NOT NULL,
  `region_id` int(11),
  `alternate_names` longtext,
  `display_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cities_light_city_region_id_246787ef_uniq` (`region_id`,`name`),
  UNIQUE KEY `cities_light_city_geoname_id_7c39be30_uniq` (`geoname_id`),
  KEY `cities_light_city_52094d6e` (`name`),
  KEY `cities_light_city_25adf148` (`name_ascii`),
  KEY `cities_light_city_56ae2a2a` (`slug`),
  KEY `cities_light_city_534dd89` (`country_id`),
  KEY `cities_light_city_9574fce` (`region_id`),
  CONSTRAINT `country_id_refs_id_107f559b` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `region_id_refs_id_bdfc538` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_city`
--

LOCK TABLES `cities_light_city` WRITE;
/*!40000 ALTER TABLE `cities_light_city` DISABLE KEYS */;
INSERT INTO `cities_light_city` VALUES (1,'Capital Federal','Capital Federal','capital-federal',NULL,1,NULL,NULL,'capitalfederalargentina capitalfederalbuenosairesargentina capitalfederalbsasargentina capitalfederalar capitalfederalbuenosairesar capitalfederalbsasar cabaargentina cababuenosairesargentina cababsasargentina cabaar cababuenosairesar cababsasar',1,'CABA','Capital Federal, Buenos Aires, Argentina');
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
  `name` varchar(200) NOT NULL,
  `name_ascii` varchar(200) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `code2` varchar(2) DEFAULT NULL,
  `code3` varchar(3) DEFAULT NULL,
  `continent` varchar(2) NOT NULL,
  `tld` varchar(5) NOT NULL,
  `geoname_id` int(11) DEFAULT NULL,
  `alternate_names` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `code2` (`code2`),
  UNIQUE KEY `code3` (`code3`),
  UNIQUE KEY `cities_light_country_geoname_id_1986e1f0_uniq` (`geoname_id`),
  KEY `cities_light_country_25adf148` (`name_ascii`),
  KEY `cities_light_country_56ae2a2a` (`slug`),
  KEY `cities_light_country_5d41016a` (`continent`),
  KEY `cities_light_country_3f00a198` (`tld`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_country`
--

LOCK TABLES `cities_light_country` WRITE;
/*!40000 ALTER TABLE `cities_light_country` DISABLE KEYS */;
INSERT INTO `cities_light_country` VALUES (1,'Argentina','Argentina','argentina',NULL,NULL,'SA','',NULL,'AR');
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
  `name` varchar(200) NOT NULL,
  `geoname_code` varchar(50) DEFAULT NULL,
  `country_id` int(11) NOT NULL,
  `geoname_id` int(11),
  `alternate_names` longtext,
  `display_name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cities_light_region_country_id_70adea81_uniq` (`country_id`,`name`),
  UNIQUE KEY `cities_light_region_geoname_id_8afbb85_uniq` (`geoname_id`),
  KEY `cities_light_region_25adf148` (`name_ascii`),
  KEY `cities_light_region_56ae2a2a` (`slug`),
  KEY `cities_light_region_52094d6e` (`name`),
  KEY `cities_light_region_5f45dfed` (`geoname_code`),
  KEY `cities_light_region_534dd89` (`country_id`),
  CONSTRAINT `country_id_refs_id_66726546` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_region`
--

LOCK TABLES `cities_light_region` WRITE;
/*!40000 ALTER TABLE `cities_light_region` DISABLE KEYS */;
INSERT INTO `cities_light_region` VALUES (1,'Buenos Aires','buenos-aires','Buenos Aires',NULL,1,NULL,'BSAS','Buenos Aires, Argentina');
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
  `name` int(11) NOT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `query_id` (`query_id`),
  KEY `core_alert_403f60f` (`user_id`),
  CONSTRAINT `query_id_refs_id_6a5692e5` FOREIGN KEY (`query_id`) REFERENCES `core_saved_query` (`id`),
  CONSTRAINT `user_id_refs_id_4954efb8` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_ambience`
--

LOCK TABLES `core_ambience` WRITE;
/*!40000 ALTER TABLE `core_ambience` DISABLE KEYS */;
INSERT INTO `core_ambience` VALUES (1,'Balcón'),(2,'Baulera'),(3,'Cocina'),(4,'Comedor'),(5,'Comedor de diario'),(6,'Dependencia servicio'),(7,'Dormitorio en suite'),(8,'Escritorio'),(9,'Hall'),(10,'Jardin'),(11,'Lavadero'),(12,'Living'),(13,'Living comedor'),(14,'Patio'),(15,'Terraza'),(16,'Toilette'),(17,'Vestidor');
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_category`
--

LOCK TABLES `core_category` WRITE;
/*!40000 ALTER TABLE `core_category` DISABLE KEYS */;
INSERT INTO `core_category` VALUES (1,'Departamentos'),(2,'Casas'),(3,'PH'),(4,'Countries y Barrios cerrados'),(5,'Quintas'),(6,'Terrenos y Lotes'),(7,'Campos y chacras'),(8,'Galpones, depósitos y edificios industriales'),(9,'Locales comerciales');
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
  `number` int(11) NOT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `country_id` int(11),
  `region_id` int(11),
  `city_id` int(11),
  PRIMARY KEY (`id`),
  KEY `core_location_534dd89` (`country_id`),
  KEY `core_location_9574fce` (`region_id`),
  KEY `core_location_586a73b5` (`city_id`),
  CONSTRAINT `city_id_refs_id_3619157e` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `country_id_refs_id_4aa1b942` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `region_id_refs_id_2a5949a5` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_location`
--

LOCK TABLES `core_location` WRITE;
/*!40000 ALTER TABLE `core_location` DISABLE KEYS */;
INSERT INTO `core_location` VALUES (2,'Las flores',100,'','',1,1,1),(3,'9 de julio',61,'','',1,1,1),(4,'ruta 2 km',203,'','',1,1,1),(5,'Av. Mitre',2250,'','',1,1,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_operation`
--

LOCK TABLES `core_operation` WRITE;
/*!40000 ALTER TABLE `core_operation` DISABLE KEYS */;
INSERT INTO `core_operation` VALUES (1,'Venta'),(2,'Alquiler');
/*!40000 ALTER TABLE `core_operation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_picture`
--

DROP TABLE IF EXISTS `core_picture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_picture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `post_id` int(11) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `file` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_picture_403f60f` (`user_id`),
  KEY `core_picture_699ae8ca` (`post_id`),
  CONSTRAINT `post_id_refs_id_44a56c68` FOREIGN KEY (`post_id`) REFERENCES `core_post` (`id`),
  CONSTRAINT `user_id_refs_id_3c821122` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_picture`
--

LOCK TABLES `core_picture` WRITE;
/*!40000 ALTER TABLE `core_picture` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_picture` ENABLE KEYS */;
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
  `category_id` int(11) NOT NULL,
  `operation_id` int(11) NOT NULL,
  `price` double NOT NULL,
  `currency_id` int(11) NOT NULL,
  `title` varchar(200) NOT NULL,
  `status` int(11) NOT NULL,
  `description` longtext NOT NULL,
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `region_id` int(11),
  `city_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id` (`property_id`),
  KEY `core_post_403f60f` (`user_id`),
  KEY `core_post_42dc49bc` (`category_id`),
  KEY `core_post_4df0bbe` (`operation_id`),
  KEY `core_post_41f657b3` (`currency_id`),
  KEY `core_post_9574fce` (`region_id`),
  KEY `core_post_586a73b5` (`city_id`),
  CONSTRAINT `category_id_refs_id_1fbd777d` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`),
  CONSTRAINT `city_id_refs_id_644511a9` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `currency_id_refs_id_639a7890` FOREIGN KEY (`currency_id`) REFERENCES `core_currency` (`id`),
  CONSTRAINT `operation_id_refs_id_12c30df5` FOREIGN KEY (`operation_id`) REFERENCES `core_operation` (`id`),
  CONSTRAINT `property_id_refs_id_7c0ffcbe` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `region_id_refs_id_589f11a4` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`),
  CONSTRAINT `user_id_refs_id_32fe5aaf` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_post`
--

LOCK TABLES `core_post` WRITE;
/*!40000 ALTER TABLE `core_post` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_post` ENABLE KEYS */;
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
  `creation_date` datetime NOT NULL,
  `last_update` datetime NOT NULL,
  `antiqueness` int(11) NOT NULL,
  `square_meters` double NOT NULL,
  `total_meters` double NOT NULL,
  `total_uncovered_meters` double DEFAULT NULL,
  `location_id` int(11) NOT NULL,
  `suitableCredit` int(11) DEFAULT NULL,
  `providesFunding` int(11) DEFAULT NULL,
  `subcategory_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `location_id` (`location_id`),
  KEY `core_property_403f60f` (`user_id`),
  KEY `core_property_42dc49bc` (`category_id`),
  KEY `core_property_6ec4c7cb` (`subcategory_id`),
  CONSTRAINT `category_id_refs_id_690fb076` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`),
  CONSTRAINT `location_id_refs_id_4a3a734b` FOREIGN KEY (`location_id`) REFERENCES `core_location` (`id`),
  CONSTRAINT `subcategory_id_refs_id_156510fd` FOREIGN KEY (`subcategory_id`) REFERENCES `core_sub_category` (`id`),
  CONSTRAINT `user_id_refs_id_730ba8f6` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property`
--

LOCK TABLES `core_property` WRITE;
/*!40000 ALTER TABLE `core_property` DISABLE KEYS */;
INSERT INTO `core_property` VALUES (2,2,1,'2014-01-29 23:08:53','2014-01-29 23:08:53',0,50,100,NULL,4,NULL,NULL,NULL),(3,2,1,'2014-01-29 23:10:49','2014-01-29 23:10:49',0,50,100,NULL,3,NULL,NULL,NULL);
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
  UNIQUE KEY `core_property_ambiences_property_id_56504891_uniq` (`property_id`,`ambience_id`),
  KEY `core_property_ambiences_6a812853` (`property_id`),
  KEY `core_property_ambiences_10f5294c` (`ambience_id`),
  CONSTRAINT `ambience_id_refs_id_1037d23e` FOREIGN KEY (`ambience_id`) REFERENCES `core_ambience` (`id`),
  CONSTRAINT `property_id_refs_id_749c42b` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_ambiences`
--

LOCK TABLES `core_property_ambiences` WRITE;
/*!40000 ALTER TABLE `core_property_ambiences` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_ambiences` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_consulting_room`
--

DROP TABLE IF EXISTS `core_property_consulting_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_consulting_room` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `garageCoverage` double DEFAULT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_6064e278` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_consulting_room`
--

LOCK TABLES `core_property_consulting_room` WRITE;
/*!40000 ALTER TABLE `core_property_consulting_room` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_consulting_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_country_house`
--

DROP TABLE IF EXISTS `core_property_country_house`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_country_house` (
  `property_ptr_id` int(11) NOT NULL,
  `frontGround` double DEFAULT NULL,
  `largeGround` double DEFAULT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityFloors` int(11) NOT NULL,
  `roofType` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_1073eeab` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_country_house`
--

LOCK TABLES `core_property_country_house` WRITE;
/*!40000 ALTER TABLE `core_property_country_house` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_country_house` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_department`
--

DROP TABLE IF EXISTS `core_property_department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_department` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityAmbiences` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `garageCoverage` double DEFAULT NULL,
  `unityType` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `suitableProfessional` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_4f13b447` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_department`
--

LOCK TABLES `core_property_department` WRITE;
/*!40000 ALTER TABLE `core_property_department` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_department` ENABLE KEYS */;
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
  UNIQUE KEY `core_property_features_property_id_3bd6bc25_uniq` (`property_id`,`feature_id`),
  KEY `core_property_features_6a812853` (`property_id`),
  KEY `core_property_features_7be9b9ad` (`feature_id`),
  CONSTRAINT `feature_id_refs_id_533da6e4` FOREIGN KEY (`feature_id`) REFERENCES `core_feature` (`id`),
  CONSTRAINT `property_id_refs_id_61d18e4c` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_features`
--

LOCK TABLES `core_property_features` WRITE;
/*!40000 ALTER TABLE `core_property_features` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_features` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_field`
--

DROP TABLE IF EXISTS `core_property_field`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_field` (
  `property_ptr_id` int(11) NOT NULL,
  `hectares` double NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_51c7cd94` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_field`
--

LOCK TABLES `core_property_field` WRITE;
/*!40000 ALTER TABLE `core_property_field` DISABLE KEYS */;
INSERT INTO `core_property_field` VALUES (2,3);
/*!40000 ALTER TABLE `core_property_field` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_garage`
--

DROP TABLE IF EXISTS `core_property_garage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_garage` (
  `property_ptr_id` int(11) NOT NULL,
  `garageCoverage` double NOT NULL,
  `expenses` double DEFAULT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_1adc10d0` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_garage`
--

LOCK TABLES `core_property_garage` WRITE;
/*!40000 ALTER TABLE `core_property_garage` DISABLE KEYS */;
INSERT INTO `core_property_garage` VALUES (3,12,NULL);
/*!40000 ALTER TABLE `core_property_garage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_house`
--

DROP TABLE IF EXISTS `core_property_house`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_house` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityFloors` int(11) NOT NULL,
  `roofType` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_754fd900` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_house`
--

LOCK TABLES `core_property_house` WRITE;
/*!40000 ALTER TABLE `core_property_house` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_house` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_industrial_building`
--

DROP TABLE IF EXISTS `core_property_industrial_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_industrial_building` (
  `property_ptr_id` int(11) NOT NULL,
  `fot` int(11) DEFAULT NULL,
  `frontGround` double DEFAULT NULL,
  `largeGround` double DEFAULT NULL,
  `quantityAmbiences` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `quantityShips` int(11) NOT NULL,
  `garageCoverage` double DEFAULT NULL,
  `unityType` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `suitableProfessional` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  `roofType` int(11) NOT NULL,
  `industrialRoofType` int(11) NOT NULL,
  `roofHeight` double DEFAULT NULL,
  `gateType` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_7e8c833a` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_industrial_building`
--

LOCK TABLES `core_property_industrial_building` WRITE;
/*!40000 ALTER TABLE `core_property_industrial_building` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_industrial_building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_land`
--

DROP TABLE IF EXISTS `core_property_land`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_land` (
  `property_ptr_id` int(11) NOT NULL,
  `frontGround` double DEFAULT NULL,
  `largeGround` double DEFAULT NULL,
  `commercialUsage` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_6f61de06` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_land`
--

LOCK TABLES `core_property_land` WRITE;
/*!40000 ALTER TABLE `core_property_land` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_land` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_local`
--

DROP TABLE IF EXISTS `core_property_local`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_local` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_fe76287` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_local`
--

LOCK TABLES `core_property_local` WRITE;
/*!40000 ALTER TABLE `core_property_local` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_local` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_office`
--

DROP TABLE IF EXISTS `core_property_office`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_office` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `garageCoverage` double DEFAULT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_25ef21b` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_office`
--

LOCK TABLES `core_property_office` WRITE;
/*!40000 ALTER TABLE `core_property_office` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_office` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_ph`
--

DROP TABLE IF EXISTS `core_property_ph`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_ph` (
  `property_ptr_id` int(11) NOT NULL,
  `quantityAmbiences` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `quantityBuildingLifts` int(11) DEFAULT NULL,
  `garageCoverage` double DEFAULT NULL,
  `unityType` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `suitableProfessional` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_32d335e9` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_ph`
--

LOCK TABLES `core_property_ph` WRITE;
/*!40000 ALTER TABLE `core_property_ph` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_ph` ENABLE KEYS */;
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
  UNIQUE KEY `core_property_services_property_id_7667c48d_uniq` (`property_id`,`service_id`),
  KEY `core_property_services_6a812853` (`property_id`),
  KEY `core_property_services_6f1d73c2` (`service_id`),
  CONSTRAINT `property_id_refs_id_32f7c62b` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `service_id_refs_id_67790458` FOREIGN KEY (`service_id`) REFERENCES `core_service` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_services`
--

LOCK TABLES `core_property_services` WRITE;
/*!40000 ALTER TABLE `core_property_services` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_shed`
--

DROP TABLE IF EXISTS `core_property_shed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_shed` (
  `property_ptr_id` int(11) NOT NULL,
  `fot` int(11) NOT NULL,
  `frontGround` int(11) NOT NULL,
  `largeGround` int(11) NOT NULL,
  `quantityAmbiences` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `quantityShips` int(11) NOT NULL,
  `garageCoverage` int(11) NOT NULL,
  `unityType` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `suitableProfessional` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  `roofType` int(11) NOT NULL,
  `industrialRoofType` int(11) NOT NULL,
  `roofHeight` double DEFAULT NULL,
  `gateType` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_3067ba33` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_shed`
--

LOCK TABLES `core_property_shed` WRITE;
/*!40000 ALTER TABLE `core_property_shed` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_shed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `core_property_storage`
--

DROP TABLE IF EXISTS `core_property_storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_property_storage` (
  `property_ptr_id` int(11) NOT NULL,
  `fot` double NOT NULL,
  `frontGround` double DEFAULT NULL,
  `largeGround` double DEFAULT NULL,
  `quantityAmbiences` int(11) NOT NULL,
  `quantityBedrooms` int(11) NOT NULL,
  `quantityBathrooms` int(11) NOT NULL,
  `quantityGarages` int(11) NOT NULL,
  `quantityShips` int(11) NOT NULL,
  `garageCoverage` double DEFAULT NULL,
  `unityType` int(11) NOT NULL,
  `orientation` int(11) NOT NULL,
  `disposition` int(11) NOT NULL,
  `buildingType` int(11) NOT NULL,
  `buildingCondition` int(11) NOT NULL,
  `buildingStatus` int(11) NOT NULL,
  `buildingCategory` int(11) NOT NULL,
  `apartmentsPerFloor` int(11) DEFAULT NULL,
  `quantityBuildingFloors` int(11) DEFAULT NULL,
  `floorNumber` int(11) DEFAULT NULL,
  `quantityElevators` int(11) NOT NULL,
  `expenses` double DEFAULT NULL,
  `suitableProfessional` int(11) NOT NULL,
  `lightness` int(11) NOT NULL,
  `roofType` int(11) NOT NULL,
  `industrialRoofType` int(11) NOT NULL,
  `roofHeight` double DEFAULT NULL,
  `gateType` int(11) NOT NULL,
  `commercialUsage` int(11) NOT NULL,
  PRIMARY KEY (`property_ptr_id`),
  CONSTRAINT `property_ptr_id_refs_id_164b9351` FOREIGN KEY (`property_ptr_id`) REFERENCES `core_property` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_property_storage`
--

LOCK TABLES `core_property_storage` WRITE;
/*!40000 ALTER TABLE `core_property_storage` DISABLE KEYS */;
/*!40000 ALTER TABLE `core_property_storage` ENABLE KEYS */;
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
  KEY `core_saved_query_403f60f` (`user_id`),
  CONSTRAINT `user_id_refs_id_348bfbd0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
  KEY `core_sub_category_42dc49bc` (`category_id`),
  CONSTRAINT `category_id_refs_id_1b3e1cc` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_sub_category`
--

LOCK TABLES `core_sub_category` WRITE;
/*!40000 ALTER TABLE `core_sub_category` DISABLE KEYS */;
INSERT INTO `core_sub_category` VALUES (1,1,'Loft'),(2,1,'Piso');
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
  `phone` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  CONSTRAINT `user_id_refs_id_37a2fbb2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_profile`
--

LOCK TABLES `core_user_profile` WRITE;
/*!40000 ALTER TABLE `core_user_profile` DISABLE KEYS */;
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
  KEY `content_type_id_refs_id_288599e6` (`content_type_id`),
  KEY `user_id_refs_id_c8665aa` (`user_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-01-29 22:47:56',2,2,'1','AGENCY',1,''),(2,'2014-01-29 22:48:03',2,2,'2','AGENT',1,''),(3,'2014-01-29 22:48:06',2,2,'3','CLIENT',1,''),(4,'2014-01-29 22:48:09',2,2,'4','USER_DEFAULT',1,''),(5,'2014-01-29 22:48:20',2,3,'2','propiet',2,'Changed password and groups.'),(6,'2014-01-29 22:48:45',2,31,'1','Argentina',1,''),(7,'2014-01-29 22:49:04',2,32,'1','Buenos Aires, Argentina',1,''),(8,'2014-01-29 22:49:26',2,33,'1','Capital Federal, Buenos Aires, Argentina',1,''),(9,'2014-01-29 22:49:55',2,21,'1','Las flores-342 > Buenos Aires-Capital Federal',1,''),(10,'2014-01-29 23:01:59',2,21,'2','Las flores-100 > Buenos Aires-Capital Federal',1,''),(11,'2014-01-29 23:02:19',2,21,'3','9 de julio-61 > Buenos Aires-Capital Federal',1,''),(12,'2014-01-29 23:07:02',2,21,'4','ruta 2 km-203 > Buenos Aires-Capital Federal',1,''),(13,'2014-01-29 23:08:51',2,9,'1','Departamentos',1,''),(14,'2014-01-29 23:08:53',2,17,'2','Departamentos-ruta 2 km-203',1,''),(15,'2014-01-29 23:09:51',2,6,'1','Venta',1,''),(16,'2014-01-29 23:10:07',2,7,'1','ARS$',1,''),(17,'2014-01-29 23:10:10',2,23,'2','Campo en venta ruta 2',1,''),(18,'2014-01-29 23:10:49',2,18,'3','Departamentos-9 de julio-61',1,''),(19,'2014-01-29 23:11:29',2,23,'3','Garage en venta 9 de julio 61 avellaneda',1,''),(20,'2014-01-29 23:11:42',2,23,'3','Garage en venta 9 de julio 61 avellaneda',2,'No fields changed.'),(21,'2014-01-30 20:32:38',2,36,'1','api.propiet.com',1,''),(22,'2014-01-30 21:47:03',2,39,'1','Loft',1,''),(23,'2014-01-30 21:47:26',2,39,'2','Piso',1,''),(24,'2014-01-31 20:49:36',2,9,'2','Casas',1,''),(25,'2014-01-31 20:51:01',2,9,'3','PH',1,''),(26,'2014-01-31 20:51:25',2,9,'4','Countries y Barrios cerrados',1,''),(27,'2014-01-31 20:51:30',2,9,'5','Quintas',1,''),(28,'2014-01-31 20:51:46',2,9,'6','Terrenos y Lotes',1,''),(29,'2014-01-31 20:52:04',2,9,'7','Campos y chacras',1,''),(30,'2014-01-31 20:52:34',2,9,'8','Galpones, depósitos y edificios industriales',1,''),(31,'2014-01-31 20:53:03',2,9,'9','Locales comerciales',1,''),(32,'2014-02-01 04:01:23',2,11,'5','Av. Mitre-2250 > Buenos Aires-Capital Federal',1,''),(33,'2014-02-01 10:19:38',2,6,'2','Alquiler',1,''),(34,'2014-02-01 10:19:49',2,13,'3','Garage en venta 9 de julio 61 avellaneda',2,'Changed operation, region and city.'),(35,'2014-02-01 10:49:39',2,13,'2','Campo en venta ruta 2',2,'Changed region and city.'),(36,'2014-02-01 11:56:52',2,2,'5','SEARCH',1,''),(37,'2014-02-01 11:57:12',2,2,'5','USER_SAVED_SEARCH',2,'Changed name.'),(38,'2014-02-01 14:02:09',2,8,'1','Agua corriente',1,''),(39,'2014-02-01 14:02:16',2,8,'2','Desagüe cloacal',1,''),(40,'2014-02-01 14:02:22',2,8,'3','Gas natural',1,''),(41,'2014-02-01 14:02:30',2,8,'4','Internet',1,''),(42,'2014-02-01 14:02:37',2,8,'5','Luz',1,''),(43,'2014-02-01 14:02:44',2,8,'6','Pavimento',1,''),(44,'2014-02-01 14:02:50',2,8,'7','Teléfono',1,''),(45,'2014-02-01 14:02:58',2,8,'8','Video cable',1,''),(46,'2014-02-01 14:03:08',2,10,'1','Balcón',1,''),(47,'2014-02-01 14:03:15',2,10,'2','Baulera',1,''),(48,'2014-02-01 14:03:25',2,10,'3','Cocina',1,''),(49,'2014-02-01 14:03:32',2,10,'4','Comedor',1,''),(50,'2014-02-01 14:03:39',2,10,'5','Comedor de diario',1,''),(51,'2014-02-01 14:03:47',2,10,'6','Dependencia servicio',1,''),(52,'2014-02-01 14:03:53',2,10,'7','Dormitorio en suite',1,''),(53,'2014-02-01 14:04:01',2,10,'8','Escritorio',1,''),(54,'2014-02-01 14:04:08',2,10,'9','Hall',1,''),(55,'2014-02-01 14:04:14',2,10,'10','Jardin',1,''),(56,'2014-02-01 14:04:22',2,10,'11','Lavadero',1,''),(57,'2014-02-01 14:04:29',2,10,'12','Living',1,''),(58,'2014-02-01 14:04:43',2,10,'13','Living comedor',1,''),(59,'2014-02-01 14:04:51',2,10,'14','Patio',1,''),(60,'2014-02-01 14:04:58',2,10,'15','Terraza',1,''),(61,'2014-02-01 14:05:05',2,10,'16','Toilette',1,''),(62,'2014-02-01 14:05:12',2,10,'17','Vestidor',1,''),(63,'2014-02-02 11:21:33',2,40,'1','1-pic-Campo en venta ruta 2',1,''),(64,'2014-02-02 11:26:48',2,40,'2','2-pic-Garage en venta 9 de julio 61 avellaneda',1,''),(65,'2014-02-02 12:02:13',2,7,'2','US$',1,''),(66,'2014-02-02 12:07:38',2,5,'1','Aire acondicionado',1,''),(67,'2014-02-02 12:07:44',2,5,'2','Alarma',1,''),(68,'2014-02-02 12:07:50',2,5,'3','Amoblado',1,''),(69,'2014-02-02 12:07:56',2,5,'4','Calefacción',1,''),(70,'2014-02-02 12:08:04',2,5,'5','Cancha deportes',1,''),(71,'2014-02-02 12:08:11',2,5,'6','Gimnasio',1,''),(72,'2014-02-02 12:08:18',2,5,'7','Hidromasaje',1,''),(73,'2014-02-02 12:08:35',2,5,'8','Laundry',1,''),(74,'2014-02-02 12:08:46',2,5,'9','Parrilla',1,''),(75,'2014-02-02 12:08:53',2,5,'10','Piscina',1,''),(76,'2014-02-02 12:09:00',2,5,'11','Quincho',1,''),(77,'2014-02-02 12:09:09',2,5,'12','Sala de juegos',1,''),(78,'2014-02-02 12:09:16',2,5,'13','Sauna',1,''),(79,'2014-02-02 12:09:23',2,5,'14','Solarium',1,''),(80,'2014-02-02 12:09:30',2,5,'15','SUM',1,''),(81,'2014-02-02 12:09:36',2,5,'16','Vigilancia',1,''),(82,'2014-02-02 12:10:01',2,19,'4','Casas-Av. Mitre-2250',3,''),(83,'2014-02-02 12:10:52',2,13,'3','Garage en venta 9 de julio 61 avellaneda',3,''),(84,'2014-02-02 12:10:52',2,13,'2','Campo en venta ruta 2',3,''),(85,'2014-02-02 12:11:16',2,3,'1','hoope',3,'');
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
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'user profile','core','userprofile'),(5,'feature','core','feature'),(6,'operation','core','operation'),(7,'currency','core','currency'),(8,'service','core','service'),(9,'category','core','category'),(10,'ambience','core','ambience'),(11,'location','core','location'),(12,'property','core','property'),(13,'post','core','post'),(14,'consulting room','core','consultingroom'),(15,'country house','core','countryhouse'),(16,'department','core','department'),(17,'field','core','field'),(18,'garage','core','garage'),(19,'house','core','house'),(20,'industrial building','core','industrialbuilding'),(21,'land','core','land'),(22,'local','core','local'),(23,'office','core','office'),(24,'ph','core','ph'),(25,'shed','core','shed'),(26,'storage','core','storage'),(27,'saved query','core','savedquery'),(28,'alert','core','alert'),(29,'api access','tastypie','apiaccess'),(30,'api key','tastypie','apikey'),(31,'country','cities_light','country'),(32,'region/state','cities_light','region'),(33,'city','cities_light','city'),(34,'content type','contenttypes','contenttype'),(35,'session','sessions','session'),(36,'site','sites','site'),(37,'log entry','admin','logentry'),(38,'migration history','south','migrationhistory'),(39,'sub category','core','subcategory'),(40,'picture','core','picture');
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
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('4455da5cb8eacdb45197b0dea32d1878','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 11:44:38'),('6259224e8de5f797c13fcb1c487843c3','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-16 12:16:53');
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
INSERT INTO `django_site` VALUES (1,'api.propiet.com','api propiet');
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'core','0001_initial','2014-01-29 22:43:27'),(2,'tastypie','0001_initial','2014-01-29 22:43:28'),(3,'tastypie','0002_add_apikey_index','2014-01-29 22:43:28'),(4,'cities_light','0001_initial','2014-01-29 22:43:28'),(5,'cities_light','0002_city_latitude_and_longitude_added','2014-01-29 22:43:28'),(6,'cities_light','0003_auto__add_field_city_search_names','2014-01-29 22:43:28'),(7,'cities_light','0004_added_region','2014-01-29 22:43:29'),(8,'cities_light','0005_set_region','2014-01-29 22:43:29'),(9,'cities_light','0006_add_city_alternate_names','2014-01-29 22:43:29'),(10,'cities_light','0007_region_geoname_id_to_geoname_code','2014-01-29 22:43:29'),(11,'cities_light','0008_add_region_geoname_id','2014-01-29 22:43:29'),(12,'cities_light','0009_alternate_names_for_all','2014-01-29 22:43:29'),(13,'cities_light','0010_set_geoname_ids','2014-01-29 22:43:29'),(14,'cities_light','0011_add_city_and_region_display_name','2014-01-29 22:43:29'),(15,'cities_light','0012_set_display_name','2014-01-29 22:43:29'),(16,'cities_light','0013_geoname_id_unique_index','2014-01-29 22:43:29'),(17,'cities_light','0014_auto__chg_field_city_search_names','2014-01-29 22:43:29'),(18,'core','0002_auto__del_field_location_city__del_field_location_country__del_field_l','2014-01-29 22:54:23'),(19,'core','0003_auto__add_field_location_country__add_field_location_region__add_field','2014-01-29 23:01:16'),(20,'core','0004_auto__add_subcategory__add_field_property_subcategory','2014-01-30 21:40:11'),(21,'core','0005_auto__add_field_post_region__add_field_post_city','2014-02-01 10:13:09'),(22,'core','0006_auto__add_picture','2014-02-01 14:28:30');
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
  `key` varchar(256) NOT NULL,
  `created` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `user_id_refs_id_56bfdb62` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apikey`
--

LOCK TABLES `tastypie_apikey` WRITE;
/*!40000 ALTER TABLE `tastypie_apikey` DISABLE KEYS */;
INSERT INTO `tastypie_apikey` VALUES (1,2,'4c5be433878e6939a6628d5476d09c9e484c9d5f','2014-01-29 22:44:15');
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

-- Dump completed on 2014-02-02 16:08:01
