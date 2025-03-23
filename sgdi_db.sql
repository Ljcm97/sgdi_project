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
INSERT INTO `alembic_version` VALUES ('8ccb4da870da');
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (1,'ARCHIVO','2025-03-20 12:08:58'),(2,'ASISTENTE ADMINISTRATIVO','2025-03-20 12:08:58'),(3,'AUDITORIA','2025-03-20 12:08:58'),(4,'CARTERA','2025-03-20 12:08:58'),(5,'COMPRAS PADDY','2025-03-20 12:08:58'),(6,'COMPRAS Y ALMACEN','2025-03-20 12:08:58'),(7,'CONTABILIDAD','2025-03-20 12:08:58'),(8,'CONTRALORIA','2025-03-20 12:08:58'),(9,'COSTOS','2025-03-20 12:08:58'),(10,'FACTURACION','2025-03-20 12:08:58'),(11,'FLETES','2025-03-20 12:08:58'),(12,'GERENTE ADMINISTRATIVO Y FINANCIERO','2025-03-20 12:08:58'),(13,'GERENTE GENERAL','2025-03-20 12:08:58'),(14,'GERENTE OPERATIVO','2025-03-20 12:08:58'),(15,'LOGISTICA','2025-03-20 12:08:58'),(16,'PRODUCCION','2025-03-20 12:08:58'),(17,'RECEPCION','2025-03-20 12:08:58'),(18,'RRHH','2025-03-20 12:08:58'),(19,'SISTEMAS','2025-03-20 12:08:58'),(20,'SST','2025-03-20 12:08:58'),(21,'SUPERNUMERARIO','2025-03-20 12:08:58'),(22,'TESORERIA','2025-03-20 12:08:58'),(23,'VENTAS','2025-03-20 12:08:58'),(88,'CALIDAD','2025-03-21 19:29:00');
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
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=235 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cargos`
--

LOCK TABLES `cargos` WRITE;
/*!40000 ALTER TABLE `cargos` DISABLE KEYS */;
INSERT INTO `cargos` VALUES (1,'ALMACENISTA','2025-03-20 12:08:58'),(2,'ANALISTA DE PROCESOS SAP','2025-03-21 12:16:42'),(3,'ANALISTA DE SISTEMAS','2025-03-21 12:16:42'),(4,'APRENDIZ SENA','2025-03-21 12:16:42'),(5,'ASISTENTE ADMINISTRATIVO','2025-03-21 12:16:42'),(6,'ASISTENTE DE CARTERA','2025-03-21 12:16:42'),(7,'ASISTENTE DE CONTABILIDAD','2025-03-21 12:16:42'),(8,'ASISTENTE DE CONTABILIDAD II','2025-03-21 12:16:42'),(9,'ASISTENTE DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42'),(10,'ASISTENTE DE COSTOS','2025-03-21 12:16:42'),(11,'ASISTENTE DE RECURSOS HUMANOS','2025-03-21 12:16:42'),(12,'ASISTENTE DE TESORERIA','2025-03-21 12:16:42'),(13,'AUXILIAR ADMINISTRATIVO','2025-03-21 12:16:42'),(14,'AUXILIAR CAFETERIA','2025-03-21 12:16:42'),(15,'AUXILIAR DE ALMACEN','2025-03-21 12:16:42'),(16,'AUXILIAR DE AUDITORIA','2025-03-21 12:16:42'),(17,'AUXILIAR DE CARTERA','2025-03-21 12:16:42'),(18,'AUXILIAR DE COMPRAS MATERIA PRIMA','2025-03-21 12:16:42'),(19,'AUXILIAR DE CONTABILIDAD','2025-03-21 12:16:42'),(20,'AUXILIAR DE TESORERIA','2025-03-21 12:16:42'),(21,'AUXILIAR DE VENTAS','2025-03-21 12:16:42'),(22,'AUXILIAR LOGISTICO','2025-03-21 12:16:42'),(24,'COMPRADOR MATERIA PRIMA TOLIMA CENTRO','2025-03-21 12:16:42'),(25,'COMPRADOR MATERIA PRIMA TOLIMA SUR','2025-03-21 12:16:42'),(26,'CONDUCTOR','2025-03-21 12:16:42'),(27,'COORDINADOR CONTROL DE CALIDAD','2025-03-21 12:16:42'),(28,'COORDINADOR DE ARCHIVO','2025-03-21 12:16:42'),(29,'COORDINADOR DE DESPACHOS','2025-03-21 12:16:42'),(30,'COORDINADOR DE VENTAS','2025-03-21 12:16:42'),(31,'COORDINADOR FLOTA PROPIA','2025-03-21 12:16:42'),(32,'COORDINADOR LOGISTICO','2025-03-21 12:16:42'),(33,'CONTRALOR','2025-03-21 12:16:42'),(34,'FACTURADOR','2025-03-21 12:16:42'),(35,'GERENTE ADMINISTRATIVO Y FINANCIERO','2025-03-21 12:16:42'),(36,'GERENTE GENERAL','2025-03-21 12:16:42'),(37,'GERENTE OPERATIVO PLANTA LA MARIA','2025-03-21 12:16:42'),(38,'JEFE DE AUDITORIA','2025-03-21 12:16:42'),(39,'JEFE DE CARTERA','2025-03-21 12:16:42'),(40,'JEFE DE COMPRAS Y ALMACEN','2025-03-21 12:16:42'),(41,'JEFE DE CONTABILIDAD','2025-03-21 12:16:42'),(42,'JEFE DE COSTOS','2025-03-21 12:16:42'),(43,'JEFE DE PLANTA U OBRA LA MARIA','2025-03-21 12:16:42'),(44,'JEFE DE RECURSOS HUMANOS','2025-03-21 12:16:42'),(45,'JEFE DE SEGURIDAD Y SALUD EN EL TRABAJO','2025-03-21 12:16:42'),(46,'JEFE GESTION DE CALIDAD','2025-03-21 12:16:42'),(47,'MENSAJERO','2025-03-21 12:16:42'),(48,'RECEPCIONISTA','2025-03-21 12:16:42'),(49,'SUPERNUMERARIO','2025-03-21 12:16:42'),(50,'SUPERNUMERARIO SST','2025-03-21 12:16:42'),(51,'SUPERVISOR DE VIGILANCIA','2025-03-21 12:16:42'),(52,'TESORERO','2025-03-21 12:16:42'),(53,'VENDEDOR','2025-03-21 12:16:42'),(54,'VIGILANTE','2025-03-21 12:16:42'),(232,'AUXILIAR SST','2025-03-21 12:16:42');
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (2,'20250322-8332','2025-03-22 10:14:00',3,'0123456789','Lina',5,'Se entregan 20 tiquetes de aguazul N° ....... etc','Sin novedades ',3,28,5,'ENTRADA',2,'2025-03-22 15:16:58'),(3,'20250322-2381','2025-03-22 12:39:00',4,'741258','Albertano',1,'Factura de celsia','Sin novedades ',17,4,7,'ENTRADA',2,'2025-03-22 17:58:36'),(4,'20250322-8960','2025-03-22 13:00:00',6,'159753','Planta aguazul',4,'Informes de Planta aguazul','Sin novedad',17,4,7,'ENTRADA',2,'2025-03-22 18:14:54');
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
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimientos`
--

