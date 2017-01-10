"""
Author: Sanjiv Upadhyaya
Date: 2016-10-03
Function: main program to populate facts and dimensions.
"""

from loader import Loader
from config import config
import transformer as trans
import psycopg2.extras
import threading
import psycopg2
import datetime
import time
import sys
import os

print("Current process date -> "+ config.end_date)

for cube_name, query in trans.transformer.iteritems():
	print('Preparing data for ' + cube_name)
	runner = Loader(cube_name)
	runner.start()


















