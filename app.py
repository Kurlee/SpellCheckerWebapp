from SpellCheckApp import create_app, db
from SpellCheckApp.models import User, Post

app = create_app('config.ProductionConfig')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
