from flask import *
environment='development'

app = Flask(__name__)
app.config['ENV'] = 'development'

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    debuging=True
    
    app.run(host="0.0.0.0",port=8081,debug=True)