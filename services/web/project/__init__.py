from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import (
    create_engine,
    Column, Integer, String, DateTime, Boolean, CheckConstraint, ForeignKey
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

import random
from datetime import date

from sqlalchemy.sql import func


def print_all_tables_data(connection):
    all_tables = connection.execute(
        f"SELECT * FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE';").all()
    all_tables = [item[2] for item in all_tables]
    final_result = ""
    for table in all_tables:
        final_result += f'<br>Table: {table}<br>'
        columns = connection.execute(f"SELECT column_name FROM information_schema.columns "
                                     f"WHERE table_schema='public' AND table_name = '{table}';").all()
        columns = [item[0] for item in columns]
        rs = connection.execute(f"SELECT * FROM {table}")
        for row in rs:
            res = ""
            for i, column in enumerate(columns):
                res += f"{column}: {row[i]} |<br>"
            final_result+=res
    return final_result

app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

DB_NAME = 'superheroes_hw'

Base = declarative_base()

class SuperHeroes(db.Model):
    __tablename__ = "superheroes"
    __table_args__ = (
        db.CheckConstraint('superhero_power >= 1 AND superhero_power <= 10'),
    )

    id = db.Column(db.Integer, primary_key=True)
    superhero_name = db.Column(db.String, nullable=False)
    superhero_power = db.Column(db.Integer, nullable=False)
    is_villain = db.Column(db.Boolean, nullable=False)
    deceased_date = db.Column(db.DateTime, server_default=None)

    children = db.relationship("Chronicles", cascade="all, delete")

    def __str__(self):
        return f"{self.superhero_name}, id: {self.id}"


class Chronicles(db.Model):
    __tablename__ = "chronicles"
    __table_args__ = (
        db.CheckConstraint('year >= 2000 AND year <= 2100'),
    )

    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('superheroes.id'))
    year = db.Column(db.Integer)
    text = db.Column(db.String)

@app.route("/")
def show_tables():
    with db.engine.connect() as connection:
        res = print_all_tables_data(connection)
    return res