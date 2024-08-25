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
	index INTEGER PRIMARY_KEY,
	Date_m DATE
);





-- Create Asian table
CREATE TABLE Asian
(
	
	Date_m DATE PRIMARY KEY,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER,
	Maternal_Mortality_Rate NUMERIC
);



-- Create Black table
CREATE TABLE Black
(
	Date_m DATE,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC
	PRIMARY KEY(Date_m) REFERENCES Hispanic(Date_m)
);



-- Create Hispanic table
CREATE TABLE Hispanic
(
	Date_m DATE PRIMARY KEY,
	Maternal_Deaths INTEGER, 
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC
);N



-- Create Native Indian table
CREATE TABLE Native_Indian
(
	Date_m DATE PRIMARY KEY,
	Maternal_Deaths INTEGER,
	Live_Births INTEGER, 
	Maternal_Mortality_Rate NUMERIC,
	PRIMARY KEY(Date_m) REFERENCES Black
);




