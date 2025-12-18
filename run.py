from app import create_app

app = create_app()


@app.cli.command("db_upgrade")
def db_upgrade():
    """Initialize or upgrade the database."""
    from flask_migrate import upgrade

    upgrade()


if __name__ == "__main__":
    app.run()

