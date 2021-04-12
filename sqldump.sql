CREATE TABLE IF NOT EXISTS Airline(
    AirlineName VARCHAR(64),
    CostStructure CHAR(64),
    Reputation INT,
    PRIMARY KEY (AirlineName)
);






CREATE TABLE IF NOT EXISTS Flight (
FlightNumber VARCHAR(7) NOT NULL,
DepartureTime INTEGER NOT NULL,
Price INTEGER NOT NULL,
ArrivalTime INTEGER NOT NULL,
LoadFactor INTEGER NOT NULL,
AirlineName VARCHAR(100),
FOREIGN KEY (AirlineName) REFERENCES Airline(AirlineName),
AirplaneModelType VARCHAR(100) NOT NULL,
FOREIGN KEY (AirplaneModelType) REFERENCES Airplane(ModelName0),
CodeDeparture CHAR(4),
CodeArrival CHAR(4),
FOREIGN KEY (CodeDeparture) REFERENCES Routes(CodeDeparture),
FOREIGN KEY (CodeArrival) REFERENCES Routes(CodeArrival),
PRIMARY KEY (FlightNumber, DepartureTime),
CONSTRAINT CHKTime CHECK (ArrivalTime > DepartureTime));


