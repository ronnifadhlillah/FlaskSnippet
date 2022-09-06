from flask import g,redirect,url_for,render_template
import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view


def templated(template=None):
    print(template)
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            template_name = template
            if template_name is None:
                template_name = f"{request.endpoint.replace('.', '/')}.html"
            ctx = f(*args, **kwargs)
            if ctx is None:
                ctx = {}
            elif not isinstance(ctx, dict):
                return ctx
            return render_template(template_name, **ctx)
        return decorated_function
    return decorator

def middleware(perm=None):
    print(perm)
    def decorator(view):
        @functools.wraps(view)
        def decFunc(**kwargs):
            print(view())
            # print(view())
            return view(**kwargs)
        return decFunc
    return decorator
