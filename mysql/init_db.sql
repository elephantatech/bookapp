-- init_db.sql
CREATE DATABASE IF NOT EXISTS db_name;
USE db_name;

CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);
