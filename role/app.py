from flask import Flask,g,render_template,Blueprint,request,session,url_for,redirect
from middleware import login_required,middleware,templated
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
    a.secret_key=b'y\xb0\xa6]L\xed\xbd\x80[\xc0\xa8\xdd\xc6]<\x9e'
    a.jinja_env.auto_reload=True
    a.DEBUG=True


    @a.before_request
    def load_logged_in_user():
        userName=session.get('user_id')
        if userName is None:
            g.user=None
        else:
            g.user=userName

    @a.route('/',methods=['GET','POST'])
    def login():
        if request.method=='POST':
            users=request.form['user']
            password=request.form['pass']
            if users in user and user[users]==password:
                session.clear()
                session['user_id']=users
                return redirect(url_for('index'))
            else:
                return render_template('login.html')
        return render_template('login.html')


    @a.route('/index',methods=['GET','POST'])
    @login_required
    @middleware({'administrator','public'})
    # @templated('index.html')
    def index():
        # return dict(value=42)
        return render_template('index.html')

    @a.route('/logout',methods=['GET','POST'])
    def logout():
        session.pop('user_id',None)
        session.clear()
        return redirect(url_for('login'))

    return a


if __name__=='__main__':
    a=build()
    a.run()
