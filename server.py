from flask import Flask, render_template

app = Flask(__name__)

## this is the URL; if you wanted a profile page, for example you would do @app.route('/profile')
@app.route('/') 
def main_page(): ## function name doesn't matter to the web app, but try and make it meaningful
	return render_template('index.html') ## flask knows to look in /templates/ sub-folder


@app.route('/showTaskReview')
def showTaskReview():
    return render_template('task-review.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

