-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: sgdi_db
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
INSERT INTO `alembic_version` VALUES ('b8e4f47c95eb');
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=247 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargos`
--

LOCK TABLES `cargos` WRITE;
/*!40000 ALTER TABLE `cargos` DISABLE KEYS */;
INSERT INTO `cargos` VALUES (1,'ALMACENISTA','2025-03-20 12:08:58',NULL,1),(3,'ANALISTA DE SISTEMAS','2025-03-21 12:16:42',NULL,1),(4,'APRENDIZ SENA','2025-03-21 12:16:42','',1),(5,'ASISTENTE ADMINISTRATIVO','2025-03-21 12:16:42',NULL,1),(6,'ASISTENTE DE CARTERA','2025-03-21 12:16:42',NULL,1),(7,'ASISTENTE DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(8,'ASISTENTE DE CONTABILIDAD II','2025-03-21 12:16:42',NULL,1),(9,'ASISTENTE DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42',NULL,1),(10,'ASISTENTE DE COSTOS','2025-03-21 12:16:42',NULL,1),(11,'ASISTENTE DE RECURSOS HUMANOS','2025-03-21 12:16:42',NULL,1),(12,'ASISTENTE DE TESORERIA','2025-03-21 12:16:42',NULL,1),(13,'AUXILIAR ADMINISTRATIVO','2025-03-21 12:16:42',NULL,1),(14,'AUXILIAR CAFETERIA','2025-03-21 12:16:42',NULL,1),(15,'AUXILIAR DE ALMACEN','2025-03-21 12:16:42',NULL,1),(16,'AUXILIAR DE AUDITORIA','2025-03-21 12:16:42',NULL,1),(17,'AUXILIAR DE CARTERA','2025-03-21 12:16:42',NULL,1),(18,'AUXILIAR DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42',NULL,1),(19,'AUXILIAR DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(20,'AUXILIAR DE TESORERIA','2025-03-21 12:16:42',NULL,1),(21,'AUXILIAR DE VENTAS','2025-03-21 12:16:42',NULL,1),(22,'AUXILIAR LOGISTICO','2025-03-21 12:16:42',NULL,1),(24,'COMPRADOR MATERIA PRIMA TOLIMA CENTRO','2025-03-21 12:16:42',NULL,1),(25,'COMPRADOR MATERIA PRIMA TOLIMA SUR','2025-03-21 12:16:42',NULL,1),(26,'CONDUCTOR','2025-03-21 12:16:42',NULL,1),(27,'COORDINADOR CONTROL DE CALIDAD','2025-03-21 12:16:42',NULL,1),(28,'COORDINADOR DE ARCHIVO','2025-03-21 12:16:42',NULL,1),(29,'COORDINADOR DE DESPACHOS','2025-03-21 12:16:42',NULL,1),(30,'COORDINADOR DE VENTAS','2025-03-21 12:16:42',NULL,1),(31,'COORDINADOR FLOTA PROPIA','2025-03-21 12:16:42',NULL,1),(32,'COORDINADOR LOGISTICO','2025-03-21 12:16:42',NULL,1),(33,'CONTRALOR','2025-03-21 12:16:42',NULL,1),(34,'FACTURADOR','2025-03-21 12:16:42',NULL,1),(35,'GERENTE ADMINISTRATIVO Y FINANCIERO','2025-03-21 12:16:42',NULL,1),(36,'GERENTE GENERAL','2025-03-21 12:16:42',NULL,1),(37,'GERENTE OPERATIVO PLANTA LA MARIA','2025-03-21 12:16:42',NULL,1),(38,'JEFE DE AUDITORIA','2025-03-21 12:16:42',NULL,1),(39,'JEFE DE CARTERA','2025-03-21 12:16:42',NULL,1),(40,'JEFE DE COMPRAS Y ALMACEN','2025-03-21 12:16:42',NULL,1),(41,'JEFE DE CONTABILIDAD','2025-03-21 12:16:42',NULL,1),(42,'JEFE DE COSTOS','2025-03-21 12:16:42',NULL,1),(43,'JEFE DE PLANTA U OBRA LA MARIA','2025-03-21 12:16:42',NULL,1),(44,'JEFE DE RECURSOS HUMANOS','2025-03-21 12:16:42',NULL,1),(45,'JEFE DE SEGURIDAD Y SALUD EN EL TRABAJO','2025-03-21 12:16:42',NULL,1),(46,'JEFE GESTION DE CALIDAD','2025-03-21 12:16:42',NULL,1),(47,'MENSAJERO','2025-03-21 12:16:42',NULL,1),(48,'RECEPCIONISTA','2025-03-21 12:16:42',NULL,1),(49,'SUPERNUMERARIO','2025-03-21 12:16:42',NULL,1),(50,'SUPERNUMERARIO SST','2025-03-21 12:16:42',NULL,1),(51,'SUPERVISOR DE VIGILANCIA','2025-03-21 12:16:42',NULL,1),(52,'TESORERO','2025-03-21 12:16:42',NULL,1),(53,'VENDEDOR','2025-03-21 12:16:42',NULL,1),(54,'VIGILANTE','2025-03-21 12:16:42',NULL,1),(232,'AUXILIAR SST','2025-03-21 12:16:42',NULL,1),(236,'AUXILIAR DE RECURSOS HUMANOS','2025-03-23 17:33:22',NULL,1),(246,'PEPITO','2025-04-07 21:33:21','',1);
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
  `ultimo_transferido_por_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `radicado` (`radicado`),
  KEY `transportadora_id` (`transportadora_id`),
  KEY `tipo_documento_id` (`tipo_documento_id`),
  KEY `area_destino_id` (`area_destino_id`),
  KEY `persona_destino_id` (`persona_destino_id`),
  KEY `estado_actual_id` (`estado_actual_id`),
  KEY `registrado_por_id` (`registrado_por_id`),
  KEY `ultimo_transferido_por_id` (`ultimo_transferido_por_id`),
  CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`transportadora_id`) REFERENCES `transportadoras` (`id`),
  CONSTRAINT `documentos_ibfk_2` FOREIGN KEY (`tipo_documento_id`) REFERENCES `tipos_documento` (`id`),
  CONSTRAINT `documentos_ibfk_3` FOREIGN KEY (`area_destino_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `documentos_ibfk_4` FOREIGN KEY (`persona_destino_id`) REFERENCES `personas` (`id`),
  CONSTRAINT `documentos_ibfk_5` FOREIGN KEY (`estado_actual_id`) REFERENCES `estados_documento` (`id`),
  CONSTRAINT `documentos_ibfk_6` FOREIGN KEY (`registrado_por_id`) REFERENCES `usuarios` (`id`),
  CONSTRAINT `documentos_ibfk_7` FOREIGN KEY (`ultimo_transferido_por_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (59,'250407-0001','2025-04-07 13:46:00',3,'45645645654','EDWARD ',3,'10 contratos antiguos ','nada que decir ',1,49,1,'ENTRADA',2,'2025-04-07 13:46:00',NULL),(60,'250407-0002','2025-04-07 13:49:00',7,'645456456456','EDWARD ',2,'10 comprobantes de egreso ','nada que decir ',1,49,1,'ENTRADA',2,'2025-04-07 13:49:00',NULL),(61,'250407-0003','2025-04-07 13:52:00',13,'645456456456','EDWARD ',6,'20 cotizaciones ','mal estado \r\n',1,49,4,'ENTRADA',2,'2025-04-07 13:52:00',23),(62,'250407-0004','2025-04-07 13:46:00',18,'645456456456','EDWARD ',9,'','',1,49,1,'ENTRADA',2,'2025-04-07 13:46:00',NULL),(63,'250407-0005','2025-04-07 17:02:00',4,'159','Recepcion aguazul',11,'Prueba','',17,4,7,'ENTRADA',2,'2025-04-07 17:02:00',9),(64,'250407-0006','2025-04-07 17:05:00',13,'0123456789','Planta Aguazul',6,'','',1,103,5,'ENTRADA',2,'2025-04-07 17:05:00',55);
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
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historial_passwords`
--

LOCK TABLES `historial_passwords` WRITE;
/*!40000 ALTER TABLE `historial_passwords` DISABLE KEYS */;
INSERT INTO `historial_passwords` VALUES (1,55,'$2b$12$/m3iCzg7nKBp0AqHUq9YGe5y9ij354Q.3pGyHrMT7R7/.snhzUyP6','2025-03-31 16:01:09'),(2,55,'$2b$12$hT9ZelvTv.9mTAeHaqcxWerqf5qS86k2ntNp8wWvK8PcMz7B6M2zq','2025-03-31 16:40:11'),(3,55,'$2b$12$hT9ZelvTv.9mTAeHaqcxWerqf5qS86k2ntNp8wWvK8PcMz7B6M2zq','2025-03-31 16:40:11'),(4,55,'$2b$12$Oaq2URN07F9RsdxEKxM64O.4V/vkmW99LksucwvLujxO.nIN1JEQ6','2025-03-31 16:48:02'),(5,55,'$2b$12$cSaK4ASMvEm58/DsVIQEMusDCwMSN5LoW60JhtXw9mPoXqkUybWBa','2025-03-31 16:54:01'),(6,55,'$2b$12$Q/plr9rUIYKxE8oWieBdveULMecFH0AU1cQ2QDF27J1lDBlZ1qqh.','2025-03-31 17:07:07'),(7,55,'$2b$12$Q/plr9rUIYKxE8oWieBdveULMecFH0AU1cQ2QDF27J1lDBlZ1qqh.','2025-03-31 17:07:07'),(8,55,'$2b$12$rXyH3rDhLRltbqSVc1ThiuRf334oJj6gch5e4gY1.ia7SmDK1rXDi','2025-03-31 17:08:25'),(9,55,'$2b$12$GHlYpAR5HhntfTnHcVEYqeuIYI4SEYG1EraqysgH3/T6Zk94M3CRW','2025-04-01 14:36:16'),(10,55,'$2b$12$EAuEh8YAQ/mIrpulyGyFtOTkUgwxPjfsHAjEkXDUkS8g2UFmG.Q6i','2025-04-01 14:37:11'),(11,55,'$2b$12$XF/xY5SGtxP0Q07QzGh3vuL4J8zmNnhQJ1lS.qsm3/nmuoyPivnza','2025-04-01 14:39:46'),(12,55,'$2b$12$Qgc0/DQSzdEThW.IJwK0SesqtD4jOx8tHJYKQeDpBB7I9JvuMYJpS','2025-04-01 14:50:34'),(13,55,'$2b$12$w.iqxmnttjvRpHxsRFnRzeOtSZLbmVcpmIiUIWLXttYkkJPPwyY4q','2025-04-01 14:50:59'),(14,10,'$2b$12$1/XsVHZv7IdsyHZARfWoeubjUBpgb6M22Kt0PTVi5vFy0DO9.iwnm','2025-04-06 19:58:13'),(15,55,'$2b$12$Wa8ryTF94oS.X.j.vBJi0O1IvOGb/877RXPWfRBaLLaFzlmehWfgC','2025-04-07 16:29:28');
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
) ENGINE=InnoDB AUTO_INCREMENT=182 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
INSERT INTO `movimientos` VALUES (170,59,'2025-04-07 13:46:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-04-07 18:49:53'),(171,60,'2025-04-07 13:49:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-04-07 18:52:37'),(172,61,'2025-04-07 13:52:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-04-07 19:06:22'),(173,62,'2025-04-07 13:46:00',2,17,4,1,49,1,'Documento registrado en recepción','2025-04-07 19:19:00'),(174,61,'2025-04-07 19:23:57',23,1,49,1,49,2,'Documento aceptado para procesamiento','2025-04-07 19:23:57'),(175,63,'2025-04-07 17:02:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-04-07 22:02:31'),(176,63,'2025-04-07 22:03:33',9,7,21,17,4,7,'Documento rechazado por MARIA PAULA LOZANO LOZANO. Motivo: Después de las 5, no recibimos documentación ','2025-04-07 22:03:33'),(177,64,'2025-04-07 17:05:00',2,17,4,1,103,1,'Documento registrado en recepción','2025-04-07 22:06:14'),(178,64,'2025-04-07 22:06:55',55,1,103,1,103,2,'Documento aceptado para procesamiento','2025-04-07 22:06:55'),(179,64,'2025-04-07 22:07:00',55,1,103,1,103,4,'Documento finalizado','2025-04-07 22:07:00'),(180,64,'2025-04-08 13:38:16',55,1,103,1,103,5,'Documento archivado','2025-04-08 13:38:16'),(181,61,'2025-04-08 13:39:01',23,1,49,1,49,4,'Documento finalizado','2025-04-08 13:39:01');
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
) ENGINE=InnoDB AUTO_INCREMENT=152 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificaciones`
--

LOCK TABLES `notificaciones` WRITE;
/*!40000 ALTER TABLE `notificaciones` DISABLE KEYS */;
INSERT INTO `notificaciones` VALUES (143,23,'Nuevo documento asignado - 250407-0001','Se te ha asignado un nuevo documento de tipo CONTRATOS.',59,1,'2025-04-07 13:49:53'),(144,23,'Nuevo documento asignado - 250407-0002','Se te ha asignado un nuevo documento de tipo COMPROBANTES.',60,0,'2025-04-07 13:52:37'),(145,23,'Nuevo documento asignado - 250407-0003','Se te ha asignado un nuevo documento de tipo COTIZACIONES.',61,1,'2025-04-07 14:06:22'),(146,23,'Nuevo documento asignado - 250407-0004','Se te ha asignado un nuevo documento de tipo MANUALES.',62,1,'2025-04-07 14:19:00'),(147,23,'Documento aceptado - 250407-0003','El documento ha sido aceptado por JAIME VARGAS RAMIREZ.',61,1,'2025-04-07 14:23:57'),(148,9,'Nuevo documento asignado - 250407-0005','Se te ha asignado un nuevo documento de tipo FLETES.',63,1,'2025-04-07 17:02:31'),(149,2,'Documento rechazado - 250407-0005','El documento ha sido rechazado por MARIA PAULA LOZANO LOZANO. Motivo: Después de las 5, no recibimos documentación ',63,1,'2025-04-07 17:03:33'),(150,55,'Nuevo documento asignado - 250407-0006','Se te ha asignado un nuevo documento de tipo COTIZACIONES.',64,1,'2025-04-07 17:06:14'),(151,55,'Documento aceptado - 250407-0006','El documento ha sido aceptado por PEPITO.',64,1,'2025-04-07 17:06:55');
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
) ENGINE=InnoDB AUTO_INCREMENT=141 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (1,'RICARDO ALEXANDER BOHÓRQUEZ MÉNDEZ','rbohorquez@arrozsonora.com.co','3112815201',1,1,19,3,1,'2025-03-20 12:08:58'),(2,'JAIRO ANTONIO LOZANO VARGAS','jalozano@arrozsonora.com.co','3102118013',1,2,20,45,1,'2025-03-20 12:08:58'),(3,'OLGA PATRICIA ORTIZ RIVAS','oortiz@arrozsonora.com.co',NULL,1,3,6,40,1,'2025-03-20 12:08:58'),(4,'YAZMINA LORENA FAYAD GUTIERREZ','yfayad@arrozsonora.com.co','3104567890',1,1,17,48,1,'2025-03-20 12:08:58'),(5,'JAIRO SEDAN MURRA','jsedan@arrozsonora.com.co',NULL,1,1,13,36,1,'2025-03-21 09:11:56'),(6,'JULIO CESAR CEPEDA RODRÍGUEZ','jcepeda@arrozsonora.com.co',NULL,1,1,14,37,1,'2025-03-21 09:11:56'),(7,'YULY SLENDY CASTILLO ROBAYO','ycastillo@arrozsonora.com.co',NULL,1,1,12,35,1,'2025-03-21 09:11:56'),(8,'MYRIAM RODRÍGUEZ ARCINIEGAS','mrodriguez@arrozsonora.com.co',NULL,1,1,8,33,1,'2025-03-21 09:11:56'),(9,'BRAYAN SANTICK QUINTERO CORDOBA','bquintero@arrozsonora.com.co',NULL,1,1,2,5,1,'2025-03-21 09:11:56'),(10,'VIVIANA CAYCEDO BOCANEGRA','vcaycedo@arrozsonora.com.co',NULL,1,1,21,49,1,'2025-03-21 09:11:56'),(11,'MARTHA YANETH DIAZ TRIGUEROS','mdiaz@arrozsonora.com.co',NULL,1,1,22,52,1,'2025-03-21 09:11:56'),(12,'SANDRA BIBIANA LAVERDE PARRA','slaverde@arrozsonora.com.co',NULL,1,1,22,13,1,'2025-03-21 09:11:56'),(13,'JUAN DAVID LOZANO GUZMAN','jlozano@arrozsonora.com.co',NULL,1,1,22,20,1,'2025-03-21 09:11:56'),(14,'DIANA MARCELA BOCANEGRA TOVAR','dbocanegra@arrozsonora.com.co',NULL,1,1,22,12,1,'2025-03-21 09:11:56'),(15,'TERESA TOVAR RIVERA','ttovar@arrozsonora.com.co',NULL,1,1,5,9,1,'2025-03-21 09:11:56'),(16,'ANGY YULITZA VARGAS PADILLA','avargas@arrozsonora.com.co',NULL,1,1,5,18,1,'2025-03-21 09:11:56'),(17,'XIMENA PAOLA BOCANEGRA ORTIZ','xbocanegra@arrozsonora.com.co',NULL,1,1,7,41,1,'2025-03-21 09:11:56'),(18,'JOAN JAIR RODRIGUEZ PORTELA','jrodriguez@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(19,'ADRIANA LUCIA GONZALEZ SERRANO','agonzalez@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(20,'LIZETH DANIELA MELO OLIS','lmelo@arrozsonora.com.co',NULL,1,1,7,8,1,'2025-03-21 09:11:56'),(21,'MARIA PAULA LOZANO LOZANO','mlozano@arrozsonora.com.co',NULL,1,1,7,19,1,'2025-03-21 09:11:56'),(22,'SILVIA PATRICIA RIVERA ZABALA','srivera@arrozsonora.com.co',NULL,1,1,7,19,1,'2025-03-21 09:11:56'),(23,'ANDRES FELIPE ARIAS VARGAS','aarias@arrozsonora.com.co',NULL,1,1,3,16,1,'2025-03-21 09:11:56'),(24,'DIANA CAROLINA RUBIANO','drubiano@arrozsonora.com.co',NULL,1,1,11,19,1,'2025-03-21 09:11:56'),(25,'ANDREA DEL PILAR MORALES TRUJILLO','amorales@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(26,'KAREN NUREIDYS CARCAMO LONDONO','kcarcamo@arrozsonora.com.co',NULL,1,1,9,42,1,'2025-03-21 09:11:56'),(27,'JULIAN ANDRES MOLINA AVILA','jmolina@arrozsonora.com.co',NULL,1,1,9,10,1,'2025-03-21 09:11:56'),(28,'NATALY TATIANA PUENTES SIERRA','npuentes@arrozsonora.com.co',NULL,1,1,3,38,1,'2025-03-21 09:11:56'),(29,'ADRIANA DEL PILAR LOPEZ BUSTOS','alopez@arrozsonora.com.co',NULL,1,1,3,16,1,'2025-03-21 09:11:56'),(31,'LEIDY JOHANA AVILA GONZALEZ','lavila@arrozsonora.com.co',NULL,1,1,4,39,1,'2025-03-21 09:11:56'),(32,'JULIETH PAOLA GONZALEZ ONATRA','jgonzalez@arrozsonora.com.co',NULL,1,1,4,6,1,'2025-03-21 09:11:56'),(33,'JONATHAN FABIAN MANRIQUE RODRIGUEZ','jmanrique@arrozsonora.com.co',NULL,1,1,4,17,1,'2025-03-21 09:11:56'),(34,'ANGIE KATHERINE ZAMORA CORDOBA','azamora@arrozsonora.com.co',NULL,1,1,4,17,0,'2025-03-21 09:11:56'),(35,'LUANA SIMONA SENDOYA ECHEVERRY','lsendoya@arrozsonora.com.co',NULL,1,1,23,30,1,'2025-03-21 09:11:56'),(36,'ANGI XIOMARA RAMIREZ ORTIZ','aramirez@arrozsonora.com.co',NULL,1,1,23,21,1,'2025-03-21 09:11:56'),(37,'JUAN JOSE COTE HERNANDEZ','jcote@arrozsonora.com.co',NULL,1,1,15,32,1,'2025-03-21 09:11:56'),(38,'ANGELA MARIA ZARTHA LEAL','azartha@arrozsonora.com.co',NULL,1,1,15,22,1,'2025-03-21 09:11:56'),(39,'JUAN PABLO CELIS CASTILLO','jcelis@arrozsonora.com.co',NULL,1,1,15,31,1,'2025-03-21 09:11:56'),(40,'ANA MARIA RODRIGUEZ MORA','arodriguez@arrozsonora.com.co',NULL,1,1,18,44,1,'2025-03-21 09:11:56'),(41,'SANDRA MILENA GARCIA GONZALEZ','sgarcia@arrozsonora.com.co',NULL,1,1,18,11,1,'2025-03-21 09:11:56'),(42,'YENDY FANNORY BRAVO GUTIERREZ','ybravo@arrozsonora.com.co',NULL,1,2,10,34,1,'2025-03-21 09:11:56'),(43,'KELLY JOHANNA GOMEZ LOZANO','kgomez@arrozsonora.com.co',NULL,1,2,20,232,1,'2025-03-21 09:11:56'),(44,'SANDRA MILENA VILLA ROJAS','smvilla@arrozsonora.com.co',NULL,1,2,88,46,1,'2025-03-21 09:11:56'),(45,'DIANA ALEJANDRA ORTIZ JARA','dortiz@arrozsonora.com.co',NULL,1,2,88,27,1,'2025-03-21 09:11:56'),(46,'JAMES EDUARDO RUEDA TRUJILLO','jrueda@arrozsonora.com.co',NULL,1,2,16,43,1,'2025-03-21 09:11:56'),(47,'LUIS ALBERTO BARRETO GUZMAN','lbarreto@arrozsonora.com.co',NULL,1,3,6,1,1,'2025-03-21 09:11:56'),(48,'LUIS ALEJANDRO OLIVEROS GUARNIZO',NULL,NULL,1,3,6,15,1,'2025-03-21 09:11:56'),(49,'JAIME VARGAS RAMIREZ','jvargas@arrozsonora.com.co',NULL,1,3,1,28,1,'2025-03-21 09:11:58'),(95,'LINA JULIETH CARVAJAL MENDOZA','aniiljulieth@hotmail.com',NULL,1,1,19,4,1,'2025-03-21 20:01:07'),(99,'JORGE ELIAS ORTIZ','jortiz@arrozsonora.com.co',NULL,1,2,23,29,1,'2025-03-23 17:44:44'),(103,'PEPITO',NULL,NULL,2,1,1,4,1,'2025-03-31 15:49:51'),(112,'LAURA DANIELA ALVIS ABREO','lalvis@arrozsonora.com.co',NULL,1,1,18,236,1,'2025-04-04 19:40:49'),(115,'STIVEN SERRANO SOLORZANO','sserrano@arrozsonora.com.co',NULL,1,1,11,19,1,'2025-04-04 21:27:39'),(117,'Modelo - ASISTENTE ADMINISTRATIVO - APRENDIZ SENA',NULL,NULL,1,1,2,4,0,'2025-04-07 21:01:52'),(118,'Modelo - AUDITORIA - APRENDIZ SENA',NULL,NULL,1,1,3,4,0,'2025-04-07 21:01:52'),(119,'Modelo - CARTERA - APRENDIZ SENA',NULL,NULL,1,1,4,4,0,'2025-04-07 21:01:52'),(120,'Modelo - COMPRAS PADDY - APRENDIZ SENA',NULL,NULL,1,1,5,4,0,'2025-04-07 21:01:52'),(121,'Modelo - COMPRAS Y ALMACEN - APRENDIZ SENA',NULL,NULL,1,1,6,4,0,'2025-04-07 21:01:52'),(122,'Modelo - CONTABILIDAD - APRENDIZ SENA',NULL,NULL,1,1,7,4,0,'2025-04-07 21:01:52'),(123,'Modelo - CONTRALORIA - APRENDIZ SENA',NULL,NULL,1,1,8,4,0,'2025-04-07 21:01:52'),(124,'Modelo - COSTOS - APRENDIZ SENA',NULL,NULL,1,1,9,4,0,'2025-04-07 21:01:52'),(125,'Modelo - FACTURACION - APRENDIZ SENA',NULL,NULL,1,1,10,4,0,'2025-04-07 21:01:52'),(126,'Modelo - FLETES - APRENDIZ SENA',NULL,NULL,1,1,11,4,0,'2025-04-07 21:01:52'),(127,'Modelo - GERENTE ADMINISTRATIVO Y FINANCIERO - APRENDIZ SENA',NULL,NULL,1,1,12,4,0,'2025-04-07 21:01:52'),(128,'Modelo - GERENTE GENERAL - APRENDIZ SENA',NULL,NULL,1,1,13,4,0,'2025-04-07 21:01:52'),(129,'Modelo - GERENTE OPERATIVO - APRENDIZ SENA',NULL,NULL,1,1,14,4,0,'2025-04-07 21:01:52'),(130,'Modelo - LOGISTICA - APRENDIZ SENA',NULL,NULL,1,1,15,4,0,'2025-04-07 21:01:52'),(131,'Modelo - PRODUCCION - APRENDIZ SENA',NULL,NULL,1,1,16,4,0,'2025-04-07 21:01:52'),(132,'Modelo - RECEPCION - APRENDIZ SENA',NULL,NULL,1,1,17,4,0,'2025-04-07 21:01:52'),(133,'Modelo - RRHH - APRENDIZ SENA',NULL,NULL,1,1,18,4,0,'2025-04-07 21:01:52'),(134,'Modelo - SST - APRENDIZ SENA',NULL,NULL,1,1,20,4,0,'2025-04-07 21:01:52'),(135,'Modelo - SUPERNUMERARIO - APRENDIZ SENA',NULL,NULL,1,1,21,4,0,'2025-04-07 21:01:52'),(136,'Modelo - TESORERIA - APRENDIZ SENA',NULL,NULL,1,1,22,4,0,'2025-04-07 21:01:52'),(137,'Modelo - VENTAS - APRENDIZ SENA',NULL,NULL,1,1,23,4,0,'2025-04-07 21:01:52'),(138,'Modelo - CALIDAD - APRENDIZ SENA',NULL,NULL,1,1,88,4,0,'2025-04-07 21:01:52'),(140,'Modelo - ASISTENTE ADMINISTRATIVO - PEPITO',NULL,NULL,1,1,2,246,0,'2025-04-07 21:33:21');
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_documento`
--

LOCK TABLES `tipos_documento` WRITE;
/*!40000 ALTER TABLE `tipos_documento` DISABLE KEYS */;
INSERT INTO `tipos_documento` VALUES (1,'FACTURAS','2025-03-20 12:08:58','',1),(2,'COMPROBANTES','2025-03-20 12:08:58','',1),(3,'CONTRATOS','2025-03-20 12:08:58','',1),(4,'CORRESPONDENCIA','2025-03-20 12:08:58','',1),(5,'TIQUETES','2025-03-20 12:08:58','',1),(6,'COTIZACIONES','2025-03-20 12:08:58','',1),(7,'ÓRDENES DE COMPRA','2025-03-20 12:08:58','',1),(8,'HOJAS DE VIDA','2025-03-20 12:08:58','',1),(9,'MANUALES','2025-03-20 12:08:58','',1),(10,'INFORMES','2025-03-20 12:08:58','',1),(11,'FLETES','2025-03-20 12:08:58','',1),(15,'LEGALIZACIONES','2025-04-03 16:14:19','',1);
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=128 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transportadoras`
--

LOCK TABLES `transportadoras` WRITE;
/*!40000 ALTER TABLE `transportadoras` DISABLE KEYS */;
INSERT INTO `transportadoras` VALUES (1,'DEPRISA','2025-03-20 12:08:58',NULL,1),(2,'SERVIENTREGA','2025-03-20 12:08:58',NULL,1),(3,'ENVIA','2025-03-20 12:08:58',NULL,1),(4,'COORDINADORA','2025-03-20 12:08:58',NULL,1),(5,'SAFERBO','2025-03-20 12:08:58',NULL,1),(6,'INTERRAPIDISIMO','2025-03-20 12:08:58',NULL,1),(7,'AXPRESS','2025-03-20 12:08:58',NULL,1),(8,'REDETRANS','2025-03-20 12:08:58',NULL,1),(9,'TCC','2025-03-20 12:08:58',NULL,1),(10,'4-72','2025-03-20 12:08:58','',1),(11,'TRANSPRENSA','2025-03-20 12:08:58',NULL,1),(12,'PORTERIA','2025-03-20 12:08:58',NULL,1),(13,'CERTIPOSTAL','2025-03-20 12:08:58',NULL,1),(14,'ENCO EXPRES','2025-03-20 12:08:58',NULL,1),(15,'X-CARGO','2025-03-20 12:08:58',NULL,1),(16,'DHL EXPRESS','2025-03-20 12:08:58',NULL,1),(17,'OPEN MARKET','2025-03-20 12:08:58',NULL,1),(18,'EXPRESO BOLIVARIANO','2025-03-20 12:08:58',NULL,1),(19,'MERCADOLIBRE','2025-03-20 12:08:58',NULL,1),(20,'INTERSERVICE','2025-03-20 12:08:58',NULL,1),(23,'MENSAJERO MOLINO SONORA','2025-03-25 13:06:00',NULL,1),(26,'ADOLFO EMILIO GONZALEZ PEREZ','2025-04-08 09:38:20','Transportadora Adolfo Emilio Gonzalez Perez',1),(27,'AGROCISCO SAS','2025-04-08 09:38:20','Transportadora Agrocisco SAS',1),(28,'ALBERTO SANCHEZ DIAZ','2025-04-08 09:38:20','Transportadora Alberto Sanchez Diaz',1),(29,'ALVARO JAVIER ORTIZ VARGAS','2025-04-08 09:38:20','Transportadora Alvaro Javier Ortiz Vargas',1),(30,'ALVARO ORTIZ BARRERO','2025-04-08 09:38:20','Transportadora Alvaro Ortiz Barrero',1),(31,'ANGEE LORENA USECHE','2025-04-08 09:38:20','Transportadora Angee Lorena Useche',1),(32,'ARIEL MOLANO','2025-04-08 09:38:20','Transportadora Ariel Molano',1),(33,'BECERRA DIAZ Y ASOCIADOS SAS','2025-04-08 09:38:20','Transportadora Becerra Diaz y Asociados SAS',1),(34,'CARLOS PORTELA','2025-04-08 09:38:20','Transportadora Carlos Portela',1),(35,'COOPERATIVA MULTIACTIVA Y DE TRANSPORTE DE SANTANDER-CETER','2025-04-08 09:38:20','Transportadora Cooperativa Multiactiva y de Transporte de Santander-CETER',1),(36,'DANIEL ARMANDO BARRERA CASTAÑEDA','2025-04-08 09:38:20','Transportadora Daniel Armando Barrera Castañeda',1),(37,'DELTRANS SAS','2025-04-08 09:38:20','Transportadora Deltrans SAS',1),(38,'EMPRESA DE TRANSPORTES MURCIA SAS','2025-04-08 09:38:20','Transportadora Empresa de Transportes Murcia SAS',1),(39,'EULISES ANGEL BAQUERO','2025-04-08 09:38:20','Transportadora Eulises Angel Baquero',1),(40,'FERNEY BAHAMON ARIAS','2025-04-08 09:38:20','Transportadora Ferney Bahamon Arias',1),(41,'FREDY CAYCEDO LOZANO','2025-04-08 09:38:20','Transportadora Fredy Caycedo Lozano',1),(42,'GEINER OSWALDO DIAZ RODRIGUEZ','2025-04-08 09:38:20','Transportadora Geiner Oswaldo Diaz Rodriguez',1),(43,'GERMAN NIÑO LOZANO','2025-04-08 09:38:20','Transportadora German Niño Lozano',1),(44,'HERIBERTO CARO AREVALO','2025-04-08 09:38:20','Transportadora Heriberto Caro Arevalo',1),(45,'HERNEY GUARNIZO ROJAS','2025-04-08 09:38:20','Transportadora Herney Guarnizo Rojas',1),(46,'IMPOCOMA SAS','2025-04-08 09:38:20','Transportadora Impocoma SAS',1),(47,'INVERCARGA SAS','2025-04-08 09:38:20','Transportadora Invercarga SAS',1),(48,'INVERSIONES MUÑOZ Y CAMARGO SAS','2025-04-08 09:38:20','Transportadora Inversiones Muñoz y Camargo SAS',1),(49,'INVERSIONES RIVETELA SAS','2025-04-08 09:38:20','Transportadora Inversiones Rivetela SAS',1),(50,'JOSE EDUARDO VELANDIA OTALORA','2025-04-08 09:38:20','Transportadora Jose Eduardo Velandia Otalora',1),(51,'JOSE POMPILIO LOPEZ NOVOA','2025-04-08 09:38:20','Transportadora Jose Pompilio Lopez Novoa',1),(52,'JUAN PABLO RODRIGUEZ CRUZ','2025-04-08 09:38:20','Transportadora Juan Pablo Rodriguez Cruz',1),(53,'JULIAN FELIPE OYUELA GUZMAN','2025-04-08 09:38:20','Transportadora Julian Felipe Oyuela Guzman',1),(54,'LOGISTICA MASTERS SAS','2025-04-08 09:38:20','Transportadora Logistica Masters SAS',1),(55,'LOGISTICA Y TRANSPORTE DEL LLANO EXPRESS SAS','2025-04-08 09:38:20','Transportadora Logistica y Transporte del Llano Express SAS',1),(56,'LUIS ORLANDO GONZALEZ SIERRA','2025-04-08 09:38:20','Transportadora Luis Orlando Gonzalez Sierra',1),(57,'OLT SA','2025-04-08 09:38:20','Transportadora OLT SA',1),(58,'OPL CARGA SAS','2025-04-08 09:38:20','Transportadora OPL Carga SAS',1),(59,'ORLANDO CALDERON LONDOÑO','2025-04-08 09:38:20','Transportadora Orlando Calderon Londoño',1),(60,'RAUMIR ROJAS CASTRO','2025-04-08 09:38:20','Transportadora Raumir Rojas Castro',1),(61,'SERVINALTRA SAS','2025-04-08 09:38:20','Transportadora Servinaltra SAS',1),(62,'SOTRAL SAS','2025-04-08 09:38:20','Transportadora Sotral SAS',1),(63,'TAGA','2025-04-08 09:38:20','Transportadora TAGA',1),(64,'TANQUES Y SERVICIOS DEL CASANARE SAS','2025-04-08 09:38:20','Transportadora Tanques y Servicios del Casanare SAS',1),(65,'TKARGA SAS','2025-04-08 09:38:20','Transportadora TKarga SAS',1),(66,'TRANSHUILA SA','2025-04-08 09:38:20','Transportadora Transhuila SA',1),(67,'TRANSPORTE LOGISTICOS DE CARGA GMT SAS','2025-04-08 09:38:20','Transportadora Transporte Logisticos de Carga GMT SAS',1),(68,'TRANSPORTES GAYCO SAS','2025-04-08 09:38:20','Transportadora Transportes Gayco SAS',1),(69,'TRANSPORTES OKENDO SAS','2025-04-08 09:38:20','Transportadora Transportes Okendo SAS',1),(70,'TRANSPORTES PRONTERRESTRE SA','2025-04-08 09:38:20','Transportadora Transportes Pronterrestre SA',1),(71,'VIACARGO SAS','2025-04-08 09:38:20','Transportadora Viacargo SAS',1),(72,'VICTOR VARGAS QUESADA','2025-04-08 09:38:20','Transportadora Victor Vargas Quesada',1),(73,'WALTER JOSE AVELLANEDA RODRIGUEZ','2025-04-08 09:38:20','Transportadora Walter Jose Avellaneda Rodriguez',1),(74,'TRANSPORTE BERNAL Y BERNAL SAS','2025-04-08 09:38:20','Transportadora Transporte Bernal y Bernal SAS',1),(75,'TRANSPORTES Y SERVICIOS TRANSER SAS','2025-04-08 09:38:20','Transportadora Transportes y Servicios Transer SAS',1),(76,'CARGOANDINA SAS','2025-04-08 09:38:20','Transportadora Cargoandina SAS',1),(77,'EMPRESA COLOMBIANA DE LOGISTICA SAS','2025-04-08 09:38:20','Transportadora Empresa Colombiana de Logistica SAS',1),(78,'WILMER CASTRO LINARES','2025-04-08 09:38:20','Transportadora Wilmer Castro Linares',1);
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unidades`
--

LOCK TABLES `unidades` WRITE;
/*!40000 ALTER TABLE `unidades` DISABLE KEYS */;
INSERT INTO `unidades` VALUES (1,'ADMINISTRACION','2025-03-20 12:08:58','',1),(2,'BASCULA Y CALIDAD','2025-03-20 12:08:58',NULL,1),(3,'ALMACEN','2025-03-20 12:08:58',NULL,1);
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
INSERT INTO `usuarios` VALUES (1,'rbohorquez','$2b$12$.Vsma9zYL6ivAOrfzNbN2uO8tw7.21nUBONXcUzOyHWPOrR82AdUq',1,1,'2025-04-08 14:32:06',1,'2025-03-20 21:18:20'),(2,'yfayad','$2b$12$.Vsma9zYL6ivAOrfzNbN2uO8tw7.21nUBONXcUzOyHWPOrR82AdUq',4,2,'2025-04-08 14:09:44',1,'2025-03-21 12:39:04'),(8,'npuentes','$2b$12$2Q44xvcj0xIBIL4R6nty2uMMOLTFFU4d3UiW1F.ZaGi9a9WcH.syK',28,3,'2025-04-07 16:25:39',1,'2025-03-22 05:06:01'),(9,'mlozano','$2b$12$ZDiZDmGcldxaGx1FIM13cOV2qk7DVCdgnD4.1ZKBRMd7QaP201ege',21,3,'2025-04-07 22:02:47',1,'2025-03-22 05:06:52'),(10,'lcarvajal','$2b$12$U.td2sPhtyCCDiAPaZzFA.ZnnOESf8llwVLfpRpgRNyeW1KGct34u',95,1,'2025-04-07 15:30:43',1,'2025-03-22 19:10:49'),(12,'alopez','$2b$12$2OYLs2AYPKiEt.5QzCN7JuRtyLbjHqN7gt173/qa4vHFH72OTLIvO',29,3,'2025-03-31 22:11:10',1,'2025-03-25 16:46:25'),(13,'agonzalez','$2b$12$WF/f7GLQiNJqgYh5tLgcTuCodR1HZjzTBhf8PBneJio2RDOLpacTi',19,3,NULL,1,'2025-03-25 16:50:53'),(14,'arodriguez','$2b$12$xitKvoCKaJ//OyJ2mx9e5Oqd3pBhbXCjGWtcZOjrtii7hJJl8kMDG',40,3,'2025-03-25 21:24:50',1,'2025-03-25 16:51:48'),(15,'amorales','$2b$12$d83P1TYpyFVXsdyxL4pF8OSS1S6kedJjHy8LX5FHJ5VrcH20wUtdu',25,3,'2025-04-01 16:59:44',1,'2025-03-25 16:53:44'),(16,'aarias','$2b$12$SXWUOMOeerQ8ukZVbTGRr.FW3xCx.GX9VZBAxAHTZp7Ui/WnhWCMK',23,3,'2025-03-31 22:10:41',1,'2025-03-25 16:54:21'),(17,'azartha','$2b$12$0FXHZgIAY/dli9Dki5OaCOzGaZtMCB42ma/sFc.H/Cp0J4MGgRm76',38,3,NULL,1,'2025-03-25 16:55:05'),(18,'aramirez','$2b$12$9/IwWDjKjzptit8QIGRbN.LbEcxfpTf6WcBAxdMFh9jiDAtqgFG1K',36,3,'2025-04-03 20:36:23',1,'2025-03-25 16:58:46'),(19,'avargas','$2b$12$2tBn9q1leEWo0efdI/P.RuxKdEt56fFnlqo0iaWin.x2CeGnochhm',16,3,'2025-04-01 14:29:39',1,'2025-03-25 17:02:23'),(20,'bquintero','$2b$12$Le3jjYqfqqXTZLdO7XNhxOpm1kek8eW7j1PBfNd.utj9lE5axDuMe',9,3,'2025-03-31 22:08:58',1,'2025-03-25 17:03:31'),(21,'dortiz','$2b$12$KOwmzywl0q0E4jBWlQu3X.iW3YF0vteH8g62m8vEZRI1p0xFut3oK',45,3,'2025-03-31 22:11:49',1,'2025-03-25 17:04:40'),(22,'dbocanegra','$2b$12$FWHVrgn2t2Q5gn/NH.vjdu0lnQuIOzyCUzGS/KBUERqUm9OPcvIjq',14,3,NULL,1,'2025-03-25 17:07:09'),(23,'jvargas','$2b$12$ExGSx/7fM9mudBS3BnSIHOL7x0CSp.vi4QyW5mOEUzvMSmEhUbdU2',49,3,'2025-04-08 13:38:50',1,'2025-03-25 17:07:57'),(24,'jalozano','$2b$12$jPoosjjHlFB41USTVPvE/uN93zxHRdE7KaARYjbZC.K/29BkAT93W',2,3,NULL,1,'2025-03-25 17:08:50'),(25,'jsedan','$2b$12$FSchTfuN9LI2BQs70hDHz.inecxoN1820dxvHIRnr0HRZzonT73V.',5,3,'2025-03-31 16:10:52',1,'2025-03-25 17:12:03'),(26,'jrueda','$2b$12$DRVa/qWbaOzvWG9oP8qem.PA/LhBardGhZsoumcsBqc/FfweEzUqW',46,3,NULL,1,'2025-03-25 17:12:43'),(27,'jrodriguez','$2b$12$NJCFGoPT2OrP2zLpi7cEI.MKm37YZuB8FFVz.oqEwrry9ACIq/hfe',18,3,NULL,1,'2025-03-25 17:15:06'),(28,'jmanrique','$2b$12$EPC6MbEsrlwvg5MnM0yoDeuEyCrWhUd7Ax5tg/xfdcl369NG2ooHm',33,3,'2025-03-31 22:25:01',1,'2025-03-25 17:16:27'),(29,'jortiz','$2b$12$96ir9Jul09nn/zQPBJoAQuDe0u2KreQu9wMTfELAIW4AEv8T2cLZe',99,3,NULL,1,'2025-03-25 19:10:55'),(30,'jlozano','$2b$12$auI6r5R7scNeBKLXy3vVZeLfaZ1HrrWnABO8TdGTwfGl7vuNjJR1a',13,3,'2025-04-01 17:13:19',1,'2025-03-25 19:11:31'),(31,'jcote','$2b$12$AlwAcV8hOAdBgP7dhJORr.oF9SEsUnpPifA7o5rXha41nRa1jCOjm',37,3,NULL,1,'2025-03-25 19:14:24'),(32,'jcelis','$2b$12$MMjPC/q2g2PJhJgRoHqax.ig74wwTxsXOgP/pbOuva8YRmnTduBYq',39,3,NULL,1,'2025-03-25 19:15:01'),(33,'jmolina','$2b$12$LWFKKoxl3Xj0kwHEBUGD7.azWnA3FQ.Ov.PlYzbLD0DSJCAPbc8D2',27,3,NULL,1,'2025-03-25 19:15:31'),(34,'jgonzalez','$2b$12$nNrGstpBWBuNxGFf44.X/uUNwYKE0MJOiJUGXKnJjnpPIrcrkOfO6',32,3,'2025-03-31 22:26:09',1,'2025-03-25 19:16:02'),(35,'jcepeda','$2b$12$cock2CS6sTofSNcrDep2vO5qCrlsX6ZAt54jqxA54vmvaDtOtxc3e',6,3,NULL,1,'2025-03-25 19:16:38'),(36,'kcarcamo','$2b$12$utcRNp60mdBKdG0JcAfwkeuZHiiS5SlxXcFoOsJCzxH2WWrqCVvum',26,3,NULL,1,'2025-03-25 19:17:14'),(37,'kgomez','$2b$12$44eUOZ2Kqk3nZG0Qar/xsOw.KM8sNQPVShco.hTab73KIEIZ5lROW',43,3,NULL,1,'2025-03-25 19:17:42'),(38,'lrodriguez','$2b$12$ZoZpw0kxSLt1u0db.aQNq.zmWXzGiOm42w9U.8JddcQc9gY0dWVDu',24,3,'2025-04-03 21:47:16',1,'2025-03-25 19:18:08'),(39,'lavila','$2b$12$smkWycwLGgGqOxIZ3kRgwuvHCY1zCvMc7wTx5NrMrgeQHzlVcVFRK',31,3,'2025-03-31 22:26:58',1,'2025-03-25 19:18:43'),(40,'lmelo','$2b$12$Fdb07A94Q3oAwg7Qq6ETJeFBCEpLTcKfjF7cDOkUJjviRc31uAYiy',20,3,'2025-04-01 17:04:42',1,'2025-03-25 19:19:41'),(41,'lsendoya','$2b$12$dyCPPmPHDIp2TOgZFqHcAeajbjYofNnLThHxjwaaRQWGObkpeIeWm',35,3,NULL,1,'2025-03-25 19:20:19'),(42,'lbarreto','$2b$12$t3gUswD1BtDVZaRSGo8IMOBTX6SocZvH6YLihA/8Nb2BO381nvCU2',47,3,NULL,1,'2025-03-25 19:20:56'),(43,'mdiaz','$2b$12$AUrqTKf0QdQEfyGeDgWmCuzW53O.v6njVtZAjU.11Mkv/nM.GVkNK',11,3,NULL,1,'2025-03-25 19:23:18'),(44,'mrodriguez','$2b$12$hIERq3qObvSHM9NSiLZ/KeI7nsJZJb8JpFic6xm/Haig/GZsBazk2',8,3,NULL,1,'2025-03-25 19:24:43'),(45,'oortiz','$2b$12$cgwdxDncLJ/XHmYr0hfJ0uQizFr8z8XpQUa78gXJRenttIRHX0qCG',3,3,NULL,1,'2025-03-25 19:25:28'),(46,'slaverde','$2b$12$NbyymTCSflxLP4mLy4w7buKnJT2psFnn/d2VV9F2OMTIJ0Xd1WhwS',12,3,'2025-04-03 22:13:13',1,'2025-03-25 19:26:01'),(47,'svilla','$2b$12$iHIMDEUQpoTcblarVA1fguXTyzCqtu8iAPc3Tvbf1hprbAIZqrKOi',44,3,'2025-03-31 22:24:32',1,'2025-03-25 19:26:40'),(48,'srivera','$2b$12$HEZvOky.QYBwWOpd3UJoHucfqZAyrvBTodAVR6tOctoni4buRexBC',22,3,NULL,1,'2025-03-25 19:28:01'),(49,'ttovar','$2b$12$Yp3O32btlkSi72/x/TWJg.1mzc/CyVf/b9EuzQO5uiiPZdHOcCd/2',15,3,'2025-04-01 14:35:06',1,'2025-03-25 19:28:30'),(50,'vcaycedo','$2b$12$0JaWzdvzbhsUmeu4JVUzk.vjOn/Lagy55XEQPDWGZQ4fOKoCELVIu',10,3,NULL,1,'2025-03-25 19:28:55'),(51,'xbocanegra','$2b$12$yF5GRGlpO.3qAHT0DAfJNeTahJpbm4GlW2ZckpUtXTkO3M5W9eBAO',17,3,NULL,1,'2025-03-25 19:29:26'),(52,'ybravo','$2b$12$VlcafJHHVMlo0lc8JNqbUeTczewU3DyVoXz/HfA8T1xsm9uweLRFu',42,3,NULL,1,'2025-03-25 19:30:07'),(53,'ycastillo','$2b$12$U1FMJq4eXXiaziXbkFpcMucCMtwc62K4.ZykPQuDOx8rxFAonNylm',7,3,NULL,1,'2025-03-25 19:30:43'),(55,'pepito','$2b$12$fLFhYQEuCH01xrWWbWA9bOhnG1dVaFu6.3MVYt3pBSPXXYoAiOlHu',103,3,'2025-04-08 13:38:07',1,'2025-03-31 15:50:26'),(56,'sgarcia','$2b$12$FZCv3yorRJ47BycGXgZoseVlZopnYrwoRN6mESwh4vJ/thdBUGJO2',41,3,'2025-04-01 12:10:28',1,'2025-03-31 22:22:31'),(58,'lalvis','$2b$12$LIc5S3N9uErWKD/SDZEhV.vGxCZ.DzG357jMAbLWC5Zq4PibGaV9W',112,3,NULL,1,'2025-04-04 19:42:50');
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
  `descripcion` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `activo` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zonas_economicas`
--

LOCK TABLES `zonas_economicas` WRITE;
/*!40000 ALTER TABLE `zonas_economicas` DISABLE KEYS */;
INSERT INTO `zonas_economicas` VALUES (1,'PLANTA LA MARIA','2025-03-20 12:08:58',NULL,1),(2,'BODEGA BARRANQUILLA','2025-03-20 12:08:58',NULL,1),(3,'PLANTA AGUAZUL','2025-03-20 12:08:58',NULL,1),(4,'BODEGA BOGOTA','2025-03-20 12:08:58',NULL,1),(5,'BODEGA CALI','2025-03-20 12:08:58',NULL,1),(6,'BODEGA GIRON','2025-03-20 12:08:58',NULL,1),(7,'BODEGA MEDELLIN','2025-03-20 12:08:58',NULL,1),(8,'BODEGA PEREIRA','2025-03-20 12:08:58',NULL,1);
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

-- Dump completed on 2025-04-08 14:45:17
