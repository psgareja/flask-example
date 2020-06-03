from flask import Flask
app=Flask('__name__')
@app.route('/')
def index():
    return "<h1>Hello Pradip</h1>"
@app.route('/information')
def info():
    return "<h1>pradip is cool guy</h1>"

@app.route('/pradip/<name>')
def pradip(name):
    return '<h1>100th letter of name: {}</h1>'.format(name)


if __name__=='__main__':
    app.run(debug=True)