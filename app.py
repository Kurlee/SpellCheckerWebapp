from SpellCheckApp import create_app, db
from SpellCheckApp.models import User, Post

if __name__ == "__main__":
    app = create_app('config.Config')


    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Post': Post}
