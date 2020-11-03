from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    list_of_users = ["ben", "luke", "bob", "matt", "jay", "bill"]
    return render_template('index.html', users=list_of_users)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
    
