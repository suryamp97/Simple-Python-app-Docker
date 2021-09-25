CREATE DATABASE htest;
use htest;

CREATE TABLE History (
  id bigint auto_increment PRIMARY KEY,
  keyw VARCHAR(50)
);

INSERT INTO History
  (id, keyw)
VALUES
  (0, 'ubi');