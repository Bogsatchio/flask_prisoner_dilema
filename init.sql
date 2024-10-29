USE simulation_dev;

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


    CREATE TABLE experimentrecord (
            experimentId VARCHAR(100) NOT NULL,
            cooperationPoints INT NOT NULL,
            oneSideBetrayalPoints INT NOT NULL,
            twoSideBetrayalPoints INT NOT NULL,
            waves INT NOT NULL,
            matches INT NOT NULL,
            rounds INT NOT NULL,
            numEliminatedPerWave INT NOT NULL,
            winnersPremium DECIMAL(10, 2) NOT NULL,
            description VARCHAR(255) NOT NULL,
            PRIMARY KEY (experimentId)
            );

    CREATE TABLE waveresult (
            experimentId VARCHAR(100) NOT NULL,
            waveId INT NOT NULL,
            playerId INT NOT NULL,
            spot INT NOT NULL,
            totalScore INT NOT NULL,
            wasEliminated BOOLEAN NOT NULL
            );


    CREATE TABLE matchrecord (
        experimentId VARCHAR(100) NOT NULL,
        waveId INT NOT NULL,
        gameId INT NOT NULL,
        matchId INT NOT NULL,
        leftPlayerId INT NOT NULL,
        rightPlayerId INT NOT NULL,
        leftPlayerFinalScore INT NOT NULL,
        rightPlayerFinalScore INT NOT NULL,
        winnerId INT NOT NULL,
        PRIMARY KEY (gameId, matchId)
    );

    CREATE TABLE roundrecord (
            gameId INT NOT NULL,
            matchId INT NOT NULL,
            roundId INT NOT NULL,
            leftPlayerResponse BOOLEAN NOT NULL,
            rightPlayerResponse BOOLEAN NOT NULL,
            outcome VARCHAR(255) NOT NULL,
            leftPlayerCurrentPoints INT NOT NULL,
            rightPlayerCurrentPoints INT NOT NULL,
            PRIMARY KEY (gameId, matchId, roundId)
        );