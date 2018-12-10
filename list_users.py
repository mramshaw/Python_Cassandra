#!/usr/bin/python

from cassandra.cluster import Cluster

RECORDS_TO_LIST = 10

cluster = Cluster()
session = cluster.connect('k8s_test')

user_list_stmt = session.prepare("SELECT * FROM users LIMIT ?")

users = session.execute(user_list_stmt, [RECORDS_TO_LIST])
for u in users:
    print u

session.shutdown()
cluster.shutdown()
