create database if not exists Marathon;
use Marathon;

create table if not exists Laufer
(
LauferID int auto_increment unique key primary key,
Herkunft varchar(64),
Email varchar(64),
Nachname varchar(64),
Vorname varchar(64),
Geburtsdatum date
);

create table if not exists Marathonlauf
(
MarathonID int auto_increment unique key primary key,
Preisgeld int,
Kilometer int,
Datum date,
Preis_für_Teilnahme int,
Besucher varchar(64)
);

create table if not exists Organisator
(
OrganisationID int auto_increment unique key primary key,
Anschrift varchar(64),
Name varchar(64),
Sponsoren varchar(64),
Telefonnummer int
);

create table if not exists Marathon_Laufer
(
Marathon_LauferID int auto_increment unique key primary key,
LauferID int,
MarathonID int,
constraint LauferID foreign key (LauferID) references Laufer (LauferID),
constraint MarathonID foreign key (MarathonID) references Marathonlauf (MarathonID)
);

create table if not exists Marathon_Organisator
(
Marathon_OrganisatorID int auto_increment unique key primary key,
OrganisationID int,
Marathon2ID int,
constraint OrganisationID foreign key (OrganisationID) references Organisator (OrganisationID),
constraint Marathon2ID foreign key (Marathon2ID) references Marathonlauf (MarathonID)
);