from flask import Flask, render_template
app=Flask('__name__')

@app.route('/')
def index():
    name="Pradip"
    user_logged_in=True
    letters=list(name)
    pradi_dict={'pradi_name':'pradip'}
    my_list=["pradip","gareja","bharat","sanjay"]
    return render_template('basic.html',name=name,letters=letters,
    pradi_dict=pradi_dict,my_list=my_list,
    user_logged_in=user_logged_in)




if __name__=='__main__':
    app.run()