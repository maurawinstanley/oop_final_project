import sqlite3
from sqlite3 import Error
from clarifai.rest import ClarifaiApp, Image as ClImage
import requests
import platform
import io
import sys
import hashlib
import pickle


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


class Object_Classifier():
    def __init__(self):
        self.app = ClarifaiApp(api_key='7d9991430a9d4fe4943315cf2651149a') #api key to clarifai app 
        self.model = self.app.public_models.general_model

    def classifyImage(self, imageURL):
        # call the clarify image recognition API 
        # return json response of items identified and confidence levels 
        self.model.model_version = 'aa7f35c01e0642fda5cf400f543e7c40'
        image = ClImage(url=imageURL)
        response = self.model.predict([image])

        return response

def main():
    db_conn = Db_Connection()
    singleton_db = db_conn.get_instance()
    print(singleton_db)
    
    #clarifai_app = Clarifai_App()

    object_classifier = Object_Classifier()
    response = object_classifier.classifyImage('https://sc01.alicdn.com/kf/HTB1FM3eLXXXXXadXXXXq6xXFXXXC/teddy-bear-stuff-toys.jpg_350x350.jpg')
    print(response)
if __name__ == '__main__':
    main()


















