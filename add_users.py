#!/usr/bin/python

from cassandra.cluster import Cluster

import logging

RECORDS_TO_ADD = 10

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

cluster = Cluster()
session = cluster.connect('k8s_test')

user_insert_stmt = session.prepare("INSERT INTO users (username, password) VALUES (?, ?)")

for i in range(RECORDS_TO_ADD):
    s = str(i)
    user = "user_" + s
    password = "password_" + s
    session.execute(user_insert_stmt, [user, password])
    log.info("Created user: " + user)

log.info(str(RECORDS_TO_ADD) + " users added")

session.shutdown()
cluster.shutdown()
