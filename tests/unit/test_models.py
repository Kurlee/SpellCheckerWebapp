from hashlib import sha256

"""
This test suite contains unit tests for the models.py file
"""


def test_new_user(new_user):
    """
    GIVIN a User model
    WHEN a new User is created
    Then check the phone number and hashed password
    :type new_user: object
    user = User(username='withphone', two_fa='1234567891')
    """
    assert new_user.get_username() == 'withphone'
    assert new_user.get_two_fa() == '1234567891'
    new_user.set_password("TestPassword")
    assert new_user.check_password("TestPassword")
    assert new_user.get_id() == 'None'


def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the Password of the user is defined to a value, or changed
    THEN check the user password returns the last defined password, as a salted hash
    """
    new_user.set_password("ChangedPassword")
    assert not new_user.check_password("TestPassword")
    assert new_user.password_hash != "ChangedPassword"
    assert new_user.check_password("ChangedPassword")
    # assert password is stored with a salt and hashed
    assert new_user.password_hash.split('$', 1)[0] == "pbkdf2:sha256:150000"
    assert new_user.password_hash.split('$', 1)[1] != sha256(b"ChangedPassword").hexdigest()


def test_user_id(new_user):
    """
    GIVEN an existing User
    WHEN the ID of the user is defined to a value
    THEN check the user ID returns a string (and not an integer) as needed by Flask-WTF
    """
    new_user.id = 17
    assert isinstance(new_user.get_id(), str)
    assert not isinstance(new_user.get_id(), int)
    assert new_user.get_id() == "17"


from SpellCheckApp.models import User

def main():
    user = User(username='test', two_fa='1234567891')
    test_setting_password(user)

if __name__ == '__main__':
    main()

