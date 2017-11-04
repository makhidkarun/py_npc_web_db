import bottle
import pymongo

#from bottle import Bottle, debug,  post, route, run 

# Using "app = Bottle() is supposed to be a best practice.
# Not getting it yet.
#app = Bottle()

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

bottle.run(host='localhost', port = 8082, reloader = True, debug = True)
