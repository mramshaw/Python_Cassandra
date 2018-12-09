#!/usr/bin/python

from cassandra.cluster import Cluster

RECORDS_TO_ADD = 10

cluster = Cluster()
session = cluster.connect('k8s_test')

user_insert_stmt = session.prepare("INSERT INTO users (username, password) VALUES (?, ?)")

for i in range(RECORDS_TO_ADD):
    s = str(i)
    session.execute(user_insert_stmt, ["user_" + s, "password_" + s])

print RECORDS_TO_ADD, "users added"
