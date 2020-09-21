-- --------------------------------------------------------
-- 호스트:                          127.0.0.1
-- 서버 버전:                        8.0.21 - MySQL Community Server - GPL
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- attend 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `attend` DEFAULT CHARACTER SET utf8 /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `attend`;

-- 테이블 attend.attendance 구조 내보내기
CREATE TABLE IF NOT EXISTS `attendance` (
  `index` int NOT NULL AUTO_INCREMENT,
  `personal_id` int NOT NULL,
  `room_id` int NOT NULL,
  `enter_time` timestamp NOT NULL,
  `exit_time` timestamp NOT NULL,
  PRIMARY KEY (`index`),
  KEY `personal_id` (`personal_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`personal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 attend.attendance:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` (`index`, `personal_id`, `room_id`, `enter_time`, `exit_time`) VALUES
	(1, 1, 4, '2020-09-17 12:52:05', '2020-09-17 20:52:10'),
	(2, 1, 4, '2020-09-17 07:52:46', '2020-09-17 11:52:53'),
	(3, 2, 4, '2020-09-17 20:53:14', '2020-09-17 22:53:15'),
	(4, 3, 3, '2020-09-17 10:53:56', '2020-09-17 20:54:01');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;

-- 테이블 attend.device 구조 내보내기
CREATE TABLE IF NOT EXISTS `device` (
  `device_id` int NOT NULL AUTO_INCREMENT,
  `personal_id` int NOT NULL,
  `mac_addr` varchar(255) NOT NULL,
  `device_index` int NOT NULL,
  PRIMARY KEY (`device_id`),
  UNIQUE KEY `mac_addr` (`mac_addr`),
  KEY `personal_id` (`personal_id`),
  CONSTRAINT `device_ibfk_1` FOREIGN KEY (`personal_id`) REFERENCES `personal` (`personal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 attend.device:~7 rows (대략적) 내보내기
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` (`device_id`, `personal_id`, `mac_addr`, `device_index`) VALUES
	(1, 1, 'aa:bb:cc:dd:ee:ff', 1),
	(2, 1, 'bb:cc:dd:ee:aa', 2),
	(3, 3, 'df:df:ee:fe:sa:aa', 1),
	(4, 2, 'ad:df:3f:32:ff:sd', 1),
	(5, 6, '0c:7a:15:d4:a7:1f', 1),
	(7, 6, '0c:93:f5:d4:a7:11', 2),
	(8, 4, '07:de:fa:23:ff:1a', 1),
	(9, 10, '12:23:45:df:ab:aa', 1);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;

-- 테이블 attend.log 구조 내보내기
CREATE TABLE IF NOT EXISTS `log` (
  `index` int NOT NULL AUTO_INCREMENT,
  `is_processed` tinyint(1) NOT NULL,
  `node_id` int NOT NULL,
  `device_id` int NOT NULL,
  `RSSI` tinyint NOT NULL,
  `time` timestamp NOT NULL,
  PRIMARY KEY (`index`),
  KEY `node_id` (`node_id`),
  KEY `device_id` (`device_id`),
  CONSTRAINT `log_ibfk_1` FOREIGN KEY (`node_id`) REFERENCES `node` (`node_id`),
  CONSTRAINT `log_ibfk_2` FOREIGN KEY (`device_id`) REFERENCES `device` (`device_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 attend.log:~11 rows (대략적) 내보내기
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` (`index`, `is_processed`, `node_id`, `device_id`, `RSSI`, `time`) VALUES
	(1, 1, 4, 1, -45, '2020-09-17 21:00:32'),
	(2, 1, 3, 1, -68, '2020-09-17 21:00:32'),
	(3, 1, 2, 1, -45, '2020-09-17 21:00:32'),
	(4, 1, 4, 3, -45, '2020-09-17 21:00:32'),
	(5, 1, 1, 1, -55, '2020-09-17 21:00:32'),
	(6, 1, 4, 2, -45, '2020-09-17 21:00:32'),
	(7, 1, 4, 4, -45, '2020-09-17 21:00:32'),
	(8, 1, 4, 1, -45, '2020-09-17 21:00:32'),
	(9, 1, 1, 2, -68, '2020-09-17 21:00:32'),
	(10, 1, 4, 1, -45, '2020-09-17 21:00:32'),
	(11, 1, 4, 2, -80, '2020-09-17 21:00:32');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;

-- 테이블 attend.node 구조 내보내기
CREATE TABLE IF NOT EXISTS `node` (
  `node_id` int NOT NULL,
  `mac_addr` varchar(255) NOT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`node_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 attend.node:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `node` DISABLE KEYS */;
INSERT INTO `node` (`node_id`, `mac_addr`, `room_id`) VALUES
	(1, '23:34:ff:ss:ab:ff', 1),
	(2, '12:df:sd:sf:ff:sd', 2),
	(3, 'df:ee:fj:dd:aa:34', 3),
	(4, 'ad:df:zz:ff:3f:bc', 4);
/*!40000 ALTER TABLE `node` ENABLE KEYS */;

-- 테이블 attend.personal 구조 내보내기
CREATE TABLE IF NOT EXISTS `personal` (
  `personal_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `id` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`personal_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 테이블 데이터 attend.personal:~7 rows (대략적) 내보내기
/*!40000 ALTER TABLE `personal` DISABLE KEYS */;
INSERT INTO `personal` (`personal_id`, `name`, `id`, `password`) VALUES
	(1, '정종민', 'alertjjm', 'abc1234'),
	(2, '서예진', 'yejinneer', 'aaa'),
	(3, '이경하', 'nulleekh', 'bbb'),
	(4, '진영훈', 'hunihuni', 'cc'),
	(5, '정주용', 'juyong', 'ccdd'),
	(6, '이경문', 'gilgil', '4623f30b926198d4284b8b9b502f1717fc4161a977960219738de203bb699a96'),
	(9, '최병준', 'goka', 'a0fb63625e06bfa24f01c67ce0a980fe17ad6be930041b1e6345c54a481c682c'),
	(10, '최원영', 'hellobob', 'df27e2da83cf40ef0f4b086af0d12515ef75293e365f4aab8e9ba0d05e650455');
/*!40000 ALTER TABLE `personal` ENABLE KEYS */;

-- 테이블 attend.spring_session 구조 내보내기
CREATE TABLE IF NOT EXISTS `spring_session` (
  `PRIMARY_ID` char(36) NOT NULL,
  `SESSION_ID` char(36) NOT NULL,
  `CREATION_TIME` bigint NOT NULL,
  `LAST_ACCESS_TIME` bigint NOT NULL,
  `MAX_INACTIVE_INTERVAL` int NOT NULL,
  `EXPIRY_TIME` bigint NOT NULL,
  `PRINCIPAL_NAME` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`PRIMARY_ID`),
  UNIQUE KEY `SPRING_SESSION_IX1` (`SESSION_ID`),
  KEY `SPRING_SESSION_IX2` (`EXPIRY_TIME`),
  KEY `SPRING_SESSION_IX3` (`PRINCIPAL_NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- 테이블 데이터 attend.spring_session:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `spring_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `spring_session` ENABLE KEYS */;

-- 테이블 attend.spring_session_attributes 구조 내보내기
CREATE TABLE IF NOT EXISTS `spring_session_attributes` (
  `SESSION_PRIMARY_ID` char(36) NOT NULL,
  `ATTRIBUTE_NAME` varchar(200) NOT NULL,
  `ATTRIBUTE_BYTES` blob NOT NULL,
  PRIMARY KEY (`SESSION_PRIMARY_ID`,`ATTRIBUTE_NAME`),
  CONSTRAINT `SPRING_SESSION_ATTRIBUTES_FK` FOREIGN KEY (`SESSION_PRIMARY_ID`) REFERENCES `spring_session` (`PRIMARY_ID`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci ROW_FORMAT=DYNAMIC;

-- 테이블 데이터 attend.spring_session_attributes:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `spring_session_attributes` DISABLE KEYS */;
/*!40000 ALTER TABLE `spring_session_attributes` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
