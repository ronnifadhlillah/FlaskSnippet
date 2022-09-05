from flask import Flask,render_template,Blueprint,request
import functools

role={
    "administrator":"1",
    "staff":"2",
    "public":"3"
}

user={
    'admin':'admin',
    'staff':'staff',
    'public':'public'
}

def eng():
    return Flask('appsName',template_folder='')

def build():
    a=eng()

    @a.route('/',methods=['GET','POST'])
    def login():
        if request.method=='POST':
            users=request.form['user']
            password=request.form['pass']
            if users in user and user[users]==password:
                session['user']=users
                return render_template('index.html')
            else:
                print('false')
        return render_template('login.html')

    @a.route('/index',methods=['GET','POST'])
    def index():
        return render_template('index.html')

    @a.before_app_request
    def loadUser():
        userName=session.get['user']
        if userName is None:
            g.user=None
        else:
            g.user=userName
    return a

    def login_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if g.user is None:
                return redirect(url_for('login'))
            return view(**kwargs)
        return wrapped_view

if __name__=='__main__':
    a=build()
    a.run()
