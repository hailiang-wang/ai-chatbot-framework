import os
from flask import Flask, render_template

app = Flask(__name__)

# Configurations
try:
    env = os.environ['APPLICATION_ENV']
except KeyError as e:
    # logging.error('Unknown environment key, defaulting to Development')
    env = 'Development'
    app.config.from_object('config.%s' % env)

@app.errorhandler(404)
def not_found(error):
    return "Not found", 404

from app.core.controllers import core as core
from app.stories.controllers import stories as stories
from app.train.controllers import train as train
from app.endpoint.controllers import endpoint as endpoint
from app.chat.controllers import chat as chat

app.register_blueprint(core)
app.register_blueprint(stories)
app.register_blueprint(train)
app.register_blueprint(endpoint)
app.register_blueprint(chat)