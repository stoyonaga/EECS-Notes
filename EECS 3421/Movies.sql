create table Movies(
    title char(100),
    year int,
    length int,
    genre char(10),
    studioName char(30),
    producerID int,
    primary key (title, year)
);

create table moviestar(
    name char(30) primary key,
    address varchar(255),
    gender char(1) default '?',
    birthdate date default null
);


