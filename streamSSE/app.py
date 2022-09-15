from flask import Flask, Response, render_template
from datetime import datetime
import random
import time
import json

a = Flask(__name__,template_folder='')
random.seed()

@a.route('/')
def index():
    return render_template('index.jinja')


@a.route('/chartData')
def chartData():
    def gmd():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(5)

    return Response(gmd(), mimetype='text/event-stream')


if __name__ == '__main__':
    a.run()
