CREATE KEYSPACE IF NOT EXISTS k8s_test WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 2};

USE "k8s_test";

CREATE TABLE IF NOT EXISTS users (
    username text PRIMARY KEY,
    password text
);

INSERT INTO users(username, password) VALUES ('Jesse', 'secret');
INSERT INTO users(username, password) VALUES ('Frank', 'password');

SELECT * from users;

// This is how to empty a table in CQL
TRUNCATE users;
