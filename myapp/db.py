import os
import pandas
import psycopg2
import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if "db" not in g:
        g.db = psycopg2.connect(
            host="localhost",
            database="cossine_db",
            user=os.environ["DB_USERNAME"],
            password=os.environ["DB_PASSWORD"],
        )
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS documents;")
    cur.execute("DROP TABLE IF EXISTS term_frequency;")

    cur.execute(
        "CREATE TABLE documents("
        "id serial PRIMARY KEY,"
        "text TEXT NOT NULL,"
        "created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);"
    )

    cur.execute(
        "CREATE TABLE term_frequency("
        "id serial PRIMARY KEY,"
        "term TEXT NOT NULL,"
        "tf_value DOUBLE PRECISION NOT NULL,"
        "document_id INTEGER,"
        "FOREIGN KEY (document_id) REFERENCES documents(id)"
        ");"
    )

    df = pandas.read_csv("myapp/dataset/dataset.csv", sep=",", encoding="utf-8")

    data_to_insert = [(text,) for text in df["text"]]
    insert_query = "INSERT INTO documents (text) VALUES (%s)"
    cur.executemany(insert_query, data_to_insert)
    conn.commit()

    cur.close()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
