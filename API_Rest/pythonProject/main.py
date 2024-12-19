from flask import Flask
from flask import Flask, jsonify, request, render_template
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response
from pydantic import BaseModel, Field
from typing import List, Optional
import mysql.connector
from time import sleep

connection = mysql.connector.connect(host="localhost", user="*", password="*", database="bd_teste")
cursor = connection.cursor()
cursor.execute(
    "create table if not exists usuarios (idUser int auto_increment primary key, Nome_usu varchar(50), email varchar(50), senha varchar(50))")
app = Flask(__name__)

spec = FlaskPydanticSpec("flask", title="Teste online")
spec.register(app)