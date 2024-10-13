CREATE TABLE abouts(
    id INTEGER PRIMARY KEY,
    avatar VARCHAR NOT NULL,
    name VARCHAR NOT NULL,
    description VARCHAR NULL,
    birthday DATETIME NOT NULL,
    website VARCHAR NULL,
    phone VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    age INTEGER NOT NULL,
    degree VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    freelance VARCHAR NULL,
    address ADDRESS NOT NULL,
);

CREATE TABLE socials(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    style VARCHAR NULL,
);

CREATE TABLE services(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    url VARCHAR NOT NULL,
    style VARCHAR NULL,
);

CREATE TABLE skills(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    procent INTEGER(100) not NULL,
);

CREATE TABLE resumes(
    id INTEGER PRIMARY KEY,
    resume_fayl VARCHAR NOT NULL,
    content TEXT NOT NULL,
);

CREATE TABLE categories(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
);

CREATE TABLE projects(
    id INTEGER PRIMARY KEY,
    img IMAGE NOT NULL,
    name VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    date DATETIME NOT NULL,
    url VARCHAR NOT NULL,
);

CREATE TABLE contacts(
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR NOT NULL,
    subject VARCHAR NOT NULL,
    message TEXT NOT NULL,
);