from SpellCheckApp import create_app, db
from SpellCheckApp.models import User, Post, History

app = create_app('config.ProductionConfig')


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'History': History}
