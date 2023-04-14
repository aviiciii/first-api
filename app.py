from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/gethackthons", methods = ["GET"])
def get_hackthons():
    hackathon_list = ["Hackathon 1", "Hackathon 2", "Hackathon 3"]
    return hackathon_list




if __name__=="__main__":
	app.run(debug = True)