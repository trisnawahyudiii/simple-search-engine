from datetime import date

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    url_for,
)

from myapp.db import get_db


bp = Blueprint("documents", __name__, url_prefix="/documents")


@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        db = get_db()
        cur = db.cursor()

        error = None
        cur.execute("SELECT * FROM documents")
        data = cur.fetchall()

        if data is None:
            error = "There is no documents"

        flash(error)

        return render_template("documents/index.html", documents=data)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == "GET":
        return render_template("documents/create.html")

    elif request.method == "POST":
        text = request.form["text"]

        db = get_db()
        cur = db.cursor()
        error = None

        if not text:
            error = "please input any text"

        if error is None:
            try:
                insert_query = "INSERT INTO documents (text) VALUES (%s)"
                cur.execute(insert_query, (text,))
                db.commit()
            except db.IntegrityError:
                error = f"Text {text} is already exist."
        else:
            return redirect(url_for("documents/index.html"))

        flash(error)

    return render_template("documents/create.html")
