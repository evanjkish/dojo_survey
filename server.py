from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "skeleton key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_survey():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form['favlang']
    session['comments'] = request.form['comments']

    return redirect('/doodoo')

@app.route('/doodoo')
def doodoo():
    return render_template('doodoo.html')


if __name__=="__main__":
    app.run(debug=True)