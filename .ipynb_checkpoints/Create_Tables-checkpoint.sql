-- Drop tables if they exist from prior tries
DROP TABLE if EXISTS Asian;
DROP TABLE if EXISTS Black;
DROP TABLE if EXISTS Hispanic;
DROP TABLE if EXISTS Native_Indian;
DROP TABLE if EXISTS Pacific_Islander;
DROP TABLE if EXISTS White;
DROP TABLE if EXISTS Dates;


-- Dates table
CREATE TABLE Dates
(
	Date_index INTEGER PRIMARY KEY,
	Date_m DATE
);


-- Create Asian table
CREATE TABLE Asian
(
	
	Asian_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER,
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
);



-- Create Black table
CREATE TABLE Black
(
	Black_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
);



-- Create Hispanic table
CREATE TABLE Hispanic
(
	Hispanic_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
);






-- Create Native Indian table
CREATE TABLE Native_Indian
(
	Native_Indian_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER,
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
);


-- Create Pacific Islander table
CREATE TABLE Pacific_Islander
(
	Pacific_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER,
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
	
);


--Create White table
CREATE TABLE White
(
	White_index INTEGER PRIMARY KEY,
	Date_index INTEGER,
	Maternal_Deaths INTEGER,
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	FOREIGN KEY(Date_index) REFERENCES Dates(Date_index)
	
);

