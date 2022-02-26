import json
import logging

import blockcypher
import requests
from application import app, get_string_from_file
#, get_db_connection, BLOCKCYPHER_API_KEY 
from flask import request, abort


@app.route('/lending')
def lending():
    return 'OK now you want to borrow eh'