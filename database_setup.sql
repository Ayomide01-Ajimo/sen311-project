CREATE DATABASE IF NOT EXISTS user_management;
USE user_management;

CREATE TABLE IF NOT EXISTS tbl_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);