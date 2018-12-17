#!/usr/bin/python

from cassandra.cluster import Cluster

import logging

RECORDS_TO_LIST = 10

log = logging.getLogger()
log.setLevel('INFO')
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s"))
log.addHandler(handler)

cluster = Cluster()
session = cluster.connect('k8s_test')

user_list_stmt = session.prepare("SELECT * FROM users LIMIT ?")

listed_count = 0
users = session.execute(user_list_stmt, [RECORDS_TO_LIST])
for u in users:
    print u
    listed_count += 1

log.info(str(listed_count) + " users listed")

session.shutdown()
cluster.shutdown()
