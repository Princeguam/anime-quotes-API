#imports and dependencies
from flask import Flask, request, redirect, render_template
from db import *
import random



#configuration
app = Flask(__name__)


#To get the total number of documents in the db
entry =Entry.objects().all()
db_total = len(entry)


# routes
@app.route('/')
def home():
    entry = Entry.objects().all()
    return f"total number of quotes in the databse is {len(entry)}"



# when i come back to this, the changes i'll make are:
# 1. to search anime by anime name and anime by id
# 2. TO search quote by everything searchable ie [keyword, character, anime, id]
# 3. to search character name by first letter or keyword.
# 








#GET QUOTE BY ANIME NAME
@app.route('/api/v1/anime', methods=['GET'])
def anime():
    if request.method == 'GET':
        name = request.args.get('name')
        items = Entry.objects(anime_name__icontains=name) 
        if len(items) > 0:
            # return render_template('index.html', items=items) #this commented part is for if i want to link it to my html page. 
            output = [{
                "Anime":item.anime_name,
                "Character":item.character_name,
                "Object_id": str(item.id),
                "Quote":item.quote,
                "ID":item.character_id }for item in items]
            return output
        else:
            return f" No anime with the name {name}"





#GET ANIME NAME BY ID
@app.route('/api/v1/anime/ID/<int:number>', methods=['GET'])
def get_anime_by_ID(number):
    items = Entry.objects(character_id = number)
    if len(items) > 0:
        output = [{"Anime":item.anime_name,
        "Character":item.character_name,
        "object_id": str(item.id),
        "Quote":item.quote,
        "ID":item.character_id }for item in items]
        return output
    else:
        return f'No anime with the ID {number}'




#GET QUOTE FROM A STARTING POINT UP TO A POINT (SPECIFIED BY THE USER) REMEMBER TO CHANGE THE ROUTE TO /quote
@app.route('/api/v1/quote/lookup/<int:number>', methods=['GET'])
def get_by_first(number):
    items = Entry.objects[1+number:].limit(20) #with limit(20), limits the amount of data that is returned.
    output = [{
    "Anime":item.anime_name,
    "Character":item.character_name,
    "Quote":item.quote,
    "ID":item.character_id, 
    "object_id":str(item.id)}for item in items]
    return output




#ENDPOINT TO GET QUOTE BASED ON ID    
@app.route('/api/v1/quotes/ID',methods=['GET'])
def get_quote_by_id():
    id = request.args.get('id')
    if request.method == 'GET':
        # return F"this is the post with the integer value {integer}"
       this_query = Entry.objects(character_id=id)
       for i in this_query:
           return({
               "Character":i.character_name,
               "Anime":i.anime_name,
               "ID": i.character_id,
               "Quotes":i.quote
           })
       


#GET RANDOM QUOTE 
@app.route('/api/v1/quotes/random',methods=['GET'])
def get_random_quote():
    random_num = random.randint(0,db_total) #generates a random number from 0 to the total number of documents in the db
    this_query = Entry.objects(character_id=random_num)
    if len(this_query) > 0:
        for item in this_query:
            output = [{
                "Anime":item.anime_name,
                "Character":item.character_name,
                "ID":item.character_id,
                "Quote":item.quote,
                "object_id":str(item.id)

            }]
            return output
    else:
        return f"Error couldnt generate quote. try again!", 500
        


#GET QUOTE BASED ON CHARACTER NAME
@app.route('/api/v1/quotes/character',methods=['GET'])
def get_quote_by_char_name():
    name = request.args.get('name')
    # return F"this is the post with the integer value {integer}"
    this_query = Entry.objects(character_name__icontains=name).all()
    if len(this_query) > 0:
        output = [{
            "Character":i.character_name,
            "Anime":i.anime_name,
            "ID": i.character_id,
            "Quotes":i.quote,
            "object_id":str(i.id)
        } for i in this_query]
        return output
    else:
        return f'Could not find any character with the name "{name}". You can submit your own quote so others can see it!'





#GET KEYWORD BASED ON KEYWORD SEARCH
@app.route('/api/v1/quotes/KW',methods=['GET'])
def get_quote_by_KW():
    text = request.args.get('text')
    # return F"this is the post with the integer value {integer}"
    this_query = Entry.objects.search_text(text).order_by('$text_score').limit(20)
    if len(this_query) > 0:
        output = [{
            "Character":i.character_name,
            "Anime":i.anime_name,
            "ID": i.character_id,
            "Quotes":i.quote,
            "object_id":str(i.id)
        } for i in this_query]
        return output
    else:
        return f'Could not find any Quote with the word "{text}". You can submit your own quote so others can see it!'















#ENDPOINT TO ADD OR DELETE FROM THE DB
@app.route('/submit', methods=['PUT','DELETE','POST'])
def submit_quote():
    the_character = request.form['character_name']
    the_anime = request.form['anime_name']
    the_quote = request.form['quote']

    the_entry = Entry.objects(quote=the_quote).first()
    if request.method == 'PUT':    
        if the_entry:
            return f'the Quote: {the_quote} by {the_character} already exist, try a different quote.'
        else:
            #here after validating that the quote doesnt exist, a new instance is created and stored to the db
            add_entry = Entry(
            character_name = the_character,
            anime_name = the_anime,
            quote = the_quote)
            
            add_entry.save()

            return f'the quote has been added succesfully!', 200
    
        # #THIS IS THE POST METHOD. NOT FOUND WHERE TO PUT THIS YET!
    if request.method == 'POST':
        
        the_character =  request.form['character_name']
        the_anime = request.form['anime_name']
        the_quote = request.form['quote']

        new_entry = Entry(
            character_name = the_character,
            anime_name = the_anime,
            quote = the_quote
            )
        new_entry.save()
        return('Succesfully added to the database' ), 201
    

        
        
    if request.method == 'DELETE':
        # DELETE THE DATA ENTERED IN THE QUERY 
        return 'deleted'























# #for reading the JSON file.
# with open('quotes.json',mode='rb+')as the_file:
#     quotes = json.load(the_file)



# #for populating the database with json file
# for item in quotes:
#     user = Entry(
#         character_name=item["Character"],
#         character_id=item["id"],
#         anime_name=item["Anime"],
#         quote=item["Quote"]
#         )
#     user.save()

