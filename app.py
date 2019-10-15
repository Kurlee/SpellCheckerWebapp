from SpellCheckApp import app, db
from SpellCheckApp.models import User, Post


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}