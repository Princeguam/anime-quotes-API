from mongoengine import *
from os import getenv
from dotenv import load_dotenv



load_dotenv()

# CONNECT TO THE MONGODB ATLAS USING THE URI

connect('quoteDB',getenv('DB_URI'))

# remember to create a .env file and add it to your .gitignore



class Entry(Document):
    character_name = StringField(required=True)
    character_id = IntField()
    anime_name = StringField(required=True)
    quote = StringField(required=True)

    #here is where the index for the text search was established
    meta = {'indexes':[
        {'fields':['$quote','$anime_name','$character_name'],
         'default_language':'english',
         'weights':{'quote': 3}
        }
        ]}


    def to_db (self):
        return{
            "character name": self.character_name,
            "character id": self.character_id,
            "anime name": self.anime_name,
            "quote":self.quote
        }
class User(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    date_joined = DateTimeField()


    def from_user_to_db(self):
        return{
            "First name":self.first_name,
            "Last name":self.last_name,
            "email":self.email,
            "date":self.date_joined
        }