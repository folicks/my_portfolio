"""
RUNNNN this command every time in shell
  pip install flask
    modules[package?] are always lower
    case
    app is object of the flask module
"""

from flask import Flask

app = Flask(__name__)



# an @ in python is a DECORATOR


@app.route("/")
def hello_world():
    return "Hello, World!"

# print(__name__)
    # this is sanity check to show 
    # where we are in the program
    # the main vs some other part
if __name__ =="__main__":
  app.run(host= "0.0.0.0", debug=True)



