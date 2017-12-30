#!/usr/bin/env python
""" server component to read traefik hosts
and present them as links """

import sys
import consul
import requests
from flask import Flask
from flask import render_template
import ConfigParser, os

app = Flask(__name__)  # pylint: disable=invalid-name

client = consul.Consul()
services = dict()

config = ConfigParser.ConfigParser()
config.readfp(open('default.cfg'))
bind_addr = config.get('attributes', 'bind_addr')
bind_port = int(config.get('attributes', 'bind_port'))

print "foo"

@app.route('/')
def index():
    """ index page function """
    foo, items = client.catalog.services()
    for service, tags in items.iteritems():
        proto = None
        if 'http' in tags:
            proto = 'http'
        if 'https' in tags:
            proto = 'https'
        if proto:
            services.update({ service: proto })
    return render_template('index.html', services=services, domain=os.getenv('DOMAIN', 'internal'))

@app.route('/ping')
def health():
    return 'pong'

if __name__ == '__main__':
    app.run(debug=True, host=bind_addr, port=bind_port)
