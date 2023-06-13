CREATE TABLE Missions (
  mission_id INT IDENTITY(1,1) PRIMARY KEY,
  start_date DATE,
  spaceman_id INT,
  mission_name VARCHAR(255),
  approximate_cost DECIMAL(10, 2),
);

CREATE TABLE ProfessionalSpacemans (
  spaceman_id INT IDENTITY(1,1) PRIMARY KEY,
  mission_id INT,
  status VARCHAR(20),
  name VARCHAR(255),
  surname VARCHAR(255),
  FOREIGN KEY (mission_id) REFERENCES Missions(mission_id)
);


CREATE TABLE NewbieSpacemans (
  spaceman_id INT IDENTITY(1,1) PRIMARY KEY,
  start_date DATE,
  end_date DATE,
  overall_training_cost DECIMAL(10, 2),
  name VARCHAR(255),
  surname VARCHAR(255)
);

ALTER TABLE Missions
ADD FOREIGN KEY (spaceman_id) REFERENCES ProfessionalSpacemans(spaceman_id)

ALTER TABLE ProfessionalSpacemans
ADD MissionName NVARCHAR(100);

ALTER TABLE Missions
ADD CrewNumber INT;

CREATE TRIGGER UpdateSpacemanStatus
ON Missions
AFTER INSERT, UPDATE
AS
BEGIN
    UPDATE ProfessionalSpacemans
    SET status = 'space'
    WHERE spaceman_id IN (SELECT spaceman_id FROM inserted)
    AND mission_id IS NOT NULL
    AND GETDATE() > (SELECT start_date FROM inserted WHERE Missions.spaceman_id = inserted.spaceman_id)
END;