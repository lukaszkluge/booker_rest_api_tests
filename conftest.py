import pytest
from endpoints.auth import Auth
from endpoints.booking import Booking

@pytest.fixture
def auth():
    return Auth()

@pytest.fixture
def booking():
    return Booking()

@pytest.fixture
def get_token(auth):
    """Fixture do pobierania tokena"""
    response = auth.login()
    assert response.status_code == 200, "Błąd autoryzacji"
    return response.json()["token"]

@pytest.fixture
def create_booking(booking):
    """Fixture do tworzenia rezerwacji"""
    payload = {
        "firstname": "John",
        "lastname": "Wick",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-02-20", "checkout": "2025-02-25"},
        "additionalneeds": "Breakfast"
    }
    response = booking.create_booking(payload)
    assert response.status_code == 200, "Błąd tworzenia rezerwacji"
    return response.json()["bookingid"]