# This project created using Flask and PostgreSQL

## Member:

1. I Wayan Trisna Wahyudi ( 2008561018 )
2. I Gusti Bagus Darmika Putra ( 2008561094 )

## How to run project:

1.  Buat venv dengan pyhon
    ```bash
    python -m venv venv
    ```
2.  Clone project dari github
    ```bash
    git clone https://github.com/trisnawahyudiii/simple-search-engine.git
    ```
3.  Create a database in your postgresql and change the database in myapp/db.py
    ```bash
    g.db = psycopg2.connect(
        host="localhost",
    >>> database="<YOUR_DATABASE_NAME>", <<<
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )
    ```
4.  Setting environtment (poweshell)
    ```bash
    $env:FLASK_APP = "myapp"
    $env:FLASK_ENV = "development"
    $env:FLASK_DEBUG = "1"
    $env:DATABASE_USERNAME= "YOUR_USERNAME"
    $env:DATABASE_password= "YOUR_DB_PASSWORD"
    ```
5.  Initialize database with pre-defined documents
    ```bash
    flask init-db
    ```
6.  Run the app
    ```bash
    flask run
    ```

## Default URL : http://127.0.0.1:5000
