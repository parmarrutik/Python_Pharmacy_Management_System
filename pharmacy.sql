-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 08, 2025 at 09:07 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pharmacy`
--

-- --------------------------------------------------------

--
-- Table structure for table `meddep`
--

CREATE TABLE `meddep` (
  `ref1` int(10) NOT NULL,
  `med1` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `meddep`
--

INSERT INTO `meddep` (`ref1`, `med1`) VALUES
(1, 'jay'),
(2, 'paracitamol'),
(3, 'pera'),
(4, 'Montecip-lc'),
(5, 'abcd');

-- --------------------------------------------------------

--
-- Table structure for table `medinfo`
--

CREATE TABLE `medinfo` (
  `ref` int(20) NOT NULL,
  `cmp` varchar(50) NOT NULL,
  `tmed` varchar(50) NOT NULL,
  `medname` varchar(50) NOT NULL,
  `lot` int(20) NOT NULL,
  `issue` int(50) NOT NULL,
  `exp` int(50) NOT NULL,
  `uses` varchar(100) NOT NULL,
  `side` varchar(100) NOT NULL,
  `prec` varchar(100) NOT NULL,
  `dos` varchar(100) NOT NULL,
  `tprice` int(20) NOT NULL,
  `proq` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `medinfo`
--

INSERT INTO `medinfo` (`ref`, `cmp`, `tmed`, `medname`, `lot`, `issue`, `exp`, `uses`, `side`, `prec`, `dos`, `tprice`, `proq`) VALUES
(1, 'rutik Company', 'Capsules', 'jay', 200, 12, 12, 'cough', 'enough', 'yes', '4', 450, 10),
(2, 'calmic ltd', 'Tablet', 'paracitamol', 123, 12, 12, 'headeche', 'no', 'no', '1 tab everyday after meal', 20, 1),
(3, 'shyam Company', 'Inhales', 'Doxing', 12, 12, 12, 'relief ', 'no', 'yes', 'depend on  your mood', 35, 1),
(123, 'cipla', 'Tablet', 'xy', 152, 25, 25, 'headache', 'no', 'no', '1 daily', 20, 10);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `meddep`
--
ALTER TABLE `meddep`
  ADD PRIMARY KEY (`ref1`);

--
-- Indexes for table `medinfo`
--
ALTER TABLE `medinfo`
  ADD PRIMARY KEY (`ref`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
