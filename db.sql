CREATE TABLE IF NOT EXISTS data (
t_id VARCHAR(32) NULL,
ttype VARCHAR(8) NULL,
category VARCHAR(7) NULL,
title VARCHAR(27) NULL,
priority VARCHAR(7) NULL,
status VARCHAR(4) NULL,
requestuser VARCHAR(6) NULL,
processmanager VARCHAR(12) NULL
);

INSERT INTO data VALUES
("c3c290048da041d687a156fcc8c3a547","Problem","Server","Cannot access email","Medium","Open","Puru","System Admin"),
("793f596d06764115ba5c7aed689391b0","Change","Network","Open port 22 on server X123","Highest","Open","Puru","System Admin"),
("05e640f95e714cea84f9b12c3b0a53fb","Incident","Other","title..","Normal","Open","chetan","System Admin");