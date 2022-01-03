CREATE TABLE Professors(
  name    VARCHAR(30),
  SSN     CHAR(9),
  PRIMARY KEY(SSN)
);

CREATE TABLE Team(
  TeamID  INTEGER,
  PRIMARY KEY(TeamID)
);

CREATE TABLE Students(
  name    VARCHAR(30),
  SSN     CHAR(9),
  PRIMARY KEY(SSN)
);

CREATE TABLE GTAs(
  name    VARCHAR(30),
  SSN     CHAR(9),
  salary  FLOAT,
  PRIMARY KEY(SSN),
  FOREIGN KEY (SSN) REFERENCES Students(SSN)
);

CREATE TABLE Class(
  Department      VARCHAR(25),
  CourseNumber    INTEGER,
  PRIMARY KEY(Department, CourseNumber)
);

CREATE TABLE Section(
  SectionID       CHAR(1),
  Department      VARCHAR(25) NOT NULL,
  CourseNumber    INTEGER NOT NULL,
  PRIMARY KEY(SectionID, Department, CourseNumber),
  FOREIGN KEY (Department, CourseNumber) REFERENCES Class(Department, CourseNumber)
);

CREATE TABLE CanTeach(
  SSN             CHAR(9),
  Department      VARCHAR(25),
  CourseNumber    INTEGER,
  PRIMARY KEY(SSN, Department, CourseNumber),
  FOREIGN KEY (SSN) REFERENCES Professors(SSN),
  FOREIGN KEY (Department, CourseNumber) REFERENCES Class(Department, CourseNumber)
);

CREATE TABLE On_Team1(
  SSN     CHAR(9),
  TeamID  INTEGER,
  PRIMARY KEY(SSN, TeamID),
  FOREIGN KEY (SSN) REFERENCES Professors(SSN),
  FOREIGN KEY (TeamID) REFERENCES Team(TeamID)
);

CREATE TABLE Admin(
  Rating  INTEGER,
  TeamID  INTEGER,
  SectionID CHAR(1),
  Department VARCHAR(25) NOT NULL,
  CourseNumber INTEGER NOT NULL,
  PRIMARY KEY(TeamID, SectionID, Department, CourseNumber),
  FOREIGN KEY (TeamID) REFERENCES Team(TeamID),
  FOREIGN KEY (SectionID, Department, CourseNumber) REFERENCES Section(SectionID, Department, CourseNumber)
);

CREATE TABLE On_Team2(
  TeamID  INTEGER,
  SSN     CHAR(9),
  PRIMARY KEY(TeamID, SSN),
  FOREIGN KEY (TeamID) REFERENCES Team(TeamID),
  FOREIGN KEY (SSN) REFERENCES GTAs(SSN)
);

CREATE TABLE Wait_For(
  Waitlist_Rank   INTEGER,
  SectionID       CHAR(1),
  Department      VARCHAR(25) NOT NULL,
  CourseNumber    INTEGER NOT NULL,
  SSN             CHAR(9),
  PRIMARY KEY(SectionID, Department, CourseNumber, SSN),
  FOREIGN KEY (SectionID, Department, CourseNumber) REFERENCES Section(SectionID, Department, CourseNumber),
  FOREIGN KEY (SSN) REFERENCES Students(SSN)
);

CREATE TABLE Take(
  Grade           VARCHAR(6),
  SectionID       CHAR(1),
  Department      VARCHAR(25) NOT NULL,
  CourseNumber    INTEGER NOT NULL,
  SSN             CHAR(9),
  FOREIGN KEY (SectionID, Department, CourseNumber) REFERENCES Section(SectionID, Department, CourseNumber),
  FOREIGN KEY (SSN) REFERENCES Students(SSN)
);

CREATE Table Req_Of(
  PR_Department           VARCHAR(25),
  PR_CourseNumber         INTEGER,
  R_Department            VARCHAR(25),
  R_CourseNumber          INTEGER,
  PRIMARY KEY(PR_Department, PR_CourseNumber, R_Department, R_CourseNumber),
  FOREIGN KEY (PR_Department, PR_CourseNumber) REFERENCES Class(Department, CourseNumber),
  FOREIGN KEY (R_Department, R_CourseNumber) REFERENCES Class(Department, CourseNumber)
);
