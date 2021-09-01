import os
from datetime import datetime

from pytz import timezone
from flask import Flask, render_template

app = Flask(__name__)

time_format = os.environ.get('TIME_FORMAT', '%H:%M:%S')
timezone_name = os.environ.get('TIMEZONE', 'Europe/Moscow')
zone = timezone(timezone_name)


@app.route("/")
def index():
    time = datetime.now(zone).strftime(time_format)
    return render_template('index.html', time=time)