LOCK TABLES `movimientos` WRITE;
/*!40000 ALTER TABLE `movimientos` DISABLE KEYS */;
INSERT INTO `movimientos` VALUES (4,2,'2025-03-22 10:14:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-22 15:16:58'),(5,2,'2025-03-22 15:36:57',9,7,21,7,21,2,'Documento aceptado para procesamiento','2025-03-22 15:36:57'),(6,2,'2025-03-22 15:38:27',9,7,21,3,28,1,'Se pasa al área de auditoria los fletes para ser auditados ','2025-03-22 15:38:27'),(7,2,'2025-03-22 15:43:12',8,3,28,3,28,2,'Documento aceptado para procesamiento','2025-03-22 15:43:12'),(8,2,'2025-03-22 15:43:16',8,3,28,3,28,4,'Documento finalizado','2025-03-22 15:43:16'),(9,2,'2025-03-22 15:43:36',8,3,28,3,28,5,'Documento archivado','2025-03-22 15:43:36'),(10,3,'2025-03-22 12:39:00',2,17,4,3,28,1,'Documento registrado en recepción','2025-03-22 17:58:36'),(11,4,'2025-03-22 13:00:00',2,17,4,7,21,1,'Documento registrado en recepción','2025-03-22 18:14:54'),(12,4,'2025-03-22 18:15:36',9,7,21,17,4,7,'Documento rechazado por Maria Paula Lozano Lozano','2025-03-22 18:15:36'),(13,3,'2025-03-22 20:29:46',8,3,28,17,4,7,'Documento rechazado por Nataly Tatiana Puentes Sierra','2025-03-22 20:29:46');
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
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notificaciones`
--

LOCK TABLES `notificaciones` WRITE;
/*!40000 ALTER TABLE `notificaciones` DISABLE KEYS */;
INSERT INTO `notificaciones` VALUES (4,9,'Nuevo documento asignado - 20250322-8332','Se te ha asignado un nuevo documento de tipo Tiquetes.',2,1,'2025-03-22 15:16:58'),(5,2,'Documento aceptado - 20250322-8332','El documento ha sido aceptado por Maria Paula Lozano Lozano.',2,0,'2025-03-22 15:36:57'),(6,8,'Documento transferido - 20250322-8332','Se te ha transferido un documento de tipo Tiquetes.',2,1,'2025-03-22 15:38:27'),(7,2,'Documento aceptado - 20250322-8332','El documento ha sido aceptado por Nataly Tatiana Puentes Sierra.',2,0,'2025-03-22 15:43:12'),(8,8,'Nuevo documento asignado - 20250322-2381','Se te ha asignado un nuevo documento de tipo Facturas.',3,1,'2025-03-22 17:58:36'),(9,9,'Nuevo documento asignado - 20250322-8960','Se te ha asignado un nuevo documento de tipo Correspondencia.',4,1,'2025-03-22 18:14:54'),(10,2,'Documento rechazado - 20250322-8960','El documento ha sido rechazado por Maria Paula Lozano Lozano.',4,0,'2025-03-22 18:15:36'),(11,2,'Documento rechazado - 20250322-2381','El documento ha sido rechazado por Nataly Tatiana Puentes Sierra.',3,0,'2025-03-22 20:29:46');
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
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personas`
--

