from flask import Flask

app=Flask('__name__')
@app.route('/')
def index():
    return '<h1>Go to pradip gareja page /pradip/name<h1>'

@app.route('/pradip/<name>')
def pradip(name):
    pradipname=''
    if name[-1]=='p':
        pradipname=name[:-1]+'iloveu'
    else:
        pradipname=name+'p'
    return "<h1>Your name is : {}</h1>".format(pradipname)

if __name__=='__main__':
    app.run(debug=True)
