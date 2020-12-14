-- phpMyAdmin SQL Dump
-- version 4.6.6deb5ubuntu0.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Dec 14, 2020 at 05:53 PM
-- Server version: 5.7.32-0ubuntu0.18.04.1
-- PHP Version: 7.2.24-0ubuntu0.18.04.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projet_breizhibus`
--
CREATE DATABASE IF NOT EXISTS `projet_breizhibus` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `projet_breizhibus`;

-- --------------------------------------------------------

--
-- Table structure for table `bus`
--

DROP TABLE IF EXISTS `bus`;
CREATE TABLE IF NOT EXISTS `bus` (
  `id_bus` int(11) NOT NULL AUTO_INCREMENT,
  `numero` varchar(4) NOT NULL,
  `registration` varchar(7) NOT NULL,
  `num_place` int(11) NOT NULL,
  `id_line` int(11) NOT NULL,
  PRIMARY KEY (`id_bus`),
  KEY `id_line` (`id_line`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `registration`, `num_place`, `id_line`) VALUES
(1, 'BB01', 'CA123DO', 20, 1),
(2, 'BB02', 'NO123EL', 30, 2),
(3, 'BB03', 'JE123UX', 20, 3),
(4, 'BB04', 'RE123PA', 30, 1),
(6, 'BB06', 'FE123TE', 30, 4),
(8, 'BB05', 'FG634DA', 42, 4);

-- --------------------------------------------------------

--
-- Table structure for table `bus_lines`
--

DROP TABLE IF EXISTS `bus_lines`;
CREATE TABLE IF NOT EXISTS `bus_lines` (
  `id_line` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id_line`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `bus_lines`
--

INSERT INTO `bus_lines` (`id_line`, `name`) VALUES
(1, 'Rouge'),
(2, 'Vert'),
(3, 'Bleu'),
(4, 'Noir');

-- --------------------------------------------------------

--
-- Table structure for table `stops`
--

DROP TABLE IF EXISTS `stops`;
CREATE TABLE IF NOT EXISTS `stops` (
  `id_stop` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `adress` varchar(50) NOT NULL,
  PRIMARY KEY (`id_stop`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stops`
--

INSERT INTO `stops` (`id_stop`, `name`, `adress`) VALUES
(1, 'Korrigan', '1 impasse du Korrigan'),
(2, 'Morgana', '2 plage Morgana'),
(3, 'L\'Ankou', '3 place du L\'Ankou'),
(4, 'Ys', '4 rue de l\'ile d\'Ys'),
(5, 'Viviane', '5 avenue de Viviane'),
(6, 'Guénolé', '6 rue Saint Guénolé');

-- --------------------------------------------------------

--
-- Table structure for table `stops_lines`
--

DROP TABLE IF EXISTS `stops_lines`;
CREATE TABLE IF NOT EXISTS `stops_lines` (
  `id_line` int(11) NOT NULL,
  `id_stop` int(11) NOT NULL,
  KEY `id_line` (`id_line`),
  KEY `id_stop` (`id_stop`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stops_lines`
--

INSERT INTO `stops_lines` (`id_line`, `id_stop`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2),
(2, 4),
(2, 6),
(3, 4),
(3, 5),
(3, 6),
(3, 1),
(4, 1),
(4, 3),
(4, 5);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_line`) REFERENCES `bus_lines` (`id_line`);

--
-- Constraints for table `stops_lines`
--
ALTER TABLE `stops_lines`
  ADD CONSTRAINT `stops_lines_ibfk_1` FOREIGN KEY (`id_line`) REFERENCES `bus_lines` (`id_line`),
  ADD CONSTRAINT `stops_lines_ibfk_2` FOREIGN KEY (`id_stop`) REFERENCES `stops` (`id_stop`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
