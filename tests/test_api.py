import pytest
import requests
from playwright.sync_api import sync_playwright
from config import LOGIN_URL


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
res = requests.post(LOGIN_URL, json={
    "email": "online.store.authority@gmail.com",
    "password": "b9uT2rXE80Ls"
})

# Extract the Bearer token from the response
bearer_token = res.json().get('token')


@pytest.mark.api
def test_post(playwright: sync_playwright):
    data = {
        "email": "online.store.authority@gmail.com",
        "password": "b9uT2rXE80Ls"
    }

    # Create a new
    context = playwright.request.new_context()

    # Use the Bearer token in the Authorization header
    resp = context.post(url=LOGIN_URL, headers={"Authorization": f"Bearer {bearer_token}"}, data=data)

    # Assertions to ensure the request was successful
    assert resp.status == 200
    assert resp.status_text == "OK"
