"""
Author: Sanjiv Upadhyaya
Date: 2016-11-15
Function: connect to the BI server and prepare tables for the pentaho cubes.
"""

from sqlalchemy import create_engine
from threading import Thread, Lock
from config import config
import transformer as trans
import pandas as pd
import threading
import psycopg2
import os


class Loader(Thread):
    __lock = Lock()

    def __init__(self,cube_name):
        Thread.__init__(self)
        self.cube_name = cube_name

    def run(self):

        try:

            conn_string = config.conn_bi
            conn = psycopg2.connect(conn_string)
            curs = conn.cursor()
            curs.execute(open(config.sql_file_path+self.cube_name+".sql", "r").read())
            conn.commit()
            conn.close()
            curs.close

            print(self.cube_name+" Cube Prepared")

        except Exception as e:
            print("Unable to access database, import error %s %s" % (str(e), self.cube_name))

