def test_unauthenticated(test_client):
    login_response = test_client.get('/login')
    register_response = test_client.get('/register')
    index_response = test_client.get('/')
    sc_response = test_client.get('/spell_check')

    assert login_response.status_code == 200
    assert register_response.status_code == 200
    assert index_response.status_code == 302
    assert sc_response.status_code == 302

def test_register(test_client):
    register_response = test_client.get('/register')
    assert b'id="uname"' in register_response.data

