def test_login_success(auth):
    """✅ Test poprawnego logowania"""
    response = auth.login(username="admin", password="password123")
    assert response.status_code == 200, "Nie udało się zalogować"
    assert "token" in response.json(), "Brak tokena w odpowiedzi"

def test_login_invalid_credentials(auth):
    """❌ Test logowania z nieprawidłowymi danymi"""
    response = auth.login(username="wrongUser", password="wrongPass")
    assert response.status_code == 200 or response.status_code == 401, "Nieoczekiwany kod odpowiedzi"
    if response.status_code == 200:
        assert "token" not in response.json(), "Token nie powinien być zwrócony"

def test_login_missing_fields(auth):
    """⚠️ Test logowania bez wymaganych pól"""
    response = auth.login(username="", password="")
    assert response.status_code in [200, 400, 401], "Nieoczekiwany kod odpowiedzi"
    if response.status_code == 200:
        assert "token" not in response.json(), "Token nie powinien być zwrócony"

