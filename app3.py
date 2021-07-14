from flask import render_template, Flask

app = Flask(__name__)


@app.route('/<name>')
def hello(name):
    return render_template('homepage.html', name=name)


@app.route('/looping/<int:number>')
def looping(number):
    return render_template('loopy.html', number=number)


if __name__ == '__main__':
    app.debug = True
    app.run()
