# Libraries

import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
import pytz

# Set the timezone to Kolkata

kolkata_tz = pytz.timezone("Asia/Kolkata")

# Custom Formatter with Kolkata Time
class KolkataFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, kolkata_tz)
        return dt.strftime(datefmt if datefmt else "%d-%m-%Y %H:%M:%S")

# Logging format

logging_format = KolkataFormatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

# HTTP Logger

funnel_logger = logging.getLogger('HTTP Logger')
funnel_logger.setLevel(logging.INFO)
funnel_handler = RotatingFileHandler('http_audits.log', maxBytes = 2000, backupCount = 5)
funnel_handler.setFormatter(logging_format)
funnel_logger.addHandler(funnel_handler)

# Baseline honeypot

from flask import Flask, render_template, request, redirect, url_for, flash

def web_honeypot(input_username="admin", input_password="password"):
    app = Flask(__name__)
    app.secret_key = "your_secret_key_here"  # Required for flash messages

    @app.route('/')
    def index():
        return render_template('wp-admin.html')

    @app.route('/wp-admin-login', methods=['POST'])
    def login():
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if username == input_username and password == input_password:
            #flash('Login successful! Access granted.', 'success')
            flash('U think you hacked Me!\nHahaha You are Trapped Man!', 'success')
        else:
            flash('Invalid username or password. Please try again.', 'error')

        return redirect(url_for('index'))

    return app

def run_web_honeypot(port = 5000, input_username = "admin", input_password = "admin"):
    run_web_honeypot_app = web_honeypot(input_username, input_password)
    run_web_honeypot_app.run(host="0.0.0.0", port=port, debug=True)
