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
            if all(i not in role[g.user] for i in perm):
                return redirect(url_for('error'))
            return view(**kwargs)
        return decFunc
    return decorator
