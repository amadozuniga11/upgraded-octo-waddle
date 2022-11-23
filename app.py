from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/classes')
def classes(): 
    return render_template('classes.html')

@app.route('/professors')
def professors():
    return render_template('professors.html')

'''if __name__ == '__main__': 
    app.run(debug=True)'''