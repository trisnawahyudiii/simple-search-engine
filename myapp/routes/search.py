from flask import (
    Blueprint,
    flash,
    url_for,
    redirect,
    render_template,
    request,
)

from myapp.db import get_db
from myapp.search_engine import get_search_result

bp = Blueprint("search", __name__)


@bp.route("/", methods=("GET", "POST"))
def index():
    if request.method == "GET":
        return render_template("search/index.html")

    elif request.method == "POST":
        db = get_db()
        cur = db.cursor()

        # read documents from db
        error = None
        cur.execute("SELECT * FROM documents")
        documents = cur.fetchall()

        if documents is None:
            error = "There is no documents"

        flash(error)

        # get search query from request
        searchQuery = request.form["searchQuery"]

        # get search result
        documentId = int(get_search_result(documents, searchQuery))

        sql = "SELECT * FROM documents WHERE id = %s"
        cur.execute(sql, (documentId,))

        result = cur.fetchone()

        cur.close()
        return render_template("search/result.html", document=result, query=searchQuery)
