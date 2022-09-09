from flask import g,redirect,url_for,render_template
from roles import role
import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view

def roles(perm=None):
    def decorator(view):
        @functools.wraps(view)
        def decFunc(**kwargs):
            # print(any(isinstance(i,dict) for i in role.values()))
            for i in role[g.user]:
                if i in perm:
                    print('test')
                else:
                    print('fuk')
            # if role['admin']['1'] in perm:
            #     print('yuuhhu')
            return view(**kwargs)
        return decFunc
    return decorator
