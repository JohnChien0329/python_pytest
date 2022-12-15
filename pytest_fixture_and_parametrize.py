import requests
import pytest

#Arrange 
@pytest.fixture(scope='session')
def build_request_body():
    def _build( itemId, itemName, restaurantId):
        return {
            "itemId": itemId,
            "itemName": itemName,
            "restaurantId": restaurantId
        }
    return _build
@pytest.fixture(scope='session')
def base_url():
    return "http://localhost:5095/api/Item"


@pytest.mark.parametrize(("itemId", "itemName", "restaurantId"), [
    ("item4", "cola", "resaurant1"),
    ("item5", "fish", "resaurant2"),
])

def test_create_user(build_request_body,
                     base_url,
                     itemId,
                     itemName,
                     restaurantId,
                     ):
    api_request = build_request_body(itemId=itemId, itemName=itemName, restaurantId=restaurantId)
    url = f"{base_url}"


    #act
    response = requests.post(url=url, json=api_request)
    
    #Assert
    assert response.status_code == 200

    
