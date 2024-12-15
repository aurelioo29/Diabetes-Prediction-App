-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Waktu pembuatan: 15 Des 2024 pada 02.23
-- Versi server: 8.0.30
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `diabetes_prediction`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `diabetes_data`
--

CREATE TABLE `diabetes_data` (
  `id` int NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `no_hp` varchar(50) DEFAULT NULL,
  `pregnancies` int DEFAULT NULL,
  `glucose` int DEFAULT NULL,
  `bloodpressure` int DEFAULT NULL,
  `skinthickness` int DEFAULT NULL,
  `insulin` int DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `diabetespedigree` float DEFAULT NULL,
  `age` int DEFAULT NULL,
  `prediction_result` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data untuk tabel `diabetes_data`
--

INSERT INTO `diabetes_data` (`id`, `name`, `no_hp`, `pregnancies`, `glucose`, `bloodpressure`, `skinthickness`, `insulin`, `bmi`, `diabetespedigree`, `age`, `prediction_result`) VALUES
(1, 'Active', '123445780', 10, 166, 74, 123, 10, 25.8, 0.201, 30, 'DIABETES'),
(2, 'tester', '1234567890', 10, 116, 72, 30, 175, 123, 100, 20, 'DIABETES'),
(3, 'tester', '134567890', 2, 148, 72, 35, 175, 200, 300, 30, 'DIABETES'),
(4, 'Cayla', '082178902345', 2, 200, 70, 30, 200, 33.6, 0.351, 31, 'DIABETES'),
(5, 'Active', '082145672390', 1, 85, 66, 29, 0, 26.6, 0.351, 31, 'TIDAK DIABETES'),
(6, 'tester', '089067462459', 2, 116, 72, 30, 10, 33.6, 0.627, 51, 'TIDAK DIABETES'),
(7, 'Cayla', '082134567890', 2, 130, 60, 35, 175, 33.6, 0.201, 40, 'TIDAK DIABETES');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `diabetes_data`
--
ALTER TABLE `diabetes_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `diabetes_data`
--
ALTER TABLE `diabetes_data`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