LOCK TABLES `personas` WRITE;
/*!40000 ALTER TABLE `personas` DISABLE KEYS */;
INSERT INTO `personas` VALUES (1,'Ricardo Alexander Bohórquez Méndez','rbohorquez@arrozsonora.com.co','3112815201',1,1,19,3,1,'2025-03-20 12:08:58'),(2,'Jairo Antonio Lozano Vargas','sst@arrozsonora.com.co','3102118013',1,2,20,45,1,'2025-03-20 12:08:58'),(3,'Olga Patricia Ortiz Rivas','oortiz@arrozsonora.com.co','',1,3,6,40,1,'2025-03-20 12:08:58'),(4,'Yazmina Lorena Fayad Gutierrez','recepcion@arrozsonora.com.co','3104567890',1,1,17,48,1,'2025-03-20 12:08:58'),(5,'Jairo Sedan Murra','jsedan@arrozsonora.com.co','',1,1,13,36,1,'2025-03-21 09:11:56'),(6,'Julio Cesar Cepeda Rodríguez','jcepeda@arrozsonora.com.co','',1,1,14,37,1,'2025-03-21 09:11:56'),(7,'Yuly Slendy Castillo Robayo','ycastillo@arrozsonora.com.co','',1,1,12,35,1,'2025-03-21 09:11:56'),(8,'Myriam Rodríguez Arciniegas','mrodriguez@arrozsonora.com.co','',1,1,8,33,1,'2025-03-21 09:11:56'),(9,'Brayan Santick Quintero Cordoba','bquintero@arrozsonora.com.co','',1,1,2,5,1,'2025-03-21 09:11:56'),(10,'Viviana Caycedo Bocanegra','vcaycedo@arrozsonora.com.co','',1,1,21,49,1,'2025-03-21 09:11:56'),(11,'Martha Yaneth Diaz Trigueros','mdiaz@arrozsonora.com.co','',1,1,22,52,1,'2025-03-21 09:11:56'),(12,'Sandra Bibiana Laverde Parra','slaverde@arrozsonora.com.co','',1,1,22,20,1,'2025-03-21 09:11:56'),(13,'Juan David Lozano Guzman','jlozano@arrozsonora.com.co','',1,1,22,12,1,'2025-03-21 09:11:56'),(14,'Diana Marcela Bocanegra Tovar','dbocanegra@arrozsonora.com.co','',1,1,22,12,1,'2025-03-21 09:11:56'),(15,'Teresa Tovar Rivera','ttovar@arrozsonora.com.co','',1,1,5,9,1,'2025-03-21 09:11:56'),(16,'Angy Yulitza Vargas Padilla','avargas@arrozsonora.com.co','',1,1,5,18,1,'2025-03-21 09:11:56'),(17,'Ximena Paola Bocanegra Ortiz','xbocanegra@arrozsonora.com.co','',1,1,7,41,1,'2025-03-21 09:11:56'),(18,'Joan Jair Rodriguez Portela','jrodriguez@arrozsonora.com.co','',1,1,7,7,1,'2025-03-21 09:11:56'),(19,'Adriana Lucia Gonzalez Serrano','agonzalez@arrozsonora.com.co','',1,1,7,7,1,'2025-03-21 09:11:56'),(20,'Lizeth Daniela Melo Olis','lmelo@arrozsonora.com.co',NULL,1,1,7,8,1,'2025-03-21 09:11:56'),(21,'Maria Paula Lozano Lozano','mlozano@arrozsonora.com.co','',1,1,7,19,1,'2025-03-21 09:11:56'),(22,'Silvia Patricia Rivera Zabala','srivera@arrozsonora.com.co','',1,1,7,19,1,'2025-03-21 09:11:56'),(23,'Andres Felipe Arias Vargas','aarias@arrozsonora.com.co','',1,1,3,16,1,'2025-03-21 09:11:56'),(24,'Laura Maria Rodriguez Cuervo','lrodriguez@arrozsonora.com.co','',1,1,11,19,1,'2025-03-21 09:11:56'),(25,'Andrea Del Pilar Morales Trujillo','amorales@arrozsonora.com.co',NULL,1,1,7,7,1,'2025-03-21 09:11:56'),(26,'Karen Nureidys Carcamo Londono','kcarcamo@arrozsonora.com.co','',1,1,9,42,1,'2025-03-21 09:11:56'),(27,'Julian Andres Molina Avila','jmolina@arrozsonora.com.co','',1,1,9,10,1,'2025-03-21 09:11:56'),(28,'Nataly Tatiana Puentes Sierra','npuentes@arrozsonora.com.co','',1,1,3,38,1,'2025-03-21 09:11:56'),(29,'Adriana del Pilar Lopez Bustos','alopez@arrozsonora.com.co','',1,1,3,16,1,'2025-03-21 09:11:56'),(30,'Lina Fernanda Fierro Fierro','lfierro@arrozsonora.com.co','',1,1,3,16,1,'2025-03-21 09:11:56'),(31,'Leidy Johana Avila Gonzalez','lavila@arrozsonora.com.co','',1,1,4,39,1,'2025-03-21 09:11:56'),(32,'Julieth Paola Gonzalez Onatra','jgonzalez@arrozsonora.com.co','',1,1,4,6,1,'2025-03-21 09:11:56'),(33,'Jonathan Fabian Manrique Rodriguez','jmanrique@arrozsonora.com.co','',1,1,4,6,1,'2025-03-21 09:11:56'),(34,'Angie Katherine Zamora Cordoba','azamora@arrozsonora.com.co','',1,1,4,6,1,'2025-03-21 09:11:56'),(35,'Luana Simona Sendoya Echeverry','lsendoya@arrozsonora.com.co','',1,1,23,30,1,'2025-03-21 09:11:56'),(36,'Angi Xiomara Ramirez Ortiz','aramirez@arrozsonora.com.co','',1,1,23,21,1,'2025-03-21 09:11:56'),(37,'Juan Jose Cote Hernandez','jcote@arrozsonora.com.co','',1,1,15,32,1,'2025-03-21 09:11:56'),(38,'Angela Maria Zartha Leal','azartha@arrozsonora.com.co','',1,1,15,22,1,'2025-03-21 09:11:56'),(39,'Juan Pablo Celis Castillo','jcelis@arrozsonora.com.co','',1,1,15,31,1,'2025-03-21 09:11:56'),(40,'Ana Maria Rodriguez Mora','arodriguez@arrozsonora.com.co','',1,1,18,44,1,'2025-03-21 09:11:56'),(41,'Sandra Milena Garcia Gonzalez','sgarcia@arrozsonora.com.co','',1,1,18,11,1,'2025-03-21 09:11:56'),(42,'Yendy Fannory Bravo Gutierrez','ybravo@arrozsonora.com.co','',1,2,10,34,1,'2025-03-21 09:11:56'),(43,'Kelly Johanna Gomez Lozano','kgomez@arrozsonora.com.co','',1,2,20,232,1,'2025-03-21 09:11:56'),(44,'Sandra Milena Villa Rojas','smvilla@arrozsonora.com.co','',1,2,88,1,1,'2025-03-21 09:11:56'),(45,'Diana Alejandra Ortiz Jara','dortiz@arrozsonora.com.co','',1,2,88,27,1,'2025-03-21 09:11:56'),(46,'James Eduardo Rueda Trujillo','jrueda@arrozsonora.com.co','',1,2,16,43,1,'2025-03-21 09:11:56'),(47,'Luis Alberto Barreto Guzman','lbarreto@arrozsonora.com.co','',1,3,6,1,1,'2025-03-21 09:11:56'),(48,'Luis Alejandro Oliveros','','',1,3,6,15,1,'2025-03-21 09:11:56'),(49,'Jaime Vargas Ramirez','jvargas@arrozsonora.com.co','',1,3,1,28,1,'2025-03-21 09:11:58'),(95,'Lina Julieth Carvajal Mendoza','','',1,1,19,4,1,'2025-03-21 20:01:07');
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=162 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles_permisos`
--

LOCK TABLES `roles_permisos` WRITE;
/*!40000 ALTER TABLE `roles_permisos` DISABLE KEYS */;
INSERT INTO `roles_permisos` VALUES (1,1,1,'2025-03-20 12:08:58'),(2,1,2,'2025-03-20 12:08:58'),(3,1,3,'2025-03-20 12:08:58'),(4,1,4,'2025-03-20 12:08:58'),(5,1,5,'2025-03-20 12:08:58'),(6,1,6,'2025-03-20 12:08:58'),(7,1,7,'2025-03-20 12:08:58'),(8,1,8,'2025-03-20 12:08:58'),(9,1,9,'2025-03-20 12:08:58'),(10,1,10,'2025-03-20 12:08:58'),(11,1,11,'2025-03-20 12:08:58'),(12,1,12,'2025-03-20 12:08:58'),(13,1,13,'2025-03-20 12:08:58'),(14,1,14,'2025-03-20 12:08:58'),(15,1,15,'2025-03-20 12:08:58'),(16,1,16,'2025-03-20 12:08:58'),(17,1,17,'2025-03-20 12:08:58'),(18,1,18,'2025-03-20 12:08:58'),(19,1,19,'2025-03-20 12:08:58'),(20,1,20,'2025-03-20 12:08:58'),(21,1,21,'2025-03-20 12:08:58'),(128,2,20,'2025-03-22 20:27:53'),(129,2,9,'2025-03-22 20:27:53'),(130,2,3,'2025-03-22 20:27:53'),(131,2,8,'2025-03-22 20:27:53'),(132,2,2,'2025-03-22 20:27:53'),(133,2,5,'2025-03-22 20:27:53'),(134,2,1,'2025-03-22 20:27:53'),(156,3,2,'2025-03-23 02:26:49'),(157,3,5,'2025-03-23 02:26:49'),(158,3,7,'2025-03-23 02:26:49'),(159,3,6,'2025-03-23 02:26:49'),(160,3,8,'2025-03-23 02:26:49'),(161,3,20,'2025-03-23 02:26:49');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_documento`
--

