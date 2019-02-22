import redis
from flask import Flask

app = Flask(__name__)
db=redis.Redis(host='localhost',port='6379',db=0)
@app.route('/')
def hello_world():
    name=db.get('name') or'World'
    return 'Hello %s!' % name

@app.route('/setname/<name>')
def setname(name):
    db.set('name',name)
    return 'Name updated.'
if __name__ == '__main__':
    app.run(debug=True)