# import of flask framework & render_template in order to be able to input our html script
from flask import Flask, render_template



# __name__: 
#    (str) --> the name of the application package

# template_folder: 
#    (str) --> the folder that contains the templates that should be used by the application. Defaults to 'templates' folder in the root path of the application.
app = Flask(
    __name__,
    template_folder='templates'
)



# route() decorator to tell Flask what URL should trigger our function
# return render_template and pass our html file as parameter
@app.route('/')
def timer():
  return render_template("timer.html")



# we run the app our selection of host & port 
# passing debug=True enables debug mode, which is mostly equivalent
if __name__ == "__main__":
	app.run(
		host='0.0.0.0',
    debug = True,
		port=8080
	)