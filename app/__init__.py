"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgn7c87dvk4k0107rjk0-a.oregon-postgres.render.com",
        database="todo_demo7",
        user="todo_demo7_user",
        password="2jUAn11344M0uE4TCC1l2haxc08CsUz1")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
