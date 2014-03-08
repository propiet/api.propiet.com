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
INSERT INTO `auth_group` VALUES (6,'ROLE_ADMIN'),(2,'ROLE_AGENT'),(3,'ROLE_CLIENT'),(1,'ROLE_COMPANY'),(7,'ROLE_SUPER_ADMIN'),(4,'ROLE_USER'),(5,'ROLE_USER_SEARCH');
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
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (2,'propiet','Propiet','.com','propiet@propiet.com','pbkdf2_sha256$10000$XsEfcimRWkvD$dT3p7nZesh4wxN6gp5ycjyqNZpbcR0zjPhf/xWHe18I=',1,1,1,'2014-03-08 13:12:42','2014-01-29 22:44:14'),(3,'admin','Admin','Propiet','admin@propiet.com','pbkdf2_sha256$10000$P7spv9kZcEI7$FI+kUOOVGUm7cfPjrp1zq9J+c/5YONsZv1b9KaFM/eo=',1,1,1,'2014-02-01 13:32:12','2014-02-01 13:32:00'),(4,'propiet_web_client','web','client','web@propiet.com','pbkdf2_sha256$10000$FlFzNFsaEnNP$7PhSNPcj5gNKj0vn63UETSPhtzn2EhZUlHe+ZH/UYdE=',0,1,0,'2014-02-02 16:35:59','2014-02-02 16:35:59'),(36,'nicolas@hoopemedia.com','Nicolas','Cuevas','nicolas@hoopemedia.com','pbkdf2_sha256$10000$gNlKIu89tsDr$jIyXcRJbA3tIfDxfMKSjTO2SIQUylUg1nA020mrZhMA=',0,1,0,'2014-02-03 19:18:06','2014-02-03 14:28:41'),(37,'agente@propiet.com','Agente','Agente','agente@propiet.com','pbkdf2_sha256$10000$RRqlGGxLBU60$dV7w8Goie+K6WNMrO9lJVDirBlmVMK4Ky4l83BuJY74=',0,1,0,'2014-03-08 12:15:27','2014-03-08 11:47:42'),(42,'inmobiliaria@propiet.com','Inmobiliaria','Inmobiliaria','inmobiliaria@propiet.com','pbkdf2_sha256$10000$EmxFIRaVe91E$+dyCD3NlnCjTUR5b077ALyHUri7QXKFUAnYupkC2TZY=',0,1,0,'2014-03-08 12:47:07','2014-03-08 12:46:40');
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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (12,2,4),(13,4,3),(14,36,1),(15,37,2),(16,42,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (2,4,7);
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
  `latitude` decimal(8,5) DEFAULT NULL,
  `longitude` decimal(8,5) DEFAULT NULL,
  `search_names` longtext NOT NULL,
  `region_id` int(11) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cities_light_city`
--

LOCK TABLES `cities_light_city` WRITE;
/*!40000 ALTER TABLE `cities_light_city` DISABLE KEYS */;
INSERT INTO `cities_light_city` VALUES (0,'Abasto','Abasto','abasto',NULL,1,NULL,NULL,'Abasto',1,'CABA','Abasto'),(1,'Agronomía','Agronomía','agronoma',NULL,1,NULL,NULL,'Agronomía',1,'CABA','Agronomía'),(2,'Almagro','Almagro','almagro',NULL,1,NULL,NULL,'Almagro',1,'CABA','Almagro'),(3,'Balvanera','Balvanera','balvanera',NULL,1,NULL,NULL,'Balvanera',1,'CABA','Balvanera'),(4,'Barracas','Barracas','barracas',NULL,1,NULL,NULL,'Barracas',1,'CABA','Barracas'),(5,'Barrio Norte','Barrio Norte','barrio-norte',NULL,1,NULL,NULL,'Barrio Norte',1,'CABA','Barrio Norte'),(6,'Belgrano','Belgrano','belgrano',NULL,1,NULL,NULL,'Belgrano',1,'CABA','Belgrano'),(7,'Boca','Boca','boca',NULL,1,NULL,NULL,'Boca',1,'CABA','Boca'),(8,'Boedo','Boedo','boedo',NULL,1,NULL,NULL,'Boedo',1,'CABA','Boedo'),(9,'Caballito','Caballito','caballito',NULL,1,NULL,NULL,'Caballito',1,'CABA','Caballito'),(10,'Catalinas','Catalinas','catalinas',NULL,1,NULL,NULL,'Catalinas',1,'CABA','Catalinas'),(11,'Centro / Microcentro','Centro / Microcentro','centro-microcentro',NULL,1,NULL,NULL,'Centro / Microcentro',1,'CABA','Centro / Microcentro'),(12,'Chacarita','Chacarita','chacarita',NULL,1,NULL,NULL,'Chacarita',1,'CABA','Chacarita'),(13,'Coghlan','Coghlan','coghlan',NULL,1,NULL,NULL,'Coghlan',1,'CABA','Coghlan'),(14,'Colegiales','Colegiales','colegiales',NULL,1,NULL,NULL,'Colegiales',1,'CABA','Colegiales'),(15,'Congreso','Congreso','congreso',NULL,1,NULL,NULL,'Congreso',1,'CABA','Congreso'),(16,'Constitución','Constitución','constitucin',NULL,1,NULL,NULL,'Constitución',1,'CABA','Constitución'),(17,'Flores','Flores','flores',NULL,1,NULL,NULL,'Flores',1,'CABA','Flores'),(18,'Floresta','Floresta','floresta',NULL,1,NULL,NULL,'Floresta',1,'CABA','Floresta'),(19,'Las Cañitas','Las Cañitas','las-caitas',NULL,1,NULL,NULL,'Las Cañitas',1,'CABA','Las Cañitas'),(20,'Liniers','Liniers','liniers',NULL,1,NULL,NULL,'Liniers',1,'CABA','Liniers'),(21,'Mataderos','Mataderos','mataderos',NULL,1,NULL,NULL,'Mataderos',1,'CABA','Mataderos'),(22,'Monserrat','Monserrat','monserrat',NULL,1,NULL,NULL,'Monserrat',1,'CABA','Monserrat'),(23,'Monte Castro','Monte Castro','monte-castro',NULL,1,NULL,NULL,'Monte Castro',1,'CABA','Monte Castro'),(24,'Nuñez','Nuñez','nuez',NULL,1,NULL,NULL,'Nuñez',1,'CABA','Nuñez'),(25,'Once','Once','once',NULL,1,NULL,NULL,'Once',1,'CABA','Once'),(26,'Palermo','Palermo','palermo',NULL,1,NULL,NULL,'Palermo',1,'CABA','Palermo'),(27,'Parque Avellaneda','Parque Avellaneda','parque-avellaneda',NULL,1,NULL,NULL,'Parque Avellaneda',1,'CABA','Parque Avellaneda'),(28,'Parque Centenario','Parque Centenario','parque-centenario',NULL,1,NULL,NULL,'Parque Centenario',1,'CABA','Parque Centenario'),(29,'Parque Chacabuco','Parque Chacabuco','parque-chacabuco',NULL,1,NULL,NULL,'Parque Chacabuco',1,'CABA','Parque Chacabuco'),(30,'Parque Chas','Parque Chas','parque-chas',NULL,1,NULL,NULL,'Parque Chas',1,'CABA','Parque Chas'),(31,'Parque Patricios','Parque Patricios','parque-patricios',NULL,1,NULL,NULL,'Parque Patricios',1,'CABA','Parque Patricios'),(32,'Paternal','Paternal','paternal',NULL,1,NULL,NULL,'Paternal',1,'CABA','Paternal'),(33,'Pompeya','Pompeya','pompeya',NULL,1,NULL,NULL,'Pompeya',1,'CABA','Pompeya'),(34,'Puerto Madero','Puerto Madero','puerto-madero',NULL,1,NULL,NULL,'Puerto Madero',1,'CABA','Puerto Madero'),(35,'Recoleta','Recoleta','recoleta',NULL,1,NULL,NULL,'Recoleta',1,'CABA','Recoleta'),(36,'Retiro','Retiro','retiro',NULL,1,NULL,NULL,'Retiro',1,'CABA','Retiro'),(37,'Saavedra','Saavedra','saavedra',NULL,1,NULL,NULL,'Saavedra',1,'CABA','Saavedra'),(38,'San Cristobal','San Cristobal','san-cristobal',NULL,1,NULL,NULL,'San Cristobal',1,'CABA','San Cristobal'),(39,'San Nicolás','San Nicolás','san-nicols',NULL,1,NULL,NULL,'San Nicolás',1,'CABA','San Nicolás'),(40,'San Telmo','San Telmo','san-telmo',NULL,1,NULL,NULL,'San Telmo',1,'CABA','San Telmo'),(41,'Tribunales','Tribunales','tribunales',NULL,1,NULL,NULL,'Tribunales',1,'CABA','Tribunales'),(42,'Velez Sarsfield','Velez Sarsfield','velez-sarsfield',NULL,1,NULL,NULL,'Velez Sarsfield',1,'CABA','Velez Sarsfield'),(43,'Versalles','Versalles','versalles',NULL,1,NULL,NULL,'Versalles',1,'CABA','Versalles'),(44,'Villa Crespo','Villa Crespo','villa-crespo',NULL,1,NULL,NULL,'Villa Crespo',1,'CABA','Villa Crespo'),(45,'Villa Devoto','Villa Devoto','villa-devoto',NULL,1,NULL,NULL,'Villa Devoto',1,'CABA','Villa Devoto'),(46,'Villa General Mitre','Villa General Mitre','villa-general-mitre',NULL,1,NULL,NULL,'Villa General Mitre',1,'CABA','Villa General Mitre'),(47,'Villa Lugano','Villa Lugano','villa-lugano',NULL,1,NULL,NULL,'Villa Lugano',1,'CABA','Villa Lugano'),(48,'Villa Luro','Villa Luro','villa-luro',NULL,1,NULL,NULL,'Villa Luro',1,'CABA','Villa Luro'),(49,'Villa Ortuzar','Villa Ortuzar','villa-ortuzar',NULL,1,NULL,NULL,'Villa Ortuzar',1,'CABA','Villa Ortuzar'),(50,'Villa Pueyrredón','Villa Pueyrredón','villa-pueyrredn',NULL,1,NULL,NULL,'Villa Pueyrredón',1,'CABA','Villa Pueyrredón'),(51,'Villa Real','Villa Real','villa-real',NULL,1,NULL,NULL,'Villa Real',1,'CABA','Villa Real'),(52,'Villa Riachuelo','Villa Riachuelo','villa-riachuelo',NULL,1,NULL,NULL,'Villa Riachuelo',1,'CABA','Villa Riachuelo'),(53,'Villa Santa Rita','Villa Santa Rita','villa-santa-rita',NULL,1,NULL,NULL,'Villa Santa Rita',1,'CABA','Villa Santa Rita'),(54,'Villa Soldati','Villa Soldati','villa-soldati',NULL,1,NULL,NULL,'Villa Soldati',1,'CABA','Villa Soldati'),(55,'Villa Urquiza','Villa Urquiza','villa-urquiza',NULL,1,NULL,NULL,'Villa Urquiza',1,'CABA','Villa Urquiza'),(56,'Villa del Parque','Villa del Parque','villa-del-parque',NULL,1,NULL,NULL,'Villa del Parque',1,'CABA','Villa del Parque');
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
  `geoname_id` int(11) DEFAULT NULL,
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
INSERT INTO `cities_light_region` VALUES (1,'Capital Federal','Capital Federal','capital-federal',NULL,1,NULL,'CABA','Cap Fed,Bs As,Argentina');
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
  `number` int(11) NOT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `country_id` int(11) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `core_location_534dd89` (`country_id`),
  KEY `core_location_9574fce` (`region_id`),
  KEY `core_location_586a73b5` (`city_id`),
  CONSTRAINT `city_id_refs_id_3619157e` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `country_id_refs_id_4aa1b942` FOREIGN KEY (`country_id`) REFERENCES `cities_light_country` (`id`),
  CONSTRAINT `region_id_refs_id_2a5949a5` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `region_id` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `agent_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `property_id` (`property_id`),
  KEY `core_post_403f60f` (`user_id`),
  KEY `core_post_42dc49bc` (`category_id`),
  KEY `core_post_4df0bbe` (`operation_id`),
  KEY `core_post_41f657b3` (`currency_id`),
  KEY `core_post_9574fce` (`region_id`),
  KEY `core_post_586a73b5` (`city_id`),
  KEY `core_post_3c13e242` (`agent_id`),
  CONSTRAINT `agent_id_refs_id_32fe5aaf` FOREIGN KEY (`agent_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `category_id_refs_id_1fbd777d` FOREIGN KEY (`category_id`) REFERENCES `core_category` (`id`),
  CONSTRAINT `city_id_refs_id_644511a9` FOREIGN KEY (`city_id`) REFERENCES `cities_light_city` (`id`),
  CONSTRAINT `currency_id_refs_id_639a7890` FOREIGN KEY (`currency_id`) REFERENCES `core_currency` (`id`),
  CONSTRAINT `operation_id_refs_id_12c30df5` FOREIGN KEY (`operation_id`) REFERENCES `core_operation` (`id`),
  CONSTRAINT `property_id_refs_id_7c0ffcbe` FOREIGN KEY (`property_id`) REFERENCES `core_property` (`id`),
  CONSTRAINT `region_id_refs_id_589f11a4` FOREIGN KEY (`region_id`) REFERENCES `cities_light_region` (`id`),
  CONSTRAINT `user_id_refs_id_32fe5aaf` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
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
  `subcategory_id` int(11) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
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
  CONSTRAINT `user_id_refs_id_37a2fbb2` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_user_profile`
--

LOCK TABLES `core_user_profile` WRITE;
/*!40000 ALTER TABLE `core_user_profile` DISABLE KEYS */;
INSERT INTO `core_user_profile` VALUES (36,'1136707653'),(42,'5491150452536');
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
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-01-29 22:47:56',2,2,'1','AGENCY',1,''),(2,'2014-01-29 22:48:03',2,2,'2','AGENT',1,''),(3,'2014-01-29 22:48:06',2,2,'3','CLIENT',1,''),(4,'2014-01-29 22:48:09',2,2,'4','USER_DEFAULT',1,''),(5,'2014-01-29 22:48:20',2,3,'2','propiet',2,'Changed password and groups.'),(6,'2014-01-29 22:48:45',2,31,'1','Argentina',1,''),(7,'2014-01-29 22:49:04',2,32,'1','Buenos Aires, Argentina',1,''),(8,'2014-01-29 22:49:26',2,33,'1','Capital Federal, Buenos Aires, Argentina',1,''),(9,'2014-01-29 22:49:55',2,21,'1','Las flores-342 > Buenos Aires-Capital Federal',1,''),(10,'2014-01-29 23:01:59',2,21,'2','Las flores-100 > Buenos Aires-Capital Federal',1,''),(11,'2014-01-29 23:02:19',2,21,'3','9 de julio-61 > Buenos Aires-Capital Federal',1,''),(12,'2014-01-29 23:07:02',2,21,'4','ruta 2 km-203 > Buenos Aires-Capital Federal',1,''),(13,'2014-01-29 23:08:51',2,9,'1','Departamentos',1,''),(14,'2014-01-29 23:08:53',2,17,'2','Departamentos-ruta 2 km-203',1,''),(15,'2014-01-29 23:09:51',2,6,'1','Venta',1,''),(16,'2014-01-29 23:10:07',2,7,'1','ARS$',1,''),(17,'2014-01-29 23:10:10',2,23,'2','Campo en venta ruta 2',1,''),(18,'2014-01-29 23:10:49',2,18,'3','Departamentos-9 de julio-61',1,''),(19,'2014-01-29 23:11:29',2,23,'3','Garage en venta 9 de julio 61 avellaneda',1,''),(20,'2014-01-29 23:11:42',2,23,'3','Garage en venta 9 de julio 61 avellaneda',2,'No fields changed.'),(21,'2014-01-30 20:32:38',2,36,'1','api.propiet.com',1,''),(22,'2014-01-30 21:47:03',2,39,'1','Loft',1,''),(23,'2014-01-30 21:47:26',2,39,'2','Piso',1,''),(24,'2014-01-31 20:49:36',2,9,'2','Casas',1,''),(25,'2014-01-31 20:51:01',2,9,'3','PH',1,''),(26,'2014-01-31 20:51:25',2,9,'4','Countries y Barrios cerrados',1,''),(27,'2014-01-31 20:51:30',2,9,'5','Quintas',1,''),(28,'2014-01-31 20:51:46',2,9,'6','Terrenos y Lotes',1,''),(29,'2014-01-31 20:52:04',2,9,'7','Campos y chacras',1,''),(30,'2014-01-31 20:52:34',2,9,'8','Galpones, depósitos y edificios industriales',1,''),(31,'2014-01-31 20:53:03',2,9,'9','Locales comerciales',1,''),(32,'2014-02-01 04:01:23',2,11,'5','Av. Mitre-2250 > Buenos Aires-Capital Federal',1,''),(33,'2014-02-01 10:19:38',2,6,'2','Alquiler',1,''),(34,'2014-02-01 10:19:49',2,13,'3','Garage en venta 9 de julio 61 avellaneda',2,'Changed operation, region and city.'),(35,'2014-02-01 10:49:39',2,13,'2','Campo en venta ruta 2',2,'Changed region and city.'),(36,'2014-02-01 11:56:52',2,2,'5','SEARCH',1,''),(37,'2014-02-01 11:57:12',2,2,'5','USER_SAVED_SEARCH',2,'Changed name.'),(38,'2014-02-01 14:02:09',2,8,'1','Agua corriente',1,''),(39,'2014-02-01 14:02:16',2,8,'2','Desagüe cloacal',1,''),(40,'2014-02-01 14:02:22',2,8,'3','Gas natural',1,''),(41,'2014-02-01 14:02:30',2,8,'4','Internet',1,''),(42,'2014-02-01 14:02:37',2,8,'5','Luz',1,''),(43,'2014-02-01 14:02:44',2,8,'6','Pavimento',1,''),(44,'2014-02-01 14:02:50',2,8,'7','Teléfono',1,''),(45,'2014-02-01 14:02:58',2,8,'8','Video cable',1,''),(46,'2014-02-01 14:03:08',2,10,'1','Balcón',1,''),(47,'2014-02-01 14:03:15',2,10,'2','Baulera',1,''),(48,'2014-02-01 14:03:25',2,10,'3','Cocina',1,''),(49,'2014-02-01 14:03:32',2,10,'4','Comedor',1,''),(50,'2014-02-01 14:03:39',2,10,'5','Comedor de diario',1,''),(51,'2014-02-01 14:03:47',2,10,'6','Dependencia servicio',1,''),(52,'2014-02-01 14:03:53',2,10,'7','Dormitorio en suite',1,''),(53,'2014-02-01 14:04:01',2,10,'8','Escritorio',1,''),(54,'2014-02-01 14:04:08',2,10,'9','Hall',1,''),(55,'2014-02-01 14:04:14',2,10,'10','Jardin',1,''),(56,'2014-02-01 14:04:22',2,10,'11','Lavadero',1,''),(57,'2014-02-01 14:04:29',2,10,'12','Living',1,''),(58,'2014-02-01 14:04:43',2,10,'13','Living comedor',1,''),(59,'2014-02-01 14:04:51',2,10,'14','Patio',1,''),(60,'2014-02-01 14:04:58',2,10,'15','Terraza',1,''),(61,'2014-02-01 14:05:05',2,10,'16','Toilette',1,''),(62,'2014-02-01 14:05:12',2,10,'17','Vestidor',1,''),(63,'2014-02-02 11:21:33',2,40,'1','1-pic-Campo en venta ruta 2',1,''),(64,'2014-02-02 11:26:48',2,40,'2','2-pic-Garage en venta 9 de julio 61 avellaneda',1,''),(65,'2014-02-02 12:02:13',2,7,'2','US$',1,''),(66,'2014-02-02 12:07:38',2,5,'1','Aire acondicionado',1,''),(67,'2014-02-02 12:07:44',2,5,'2','Alarma',1,''),(68,'2014-02-02 12:07:50',2,5,'3','Amoblado',1,''),(69,'2014-02-02 12:07:56',2,5,'4','Calefacción',1,''),(70,'2014-02-02 12:08:04',2,5,'5','Cancha deportes',1,''),(71,'2014-02-02 12:08:11',2,5,'6','Gimnasio',1,''),(72,'2014-02-02 12:08:18',2,5,'7','Hidromasaje',1,''),(73,'2014-02-02 12:08:35',2,5,'8','Laundry',1,''),(74,'2014-02-02 12:08:46',2,5,'9','Parrilla',1,''),(75,'2014-02-02 12:08:53',2,5,'10','Piscina',1,''),(76,'2014-02-02 12:09:00',2,5,'11','Quincho',1,''),(77,'2014-02-02 12:09:09',2,5,'12','Sala de juegos',1,''),(78,'2014-02-02 12:09:16',2,5,'13','Sauna',1,''),(79,'2014-02-02 12:09:23',2,5,'14','Solarium',1,''),(80,'2014-02-02 12:09:30',2,5,'15','SUM',1,''),(81,'2014-02-02 12:09:36',2,5,'16','Vigilancia',1,''),(82,'2014-02-02 12:10:01',2,19,'4','Casas-Av. Mitre-2250',3,''),(83,'2014-02-02 12:10:52',2,13,'3','Garage en venta 9 de julio 61 avellaneda',3,''),(84,'2014-02-02 12:10:52',2,13,'2','Campo en venta ruta 2',3,''),(85,'2014-02-02 12:11:16',2,3,'1','hoope',3,''),(86,'2014-02-02 16:35:59',2,3,'4','propiet_web_client',1,''),(87,'2014-02-02 16:36:44',2,3,'4','propiet_web_client',2,'Changed password, first_name, last_name, groups and user_permissions.'),(88,'2014-02-03 07:14:44',2,3,'5','sharedaplication@test.com',3,''),(89,'2014-02-03 07:21:58',2,3,'6','test@hotmail.com',3,''),(90,'2014-02-03 07:23:23',2,3,'7','test@hotmail.com',3,''),(91,'2014-02-03 07:25:10',2,3,'9','sharedaplication@hotmail.com',3,''),(92,'2014-02-03 07:29:48',2,3,'10','sharedaplication@hotmail.com',3,''),(93,'2014-02-03 07:32:18',2,3,'11','test@test.coms',2,'Changed password.'),(94,'2014-02-03 07:32:25',2,3,'11','test@test.com',2,'Changed username and password.'),(95,'2014-02-03 14:28:05',2,3,'11','test@test.com',3,''),(96,'2014-02-03 14:45:55',2,13,'4','9 de julio depto venta',1,''),(97,'2014-02-03 14:46:00',2,13,'4','9 de julio depto venta',2,'No fields changed.'),(98,'2014-02-03 14:47:17',2,13,'5','Departamento Alquiler  Capital  Fed - CAballito',1,''),(99,'2014-03-08 11:20:23',2,39,'3','aaaa',1,''),(100,'2014-03-08 11:20:39',2,39,'1','Dúplex',2,'Changed name.'),(101,'2014-03-08 11:20:47',2,39,'2','Triplex',2,'Changed name.'),(102,'2014-03-08 11:20:54',2,39,'3','Loft',2,'Changed name.'),(103,'2014-03-08 11:21:08',2,39,'4','Piso',1,''),(104,'2014-03-08 11:21:14',2,39,'5','Semipiso',1,''),(105,'2014-03-08 11:21:20',2,39,'6','Penthouse',1,''),(106,'2014-03-08 11:21:26',2,39,'7','Departamento',1,''),(107,'2014-03-08 11:21:34',2,39,'8','Dúplex',1,''),(108,'2014-03-08 11:21:41',2,39,'9','Triplex',1,''),(109,'2014-03-08 11:21:46',2,39,'10','Chalet',1,''),(110,'2014-03-08 11:21:52',2,39,'11','Cabaña',1,''),(111,'2014-03-08 11:21:57',2,39,'12','Casa',1,''),(112,'2014-03-08 11:22:05',2,39,'13','PH',1,''),(113,'2014-03-08 11:22:12',2,39,'14','Casa',1,''),(114,'2014-03-08 11:22:19',2,39,'15','Departamento',1,''),(115,'2014-03-08 11:22:25',2,39,'16','Terreno',1,''),(116,'2014-03-08 11:22:32',2,39,'17','Quintas',1,''),(117,'2014-03-08 11:22:51',2,39,'18','Terrenos y Lotes',1,''),(118,'2014-03-08 11:23:03',2,39,'19','Campos y chacras',1,''),(119,'2014-03-08 11:23:12',2,39,'20','Galpones',1,''),(120,'2014-03-08 11:23:19',2,39,'21','Depósitos',1,''),(121,'2014-03-08 11:23:28',2,39,'22','Edificios industriales',1,''),(122,'2014-03-08 11:23:37',2,39,'23','Locales comerciales',1,''),(123,'2014-03-08 11:24:51',2,39,'24','Oficinas',1,''),(124,'2014-03-08 11:25:14',2,9,'10','ss',1,''),(125,'2014-03-08 11:25:24',2,9,'10','Oficinas',2,'Changed name.'),(126,'2014-03-08 11:25:29',2,9,'11','Consultorios',1,''),(127,'2014-03-08 11:25:33',2,9,'12','Cocheras',1,''),(128,'2014-03-08 11:25:47',2,39,'24','Oficinas',2,'Changed category.'),(129,'2014-03-08 11:25:54',2,39,'25','Consultorios',1,''),(130,'2014-03-08 11:26:03',2,39,'26','Cocheras',1,''),(131,'2014-03-08 11:26:26',2,11,'6','a-0 > Capital Federal-Abasto',1,''),(132,'2014-03-08 11:26:32',2,11,'6','a-0 > Capital Federal-Abasto',3,''),(133,'2014-03-08 11:26:32',2,11,'5','Av. Mitre-2250 > Capital Federal-Agronomía',3,''),(134,'2014-03-08 11:26:32',2,11,'4','ruta 2 km-203 > Capital Federal-Agronomía',3,''),(135,'2014-03-08 11:26:32',2,11,'3','9 de julio-61 > Capital Federal-Agronomía',3,''),(136,'2014-03-08 11:26:32',2,11,'2','Las flores-100 > Capital Federal-Agronomía',3,''),(137,'2014-03-08 11:26:56',2,2,'6','a',1,''),(138,'2014-03-08 11:27:06',2,2,'4','ROLE_USER',2,'Changed name.'),(139,'2014-03-08 11:27:16',2,2,'3','ROLE_CLIENT',2,'Changed name.'),(140,'2014-03-08 11:27:23',2,2,'1','ROLE_COMPANY',2,'Changed name.'),(141,'2014-03-08 11:27:32',2,2,'5','ROLE_USER_SEARCH',2,'Changed name.'),(142,'2014-03-08 11:27:40',2,2,'2','ROLE_AGENT',2,'Changed name.'),(143,'2014-03-08 11:27:50',2,2,'6','ROLE_ADMIN',2,'Changed name.'),(144,'2014-03-08 11:28:00',2,2,'7','ROLE_SUPER_ADMIN',1,''),(145,'2014-03-08 11:29:20',2,3,'2','propiet',2,'Changed password, first_name and last_name.'),(146,'2014-03-08 11:29:39',2,3,'3','Admin',2,'Changed username, password, first_name, last_name and email.'),(147,'2014-03-08 11:30:04',2,3,'4','propiet_web_client',2,'Changed password, first_name, last_name and email.'),(148,'2014-03-08 11:30:17',2,3,'3','admin',2,'Changed username and password.'),(149,'2014-03-08 11:30:50',2,3,'36','nicolas@hoopemedia.com',2,'Changed username, password, first_name, last_name and email.'),(150,'2014-03-08 11:31:27',2,6,'3','Emprendimiento',1,''),(151,'2014-03-08 12:44:24',2,11,'7','Baker Street-221 > Capital Federal-Flores',3,'');
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
INSERT INTO `django_session` VALUES ('01681d318253101c6803cb14a026bf66','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 10:43:09'),('01fa52c546055dfc9f9cc2a73fc044b0','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-03-22 13:12:42'),('059d6d7af1872fe0269bbe4929393cdf','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:30:39'),('07d691bc6921b351835711e11d961987','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 10:08:07'),('0d24e925ea20833e16609a826cf442d0','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 23:49:56'),('0db1081eebb5f7ca437418eec64af7b6','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-16 19:13:53'),('17824e2fe8e1316bf7ce1c25fbb68c10','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 23:49:16'),('2520f67afe3af3e914303e7dc85b33d8','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 09:58:19'),('2702af1d04cf9243c0ad0040f9927b74','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:20:24'),('28b719a4b3e0256a941f459db84eb554','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 10:05:56'),('2e516c3b2300c639efbea221a628bab0','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 23:48:49'),('2e60fc7ca968367125760c8f53cae54c','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:17:49'),('2e7a491555b67b1e2490402a334ff234','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:26:56'),('343e00e52a36639e1a3f6b5ba56e291f','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 15:02:29'),('391bfea4f7ad98214c61e9a5911b8e05','YmM3OWNjMjg0MWEzMTU1NjlkMThlMjczMTJjMDQ4YzUyZmM4Mjk2ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg==\n','2014-03-22 12:14:10'),('3d301095b46d673a6e402270e38fa4d3','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-03-22 11:41:04'),('41f7d97e4fa65d0d5321ea87b78dd735','ZGI4OTBiNDQ1ZWJhMDJhZGMyNTM3Yzg2ZDMxOTNhNWU0MjYxYjZmODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASp1Lg==\n','2014-03-22 12:47:08'),('4231992d4e835899ea1bfbcd7b4d838a','NGJmZjczZmI0ZDhiNTc1NmViZThkMjk2ZmRmOTQyYzdmZjcyZTdmNTqAAn1xAVUKdGVzdGNvb2tp\nZXECVQZ3b3JrZWRxA3Mu\n','2014-02-22 01:43:46'),('4455da5cb8eacdb45197b0dea32d1878','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 11:44:38'),('49d99cf75af48a4a367d247f122c4663','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:50:12'),('4a49ed1adad81eba88559fde7ebf5a4c','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:19:53'),('50c18f7d9e308e84d39cb5f4e9c0032b','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:31:12'),('5183f07a6b104d761de7ebbd282ca51d','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:56:32'),('5188df439c83b4e24a39745a0c8132d1','NDJkMWY3ZjRiZDc3MmNlMDM1YWMyMzBhY2U1MDg5NzhhMjI2YTVmYzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASR1Lg==\n','2014-02-17 14:28:57'),('58f969d29564f846ed641cdec2d8b752','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 15:02:07'),('5baab38703073dde1684a235ede16840','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:24:45'),('5c3ed494ab0bf886c83278691d3d2487','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:24:20'),('5c8179d6d6215277ac245f921c9194d1','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:25:47'),('5d63eca83d5796b26b21557994cb2c66','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:29:50'),('601ff07f866f16b1345da2d009ad5b17','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-03-22 11:28:14'),('6259224e8de5f797c13fcb1c487843c3','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-16 12:16:53'),('64cefa313dc0806e36189e0b58aff7d5','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:15:58'),('6a282548dc927e3fda04f02cfb3de1da','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:32:56'),('6c08d7877da86f60c0878b220aa017ca','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:08:47'),('76cf2c1a947047236461ddf2c4a77434','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:31:00'),('7e3a6c2f46767a29f8ac6618ec2d755a','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 13:25:13'),('81c9acf1b44dd520bc5ac757325e211c','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:33:06'),('86d952d18924b3ccfb31f4fa1e71fa9e','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:33:44'),('948037c1f814208a466ab29f6fe80b82','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:15:04'),('a27df55f14804a1acb3ea13fe5ca2806','YmM3OWNjMjg0MWEzMTU1NjlkMThlMjczMTJjMDQ4YzUyZmM4Mjk2ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg==\n','2014-03-22 11:58:49'),('a52af9bc5b6285ddbb5fb8bb502c9f63','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:24:25'),('aa75d2bbc7e1b5b2d62e1cff55171bdf','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:31:46'),('aaef134d0f6efb95960edaf376820536','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:16:13'),('b01380897c8bb6e2dec06a21191b15aa','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 13:02:54'),('b430066f41d3b51ea7fe8f14b3075e37','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 05:51:37'),('b66f68eb188af6f2e5dec724ab2fcf2f','NDFmOGYyNTY2NzRiNmM4NjExMmY0ZjM4NWFlOTI5YmIyZDkzMGY3NjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQp1Lg==\n','2014-02-17 07:29:03'),('b9b03d551b59f6c4cd593e8b0cf5b98b','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:32:17'),('bb9fed8f3458e46ad512e561205c3eaa','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:31:06'),('be3400f83a8ad44d3b70f554a6275d1c','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 11:29:54'),('caad269f3b069fe9b259162de290d242','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 19:38:34'),('ce2ab04c38a879cf810164adc521fe87','YmM3OWNjMjg0MWEzMTU1NjlkMThlMjczMTJjMDQ4YzUyZmM4Mjk2ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg==\n','2014-03-22 12:13:19'),('cfcce7923afe7ff00f42eece5942673e','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 20:07:31'),('d16d14f5c5bbdd05285061e43e19b232','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 10:03:40'),('dc326102556438fdc9f66451b25464b4','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:16:46'),('df05cb0edd01aa3230580651dc0fa8ff','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:19:09'),('df3f176497ef50bfa5c1cf184136c1a4','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 19:08:50'),('e042d4ebda1a2291ba05bcef7635eccb','YmM3OWNjMjg0MWEzMTU1NjlkMThlMjczMTJjMDQ4YzUyZmM4Mjk2ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg==\n','2014-03-22 11:48:34'),('e11ec6d6951d0318f4e505d53126d65b','YjRjMjk3ZmNmMDZkMjVhNWMxNzg5YmQ3OWY2ZjdmYmY4YTk1NGRiNjqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQt1Lg==\n','2014-02-17 07:32:32'),('e3b90739eccf48e5eae0e2feece8d5c4','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 23:50:58'),('e8ee9948c0d8faa8096f56799d4d05d6','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-16 18:51:11'),('f00717bd9260fe4ca629d0fc5efc8224','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:17:12'),('f008542edf3d337ff48eabae90c7a571','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-15 18:25:35'),('f25a439cd97c0c48df6ae8bc05241e25','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-23 14:21:39'),('f45eed30e64ec392c5da9b04b8ab2acc','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-03-22 12:41:58'),('f8920035eea5eb1ea60c16a975f42fc2','NDJkMWY3ZjRiZDc3MmNlMDM1YWMyMzBhY2U1MDg5NzhhMjI2YTVmYzqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASR1Lg==\n','2014-02-17 19:18:06'),('f9db226047131d830e8ed369778ac363','YmM3OWNjMjg0MWEzMTU1NjlkMThlMjczMTJjMDQ4YzUyZmM4Mjk2ODqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKASV1Lg==\n','2014-03-22 12:15:27'),('fb4afb05658c60045c084864f6d75d39','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:15:43'),('fc250cb6693062717e20b483a699aa61','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 09:56:19'),('fff25549af595d7840595fccf16c8a89','NzZhOTVkYmIxYWNhYTI0YzQ3ZTBkMWEzZTk3ZWY0ZDQyZmE5MjRmNDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2014-02-17 14:15:55');
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
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'core','0001_initial','2014-01-29 22:43:27'),(2,'tastypie','0001_initial','2014-01-29 22:43:28'),(3,'tastypie','0002_add_apikey_index','2014-01-29 22:43:28'),(4,'cities_light','0001_initial','2014-01-29 22:43:28'),(5,'cities_light','0002_city_latitude_and_longitude_added','2014-01-29 22:43:28'),(6,'cities_light','0003_auto__add_field_city_search_names','2014-01-29 22:43:28'),(7,'cities_light','0004_added_region','2014-01-29 22:43:29'),(8,'cities_light','0005_set_region','2014-01-29 22:43:29'),(9,'cities_light','0006_add_city_alternate_names','2014-01-29 22:43:29'),(10,'cities_light','0007_region_geoname_id_to_geoname_code','2014-01-29 22:43:29'),(11,'cities_light','0008_add_region_geoname_id','2014-01-29 22:43:29'),(12,'cities_light','0009_alternate_names_for_all','2014-01-29 22:43:29'),(13,'cities_light','0010_set_geoname_ids','2014-01-29 22:43:29'),(14,'cities_light','0011_add_city_and_region_display_name','2014-01-29 22:43:29'),(15,'cities_light','0012_set_display_name','2014-01-29 22:43:29'),(16,'cities_light','0013_geoname_id_unique_index','2014-01-29 22:43:29'),(17,'cities_light','0014_auto__chg_field_city_search_names','2014-01-29 22:43:29'),(23,'core','0002_auto__del_field_ph_quantityBuildingLifts__chg_field_userprofile_phone_','2014-03-08 12:45:12');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tastypie_apikey`
--

LOCK TABLES `tastypie_apikey` WRITE;
/*!40000 ALTER TABLE `tastypie_apikey` DISABLE KEYS */;
INSERT INTO `tastypie_apikey` VALUES (1,2,'4c5be433878e6939a6628d5476d09c9e484c9d5f','2014-01-29 22:44:15'),(2,3,'1d52c5e2b6da665e57001516fe10957e367f220c','2014-02-01 13:32:00'),(3,4,'b084cdaef1a52f089c59807724abd0dee5d2ca93','2014-02-02 16:35:59'),(10,36,'98604798a46e39cb4daab7b1f4b76a1168375052','2014-02-03 14:28:41'),(11,37,'f929ed5e6f08f177ef45552d8dc37734f38598b6','2014-03-08 11:47:42'),(12,42,'805b590e47790181d4ac83c9a91b3e1bd90681ae','2014-03-08 12:46:41');
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

-- Dump completed on 2014-03-08 16:17:13
