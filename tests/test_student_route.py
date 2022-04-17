from fastapi.testclient import TestClient
import sys
sys.path.insert(0,"../labtest_06")
from main import app 
client = TestClient(app)

def test_post_to_insert(db):
    response = client.post(
        "/students/",
        json={
            "name":"string",
            "description":"string",
            "completed":"true",
            "date":"string"
        }
    )
    assert response.status_code == 200 
    assert response.json()[0]["name"] == "string"
    assert response.json()[0]["description"] == "string"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_put_update(db):
    response = client.put(
        "/students/6238b47bbf014672aab0dfa8",
        json={
            "name": "update",
            "description": "string2",
            "completed": "true",
            "date": "string"
        }
    )
    assert response.status_code == 200
    assert response.json()[0]["name"] == "update"
    assert response.json()[0]["description"] == "string2"
    assert response.json()[0]["completed"] == True
    assert response.json()[0]["date"] == "string"

def test_student_delete(db):
    response = client.delete(
        "/students/6238b47bbf014672aab0dfa8"
        
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}