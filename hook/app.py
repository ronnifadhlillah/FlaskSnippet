from flask import Flask,render_template,request,Blueprint
import hook

# Flask initialize
def eng():
    return Flask('appName',template_folder='')

# Flask main engine
def build():
    a=eng()
    # Init hook using before_request function
    beforeReq(a)

    # Simple route
    @a.route('/')
    def index():
        return render_template('index.html')
    return a

# set hook at jinja global
def beforeReq(a):
    @a.before_request
    def bind():
        g=hook.globalDefOfHook()
        for b in g:
            a.jinja_env.globals[b['key']]=b['value']

# The connector used to hook.py
def bindHook(k,v):
    arr={
        'key':k,
        'value':v
    }
    return arr

if __name__=="__main__":
    a=build()
    a.run()
