from flask.cli import FlaskGroup
import click

from app import app
from app import db


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()