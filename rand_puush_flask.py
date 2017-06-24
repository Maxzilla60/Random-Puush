from flask import Flask, render_template
app = Flask(__name__)

from rand_puush_script import rand_puush

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/get", methods=['GET'])
def get():
	link = rand_puush()
	return link

if __name__ == "__main__":
    app.run(threaded=True)
