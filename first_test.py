# how to run flask? ->
# export FLASK_APP=main_file_name.py
# flask run


from flask import Flask, render_template, request
from temp import printMessage
from anotherTemp import htmlOutputTrick
app = Flask(__name__)


@app.route('/')
def main():
	# print("Hello Users")
	x = first_function()
	y = second_function()
	return x+" "+y+" "+" Bye"


if __name__ == '__main__':
   app.run(debug = True)


