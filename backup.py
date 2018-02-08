#!/usr/bin/python
import requests
import json
import os

user = os.environ['BKUP_USER']
password = os.environ['BKUP_PASS']
host = os.environ['BKUP_HOST']


dbs = requests.get('http://%s:%s@%s/api/search'%(user,password,host)).json()

for db in dbs:
    if 'backup' in db['tags']:
        print 'backing up ' + db['title']
        db_json = requests.get('http://%s:%s@%s/api/dashboards/%s'%(user,
                                                                password,
                                                                host,
                                                                db['uri'])
                                                                ).json()

        out_file = open('dashboards/' + db['title'] + '.json', 'w')
        out_file.write(json.dumps(db_json, indent=4, sort_keys=True))
        out_file.close()
