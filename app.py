import pyrebase

config = {

}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def basic():
    usr = db.child("usr").get()
    usr0 = usr.val()
    usr0.pop(0)
    if request.method == 'POST':   
        mac = request.form['name']
        db.child("usr").child(len(usr0)+1).set(mac)
        return render_template('index.html', t = usr0)
    return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)




