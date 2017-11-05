# Many code ideas, and pretty much all the best ones, come from
# the MongoDB University M101P on-line class. Highly recommended!
# https://university.mongodb.com/courses/M101P/about


import bottle
import pymongo
import sys

# Not sure on this.
#from bottle import Bottle, debug,  post, route, run 

# Using "app = Bottle() is supposed to be a best practice.
# Not getting it yet.
# app = Bottle()

# When does the connection close? Should closure be explicit?
connection = pymongo.MongoClient('localhost', 27017)
db = connection.dragons
db_name = db.dragons


@bottle.route('/dragon')
def index():
  return bottle.template('find_dragon.tpl')

@bottle.post('/select_dragon')
def select_dragon():
  dragon = bottle.request.forms.get('dragon_name')
  dragon_name = str(dragon)
  person = db_name.find_one({'name' : dragon_name})
  if (person == None or person == ""):
    return "No Dragon found."
  else:
    # First string in parens is template. 
    # First string in curly braces is route.
    return bottle.template('dragon_selection', {"dragon":person})

@bottle.post('/update_dragon')
def update_dragon():
  dragon = bottle.request.forms.get('search_name')
  search_name = str(dragon)
  person      = db_name.find_one({'name': search_name})
  if ( person == None or person == ""):
    return "No Dragon found."
  else:
    return bottle.template("update_dragon", {'dragon':person})

@bottle.post('/upsert_dragon')
def upsert_dragon():
  dragon        = bottle.request.forms.get('search_name')
  search_name   = str(dragon)
  person        = db_name.find_one({'name': search_name})
  if ( person == None or person == ""):
    return "No Dragon found."
  else:
    name        = bottle.request.forms.get('dragon_name')
    upp         = bottle.request.forms.get('dragon_upp')
    try:
      result = db_name.update_one({'name': search_name},
                {'$set': {'name':name, 'upp':upp}})
      person        = db_name.find_one({'name': search_name})
    except:
      print("Error on update.")
      print(sys.exec_info()[0])

  return bottle.template('dragon_selection', {"dragon":person})

## Run stuff

bottle.run(host='localhost', port = 8082, reloader = True, debug = True)
