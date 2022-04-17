from pydoc import cli
from urllib import response
from fastapi.testclient import TestClient
import sys        
sys.path.insert(0, '../labtest_06')        
from main import app

client = TestClient(app)
    
def test_year_data_api():
    output = 25
    input = "2540"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() == {"age": output}

def test_year_Zero():
    output = "Value = 0 or less than"
    input = "0"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() =={"age":output}
    
def test_year_Out_of_bound():
    output = "Value out of Bound"
    input = "2566"
    response = client.get("/service/getage?year="+input)
    assert response.status_code == 200
    assert response.json() =={"age":output}