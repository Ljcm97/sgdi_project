-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: sgdi_db
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('c33c25115228');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `areas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'ARCHIVO','2025-03-20 12:08:58',NULL,1),(2,'ASISTENTE ADMINISTRATIVO','2025-03-20 12:08:58',NULL,1),(3,'AUDITORIA','2025-03-20 12:08:58',NULL,1),(4,'CARTERA','2025-03-20 12:08:58',NULL,1),(5,'COMPRAS PADDY','2025-03-20 12:08:58',NULL,1),(6,'COMPRAS Y ALMACEN','2025-03-20 12:08:58',NULL,1),(7,'CONTABILIDAD','2025-03-20 12:08:58',NULL,1),(8,'CONTRALORIA','2025-03-20 12:08:58',NULL,1),(9,'COSTOS','2025-03-20 12:08:58',NULL,1),(10,'FACTURACION','2025-03-20 12:08:58',NULL,1),(11,'FLETES','2025-03-20 12:08:58',NULL,1),(12,'GERENTE ADMINISTRATIVO Y FINANCIERO','2025-03-20 12:08:58',NULL,1),(13,'GERENTE GENERAL','2025-03-20 12:08:58',NULL,1),(14,'GERENTE OPERATIVO','2025-03-20 12:08:58',NULL,1),(15,'LOGISTICA','2025-03-20 12:08:58',NULL,1),(16,'PRODUCCION','2025-03-20 12:08:58',NULL,1),(17,'RECEPCION','2025-03-20 12:08:58',NULL,1),(18,'RRHH','2025-03-20 12:08:58',NULL,1),(19,'SISTEMAS','2025-03-20 12:08:58',NULL,1),(20,'SST','2025-03-20 12:08:58',NULL,1),(21,'SUPERNUMERARIO','2025-03-20 12:08:58',NULL,1),(22,'TESORERIA','2025-03-20 12:08:58',NULL,1),(23,'VENTAS','2025-03-20 12:08:58',NULL,1),(88,'CALIDAD','2025-03-21 19:29:00',NULL,1);
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cargos`
--

DROP TABLE IF EXISTS `cargos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cargos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  `descripcion` text COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=245 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargos`
--

