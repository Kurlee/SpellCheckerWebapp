from SpellCheckApp.models import User

def test_users_in_db(init_database):
    db = init_database
    users = User.query.all()
    print (users)



def main():
    from tests.conftest import init_database
    test_users_in_db(init_database)


if __name__=="__main__":
    main()

