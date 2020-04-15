import sqlite3
from sqlite3 import Error
from clarifai.rest import ClarifaiApp, Image as ClImage
import requests
import platform
import io
import sys
import hashlib
import pickle

from client import Client


#create a singleton factory pattern db connection to connect ot sqlite db 
class Db_Connection():
    """ create a database connection to a SQLite database """
    __conn_instance = None

    @staticmethod
    def get_instance():
        if Db_Connection.__conn_instance == None:
             Db_Connection()
        return Db_Connection.__conn_instance

    def __init__(self):
        try:
            conn = sqlite3.connect(r"C:\sqlite\db\pythonsqlite.db") #connect to db 
            print(sqlite3.version)
            Db_Connection.__conn_instance = conn
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
 
class Clarifai_App():
    def __init__(self):
        self.app = ClarifaiApp(api_key='7d9991430a9d4fe4943315cf2651149a') #api key to clarifai app 
        print("app: ", self.app)
























