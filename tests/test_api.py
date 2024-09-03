import pytest
import requests

from playwright.sync_api import sync_playwright
@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
    # Arrange
    url = 'https://api.duckduckgo.com/?q=python+programming&format=json'
    # Act
    response = requests.get(url)
    body = response.json()
    # Assert
    assert response.status_code == 200
    assert "Python" in body["AbstractText"]


# Get the Bearer token from the login endpoint
response = requests.post('https://onlinestorepredprod.onrender.com/auth/login', json={
    "email": "online.store.authority@gmail.com",
    "password": "b9uT2rXE80Ls"
})

# Extract the Bearer token from the response
bearer_token = response.json().get('token')

if bearer_token:
    def test_post(playwright: sync_playwright):
        data = {
            "email": "online.store.authority@gmail.com",
            "password": "b9uT2rXE80Ls"
        }

        # Create a new context
        context = playwright.request.new_context()

        # Use the Bearer token in the Authorization header
        response = context.post(
            url="https://onlinestorepredprod.onrender.com/auth/login",
            headers={"Authorization": f"Bearer {bearer_token}"},
            data=data
        )

        print(response)

        # Assertions to ensure the request was successful
        assert response.status == 200
        assert response.status_text == "OK"
else:
    print("Failed to retrieve the Bearer token")

