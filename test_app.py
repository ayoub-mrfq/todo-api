from app import app

def test_get_taches():
    client = app.test_client()
    response = client.get('/taches')
    assert response.status_code == 200


def test_post_taches() :
    client = app.test_client()
    response = client.post('/taches', json={"titre":"Apprendre Docker"})
    assert response.status_code == 201
