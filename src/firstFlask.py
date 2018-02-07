from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Can I make live changes?!<br>I can! I can make live changes and not have to re-run the Python interpreter!"

if __name__ == '__main__':
	app.run(debug = True)
