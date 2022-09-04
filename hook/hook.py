from app import bindHook as hook
import socket
import flask

def globalDefOfHook():
    arr=(
        hook('host',socket.gethostname()),
        hook('flask_version',flask.__version__),
    # add here for more hook include (,) in every end of line
    )
    return arr
