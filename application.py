from flask import Flask
from dotenv import load_dotenv

import os,sys

app = Flask(__name__)


def get_string_from_file(file_path: str) -> str:
    """
    Helper method to read a file in as a string
    :param file_path: the path to the file
    :return: string representation of the file
    """
    with open(file_path, 'r') as file:
        return file.read()

#import routes for lending



#app.run(host='0.0.0.0', port=81)


import lending_routes