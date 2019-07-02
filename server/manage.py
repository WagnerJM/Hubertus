from flask.cli import FlaskGroup

from app import create_app
from app.database import db

from app.api.user.models import User
from app.api.stammdaten.models import SentosaSetting


app = create_app()
cli = FlaskGroup(create_app=create_app)
prompt = "> "


@cli.command('create_admin')
def create_admin_user():
    if not User.query.filter_by(is_admin=True).first():
        print("Username: ")
        username = input(prompt)
        print("Email: ")
        email = input(prompt)
        print("Password: ")
        pw1 = input(prompt)
        print("Password repeat: ")
        pw2 = input(prompt)

        if pw1 == pw2:
            user = User(username, pw1, email)
            user.is_admin = True
            user.save()
            print("Admin user created")
        else:
            print("Admin user already exists")




if __name__ == '__main__':
    cli()
