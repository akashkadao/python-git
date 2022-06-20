from app import app

def test1():
    response = app.test_client().get("/")
    assert response.status_code == 200
    
def test2():
    response = app.test_client().get("/base")
    assert response.status_code == 200
    
def test3():
    response = app.test_client().get("/base")
    assert b"My Friend List" in response.data
    assert b"Added Friend" in response.data    
    assert b"things" in response.data 
