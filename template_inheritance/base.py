from flask import Flask, render_template

app=Flask('__name__')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/pradip/<name>')
def pradipname(name):
    return render_template('pradip.html',name=name)


if __name__=='__main__':
    app.run()
