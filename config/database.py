from pymongo import MongoClient
import ssl
from core import config


client = MongoClient("mongodb+srv://"+config.settings.user_name+":"+config.settings.pass_word+"@"+config.settings.host+"/myFirstDatabase?retryWrites=true&w=majority")


db = client.students

collection_name = db["todos_app"]
students_collection = db["students"]
courses_collection = db["courses"]