LOCK TABLES `cargos` WRITE;
/*!40000 ALTER TABLE `cargos` DISABLE KEYS */;
INSERT INTO `cargos` VALUES (1,'ALMACENISTA','2025-03-20 12:08:58',NULL,1),(3,'ANALISTA DE SISTEMAS','2025-03-21 12:16:42',NULL,1),(4,'APRENDIZ SENA','2025-03-21 12:16:42',NULL,1),(5,'ASISTENTE ADMINISTRATIVO','2025-03-21 12:16:42',NULL,1),(6,'ASISTENTE DE CARTERA','2025-03-21 12:16:42',NULL,1),(7,'ASISTENTE DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(8,'ASISTENTE DE CONTABILIDAD II','2025-03-21 12:16:42',NULL,1),(9,'ASISTENTE DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42',NULL,1),(10,'ASISTENTE DE COSTOS','2025-03-21 12:16:42',NULL,1),(11,'ASISTENTE DE RECURSOS HUMANOS','2025-03-21 12:16:42',NULL,1),(12,'ASISTENTE DE TESORERIA','2025-03-21 12:16:42',NULL,1),(13,'AUXILIAR ADMINISTRATIVO','2025-03-21 12:16:42',NULL,1),(14,'AUXILIAR CAFETERIA','2025-03-21 12:16:42',NULL,1),(15,'AUXILIAR DE ALMACEN','2025-03-21 12:16:42',NULL,1),(16,'AUXILIAR DE AUDITORIA','2025-03-21 12:16:42',NULL,1),(17,'AUXILIAR DE CARTERA','2025-03-21 12:16:42',NULL,1),(18,'AUXILIAR DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42',NULL,1),(19,'AUXILIAR DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(20,'AUXILIAR DE TESORERIA','2025-03-21 12:16:42',NULL,1),(21,'AUXILIAR DE VENTAS','2025-03-21 12:16:42',NULL,1),(22,'AUXILIAR LOGISTICO','2025-03-21 12:16:42',NULL,1),(24,'COMPRADOR MATERIA PRIMA TOLIMA CENTRO','2025-03-21 12:16:42',NULL,1),(25,'COMPRADOR MATERIA PRIMA TOLIMA SUR','2025-03-21 12:16:42',NULL,1),(26,'CONDUCTOR','2025-03-21 12:16:42',NULL,1),(27,'COORDINADOR CONTROL DE CALIDAD','2025-03-21 12:16:42',NULL,1),(28,'COORDINADOR DE ARCHIVO','2025-03-21 12:16:42',NULL,1),(29,'COORDINADOR DE DESPACHOS','2025-03-21 12:16:42',NULL,1),(30,'COORDINADOR DE VENTAS','2025-03-21 12:16:42',NULL,1),(31,'COORDINADOR FLOTA PROPIA','2025-03-21 12:16:42',NULL,1),(32,'COORDINADOR LOGISTICO','2025-03-21 12:16:42',NULL,1),(33,'CONTRALOR','2025-03-21 12:16:42',NULL,1),(34,'FACTURADOR','2025-03-21 12:16:42',NULL,1),(35,'GERENTE ADMINISTRATIVO Y FINANCIERO','2025-03-21 12:16:42',NULL,1),(36,'GERENTE GENERAL','2025-03-21 12:16:42',NULL,1),(37,'GERENTE OPERATIVO PLANTA LA MARIA','2025-03-21 12:16:42',NULL,1),(38,'JEFE DE AUDITORIA','2025-03-21 12:16:42',NULL,1),(39,'JEFE DE CARTERA','2025-03-21 12:16:42',NULL,1),(40,'JEFE DE COMPRAS Y ALMACEN','2025-03-21 12:16:42',NULL,1),(41,'JEFE DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(42,'JEFE DE COSTOS','2025-03-21 12:16:42',NULL,1),(43,'JEFE DE PLANTA U OBRA LA MARIA','2025-03-21 12:16:42',NULL,1),(44,'JEFE DE RECURSOS HUMANOS','2025-03-21 12:16:42',NULL,1),(45,'JEFE DE SEGURIDAD Y SALUD EN EL TRABAJO','2025-03-21 12:16:42',NULL,1),(46,'JEFE GESTION DE CALIDAD','2025-03-21 12:16:42',NULL,1),(47,'MENSAJERO','2025-03-21 12:16:42',NULL,1),(48,'RECEPCIONISTA','2025-03-21 12:16:42',NULL,1),(49,'SUPERNUMERARIO','2025-03-21 12:16:42',NULL,1),(50,'SUPERNUMERARIO SST','2025-03-21 12:16:42',NULL,1),(51,'SUPERVISOR DE VIGILANCIA','2025-03-21 12:16:42',NULL,1),(52,'TESORERO','2025-03-21 12:16:42',NULL,1),(53,'VENDEDOR','2025-03-21 12:16:42',NULL,1),(54,'VIGILANTE','2025-03-21 12:16:42',NULL,1),(232,'AUXILIAR SST','2025-03-21 12:16:42',NULL,1),(236,'AUXILIAR DE RECURSOS HUMANOS','2025-03-23 17:33:22',NULL,1);
/*!40000 ALTER TABLE `cargos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `documentos`
--

DROP TABLE IF EXISTS `documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `radicado` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `fecha_recepcion` datetime NOT NULL,
  `transportadora_id` int NOT NULL,
  `numero_guia` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `remitente` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `tipo_documento_id` int NOT NULL,
  `contenido` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `observaciones` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `area_destino_id` int NOT NULL,
  `persona_destino_id` int NOT NULL,
  `estado_actual_id` int NOT NULL,
  `tipo` enum('ENTRADA','SALIDA') CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `registrado_por_id` int NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `radicado` (`radicado`),
  KEY `transportadora_id` (`transportadora_id`),
  KEY `tipo_documento_id` (`tipo_documento_id`),
  KEY `area_destino_id` (`area_destino_id`),
  KEY `persona_destino_id` (`persona_destino_id`),
  KEY `estado_actual_id` (`estado_actual_id`),
  KEY `registrado_por_id` (`registrado_por_id`),
  CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`transportadora_id`) REFERENCES `transportadoras` (`id`),
  CONSTRAINT `documentos_ibfk_2` FOREIGN KEY (`tipo_documento_id`) REFERENCES `tipos_documento` (`id`),
  CONSTRAINT `documentos_ibfk_3` FOREIGN KEY (`area_destino_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `documentos_ibfk_4` FOREIGN KEY (`persona_destino_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `documentos_ibfk_5` FOREIGN KEY (`estado_actual_id`) REFERENCES `estados_documento` (`id`),
  CONSTRAINT `documentos_ibfk_6` FOREIGN KEY (`registrado_por_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (2,'20250322-8332','2025-03-22 10:14:00',3,'0123456789','Lina',5,'Se entregan 20 tiquetes de aguazul N° ....... etc','Sin novedades ',3,28,5,'ENTRADA',2,'2025-03-22 15:16:58'),(3,'20250322-2381','2025-03-22 12:39:00',4,'741258','Albertano',1,'Factura de celsia','Sin novedades ',17,4,7,'ENTRADA',2,'2025-03-22 17:58:36'),(4,'20250322-8960','2025-03-22 13:00:00',6,'159753','Planta aguazul',4,'Informes de Planta aguazul','Sin novedad',17,4,7,'ENTRADA',2,'2025-03-22 18:14:54'),(5,'20250323-7054','2025-03-23 00:08:00',2,'159','Oscar',4,'','',7,21,4,'ENTRADA',2,'2025-03-23 05:09:53'),(6,'20250323-7371','2025-03-23 18:26:00',3,'147852','Oscar',4,'Informes de Aguazul','Sin novedad',7,21,4,'ENTRADA',2,'2025-03-23 23:27:34'),(7,'20250324-4787','2025-03-24 20:42:00',9,'147852','Edward',4,'','Sin novedad',7,21,3,'ENTRADA',2,'2025-03-25 01:45:35'),(8,'20250325-1091','2025-03-25 07:48:00',3,'0123456789','Planta Aguazul',4,'Caja menor almacén aguazul','Sin novedad',1,103,3,'ENTRADA',2,'2025-03-25 12:52:49'),(9,'20250325-8517','2025-03-25 07:53:00',4,'159','Planta Barranquilla',1,'Factura proveedores ','',7,21,2,'ENTRADA',2,'2025-03-25 12:55:21'),(10,'20250325-4519','2025-03-25 11:40:00',6,'2121313','Planta Barranquilla',7,'Prueba','',17,4,7,'ENTRADA',1,'2025-03-25 16:41:43'),(11,'20250325-2337','2025-03-25 16:00:00',4,'45456654654','EDWARD ',2,'FACTURAS ','COMPRAS DE PORTATIL ',17,4,4,'ENTRADA',1,'2025-03-25 21:03:06'),(12,'20250325-2768','2025-03-25 16:14:00',2,'55725241','OSCAR',5,'52 TIQUETES','SE ENTREGAN 52 TIQUETES EN BUEN ESTADO',13,5,4,'SALIDA',2,'2025-03-25 21:17:10'),(13,'20250326-3410','2025-03-26 11:46:00',7,'446456546','EDWARD ',2,'FACTURAS ','COMPRAS DE PORTATIL ',17,4,7,'ENTRADA',2,'2025-03-26 16:47:36'),(14,'20250326-8614','2025-03-26 11:50:00',6,'4556654646','EDWARD ',8,'hojas de vida ','hojas de vida ',7,21,1,'ENTRADA',2,'2025-03-26 16:50:56'),(15,'20250326-4212','2025-03-26 11:50:00',4,'7575','EDWARD ',3,'445','420',7,21,1,'ENTRADA',2,'2025-03-26 16:53:00'),(16,'20250326-1532','2025-03-26 11:54:00',19,'55725241','OSCAR',5,'50 tiquetes','50 tiquetes',2,9,4,'ENTRADA',2,'2025-03-26 16:54:57'),(17,'20250327-1375','2025-03-27 11:41:00',7,'55725241','OSCAR',5,'se envian 10 tiquetes','',2,9,5,'ENTRADA',2,'2025-03-27 16:41:47'),(18,'20250327-0987','2025-03-27 11:59:00',14,'55725241','OSCAR',7,'','',17,4,7,'ENTRADA',10,'2025-03-27 16:59:59'),(19,'20250331-1212','2025-03-31 09:34:00',1,'124534532','OSCAR HERRERA',5,'66 TIQUETES','',1,49,4,'ENTRADA',2,'2025-03-31 09:34:00'),(20,'20250331-2417','2025-03-31 11:10:00',3,'5356','OSCAR HERRERA',5,'ff ','',15,38,2,'ENTRADA',2,'2025-03-31 11:10:00'),(21,'20250331-4149','2025-03-31 11:18:00',4,'0123456789','Recepción aguazul',2,'','',7,21,3,'ENTRADA',2,'2025-03-31 11:18:00'),(22,'20250331-6067','2025-03-31 12:00:00',13,'159','TONY',2,'','',7,21,4,'ENTRADA',2,'2025-03-31 12:00:00'),(23,'20250331-5856','2025-03-31 12:07:00',4,'159','Oscar',5,'Prueba','',17,4,7,'ENTRADA',2,'2025-03-31 12:07:00'),(24,'20250331-1906','2025-03-31 12:08:00',3,'2121313','Recepción aguazul',11,'Prueba','2',1,103,3,'ENTRADA',2,'2025-03-31 12:08:00'),(25,'20250331-8407','2025-03-31 13:42:00',1,'159','Planta Aguazul',8,'Prueba 2','',1,103,3,'ENTRADA',2,'2025-03-31 13:42:00'),(26,'20250331-5525','2025-03-31 17:02:00',3,'45456654654','EDWARD ',2,'GHHIJHI','GVYGUGUY',1,49,1,'ENTRADA',1,'2025-03-31 17:02:00'),(27,'20250331-6205','2025-03-31 17:02:00',3,'45456654654','EDWARD ',2,'GHHIJHI','GVYGUGUY',1,49,1,'ENTRADA',1,'2025-03-31 17:02:00'),(28,'20250331-6413','2025-03-31 17:03:00',23,'645456456456','EDWARD ',8,'GRREREER','RER',11,24,1,'ENTRADA',1,'2025-03-31 17:03:00'),(29,'20250331-6372','2025-03-31 17:03:00',23,'645456456456','EDWARD ',8,'GRREREER','RER',11,24,1,'ENTRADA',1,'2025-03-31 17:03:00'),(30,'20250331-2484','2025-03-31 17:06:00',10,'645456456456','EDWARD ',9,'YU','GUV',17,4,7,'ENTRADA',1,'2025-03-31 17:06:00'),(31,'20250331-7517','2025-03-31 17:06:00',6,'645456456456','EDWARD ',7,'7IIK','YUKKY',1,49,1,'ENTRADA',1,'2025-03-31 17:06:00'),(32,'20250331-8814','2025-03-31 17:06:00',6,'645456456456','EDWARD ',7,'7IIK','YUKKY',1,49,1,'ENTRADA',1,'2025-03-31 17:06:00'),(33,'20250331-6964','2025-03-31 17:07:00',6,'645456456456','EDWARD ',8,'5YE','RTHREHE',88,44,2,'ENTRADA',1,'2025-03-31 17:07:00'),(34,'20250331-6654','2025-03-31 17:23:00',7,'45645645654','EDWARD ',3,'yiutiu','uii7yyi',5,16,2,'ENTRADA',2,'2025-03-31 17:23:00'),(35,'20250401-1305','2025-04-01 07:37:00',23,'489552','OSCAR HERRERA',5,'12 tiquetes ','',19,1,4,'ENTRADA',2,'2025-04-01 07:37:00'),(36,'20250401-3459','2025-04-01 07:38:00',4,'778555','OSCAR HERRERA',7,'14 ordenes de compra','',19,1,4,'ENTRADA',2,'2025-04-01 07:38:00'),(37,'20250401-5530','2025-04-01 07:39:00',20,'7885125','OSCAR HERRERA',10,'45 informes','',19,1,5,'ENTRADA',2,'2025-04-01 07:39:00'),(38,'20250401-3639','2025-04-01 07:39:00',4,'4454542424','OSCAR HERRERA',3,'','',1,103,1,'ENTRADA',2,'2025-04-01 07:39:00'),(39,'20250401-8048','2025-04-01 07:48:00',20,'4242421','OSCAR HERRERA',6,'','',17,4,7,'ENTRADA',2,'2025-04-01 07:48:00'),(40,'20250401-5513','2025-04-01 07:48:00',20,'7575754','OSCAR HERRERA',10,'','',1,49,5,'ENTRADA',2,'2025-04-01 07:48:00'),(41,'20250401-2543','2025-04-01 09:09:00',19,'56456156','OSCAR HERRERA',7,'','',5,15,4,'ENTRADA',2,'2025-04-01 09:09:00'),(42,'20250401-9644','2025-04-01 10:05:00',1,'7885125','OSCAR HERRERA',7,'','',3,28,4,'ENTRADA',2,'2025-04-01 10:05:00'),(43,'20250401-8993','2025-04-01 10:05:00',3,'489552','OSCAR HERRERA',9,'','',17,4,7,'ENTRADA',2,'2025-04-01 10:05:00'),(44,'20250401-0089','2025-04-01 10:08:00',1,'778555','OSCAR HERRERA',8,'','',3,28,4,'ENTRADA',2,'2025-04-01 10:08:00'),(45,'20250401-5140','2025-04-01 10:39:00',4,'159','Oscar',5,'Prueba','',3,28,4,'ENTRADA',2,'2025-04-01 10:39:00'),(46,'20250401-0209','2025-04-01 11:39:00',14,'7885125','OSCAR HERRERA',6,'','',3,28,4,'ENTRADA',2,'2025-04-01 11:39:00'),(47,'20250401-3164','2025-04-01 11:54:00',3,'778555','flexo spring',1,'','',22,13,5,'ENTRADA',2,'2025-04-01 11:54:00'),(48,'20250401-4084','2025-04-01 11:56:00',3,'489552','cosmoagro',1,'se entregan 17 facturas de cosmoagro ','se reciben en hora de almuerzo ',7,25,5,'ENTRADA',2,'2025-04-01 11:56:00'),(49,'250403-0001','2025-04-03 11:04:00',4,'159','Recepcion aguazul',5,'','',1,103,1,'ENTRADA',2,'2025-04-03 11:04:00'),(50,'250403-0002','2025-04-03 14:28:00',3,'4578','OSCAR ',2,'TI','HSHJS',1,49,1,'ENTRADA',2,'2025-04-03 14:28:00'),(51,'250403-0003','2025-04-03 15:46:00',4,'489552','OSCAR HERRERA',15,'Prueba','1',3,28,4,'ENTRADA',2,'2025-04-03 15:46:00'),(52,'250403-0004','2025-04-03 16:24:00',3,'1234567890','Bodega Bogotá',11,'Prueba flete Paddy','Sin novedad',22,12,3,'ENTRADA',2,'2025-04-03 16:24:00'),(53,'250403-0005','2025-04-03 17:08:00',4,'159','Taga',5,'Se entrega 50 tiquetes','Sin novedad',3,28,1,'ENTRADA',2,'2025-04-03 17:08:00');
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados_documento`
--

DROP TABLE IF EXISTS `estados_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados_documento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `color` varchar(7) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados_documento`
--

LOCK TABLES `estados_documento` WRITE;
/*!40000 ALTER TABLE `estados_documento` DISABLE KEYS */;
INSERT INTO `estados_documento` VALUES (1,'Recibido','Documento recibido en recepción','#1d2c96','2025-03-20 12:08:58'),(2,'En proceso','Documento en proceso de revisión','#f39c12','2025-03-20 12:08:58'),(3,'Transferido','Documento transferido a otra área','#9b59b6','2025-03-20 12:08:58'),(4,'Finalizado','Proceso completado','#357234','2025-03-20 12:08:58'),(5,'Archivado','Documento archivado','#c1c2c2','2025-03-20 12:08:58'),(7,'Rechazado','Documento rechazado por el destinatario','#e20505','2025-03-22 10:04:38');
/*!40000 ALTER TABLE `estados_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historial_passwords`
--

DROP TABLE IF EXISTS `historial_passwords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historial_passwords` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `password` varchar(255) NOT NULL,
  `creado_en` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  CONSTRAINT `historial_passwords_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_passwords`
--

LOCK TABLES `historial_passwords` WRITE;
/*!40000 ALTER TABLE `historial_passwords` DISABLE KEYS */;
INSERT INTO `historial_passwords` VALUES (1,55,'$2b$12$/m3iCzg7nKBp0AqHUq9YGe5y9ij354Q.3pGyHrMT7R7/.snhzUyP6','2025-03-31 16:01:09'),(2,55,'$2b$12$hT9ZelvTv.9mTAeHaqcxWerqf5qS86k2ntNp8wWvK8PcMz7B6M2zq','2025-03-31 16:40:11'),(3,55,'$2b$12$hT9ZelvTv.9mTAeHaqcxWerqf5qS86k2ntNp8wWvK8PcMz7B6M2zq','2025-03-31 16:40:11'),(4,55,'$2b$12$Oaq2URN07F9RsdxEKxM64O.4V/vkmW99LksucwvLujxO.nIN1JEQ6','2025-03-31 16:48:02'),(5,55,'$2b$12$cSaK4ASMvEm58/DsVIQEMusDCwMSN5LoW60JhtXw9mPoXqkUybWBa','2025-03-31 16:54:01'),(6,55,'$2b$12$Q/plr9rUIYKxE8oWieBdveULMecFH0AU1cQ2QDF27J1lDBlZ1qqh.','2025-03-31 17:07:07'),(7,55,'$2b$12$Q/plr9rUIYKxE8oWieBdveULMecFH0AU1cQ2QDF27J1lDBlZ1qqh.','2025-03-31 17:07:07'),(8,55,'$2b$12$rXyH3rDhLRltbqSVc1ThiuRf334oJj6gch5e4gY1.ia7SmDK1rXDi','2025-03-31 17:08:25'),(9,55,'$2b$12$GHlYpAR5HhntfTnHcVEYqeuIYI4SEYG1EraqysgH3/T6Zk94M3CRW','2025-04-01 14:36:16'),(10,55,'$2b$12$EAuEh8YAQ/mIrpulyGyFtOTkUgwxPjfsHAjEkXDUkS8g2UFmG.Q6i','2025-04-01 14:37:11'),(11,55,'$2b$12$XF/xY5SGtxP0Q07QzGh3vuL4J8zmNnhQJ1lS.qsm3/nmuoyPivnza','2025-04-01 14:39:46'),(12,55,'$2b$12$Qgc0/DQSzdEThW.IJwK0SesqtD4jOx8tHJYKQeDpBB7I9JvuMYJpS','2025-04-01 14:50:34'),(13,55,'$2b$12$w.iqxmnttjvRpHxsRFnRzeOtSZLbmVcpmIiUIWLXttYkkJPPwyY4q','2025-04-01 14:50:59');
/*!40000 ALTER TABLE `historial_passwords` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimientos`
--

DROP TABLE IF EXISTS `movimientos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimientos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `documento_id` int NOT NULL,
  `fecha_hora` datetime NOT NULL,
  `usuario_origen_id` int NOT NULL,
  `area_origen_id` int NOT NULL,
  `persona_origen_id` int NOT NULL,
  `area_destino_id` int NOT NULL,
  `persona_destino_id` int NOT NULL,
  `estado_documento_id` int NOT NULL,
  `observaciones` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `usuario_origen_id` (`usuario_origen_id`),
  KEY `area_origen_id` (`area_origen_id`),
  KEY `persona_origen_id` (`persona_origen_id`),
  KEY `area_destino_id` (`area_destino_id`),
  KEY `persona_destino_id` (`persona_destino_id`),
  KEY `estado_documento_id` (`estado_documento_id`),
  KEY `documento_id` (`documento_id`),
  CONSTRAINT `movimientos_ibfk_2` FOREIGN KEY (`usuario_origen_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `movimientos_ibfk_3` FOREIGN KEY (`area_origen_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `movimientos_ibfk_4` FOREIGN KEY (`persona_origen_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `movimientos_ibfk_5` FOREIGN KEY (`area_destino_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `movimientos_ibfk_6` FOREIGN KEY (`persona_destino_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `movimientos_ibfk_7` FOREIGN KEY (`estado_documento_id`) REFERENCES `estados_documento` (`id`),
  CONSTRAINT `movimientos_ibfk_8` FOREIGN KEY (`documento_id`) REFERENCES `documentos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=148 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
INSERT INTO `movimientos` VALUES (4,2,'2025-03-22 10:14:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-22 15:16:58'),(5,2,'2025-03-22 15:36:57',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-22 15:36:57'),(6,2,'2025-03-22 15:38:27',9,7,21,3,28,1,'Se pasa al área de auditoria los fletes para ser auditados ','2025-03-22 15:38:27'),(7,2,'2025-03-22 15:43:12',8,3,28,3,28,2,'Documento aceptado para procesamiento','2025-03-22 15:43:12'),(8,2,'2025-03-22 15:43:16',8,3,28,3,28,4,'Documento finalizado','2025-03-22 15:43:16'),(9,2,'2025-03-22 15:43:36',8,3,28,3,28,5,'Documento archivado','2025-03-22 15:43:36'),(10,3,'2025-03-22 12:39:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-03-22 17:58:36'),(11,4,'2025-03-22 13:00:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-22 18:14:54'),(12,4,'2025-03-22 18:15:36',9,7,21,17,4,7,'Documento rechazado por Maria Paula Lozano Lozano','2025-03-22 18:15:36'),(13,3,'2025-03-22 20:29:46',8,3,28,17,4,7,'Documento rechazado por Nataly Tatiana Puentes Sierra','2025-03-22 20:29:46'),(14,5,'2025-03-23 00:08:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-23 05:09:53'),(15,5,'2025-03-23 05:11:02',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-23 05:11:02'),(16,5,'2025-03-23 05:20:09',9,7,21,7,21,4,'Documento finalizado','2025-03-23 05:20:09'),(17,6,'2025-03-23 18:26:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-23 23:27:34'),(18,6,'2025-03-23 23:28:00',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-23 23:28:00'),(19,6,'2025-03-23 23:28:31',9,7,21,7,21,4,'Documento finalizado','2025-03-23 23:28:31'),(20,7,'2025-03-24 20:42:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-03-25 01:45:35'),(21,7,'2025-03-25 01:48:04',8,3,28,3,28,2,'Documento aceptado para procesamiento','2025-03-25 01:48:04'),(22,7,'2025-03-25 01:50:24',8,3,28,7,21,3,'','2025-03-25 01:50:24'),(23,8,'2025-03-25 07:48:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-03-25 12:52:49'),(24,9,'2025-03-25 07:53:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-25 12:55:21'),(25,10,'2025-03-25 11:40:00',1,19,1,7,21,1,'Documento registrado en recepción','2025-03-25 16:41:43'),(26,10,'2025-03-25 16:42:31',9,7,21,17,4,7,'Documento rechazado por Maria Paula Lozano Lozano','2025-03-25 16:42:31'),(27,11,'2025-03-25 16:00:00',1,19,1,19,95,1,'Documento registrado en recepción','2025-03-25 21:03:06'),(28,11,'2025-03-25 21:05:14',10,19,95,1,49,5,'','2025-03-25 21:05:14'),(29,11,'2025-03-25 21:06:57',23,1,49,17,4,2,'CARTERA ','2025-03-25 21:06:57'),(30,11,'2025-03-25 21:12:44',2,17,4,17,4,4,'Documento finalizado','2025-03-25 21:12:44'),(31,12,'2025-03-25 16:14:00',2,17,4,7,25,1,'Documento registrado en recepción','2025-03-25 21:17:10'),(32,12,'2025-03-25 21:21:23',15,7,25,4,33,2,'52 FACURAS PARA CARTERA ','2025-03-25 21:21:23'),(33,12,'2025-03-25 21:22:07',28,4,33,13,5,2,'','2025-03-25 21:22:07'),(34,13,'2025-03-26 11:46:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-26 16:47:36'),(35,13,'2025-03-26 16:48:36',9,7,21,17,4,7,'Documento rechazado por Maria Paula Lozano Lozano','2025-03-26 16:48:36'),(36,9,'2025-03-26 16:48:53',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-26 16:48:53'),(37,14,'2025-03-26 11:50:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-26 16:50:56'),(38,15,'2025-03-26 11:50:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-26 16:53:00'),(39,16,'2025-03-26 11:54:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-26 16:54:57'),(40,16,'2025-03-26 16:56:16',9,7,21,2,9,2,'420','2025-03-26 16:56:16'),(41,16,'2025-03-26 16:56:55',20,2,9,2,9,4,'Documento finalizado','2025-03-26 16:56:55'),(42,17,'2025-03-27 11:41:00',2,17,4,2,9,1,'Documento registrado en recepción','2025-03-27 16:41:47'),(43,18,'2025-03-27 11:59:00',10,19,95,2,9,1,'Documento registrado en recepción','2025-03-27 16:59:59'),(44,18,'2025-03-27 17:00:52',20,2,9,17,4,7,'Documento rechazado por Brayan Santick Quintero Cordoba','2025-03-27 17:00:52'),(45,17,'2025-03-27 17:01:21',20,2,9,2,9,2,'Documento aceptado para procesamiento','2025-03-27 17:01:21'),(46,17,'2025-03-27 17:01:21',20,2,9,2,9,2,'Documento aceptado para procesamiento','2025-03-27 17:01:21'),(47,17,'2025-03-27 17:01:29',20,2,9,2,9,4,'Documento finalizado','2025-03-27 17:01:29'),(48,17,'2025-03-27 17:01:35',20,2,9,2,9,5,'Documento archivado','2025-03-27 17:01:35'),(49,19,'2025-03-31 09:34:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-03-31 14:34:42'),(50,19,'2025-03-31 14:36:06',23,1,49,2,9,2,'....','2025-03-31 14:36:06'),(51,19,'2025-03-31 16:09:48',20,2,9,1,49,2,'','2025-03-31 16:09:48'),(52,20,'2025-03-31 11:10:00',2,17,4,13,5,1,'Documento registrado en recepción','2025-03-31 16:10:42'),(53,20,'2025-03-31 16:11:07',25,13,5,15,38,2,'','2025-03-31 16:11:07'),(54,12,'2025-03-31 16:11:13',25,13,5,13,5,4,'Documento finalizado','2025-03-31 16:11:13'),(55,19,'2025-03-31 16:11:38',23,1,49,1,49,4,'Documento finalizado','2025-03-31 16:11:38'),(56,21,'2025-03-31 11:18:00',2,17,4,11,24,1,'Documento registrado en recepción','2025-03-31 16:19:34'),(57,21,'2025-03-31 16:20:19',38,11,24,11,24,2,'Documento aceptado para procesamiento','2025-03-31 16:20:19'),(58,21,'2025-03-31 16:20:56',38,11,24,1,103,3,'','2025-03-31 16:20:56'),(59,21,'2025-03-31 16:22:06',55,1,103,7,21,3,'','2025-03-31 16:22:06'),(60,22,'2025-03-31 12:00:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-31 17:01:16'),(61,22,'2025-03-31 17:01:50',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-31 17:01:50'),(62,22,'2025-03-31 17:03:54',9,7,21,7,21,4,'Documento finalizado','2025-03-31 17:03:54'),(63,23,'2025-03-31 12:07:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-31 17:07:37'),(64,23,'2025-03-31 17:07:58',9,7,21,17,4,7,'Documento rechazado por Maria Paula Lozano Lozano','2025-03-31 17:07:58'),(65,24,'2025-03-31 12:08:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-31 17:10:08'),(66,24,'2025-03-31 17:10:55',9,7,21,3,28,3,'','2025-03-31 17:10:55'),(67,25,'2025-03-31 13:42:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-31 18:43:16'),(68,25,'2025-03-31 18:44:11',9,7,21,3,28,3,'','2025-03-31 18:44:11'),(69,25,'2025-03-31 18:45:20',8,3,28,1,103,3,'','2025-03-31 18:45:20'),(70,8,'2025-03-31 19:29:48',8,3,28,1,103,3,'','2025-03-31 19:29:48'),(71,24,'2025-03-31 19:46:48',8,3,28,1,103,3,'','2025-03-31 19:46:48'),(72,26,'2025-03-31 17:02:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:03:25'),(73,27,'2025-03-31 17:02:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:03:26'),(74,28,'2025-03-31 17:03:00',1,19,1,11,24,1,'Documento registrado en recepción','2025-03-31 22:04:25'),(75,29,'2025-03-31 17:03:00',1,19,1,11,24,1,'Documento registrado en recepción','2025-03-31 22:04:25'),(76,30,'2025-03-31 17:06:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:06:38'),(77,30,'2025-03-31 22:07:18',23,1,49,17,4,7,'Documento rechazado por Jaime Vargas Ramirez','2025-03-31 22:07:18'),(78,31,'2025-03-31 17:06:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:07:36'),(79,32,'2025-03-31 17:06:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:07:36'),(80,33,'2025-03-31 17:07:00',1,19,1,1,49,1,'Documento registrado en recepción','2025-03-31 22:08:31'),(81,33,'2025-03-31 22:09:12',23,1,49,2,9,3,'se tranfieren 12 hojas de vida ','2025-03-31 22:09:12'),(82,33,'2025-03-31 22:10:02',20,2,9,3,28,2,'MANUALES ','2025-03-31 22:10:02'),(83,33,'2025-03-31 22:10:38',8,3,28,3,23,3,'','2025-03-31 22:10:38'),(84,33,'2025-03-31 22:11:05',16,3,23,3,29,2,'RWER','2025-03-31 22:11:05'),(85,33,'2025-03-31 22:11:51',12,3,29,88,45,2,'','2025-03-31 22:11:51'),(86,33,'2025-03-31 22:12:14',21,88,45,88,44,2,'46564','2025-03-31 22:12:14'),(87,33,'2025-03-31 22:12:14',21,88,45,88,44,2,'46564','2025-03-31 22:12:14'),(88,34,'2025-03-31 17:23:00',2,17,4,88,44,1,'Documento registrado en recepción','2025-03-31 22:24:30'),(89,34,'2025-03-31 22:24:58',47,88,44,4,33,2,'','2025-03-31 22:24:58'),(90,34,'2025-03-31 22:25:20',28,4,33,4,32,2,'rththrtrrt','2025-03-31 22:25:20'),(91,34,'2025-03-31 22:26:39',34,4,32,4,31,3,'','2025-03-31 22:26:39'),(92,34,'2025-03-31 22:27:30',39,4,31,5,16,2,'1232545','2025-03-31 22:27:30'),(93,35,'2025-04-01 07:37:00',2,17,4,19,1,1,'Documento registrado en recepción','2025-04-01 12:38:12'),(94,36,'2025-04-01 07:38:00',2,17,4,19,1,1,'Documento registrado en recepción','2025-04-01 12:39:11'),(95,37,'2025-04-01 07:39:00',2,17,4,19,1,1,'Documento registrado en recepción','2025-04-01 12:39:39'),(96,38,'2025-04-01 07:39:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-01 12:48:25'),(97,39,'2025-04-01 07:48:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-01 12:48:46'),(98,40,'2025-04-01 07:48:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-01 12:49:01'),(99,40,'2025-04-01 14:09:51',55,1,103,1,103,2,'Documento aceptado para procesamiento','2025-04-01 14:09:51'),(100,39,'2025-04-01 14:10:01',55,1,103,17,4,7,'Documento rechazado por pepito','2025-04-01 14:10:01'),(101,41,'2025-04-01 09:09:00',2,17,4,5,16,1,'Documento registrado en recepción','2025-04-01 14:31:30'),(102,41,'2025-04-01 14:34:19',19,5,16,5,15,2,'compras  ','2025-04-01 14:34:19'),(103,42,'2025-04-01 10:05:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-04-01 15:05:57'),(104,43,'2025-04-01 10:05:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-04-01 15:06:52'),(105,44,'2025-04-01 10:08:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-04-01 15:08:56'),(106,44,'2025-04-01 15:09:35',8,3,28,3,28,2,'Documento aceptado para procesamiento','2025-04-01 15:09:35'),(107,43,'2025-04-01 15:10:13',8,3,28,17,4,7,'Documento rechazado por Nataly Tatiana Puentes Sierra','2025-04-01 15:10:13'),(108,42,'2025-04-01 15:10:46',8,3,28,3,28,2,'Documento aceptado para procesamiento','2025-04-01 15:10:46'),(109,45,'2025-04-01 10:39:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-01 15:39:59'),(110,40,'2025-04-01 16:35:44',55,1,103,1,103,4,'Documento finalizado','2025-04-01 16:35:44'),(111,40,'2025-04-01 16:37:29',55,1,103,1,49,4,'123','2025-04-01 16:37:29'),(112,40,'2025-04-01 16:38:06',23,1,49,1,49,5,'Documento archivado','2025-04-01 16:38:06'),(113,46,'2025-04-01 11:39:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-01 16:39:48'),(114,46,'2025-04-01 16:40:46',55,1,103,17,4,7,'Documento rechazado por pepito','2025-04-01 16:40:46'),(115,46,'2025-04-01 16:42:12',2,17,4,19,1,2,'','2025-04-01 16:42:12'),(116,46,'2025-04-01 16:42:49',1,19,1,3,28,2,'123','2025-04-01 16:42:49'),(117,47,'2025-04-01 11:54:00',2,17,4,7,20,1,'Documento registrado en recepción','2025-04-01 16:56:26'),(118,48,'2025-04-01 11:56:00',2,17,4,7,25,1,'Documento registrado en recepción','2025-04-01 16:58:13'),(119,48,'2025-04-01 17:04:05',15,7,25,7,25,2,'Documento aceptado para procesamiento','2025-04-01 17:04:05'),(120,47,'2025-04-01 17:05:25',40,7,20,7,20,2,'Documento aceptado para procesamiento','2025-04-01 17:05:25'),(121,47,'2025-04-01 17:12:34',40,7,20,22,13,5,'','2025-04-01 17:12:34'),(122,48,'2025-04-02 16:40:39',1,7,25,7,25,4,'Documento finalizado','2025-04-02 16:40:39'),(123,48,'2025-04-02 16:40:46',1,7,25,7,25,5,'Documento archivado','2025-04-02 16:40:46'),(124,35,'2025-04-03 14:18:04',1,19,1,19,1,2,'Documento aceptado para procesamiento','2025-04-03 14:18:04'),(125,46,'2025-04-03 15:28:25',2,3,28,3,28,4,'Documento finalizado','2025-04-03 15:28:25'),(126,44,'2025-04-03 15:28:41',2,3,28,3,28,4,'Documento finalizado','2025-04-03 15:28:41'),(127,45,'2025-04-03 15:29:12',2,1,103,3,28,2,'','2025-04-03 15:29:12'),(128,45,'2025-04-03 15:29:16',2,3,28,3,28,4,'Documento finalizado','2025-04-03 15:29:16'),(129,42,'2025-04-03 15:29:28',2,3,28,3,28,4,'Documento finalizado','2025-04-03 15:29:28'),(130,41,'2025-04-03 15:29:47',2,5,15,5,15,4,'Documento finalizado','2025-04-03 15:29:47'),(131,37,'2025-04-03 15:50:46',1,19,1,19,1,2,'Documento aceptado para procesamiento','2025-04-03 15:50:46'),(132,37,'2025-04-03 15:52:10',1,19,1,19,1,4,'Documento finalizado','2025-04-03 15:52:10'),(133,37,'2025-04-03 15:53:11',1,19,1,19,1,5,'Documento archivado','2025-04-03 15:53:11'),(134,35,'2025-04-03 15:54:04',1,19,1,19,1,4,'Documento finalizado','2025-04-03 15:54:04'),(135,36,'2025-04-03 15:54:42',1,19,1,19,1,2,'Documento aceptado para procesamiento','2025-04-03 15:54:42'),(136,36,'2025-04-03 15:54:48',1,19,1,19,1,4,'Documento finalizado','2025-04-03 15:54:48'),(137,49,'2025-04-03 11:04:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-03 16:04:33'),(138,50,'2025-04-03 14:28:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-04-03 19:30:33'),(139,51,'2025-04-03 15:46:00',2,17,4,19,1,1,'Documento registrado en recepción','2025-04-03 20:47:41'),(140,51,'2025-04-03 20:48:04',1,19,1,19,1,2,'Documento aceptado para procesamiento','2025-04-03 20:48:04'),(141,51,'2025-04-03 20:48:23',1,19,1,3,28,2,'','2025-04-03 20:48:23'),(142,51,'2025-04-03 20:49:28',8,3,28,3,28,4,'Documento finalizado','2025-04-03 20:49:28'),(143,52,'2025-04-03 16:24:00',2,17,4,11,24,1,'Documento registrado en recepción','2025-04-03 21:34:54'),(144,52,'2025-04-03 21:58:54',38,11,24,11,24,2,'Documento aceptado para procesamiento','2025-04-03 21:58:55'),(145,52,'2025-04-03 22:02:37',38,11,24,3,28,3,'Fuera de fecha ','2025-04-03 22:02:37'),(146,52,'2025-04-03 22:08:03',8,3,28,22,12,3,'Auditado a conformidad','2025-04-03 22:08:03'),(147,53,'2025-04-03 17:08:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-04-03 22:09:29');
/*!40000 ALTER TABLE `movimientos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notificaciones`
--

DROP TABLE IF EXISTS `notificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notificaciones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `titulo` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `mensaje` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `documento_id` int DEFAULT NULL,
  `leida` tinyint(1) DEFAULT '0',
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `documento_id` (`documento_id`),
  CONSTRAINT `notificaciones_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `notificaciones_ibfk_2` FOREIGN KEY (`documento_id`) REFERENCES `documentos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificaciones`
--

LOCK TABLES `notificaciones` WRITE;
/*!40000 ALTER TABLE `notificaciones` DISABLE KEYS */;
INSERT INTO `notificaciones` VALUES (4,9,'Nuevo documento asignado - 20250322-8332','Se te ha asignado un nuevo documento de tipo Tiquetes.',2,1,'2025-03-22 15:16:58'),(5,2,'Documento aceptado - 20250322-8332','El documento ha sido aceptado por Maria Paula Lozano Lozano.',2,1,'2025-03-22 15:36:57'),(6,8,'Documento transferido - 20250322-8332','Se te ha transferido un documento de tipo Tiquetes.',2,1,'2025-03-22 15:38:27'),(7,2,'Documento aceptado - 20250322-8332','El documento ha sido aceptado por Nataly Tatiana Puentes Sierra.',2,1,'2025-03-22 15:43:12'),(8,8,'Nuevo documento asignado - 20250322-2381','Se te ha asignado un nuevo documento de tipo Facturas.',3,1,'2025-03-22 17:58:36'),(9,9,'Nuevo documento asignado - 20250322-8960','Se te ha asignado un nuevo documento de tipo Correspondencia.',4,1,'2025-03-22 18:14:54'),(10,2,'Documento rechazado - 20250322-8960','El documento ha sido rechazado por Maria Paula Lozano Lozano.',4,1,'2025-03-22 18:15:36'),(11,2,'Documento rechazado - 20250322-2381','El documento ha sido rechazado por Nataly Tatiana Puentes Sierra.',3,1,'2025-03-22 20:29:46'),(12,9,'Nuevo documento asignado - 20250323-7054','Se te ha asignado un nuevo documento de tipo Correspondencia.',5,1,'2025-03-23 05:09:53'),(13,2,'Documento aceptado - 20250323-7054','El documento ha sido aceptado por Maria Paula Lozano Lozano.',5,1,'2025-03-23 05:11:02'),(14,9,'Nuevo documento asignado - 20250323-7371','Se te ha asignado un nuevo documento de tipo Correspondencia.',6,1,'2025-03-23 23:27:34'),(15,2,'Documento aceptado - 20250323-7371','El documento ha sido aceptado por Maria Paula Lozano Lozano.',6,1,'2025-03-23 23:28:00'),(16,8,'Nuevo documento asignado - 20250324-4787','Se te ha asignado un nuevo documento de tipo Correspondencia.',7,1,'2025-03-25 01:45:35'),(17,2,'Documento aceptado - 20250324-4787','El documento ha sido aceptado por Nataly Tatiana Puentes Sierra.',7,1,'2025-03-25 01:48:04'),(18,9,'Documento transferido - 20250324-4787','Se te ha transferido un documento de tipo Correspondencia.',7,0,'2025-03-25 01:50:24'),(19,8,'Nuevo documento asignado - 20250325-1091','Se te ha asignado un nuevo documento de tipo Correspondencia.',8,1,'2025-03-25 12:52:49'),(20,9,'Nuevo documento asignado - 20250325-8517','Se te ha asignado un nuevo documento de tipo Facturas.',9,1,'2025-03-25 12:55:21'),(21,9,'Nuevo documento asignado - 20250325-4519','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',10,1,'2025-03-25 16:41:43'),(22,2,'Documento rechazado - 20250325-4519','El documento ha sido rechazado por Maria Paula Lozano Lozano.',10,1,'2025-03-25 16:42:31'),(23,10,'Nuevo documento asignado - 20250325-2337','Se te ha asignado un nuevo documento de tipo Comprobantes.',11,1,'2025-03-25 21:03:06'),(24,23,'Documento transferido - 20250325-2337','Se te ha transferido un documento de tipo Comprobantes.',11,1,'2025-03-25 21:05:14'),(25,2,'Documento transferido - 20250325-2337','Se te ha transferido un documento de tipo Comprobantes.',11,1,'2025-03-25 21:06:57'),(26,15,'Nuevo documento asignado - 20250325-2768','Se te ha asignado un nuevo documento de tipo Tiquetes.',12,1,'2025-03-25 21:17:10'),(27,28,'Documento transferido - 20250325-2768','Se te ha transferido un documento de tipo Tiquetes.',12,1,'2025-03-25 21:21:23'),(28,25,'Documento transferido - 20250325-2768','Se te ha transferido un documento de tipo Tiquetes.',12,1,'2025-03-25 21:22:07'),(29,9,'Nuevo documento asignado - 20250326-3410','Se te ha asignado un nuevo documento de tipo Comprobantes.',13,1,'2025-03-26 16:47:36'),(30,2,'Documento rechazado - 20250326-3410','El documento ha sido rechazado por Maria Paula Lozano Lozano.',13,1,'2025-03-26 16:48:36'),(31,2,'Documento aceptado - 20250325-8517','El documento ha sido aceptado por Maria Paula Lozano Lozano.',9,1,'2025-03-26 16:48:53'),(32,9,'Nuevo documento asignado - 20250326-8614','Se te ha asignado un nuevo documento de tipo Hojas de vida.',14,0,'2025-03-26 16:50:56'),(33,9,'Nuevo documento asignado - 20250326-4212','Se te ha asignado un nuevo documento de tipo Contratos.',15,1,'2025-03-26 16:53:00'),(34,9,'Nuevo documento asignado - 20250326-1532','Se te ha asignado un nuevo documento de tipo Tiquetes.',16,1,'2025-03-26 16:54:57'),(35,20,'Documento transferido - 20250326-1532','Se te ha transferido un documento de tipo Tiquetes.',16,1,'2025-03-26 16:56:16'),(36,20,'Nuevo documento asignado - 20250327-1375','Se te ha asignado un nuevo documento de tipo Tiquetes.',17,1,'2025-03-27 16:41:47'),(37,20,'Nuevo documento asignado - 20250327-0987','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',18,1,'2025-03-27 16:59:59'),(38,2,'Documento rechazado - 20250327-0987','El documento ha sido rechazado por Brayan Santick Quintero Cordoba.',18,1,'2025-03-27 17:00:52'),(39,2,'Documento aceptado - 20250327-1375','El documento ha sido aceptado por Brayan Santick Quintero Cordoba.',17,1,'2025-03-27 17:01:21'),(40,2,'Documento aceptado - 20250327-1375','El documento ha sido aceptado por Brayan Santick Quintero Cordoba.',17,1,'2025-03-27 17:01:21'),(41,23,'Nuevo documento asignado - 20250331-1212','Se te ha asignado un nuevo documento de tipo Tiquetes.',19,1,'2025-03-31 09:34:42'),(42,20,'Documento transferido - 20250331-1212','Se te ha transferido un documento de tipo Tiquetes.',19,1,'2025-03-31 09:36:06'),(43,23,'Documento transferido - 20250331-1212','Se te ha transferido un documento de tipo Tiquetes.',19,1,'2025-03-31 11:09:48'),(44,25,'Nuevo documento asignado - 20250331-2417','Se te ha asignado un nuevo documento de tipo Tiquetes.',20,1,'2025-03-31 11:10:42'),(45,17,'Documento transferido - 20250331-2417','Se te ha transferido un documento de tipo Tiquetes.',20,0,'2025-03-31 11:11:07'),(46,38,'Nuevo documento asignado - 20250331-4149','Se te ha asignado un nuevo documento de tipo Comprobantes.',21,1,'2025-03-31 11:19:34'),(47,2,'Documento aceptado - 20250331-4149','El documento ha sido aceptado por Laura Maria Rodriguez Cuervo.',21,1,'2025-03-31 11:20:19'),(48,55,'Documento transferido - 20250331-4149','Se te ha transferido un documento de tipo Comprobantes.',21,1,'2025-03-31 11:20:56'),(49,9,'Documento transferido - 20250331-4149','Se te ha transferido un documento de tipo Comprobantes.',21,1,'2025-03-31 11:22:06'),(50,9,'Nuevo documento asignado - 20250331-6067','Se te ha asignado un nuevo documento de tipo Comprobantes.',22,1,'2025-03-31 12:01:16'),(51,2,'Documento aceptado - 20250331-6067','El documento ha sido aceptado por Maria Paula Lozano Lozano.',22,1,'2025-03-31 12:01:50'),(52,9,'Nuevo documento asignado - 20250331-5856','Se te ha asignado un nuevo documento de tipo Tiquetes.',23,1,'2025-03-31 12:07:37'),(53,2,'Documento rechazado - 20250331-5856','El documento ha sido rechazado por Maria Paula Lozano Lozano.',23,1,'2025-03-31 12:07:58'),(54,9,'Nuevo documento asignado - 20250331-1906','Se te ha asignado un nuevo documento de tipo Fletes.',24,1,'2025-03-31 12:10:08'),(55,8,'Documento transferido - 20250331-1906','Se te ha transferido un documento de tipo Fletes.',24,1,'2025-03-31 12:10:55'),(56,9,'Nuevo documento asignado - 20250331-8407','Se te ha asignado un nuevo documento de tipo Hojas de vida.',25,1,'2025-03-31 13:43:16'),(57,8,'Documento transferido - 20250331-8407','Se te ha transferido un documento de tipo Hojas de vida.',25,1,'2025-03-31 13:44:11'),(58,55,'Documento transferido - 20250331-8407','Se te ha transferido un documento de tipo Hojas de vida.',25,1,'2025-03-31 13:45:20'),(59,55,'Documento transferido - 20250325-1091','Se te ha transferido un documento de tipo Correspondencia.',8,1,'2025-03-31 14:29:48'),(60,55,'Documento transferido - 20250331-1906','Se te ha transferido un documento de tipo Fletes.',24,1,'2025-03-31 14:46:48'),(61,23,'Nuevo documento asignado - 20250331-5525','Se te ha asignado un nuevo documento de tipo Comprobantes.',26,1,'2025-03-31 17:03:25'),(62,23,'Nuevo documento asignado - 20250331-6205','Se te ha asignado un nuevo documento de tipo Comprobantes.',27,1,'2025-03-31 17:03:26'),(63,38,'Nuevo documento asignado - 20250331-6413','Se te ha asignado un nuevo documento de tipo Hojas de vida.',28,0,'2025-03-31 17:04:25'),(64,38,'Nuevo documento asignado - 20250331-6372','Se te ha asignado un nuevo documento de tipo Hojas de vida.',29,0,'2025-03-31 17:04:25'),(65,23,'Nuevo documento asignado - 20250331-2484','Se te ha asignado un nuevo documento de tipo Manuales.',30,1,'2025-03-31 17:06:38'),(66,2,'Documento rechazado - 20250331-2484','El documento ha sido rechazado por Jaime Vargas Ramirez.',30,0,'2025-03-31 17:07:18'),(67,23,'Nuevo documento asignado - 20250331-7517','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',31,1,'2025-03-31 17:07:36'),(68,23,'Nuevo documento asignado - 20250331-8814','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',32,1,'2025-03-31 17:07:36'),(69,23,'Nuevo documento asignado - 20250331-6964','Se te ha asignado un nuevo documento de tipo Hojas de vida.',33,1,'2025-03-31 17:08:31'),(70,20,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,1,'2025-03-31 17:09:12'),(71,8,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,1,'2025-03-31 17:10:02'),(72,16,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,1,'2025-03-31 17:10:38'),(73,12,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,1,'2025-03-31 17:11:05'),(74,21,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,1,'2025-03-31 17:11:51'),(75,47,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,0,'2025-03-31 17:12:14'),(76,47,'Documento transferido - 20250331-6964','Se te ha transferido un documento de tipo Hojas de vida.',33,0,'2025-03-31 17:12:14'),(77,47,'Nuevo documento asignado - 20250331-6654','Se te ha asignado un nuevo documento de tipo Contratos.',34,1,'2025-03-31 17:24:30'),(78,28,'Documento transferido - 20250331-6654','Se te ha transferido un documento de tipo Contratos.',34,1,'2025-03-31 17:24:58'),(79,34,'Documento transferido - 20250331-6654','Se te ha transferido un documento de tipo Contratos.',34,1,'2025-03-31 17:25:20'),(80,39,'Documento transferido - 20250331-6654','Se te ha transferido un documento de tipo Contratos.',34,1,'2025-03-31 17:26:39'),(81,19,'Documento transferido - 20250331-6654','Se te ha transferido un documento de tipo Contratos.',34,1,'2025-03-31 17:27:30'),(82,1,'Nuevo documento asignado - 20250401-1305','Se te ha asignado un nuevo documento de tipo Tiquetes.',35,1,'2025-04-01 07:38:12'),(83,1,'Nuevo documento asignado - 20250401-3459','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',36,1,'2025-04-01 07:39:11'),(84,1,'Nuevo documento asignado - 20250401-5530','Se te ha asignado un nuevo documento de tipo Informes.',37,1,'2025-04-01 07:39:39'),(85,55,'Nuevo documento asignado - 20250401-3639','Se te ha asignado un nuevo documento de tipo Contratos.',38,1,'2025-04-01 07:48:25'),(86,55,'Nuevo documento asignado - 20250401-8048','Se te ha asignado un nuevo documento de tipo Cotizaciones.',39,1,'2025-04-01 07:48:46'),(87,55,'Nuevo documento asignado - 20250401-5513','Se te ha asignado un nuevo documento de tipo Informes.',40,1,'2025-04-01 07:49:01'),(88,2,'Documento aceptado - 20250401-5513','El documento ha sido aceptado por pepito.',40,0,'2025-04-01 09:09:51'),(89,2,'Documento rechazado - 20250401-8048','El documento ha sido rechazado por pepito.',39,0,'2025-04-01 09:10:01'),(90,19,'Nuevo documento asignado - 20250401-2543','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',41,1,'2025-04-01 09:31:30'),(91,49,'Documento transferido - 20250401-2543','Se te ha transferido un documento de tipo Órdenes de compra.',41,1,'2025-04-01 09:34:19'),(92,8,'Nuevo documento asignado - 20250401-9644','Se te ha asignado un nuevo documento de tipo Órdenes de compra.',42,1,'2025-04-01 10:05:57'),(93,8,'Nuevo documento asignado - 20250401-8993','Se te ha asignado un nuevo documento de tipo Manuales.',43,0,'2025-04-01 10:06:52'),(94,8,'Nuevo documento asignado - 20250401-0089','Se te ha asignado un nuevo documento de tipo Hojas de vida.',44,1,'2025-04-01 10:08:56'),(95,2,'Documento aceptado - 20250401-0089','El documento ha sido aceptado por Nataly Tatiana Puentes Sierra.',44,0,'2025-04-01 10:09:35'),(96,2,'Documento rechazado - 20250401-8993','El documento ha sido rechazado por Nataly Tatiana Puentes Sierra.',43,1,'2025-04-01 10:10:13'),(97,2,'Documento aceptado - 20250401-9644','El documento ha sido aceptado por Nataly Tatiana Puentes Sierra.',42,0,'2025-04-01 10:10:46'),(98,55,'Nuevo documento asignado - 20250401-5140','Se te ha asignado un nuevo documento de tipo Tiquetes.',45,0,'2025-04-01 10:39:59'),(99,23,'Documento transferido - 20250401-5513','Se te ha transferido un documento de tipo Informes.',40,1,'2025-04-01 11:37:29'),(100,55,'Nuevo documento asignado - 20250401-0209','Se te ha asignado un nuevo documento de tipo Cotizaciones.',46,1,'2025-04-01 11:39:48'),(101,2,'Documento rechazado - 20250401-0209','El documento ha sido rechazado por pepito.',46,1,'2025-04-01 11:40:46'),(102,1,'Documento transferido - 20250401-0209','Se te ha transferido un documento de tipo Cotizaciones.',46,1,'2025-04-01 11:42:12'),(103,8,'Documento transferido - 20250401-0209','Se te ha transferido un documento de tipo Cotizaciones.',46,1,'2025-04-01 11:42:49'),(104,40,'Nuevo documento asignado - 20250401-3164','Se te ha asignado un nuevo documento de tipo Facturas.',47,1,'2025-04-01 11:56:26'),(105,15,'Nuevo documento asignado - 20250401-4084','Se te ha asignado un nuevo documento de tipo Facturas.',48,1,'2025-04-01 11:58:13'),(106,2,'Documento aceptado - 20250401-4084','El documento ha sido aceptado por Andrea Del Pilar Morales Trujillo.',48,0,'2025-04-01 12:04:05'),(107,2,'Documento aceptado - 20250401-3164','El documento ha sido aceptado por Lizeth Daniela Melo Olis.',47,0,'2025-04-01 12:05:25'),(108,30,'Documento transferido - 20250401-3164','Se te ha transferido un documento de tipo Facturas.',47,1,'2025-04-01 12:12:34'),(109,2,'Documento aceptado - 20250401-1305','El documento ha sido aceptado por RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ.',35,0,'2025-04-03 09:18:04'),(110,8,'Documento transferido - 20250401-5140','Se te ha transferido un documento de tipo Tiquetes.',45,0,'2025-04-03 10:29:12'),(111,2,'Documento aceptado - 20250401-5530','El documento ha sido aceptado por RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ.',37,0,'2025-04-03 10:50:46'),(112,2,'Documento aceptado - 20250401-3459','El documento ha sido aceptado por RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ.',36,0,'2025-04-03 10:54:42'),(113,55,'Nuevo documento asignado - 250403-0001','Se te ha asignado un nuevo documento de tipo Tiquetes.',49,0,'2025-04-03 11:04:33'),(114,23,'Nuevo documento asignado - 250403-0002','Se te ha asignado un nuevo documento de tipo Comprobantes.',50,1,'2025-04-03 14:30:33'),(115,1,'Nuevo documento asignado - 250403-0003','Se te ha asignado un nuevo documento de tipo Legalizaciones.',51,1,'2025-04-03 15:47:41'),(116,2,'Documento aceptado - 250403-0003','El documento ha sido aceptado por RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ.',51,0,'2025-04-03 15:48:04'),(117,8,'Documento transferido - 250403-0003','Se te ha transferido un documento de tipo Legalizaciones.',51,1,'2025-04-03 15:48:23'),(118,38,'Nuevo documento asignado - 250403-0004','Se te ha asignado un nuevo documento de tipo Fletes.',52,1,'2025-04-03 16:34:54'),(119,2,'Documento aceptado - 250403-0004','El documento ha sido aceptado por LAURA MARIA RODRIGUEZ CUERVO.',52,0,'2025-04-03 16:58:55'),(120,8,'Documento transferido - 250403-0004','Se te ha transferido un documento de tipo Fletes.',52,1,'2025-04-03 17:02:37'),(121,46,'Documento transferido - 250403-0004','Se te ha transferido un documento de tipo Fletes.',52,1,'2025-04-03 17:08:03'),(122,8,'Nuevo documento asignado - 250403-0005','Se te ha asignado un nuevo documento de tipo Tiquetes.',53,1,'2025-04-03 17:09:29');
/*!40000 ALTER TABLE `notificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permisos`
--

DROP TABLE IF EXISTS `permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permisos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permisos`
--

LOCK TABLES `permisos` WRITE;
/*!40000 ALTER TABLE `permisos` DISABLE KEYS */;
INSERT INTO `permisos` VALUES (1,'Crear documento','Puede crear documentos','2025-03-20 12:08:58'),(2,'Ver documento','Puede ver documentos','2025-03-20 12:08:58'),(3,'Editar documento','Puede editar documentos','2025-03-20 12:08:58'),(4,'Eliminar documento','Puede eliminar documentos','2025-03-20 12:08:58'),(5,'Transferir documento','Puede transferir documentos','2025-03-20 12:08:58'),(6,'Aceptar documento','Puede aceptar documentos','2025-03-20 12:08:58'),(7,'Rechazar documento','Puede rechazar documentos','2025-03-20 12:08:58'),(8,'Ver historial','Puede ver el historial de documentos','2025-03-20 12:08:58'),(9,'Ver reportes','Puede ver reportes','2025-03-20 12:08:58'),(10,'Administrar usuarios','Puede administrar usuarios','2025-03-20 12:08:58'),(11,'Administrar roles','Puede administrar roles','2025-03-20 12:08:58'),(12,'Administrar personas','Puede administrar personas','2025-03-20 12:08:58'),(13,'Administrar areas','Puede administrar áreas','2025-03-20 12:08:58'),(14,'Administrar unidades','Puede administrar unidades','2025-03-20 12:08:58'),(15,'Administrar cargos','Puede administrar cargos','2025-03-20 12:08:58'),(16,'Administrar zonas','Puede administrar zonas económicas','2025-03-20 12:08:58'),(17,'Administrar transportadoras','Puede administrar transportadoras','2025-03-20 12:08:58'),(18,'Administrar tipos de documento','Puede administrar tipos de documento','2025-03-20 12:08:58'),(19,'Administrar estados','Puede administrar estados de documento','2025-03-20 12:08:58'),(20,'Cambiar contraseña','Puede cambiar su contraseña','2025-03-20 12:08:58'),(21,'Cambiar contraseña de otros','Puede cambiar la contraseña de otros usuarios','2025-03-20 12:08:58');
/*!40000 ALTER TABLE `permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personas`
--

DROP TABLE IF EXISTS `personas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `personas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombres_apellidos` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `telefono` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `zona_economica_id` int NOT NULL,
  `unidad_id` int NOT NULL,
  `area_id` int NOT NULL,
  `cargo_id` int NOT NULL,
  `activo` tinyint(1) DEFAULT '1',
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `zona_economica_id` (`zona_economica_id`),
  KEY `unidad_id` (`unidad_id`),
  KEY `area_id` (`area_id`),
  KEY `cargo_id` (`cargo_id`),
  CONSTRAINT `personas_ibfk_1` FOREIGN KEY (`zona_economica_id`) REFERENCES `zonas_economicas` (`id`),
  CONSTRAINT `personas_ibfk_2` FOREIGN KEY (`unidad_id`) REFERENCES `unidades` (`id`),
  CONSTRAINT `personas_ibfk_3` FOREIGN KEY (`area_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `personas_ibfk_4` FOREIGN KEY (`cargo_id`) REFERENCES `cargos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (1,'RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ','rbohorquez@arrozsonora.com.co','3112815201',1,1,19,3,1,'2025-03-20 12:08:58'),(2,'JAIRO ANTONIO LOZANO VARGAS','jalozano@arrozsonora.com.co','3102118013',1,2,20,45,1,'2025-03-20 12:08:58'),(3,'OLGA PATRICIA ORTIZ RIVAS','oortiz@arrozsonora.com.co',NULL,1,3,6,40,1,'2025-03-20 12:08:58'),(4,'YAZMINA LORENA FAYAD GUTIERREZ','yfayad@arrozsonora.com.co','3104567890',1,1,17,48,1,'2025-03-20 12:08:58'),(5,'JAIRO SEDAN MURRA','jsedan@arrozsonora.com.co',NULL,1,1,13,36,1,'2025-03-21 09:11:56'),(6,'JULIO CESAR CEPEDA RODRÍGUEZ','jcepeda@arrozsonora.com.co',NULL,1,1,14,37,1,'2025-03-21 09:11:56'),(7,'YULY SLENDY CASTILLO ROBAYO','ycastillo@arrozsonora.com.co',NULL,1,1,12,35,1,'2025-03-21 09:11:56'),(8,'MYRIAM RODRÍGUEZ ARCINIEGAS','mrodriguez@arrozsonora.com.co',NULL,1,1,8,33,1,'2025-03-21 09:11:56'),(9,'BRAYAN SANTICK QUINTERO CORDOBA','bquintero@arrozsonora.com.co',NULL,1,1,2,5,1,'2025-03-21 09:11:56'),(10,'VIVIANA CAYCEDO BOCANEGRA','vcaycedo@arrozsonora.com.co',NULL,1,1,21,49,1,'2025-03-21 09:11:56'),(11,'MARTHA YANETH DIAZ TRIGUEROS','mdiaz@arrozsonora.com.co',NULL,1,1,22,52,1,'2025-03-21 09:11:56'),(12,'SANDRA BIBIANA LAVERDE PARRA','slaverde@arrozsonora.com.co',NULL,1,1,22,13,1,'2025-03-21 09:11:56'),(13,'JUAN DAVID LOZANO GUZMAN','jlozano@arrozsonora.com.co',NULL,1,1,22,20,1,'2025-03-21 09:11:56'),(14,'DIANA MARCELA BOCANEGRA TOVAR','dbocanegra@arrozsonora.com.co',NULL,1,1,22,12,1,'2025-03-21 09:11:56'),(15,'TERESA TOVAR RIVERA','ttovar@arrozsonora.com.co',NULL,1,1,5,9,1,'2025-03-21 09:11:56'),(16,'ANGY YULITZA VARGAS PADILLA','avargas@arrozsonora.com.co',NULL,1,1,5,18,1,'2025-03-21 09:11:56'),(17,'XIMENA PAOLA BOCANEGRA ORTIZ','xbocanegra@arrozsonora.com.co',NULL,1,1,7,41,1,'2025-03-21 09:11:56'),(18,'JOAN JAIR RODRIGUEZ PORTELA','jrodriguez@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(19,'ADRIANA LUCIA GONZALEZ SERRANO','agonzalez@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(20,'LIZETH DANIELA MELO OLIS','lmelo@arrozsonora.com.co',NULL,1,1,7,8,1,'2025-03-21 09:11:56'),(21,'MARIA PAULA LOZANO LOZANO','mlozano@arrozsonora.com.co',NULL,1,1,7,19,1,'2025-03-21 09:11:56'),(22,'SILVIA PATRICIA RIVERA ZABALA','srivera@arrozsonora.com.co',NULL,1,1,7,19,1,'2025-03-21 09:11:56'),(23,'ANDRES FELIPE ARIAS VARGAS','aarias@arrozsonora.com.co',NULL,1,1,3,16,1,'2025-03-21 09:11:56'),(24,'DIANA CAROLINA RUBIANO','drubiano@arrozsonora.com.co',NULL,1,1,11,19,1,'2025-03-21 09:11:56'),(25,'ANDREA DEL PILAR MORALES TRUJILLO','amorales@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(26,'KAREN NUREIDYS CARCAMO LONDONO','kcarcamo@arrozsonora.com.co',NULL,1,1,9,42,1,'2025-03-21 09:11:56'),(27,'JULIAN ANDRES MOLINA AVILA','jmolina@arrozsonora.com.co',NULL,1,1,9,10,1,'2025-03-21 09:11:56'),(28,'NATALY TATIANA PUENTES SIERRA','npuentes@arrozsonora.com.co',NULL,1,1,3,38,1,'2025-03-21 09:11:56'),(29,'ADRIANA DEL PILAR LOPEZ BUSTOS','alopez@arrozsonora.com.co',NULL,1,1,3,16,1,'2025-03-21 09:11:56'),(30,'LINA FERNANDA FIERRO FIERRO','lfierro@arrozsonora.com.co',NULL,1,1,3,16,0,'2025-03-21 09:11:56'),(31,'LEIDY JOHANA AVILA GONZALEZ','lavila@arrozsonora.com.co',NULL,1,1,4,39,1,'2025-03-21 09:11:56'),(32,'JULIETH PAOLA GONZALEZ ONATRA','jgonzalez@arrozsonora.com.co',NULL,1,1,4,6,1,'2025-03-21 09:11:56'),(33,'JONATHAN FABIAN MANRIQUE RODRIGUEZ','jmanrique@arrozsonora.com.co',NULL,1,1,4,17,1,'2025-03-21 09:11:56'),(34,'ANGIE KATHERINE ZAMORA CORDOBA','azamora@arrozsonora.com.co',NULL,1,1,4,17,0,'2025-03-21 09:11:56'),(35,'LUANA SIMONA SENDOYA ECHEVERRY','lsendoya@arrozsonora.com.co',NULL,1,1,23,30,1,'2025-03-21 09:11:56'),(36,'ANGI XIOMARA RAMIREZ ORTIZ','aramirez@arrozsonora.com.co',NULL,1,1,23,21,1,'2025-03-21 09:11:56'),(37,'JUAN JOSE COTE HERNANDEZ','jcote@arrozsonora.com.co',NULL,1,1,15,32,1,'2025-03-21 09:11:56'),(38,'ANGELA MARIA ZARTHA LEAL','azartha@arrozsonora.com.co',NULL,1,1,15,22,1,'2025-03-21 09:11:56'),(39,'JUAN PABLO CELIS CASTILLO','jcelis@arrozsonora.com.co',NULL,1,1,15,31,1,'2025-03-21 09:11:56'),(40,'ANA MARIA RODRIGUEZ MORA','arodriguez@arrozsonora.com.co',NULL,1,1,18,44,1,'2025-03-21 09:11:56'),(41,'SANDRA MILENA GARCIA GONZALEZ','sgarcia@arrozsonora.com.co',NULL,1,1,18,11,1,'2025-03-21 09:11:56'),(42,'YENDY FANNORY BRAVO GUTIERREZ','ybravo@arrozsonora.com.co',NULL,1,2,10,34,1,'2025-03-21 09:11:56'),(43,'KELLY JOHANNA GOMEZ LOZANO','kgomez@arrozsonora.com.co',NULL,1,2,20,232,1,'2025-03-21 09:11:56'),(44,'SANDRA MILENA VILLA ROJAS','smvilla@arrozsonora.com.co',NULL,1,2,88,46,1,'2025-03-21 09:11:56'),(45,'DIANA ALEJANDRA ORTIZ JARA','dortiz@arrozsonora.com.co',NULL,1,2,88,27,1,'2025-03-21 09:11:56'),(46,'JAMES EDUARDO RUEDA TRUJILLO','jrueda@arrozsonora.com.co',NULL,1,2,16,43,1,'2025-03-21 09:11:56'),(47,'LUIS ALBERTO BARRETO GUZMAN','lbarreto@arrozsonora.com.co',NULL,1,3,6,1,1,'2025-03-21 09:11:56'),(48,'LUIS ALEJANDRO OLIVEROS GUARNIZO',NULL,NULL,1,3,6,15,1,'2025-03-21 09:11:56'),(49,'JAIME VARGAS RAMIREZ','jvargas@arrozsonora.com.co',NULL,1,3,1,28,1,'2025-03-21 09:11:58'),(95,'LINA JULIETH CARVAJAL MENDOZA','linajuliethcarvajalmendoza@gmail.com',NULL,1,1,19,4,1,'2025-03-21 20:01:07'),(99,'JORGE ELIAS ORTIZ','jortiz@arrozsonora.com.co',NULL,1,2,23,29,1,'2025-03-23 17:44:44'),(103,'PEPITO',NULL,NULL,2,1,1,4,1,'2025-03-31 15:49:51'),(112,'LAURA DANIELA ALVIS ABREO','lalvis@arrozsonora.com.co',NULL,1,1,18,236,1,'2025-04-04 19:40:49'),(113,'Modelo - RRHH - AUXILIAR DE RECURSOS HUMANOS',NULL,NULL,1,1,18,236,0,'2025-04-04 19:54:08'),(114,'Modelo - RRHH - APRENDIZ SENA',NULL,NULL,1,1,18,4,0,'2025-04-04 19:54:08'),(115,'STIVEN SERRANO SOLORZANO','sserrano@arrozsonora.com.co',NULL,1,1,11,19,1,'2025-04-04 21:27:39');
/*!40000 ALTER TABLE `personas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'Superadministrador','Tiene acceso completo a todos los módulos del sistema','2025-03-20 12:08:58'),(2,'Recepción','Encargado de registrar entradas y salidas de documentos','2025-03-20 12:08:58'),(3,'Usuario','Acceso limitado a sus documentos y áreas asignadas','2025-03-20 12:08:58');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles_permisos`
--

DROP TABLE IF EXISTS `roles_permisos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles_permisos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rol_id` int NOT NULL,
  `permiso_id` int NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `rol_id` (`rol_id`),
  KEY `permiso_id` (`permiso_id`),
  CONSTRAINT `roles_permisos_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `roles_permisos_ibfk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permisos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=171 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles_permisos`
--

LOCK TABLES `roles_permisos` WRITE;
/*!40000 ALTER TABLE `roles_permisos` DISABLE KEYS */;
INSERT INTO `roles_permisos` VALUES (1,1,1,'2025-03-20 12:08:58'),(2,1,2,'2025-03-20 12:08:58'),(3,1,3,'2025-03-20 12:08:58'),(4,1,4,'2025-03-20 12:08:58'),(5,1,5,'2025-03-20 12:08:58'),(6,1,6,'2025-03-20 12:08:58'),(7,1,7,'2025-03-20 12:08:58'),(8,1,8,'2025-03-20 12:08:58'),(9,1,9,'2025-03-20 12:08:58'),(10,1,10,'2025-03-20 12:08:58'),(11,1,11,'2025-03-20 12:08:58'),(12,1,12,'2025-03-20 12:08:58'),(13,1,13,'2025-03-20 12:08:58'),(14,1,14,'2025-03-20 12:08:58'),(15,1,15,'2025-03-20 12:08:58'),(16,1,16,'2025-03-20 12:08:58'),(17,1,17,'2025-03-20 12:08:58'),(18,1,18,'2025-03-20 12:08:58'),(19,1,19,'2025-03-20 12:08:58'),(20,1,20,'2025-03-20 12:08:58'),(21,1,21,'2025-03-20 12:08:58'),(156,3,2,'2025-03-23 02:26:49'),(157,3,5,'2025-03-23 02:26:49'),(158,3,7,'2025-03-23 02:26:49'),(159,3,6,'2025-03-23 02:26:49'),(160,3,8,'2025-03-23 02:26:49'),(161,3,20,'2025-03-23 02:26:49'),(162,2,3,'2025-03-23 02:47:37'),(163,2,20,'2025-03-23 02:47:37'),(164,2,8,'2025-03-23 02:47:37'),(165,2,1,'2025-03-23 02:47:37'),(166,2,2,'2025-03-23 02:47:37'),(167,2,9,'2025-03-23 02:47:37'),(168,2,5,'2025-03-23 02:47:37');
/*!40000 ALTER TABLE `roles_permisos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_documento`
--

DROP TABLE IF EXISTS `tipos_documento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_documento` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_documento`
--

LOCK TABLES `tipos_documento` WRITE;
/*!40000 ALTER TABLE `tipos_documento` DISABLE KEYS */;
INSERT INTO `tipos_documento` VALUES (1,'Facturas','2025-03-20 12:08:58'),(2,'Comprobantes','2025-03-20 12:08:58'),(3,'Contratos','2025-03-20 12:08:58'),(4,'Correspondencia','2025-03-20 12:08:58'),(5,'Tiquetes','2025-03-20 12:08:58'),(6,'Cotizaciones','2025-03-20 12:08:58'),(7,'Órdenes de compra','2025-03-20 12:08:58'),(8,'Hojas de vida','2025-03-20 12:08:58'),(9,'Manuales','2025-03-20 12:08:58'),(10,'Informes','2025-03-20 12:08:58'),(11,'Fletes','2025-03-20 12:08:58'),(15,'Legalizaciones','2025-04-03 16:14:19');
/*!40000 ALTER TABLE `tipos_documento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transportadoras`
--

DROP TABLE IF EXISTS `transportadoras`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transportadoras` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transportadoras`
--

LOCK TABLES `transportadoras` WRITE;
/*!40000 ALTER TABLE `transportadoras` DISABLE KEYS */;
INSERT INTO `transportadoras` VALUES (1,'DEPRISA','2025-03-20 12:08:58'),(2,'SERVIENTREGA','2025-03-20 12:08:58'),(3,'ENVIA','2025-03-20 12:08:58'),(4,'COORDINADORA','2025-03-20 12:08:58'),(5,'SAFERBO','2025-03-20 12:08:58'),(6,'INTERRAPIDISIMO','2025-03-20 12:08:58'),(7,'AXPRESS','2025-03-20 12:08:58'),(8,'REDETRANS','2025-03-20 12:08:58'),(9,'TCC','2025-03-20 12:08:58'),(10,'4-72','2025-03-20 12:08:58'),(11,'TRANSPRENSA','2025-03-20 12:08:58'),(12,'PORTERIA','2025-03-20 12:08:58'),(13,'CERTIPOSTAL','2025-03-20 12:08:58'),(14,'ENCO EXPRES','2025-03-20 12:08:58'),(15,'X-CARGO','2025-03-20 12:08:58'),(16,'DHL EXPRESS','2025-03-20 12:08:58'),(17,'OPEN MARKET','2025-03-20 12:08:58'),(18,'EXPRESO BOLIVARIANO','2025-03-20 12:08:58'),(19,'MERCADOLIBRE','2025-03-20 12:08:58'),(20,'INTERSERVICE','2025-03-20 12:08:58'),(23,'MENSAJERO MOLINO SONORA','2025-03-25 13:06:00');
/*!40000 ALTER TABLE `transportadoras` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unidades`
--

DROP TABLE IF EXISTS `unidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `unidades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidades`
--

LOCK TABLES `unidades` WRITE;
/*!40000 ALTER TABLE `unidades` DISABLE KEYS */;
INSERT INTO `unidades` VALUES (1,'ADMINISTRACION','2025-03-20 12:08:58'),(2,'BASCULA Y CALIDAD','2025-03-20 12:08:58'),(3,'ALMACEN','2025-03-20 12:08:58');
/*!40000 ALTER TABLE `unidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `persona_id` int NOT NULL,
  `rol_id` int NOT NULL,
  `ultimo_acceso` datetime DEFAULT NULL,
  `activo` tinyint(1) DEFAULT '1',
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `rol_id` (`rol_id`),
  KEY `persona_id` (`persona_id`),
  CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `usuarios_ibfk_3` FOREIGN KEY (`persona_id`) REFERENCES `personas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'rbohorquez','$2b$12$.Vsma9zYL6ivAOrfzNbN2uO8tw7.21nUBONXcUzOyHWPOrR82AdUq',1,1,'2025-04-05 23:43:25',1,'2025-03-20 21:18:20'),(2,'yfayad','$2b$12$.Vsma9zYL6ivAOrfzNbN2uO8tw7.21nUBONXcUzOyHWPOrR82AdUq',4,2,'2025-04-03 22:08:42',1,'2025-03-21 12:39:04'),(8,'npuentes','$2b$12$2Q44xvcj0xIBIL4R6nty2uMMOLTFFU4d3UiW1F.ZaGi9a9WcH.syK',28,3,'2025-04-03 22:08:20',1,'2025-03-22 05:06:01'),(9,'mlozano','$2b$12$ZDiZDmGcldxaGx1FIM13cOV2qk7DVCdgnD4.1ZKBRMd7QaP201ege',21,3,'2025-03-31 18:43:52',1,'2025-03-22 05:06:52'),(10,'lcarvajal','$2b$12$1/XsVHZv7IdsyHZARfWoeubjUBpgb6M22Kt0PTVi5vFy0DO9.iwnm',95,1,'2025-03-31 22:19:16',1,'2025-03-22 19:10:49'),(12,'alopez','$2b$12$2OYLs2AYPKiEt.5QzCN7JuRtyLbjHqN7gt173/qa4vHFH72OTLIvO',29,3,'2025-03-31 22:11:10',1,'2025-03-25 16:46:25'),(13,'agonzalez','$2b$12$WF/f7GLQiNJqgYh5tLgcTuCodR1HZjzTBhf8PBneJio2RDOLpacTi',19,3,NULL,1,'2025-03-25 16:50:53'),(14,'arodriguez','$2b$12$xitKvoCKaJ//OyJ2mx9e5Oqd3pBhbXCjGWtcZOjrtii7hJJl8kMDG',40,3,'2025-03-25 21:24:50',1,'2025-03-25 16:51:48'),(15,'amorales','$2b$12$d83P1TYpyFVXsdyxL4pF8OSS1S6kedJjHy8LX5FHJ5VrcH20wUtdu',25,3,'2025-04-01 16:59:44',1,'2025-03-25 16:53:44'),(16,'aarias','$2b$12$SXWUOMOeerQ8ukZVbTGRr.FW3xCx.GX9VZBAxAHTZp7Ui/WnhWCMK',23,3,'2025-03-31 22:10:41',1,'2025-03-25 16:54:21'),(17,'azartha','$2b$12$0FXHZgIAY/dli9Dki5OaCOzGaZtMCB42ma/sFc.H/Cp0J4MGgRm76',38,3,NULL,1,'2025-03-25 16:55:05'),(18,'aramirez','$2b$12$9/IwWDjKjzptit8QIGRbN.LbEcxfpTf6WcBAxdMFh9jiDAtqgFG1K',36,3,'2025-04-03 20:36:23',1,'2025-03-25 16:58:46'),(19,'avargas','$2b$12$2tBn9q1leEWo0efdI/P.RuxKdEt56fFnlqo0iaWin.x2CeGnochhm',16,3,'2025-04-01 14:29:39',1,'2025-03-25 17:02:23'),(20,'bquintero','$2b$12$Le3jjYqfqqXTZLdO7XNhxOpm1kek8eW7j1PBfNd.utj9lE5axDuMe',9,3,'2025-03-31 22:08:58',1,'2025-03-25 17:03:31'),(21,'dortiz','$2b$12$KOwmzywl0q0E4jBWlQu3X.iW3YF0vteH8g62m8vEZRI1p0xFut3oK',45,3,'2025-03-31 22:11:49',1,'2025-03-25 17:04:40'),(22,'dbocanegra','$2b$12$FWHVrgn2t2Q5gn/NH.vjdu0lnQuIOzyCUzGS/KBUERqUm9OPcvIjq',14,3,NULL,1,'2025-03-25 17:07:09'),(23,'jvargas','$2b$12$ExGSx/7fM9mudBS3BnSIHOL7x0CSp.vi4QyW5mOEUzvMSmEhUbdU2',49,3,'2025-04-04 19:39:56',1,'2025-03-25 17:07:57'),(24,'jalozano','$2b$12$jPoosjjHlFB41USTVPvE/uN93zxHRdE7KaARYjbZC.K/29BkAT93W',2,3,NULL,1,'2025-03-25 17:08:50'),(25,'jsedan','$2b$12$FSchTfuN9LI2BQs70hDHz.inecxoN1820dxvHIRnr0HRZzonT73V.',5,3,'2025-03-31 16:10:52',1,'2025-03-25 17:12:03'),(26,'jrueda','$2b$12$DRVa/qWbaOzvWG9oP8qem.PA/LhBardGhZsoumcsBqc/FfweEzUqW',46,3,NULL,1,'2025-03-25 17:12:43'),(27,'jrodriguez','$2b$12$NJCFGoPT2OrP2zLpi7cEI.MKm37YZuB8FFVz.oqEwrry9ACIq/hfe',18,3,NULL,1,'2025-03-25 17:15:06'),(28,'jmanrique','$2b$12$EPC6MbEsrlwvg5MnM0yoDeuEyCrWhUd7Ax5tg/xfdcl369NG2ooHm',33,3,'2025-03-31 22:25:01',1,'2025-03-25 17:16:27'),(29,'jortiz','$2b$12$96ir9Jul09nn/zQPBJoAQuDe0u2KreQu9wMTfELAIW4AEv8T2cLZe',99,3,NULL,1,'2025-03-25 19:10:55'),(30,'jlozano','$2b$12$auI6r5R7scNeBKLXy3vVZeLfaZ1HrrWnABO8TdGTwfGl7vuNjJR1a',13,3,'2025-04-01 17:13:19',1,'2025-03-25 19:11:31'),(31,'jcote','$2b$12$AlwAcV8hOAdBgP7dhJORr.oF9SEsUnpPifA7o5rXha41nRa1jCOjm',37,3,NULL,1,'2025-03-25 19:14:24'),(32,'jcelis','$2b$12$MMjPC/q2g2PJhJgRoHqax.ig74wwTxsXOgP/pbOuva8YRmnTduBYq',39,3,NULL,1,'2025-03-25 19:15:01'),(33,'jmolina','$2b$12$LWFKKoxl3Xj0kwHEBUGD7.azWnA3FQ.Ov.PlYzbLD0DSJCAPbc8D2',27,3,NULL,1,'2025-03-25 19:15:31'),(34,'jgonzalez','$2b$12$nNrGstpBWBuNxGFf44.X/uUNwYKE0MJOiJUGXKnJjnpPIrcrkOfO6',32,3,'2025-03-31 22:26:09',1,'2025-03-25 19:16:02'),(35,'jcepeda','$2b$12$cock2CS6sTofSNcrDep2vO5qCrlsX6ZAt54jqxA54vmvaDtOtxc3e',6,3,NULL,1,'2025-03-25 19:16:38'),(36,'kcarcamo','$2b$12$utcRNp60mdBKdG0JcAfwkeuZHiiS5SlxXcFoOsJCzxH2WWrqCVvum',26,3,NULL,1,'2025-03-25 19:17:14'),(37,'kgomez','$2b$12$44eUOZ2Kqk3nZG0Qar/xsOw.KM8sNQPVShco.hTab73KIEIZ5lROW',43,3,NULL,1,'2025-03-25 19:17:42'),(38,'lrodriguez','$2b$12$ZoZpw0kxSLt1u0db.aQNq.zmWXzGiOm42w9U.8JddcQc9gY0dWVDu',24,3,'2025-04-03 21:47:16',1,'2025-03-25 19:18:08'),(39,'lavila','$2b$12$smkWycwLGgGqOxIZ3kRgwuvHCY1zCvMc7wTx5NrMrgeQHzlVcVFRK',31,3,'2025-03-31 22:26:58',1,'2025-03-25 19:18:43'),(40,'lmelo','$2b$12$Fdb07A94Q3oAwg7Qq6ETJeFBCEpLTcKfjF7cDOkUJjviRc31uAYiy',20,3,'2025-04-01 17:04:42',1,'2025-03-25 19:19:41'),(41,'lsendoya','$2b$12$dyCPPmPHDIp2TOgZFqHcAeajbjYofNnLThHxjwaaRQWGObkpeIeWm',35,3,NULL,1,'2025-03-25 19:20:19'),(42,'lbarreto','$2b$12$t3gUswD1BtDVZaRSGo8IMOBTX6SocZvH6YLihA/8Nb2BO381nvCU2',47,3,NULL,1,'2025-03-25 19:20:56'),(43,'mdiaz','$2b$12$AUrqTKf0QdQEfyGeDgWmCuzW53O.v6njVtZAjU.11Mkv/nM.GVkNK',11,3,NULL,1,'2025-03-25 19:23:18'),(44,'mrodriguez','$2b$12$hIERq3qObvSHM9NSiLZ/KeI7nsJZJb8JpFic6xm/Haig/GZsBazk2',8,3,NULL,1,'2025-03-25 19:24:43'),(45,'oortiz','$2b$12$cgwdxDncLJ/XHmYr0hfJ0uQizFr8z8XpQUa78gXJRenttIRHX0qCG',3,3,NULL,1,'2025-03-25 19:25:28'),(46,'slaverde','$2b$12$NbyymTCSflxLP4mLy4w7buKnJT2psFnn/d2VV9F2OMTIJ0Xd1WhwS',12,3,'2025-04-03 22:13:13',1,'2025-03-25 19:26:01'),(47,'svilla','$2b$12$iHIMDEUQpoTcblarVA1fguXTyzCqtu8iAPc3Tvbf1hprbAIZqrKOi',44,3,'2025-03-31 22:24:32',1,'2025-03-25 19:26:40'),(48,'srivera','$2b$12$HEZvOky.QYBwWOpd3UJoHucfqZAyrvBTodAVR6tOctoni4buRexBC',22,3,NULL,1,'2025-03-25 19:28:01'),(49,'ttovar','$2b$12$Yp3O32btlkSi72/x/TWJg.1mzc/CyVf/b9EuzQO5uiiPZdHOcCd/2',15,3,'2025-04-01 14:35:06',1,'2025-03-25 19:28:30'),(50,'vcaycedo','$2b$12$0JaWzdvzbhsUmeu4JVUzk.vjOn/Lagy55XEQPDWGZQ4fOKoCELVIu',10,3,NULL,1,'2025-03-25 19:28:55'),(51,'xbocanegra','$2b$12$yF5GRGlpO.3qAHT0DAfJNeTahJpbm4GlW2ZckpUtXTkO3M5W9eBAO',17,3,NULL,1,'2025-03-25 19:29:26'),(52,'ybravo','$2b$12$VlcafJHHVMlo0lc8JNqbUeTczewU3DyVoXz/HfA8T1xsm9uweLRFu',42,3,NULL,1,'2025-03-25 19:30:07'),(53,'ycastillo','$2b$12$U1FMJq4eXXiaziXbkFpcMucCMtwc62K4.ZykPQuDOx8rxFAonNylm',7,3,NULL,1,'2025-03-25 19:30:43'),(55,'pepito','$2b$12$Wa8ryTF94oS.X.j.vBJi0O1IvOGb/877RXPWfRBaLLaFzlmehWfgC',103,3,'2025-04-01 15:39:35',1,'2025-03-31 15:50:26'),(56,'sgarcia','$2b$12$FZCv3yorRJ47BycGXgZoseVlZopnYrwoRN6mESwh4vJ/thdBUGJO2',41,3,'2025-04-01 12:10:28',1,'2025-03-31 22:22:31'),(58,'lalvis','$2b$12$LIc5S3N9uErWKD/SDZEhV.vGxCZ.DzG357jMAbLWC5Zq4PibGaV9W',112,3,NULL,1,'2025-04-04 19:42:50');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zonas_economicas`
--

DROP TABLE IF EXISTS `zonas_economicas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `zonas_economicas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `creado_en` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zonas_economicas`
--

LOCK TABLES `zonas_economicas` WRITE;
/*!40000 ALTER TABLE `zonas_economicas` DISABLE KEYS */;
INSERT INTO `zonas_economicas` VALUES (1,'PLANTA LA MARIA','2025-03-20 12:08:58'),(2,'BODEGA BARRANQUILLA','2025-03-20 12:08:58'),(3,'PLANTA AGUAZUL','2025-03-20 12:08:58'),(4,'BODEGA BOGOTA','2025-03-20 12:08:58'),(5,'BODEGA CALI','2025-03-20 12:08:58'),(6,'BODEGA GIRON','2025-03-20 12:08:58'),(7,'BODEGA MEDELLIN','2025-03-20 12:08:58'),(8,'BODEGA PEREIRA','2025-03-20 12:08:58');
/*!40000 ALTER TABLE `zonas_economicas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-04-05 19:35:23
