from gevent import monkey
monkey.patch_all()
 
from flask import Flask
app = Flask(__name__)
 
@app.route('/v2/index')
def hello_world():
    return 'Hello World INdex!'
 
if __name__ == '__main__':
    app.run()
