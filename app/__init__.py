"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgpp940rddl9mmoc4180-a.oregon-postgres.render.com",
        database="todo_demo_ina7",
        user="todo_demo_ina7_user",
        password="K4tlPlJiAFaXNMwfeDUVFXggoYhA2Gs3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
