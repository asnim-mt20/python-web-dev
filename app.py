from flask import Flask

#object of the class Flask
app = Flask(__name__)


#route
@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


#local host
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
