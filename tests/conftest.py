from services.auth import auth

def pytest_sessionstart(session):
    try:
        auth.create_user(email="test@vibe.com", password="password123")
    except:
        print("hi")