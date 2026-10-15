import allure
import requests

from utils.config import Config
@allure.title("API Login - Valid Credentials")
@allure.description(
    "Verify that Firebase authentication succeeds "
    "with valid credentials."
)

def test_login_api():
    with allure.step("Validate environment configuration"):
     config = Config()
    

    assert config.username, "APP_USERNAME is not configured"
    assert config.password, "APP_PASSWORD is not configured"
    assert config.firebase_api_key, "FIREBASE_API_KEY is not configured"

    url = (
        "https://identitytoolkit.googleapis.com/v1/"
        "accounts:signInWithPassword"
    )
    
    with allure.step("Send Firebase login request"):
     response = requests.post(
        url,
        params={"key": config.firebase_api_key},
        json={
            "email": config.username,
            "password": config.password,
            "returnSecureToken": True,
        },
        timeout=30,
    )

    print("Status:", response.status_code)

    data = response.json()

    if response.status_code != 200:
        # Avoid printing the full request or credentials.
        print("Firebase error:", data.get("error", {}).get("message"))
    with allure.step("Verify successful authentication"):  
     assert response.status_code == 200, "Firebase login failed"
     assert data.get("idToken"), "Missing idToken"
     assert data.get("refreshToken"), "Missing refreshToken"
     assert data.get("localId"), "Missing localId"
     print("Firebase login successful!")
     print("HTTP Status:", response.status_code)
     print("idToken received:", bool(data.get("idToken")))
     print("refreshToken received:", bool(data.get("refreshToken")))
     print("localId received:", bool(data.get("localId")))



