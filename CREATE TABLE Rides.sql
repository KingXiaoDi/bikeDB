USE biking;
CREATE TABLE Rides (
    RideID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    RideDate date NOT NULL,
    LocationStart nvarchar(30) NOT NULL,
    LocationEnd nvarchar(30) NOT NULL,
    Distance decimal(8,4) NOT NULL,
    TimeStart time,
    TimeEnd time);