LOCK TABLES `tipos_documento` WRITE;
/*!40000 ALTER TABLE `tipos_documento` DISABLE KEYS */;
INSERT INTO `tipos_documento` VALUES (1,'Facturas','2025-03-20 12:08:58'),(2,'Comprobantes','2025-03-20 12:08:58'),(3,'Contratos','2025-03-20 12:08:58'),(4,'Correspondencia','2025-03-20 12:08:58'),(5,'Tiquetes','2025-03-20 12:08:58'),(6,'Cotizaciones','2025-03-20 12:08:58'),(7,'Órdenes de compra','2025-03-20 12:08:58'),(8,'Hojas de vida','2025-03-20 12:08:58'),(9,'Manuales','2025-03-20 12:08:58'),(10,'Informes','2025-03-20 12:08:58'),(11,'Fletes','2025-03-20 12:08:58');
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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transportadoras`
--

LOCK TABLES `transportadoras` WRITE;
/*!40000 ALTER TABLE `transportadoras` DISABLE KEYS */;
INSERT INTO `transportadoras` VALUES (1,'DEPRISA','2025-03-20 12:08:58'),(2,'SERVIENTREGA','2025-03-20 12:08:58'),(3,'ENVIA','2025-03-20 12:08:58'),(4,'COORDINADORA','2025-03-20 12:08:58'),(5,'SAFERBO','2025-03-20 12:08:58'),(6,'INTERRAPIDISIMO','2025-03-20 12:08:58'),(7,'AXPRESS','2025-03-20 12:08:58'),(8,'REDETRANS','2025-03-20 12:08:58'),(9,'TCC','2025-03-20 12:08:58'),(10,'4-72','2025-03-20 12:08:58'),(11,'TRANSPRENSA','2025-03-20 12:08:58'),(12,'PORTERIA','2025-03-20 12:08:58'),(13,'CERTIPOSTAL','2025-03-20 12:08:58'),(14,'ENCO EXPRES','2025-03-20 12:08:58'),(15,'X-CARGO','2025-03-20 12:08:58'),(16,'DHL EXPRESS','2025-03-20 12:08:58'),(17,'OPEN MARKET','2025-03-20 12:08:58'),(18,'EXPRESO BOLIVARIANO','2025-03-20 12:08:58'),(19,'MERCADOLIBRE','2025-03-20 12:08:58'),(20,'INTERSERVICE','2025-03-20 12:08:58');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'rbohorquez','$2b$12$h8H9COaJrgpqyE9sQewA7.bMWNcJk1eIJcOKInxqTrcOtuWmji77i',1,1,'2025-03-23 02:23:19',1,'2025-03-20 21:18:20'),(2,'yfayad','$2b$12$.Vsma9zYL6ivAOrfzNbN2uO8tw7.21nUBONXcUzOyHWPOrR82AdUq',4,2,'2025-03-22 17:39:29',1,'2025-03-21 12:39:04'),(8,'npuentes','$2b$12$2Q44xvcj0xIBIL4R6nty2uMMOLTFFU4d3UiW1F.ZaGi9a9WcH.syK',28,3,'2025-03-22 20:29:35',1,'2025-03-22 05:06:01'),(9,'mlozano','$2b$12$ZDiZDmGcldxaGx1FIM13cOV2qk7DVCdgnD4.1ZKBRMd7QaP201ege',21,3,'2025-03-22 18:15:19',1,'2025-03-22 05:06:52'),(10,'lcarvajal','$2b$12$nlV/o7UKblD7DYbux5PBr.SQGbFC2sqmiLrbmEvVxa7oirshtdP6u',95,1,NULL,1,'2025-03-22 19:10:49');
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
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

-- Dump completed on 2025-03-22 21:45:11
