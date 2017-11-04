import bottle
import pymongo

connection = pymongo.MongoClient('localhost', 27017)
db = connection.dragons
db_name = db.dragons


@bottle.route('/dragon')
def index():
  return bottle.template('find_dragon.tpl')

@bottle.post('/find_dragon')
def find_dragon():
  dragon = bottle.request.forms.get('dragon_name')
  dragon_name = str(dragon)
  person = db_name.find_one({'name' : dragon_name})
  if (person == None or person == ""):
    return "No Dragon found."
  else:
    # First string in parens is template. 
    # First string in curly braces is route.
    return bottle.template('dragon_selection', {"dragon":person})

bottle.debug(True)
bottle.run(host='localhost', port = 8082)
