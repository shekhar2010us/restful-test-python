from flask import Flask

app = Flask(__name__)

# run through localhost:5000/hello
@app.route("/hello")
def hello():
    return "Hello World 2!"

if __name__ == '__main__':
    app.run(debug=True)