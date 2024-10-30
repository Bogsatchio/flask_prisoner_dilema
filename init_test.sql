CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE players (
        experimentId VARCHAR(100) NOT NULL,
        playerId INT NOT NULL,
        name VARCHAR(50) NOT NULL,
        waveJoined INT NOT NULL,
        strategyType VARCHAR(50) NOT NULL,
        strategyTemper VARCHAR(50) NOT NULL,
        description VARCHAR(255) NOT NULL,
        PRIMARY KEY (experimentId, playerId)
        );