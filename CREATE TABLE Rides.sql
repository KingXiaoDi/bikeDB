CREATE TABLE Rides (
    RideID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RideDate date NOT NULL,
    StartPoint nvarchar(30) NOT NULL,
    EndPoint nvarchar(30) NOT NULL,
    Distance decimal(8,4) NOT NULL,
    StartTime time,
    EndTime time);