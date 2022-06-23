from flask import Flask, render_template, jsonify
import datetime
import random

app = Flask(__name__)
state = {}

@app.route('/')
def index():
    global state
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'time': timeString,
      'state': state.get('channel1', 0)
      }
    return render_template('index.html', **templateData)

@app.route('/post/<channel_id>/<value>')
def post_data(channel_id, value):
    global state
    state[channel_id] = value
    return 'OK'

@app.route('/get/<channel_id>')
def get_data(channel_id):
    global state
    return jsonify(
        value=state.get(channel_id, 0)
    )

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
