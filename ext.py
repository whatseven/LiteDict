import os

BASEDIR=os.getcwd()

REMOTEDBPATH = os.path.join(BASEDIR,"../ScienceAmericanSpider/db.db3")
LOCALDBPATH = os.path.join(BASEDIR,"resources/localDb")
INDEXDBPATH = os.path.join(BASEDIR,"resources/indexDb")

WORDRECORD = os.path.join(BASEDIR,"resources/recordDB.db")
EXPORTPATH = os.path.join(BASEDIR,"export/")

HOST = 'http://111.231.116.139:7005'
