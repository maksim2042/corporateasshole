corporateasshole
================

CorporateAsshole.org

Logging in:
=============
ssh -i credentials/corp_ahole.pem ubuntu@dev.corporateasshole.org

Make sure to set permissions for credentials/corp_ahole.pem at 400:

>> chmod 400 credentials/corp_ahole.pem

(for Linux/Mac. Windows people -- get a real computer!)

Using MongoDB:
===============

Create an SSH Tunnel :

ssh -i credentials/corp_ahole.pem -L 27018:localhost:27017 ubuntu@dev.corporateasshole.org

Make sure you have a MongoDB client installed -- command line mongo or MongoHub

> mongo localhost:27018

Connecting from Python:

import pymongo
mongo_uri='mongodb://localhost:27018/corp_ahole'
db=pymongo.MongoClient(mongo_uri).corp_ahole

THAT'S IT -- you are now connected. 

*KEEP THE SSH SESSION OPEN -- IT KEEPS THE PORTS OPEN THROUGH THE FIREWALL*


