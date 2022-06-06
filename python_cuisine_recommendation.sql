-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 01, 2022 at 03:47 PM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `python_cuisine_recommendation`
--

-- --------------------------------------------------------

--
-- Table structure for table `booking_details`
--

CREATE TABLE `booking_details` (
  `id` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `food` varchar(100) NOT NULL,
  `vote` varchar(100) NOT NULL,
  `rating` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `quantity` varchar(100) NOT NULL,
  `total` varchar(100) NOT NULL,
  `customer_name` varchar(100) NOT NULL,
  `customer_address` varchar(100) NOT NULL,
  `customer_contact` varchar(100) NOT NULL,
  `card_no` varchar(100) NOT NULL,
  `holder_name` varchar(100) NOT NULL,
  `cdate` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `booking_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `review_details`
--

CREATE TABLE `review_details` (
  `id` int(100) NOT NULL,
  `uname` varchar(100) NOT NULL,
  `review` varchar(100) NOT NULL,
  `today` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `review_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `search_details`
--

CREATE TABLE `search_details` (
  `name` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  `CUSINE_CATEGORY` varchar(100) NOT NULL,
  `TIMING` varchar(100) NOT NULL,
  `RATING_TYPE` varchar(100) NOT NULL,
  `RATING` varchar(100) NOT NULL,
  `VOTES` varchar(100) NOT NULL,
  `comfort_food` varchar(100) NOT NULL,
  `comfort_food_reasons` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `search_details`
--


-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

CREATE TABLE `user_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `age` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `report` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

