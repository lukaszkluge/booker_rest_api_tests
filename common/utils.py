import random
import string


def random_string(length=8):
    """Generuje losowy ciąg znaków."""
    return ''.join(random.choices(string.ascii_letters, k=length))


def random_price(min_price=50, max_price=500):
    """Generuje losową cenę w zadanym zakresie."""
    return random.randint(min_price, max_price)


def create_booking_payload(firstname=None, lastname=None, totalprice=None,
                           depositpaid=True, checkin="2025-03-01", checkout="2025-03-05",
                           additionalneeds="Breakfast"):
    """Tworzy payload dla rezerwacji z domyślnymi lub losowymi danymi."""
    return {
        "firstname": firstname or random_string(),
        "lastname": lastname or random_string(),
        "totalprice": totalprice if totalprice is not None else random_price(),
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": additionalneeds
    }

def valid_booking_payload():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2025-02-20", "checkout": "2025-02-25"},
        "additionalneeds": "Breakfast"
    }

def invalid_booking_payload(missing_fields=None, invalid_types=None):
    payload = valid_booking_payload()

    if missing_fields:
        for field in missing_fields:
            payload.pop(field, None)

    if invalid_types:
        for field, value in invalid_types.items():
            payload[field] = value

    return payload


def validate_booking_response(response, expected_firstname=None):
    """Waliduje odpowiedź z API dla rezerwacji."""
    assert response.status_code == 200, f"Niepoprawny status code: {response.status_code}"
    data = response.json()
    assert "bookingid" in data, "Brakuje bookingid w odpowiedzi"
    if expected_firstname:
        assert data["booking"]["firstname"] == expected_firstname, "Niepoprawne imię"


def validate_error_response(response, expected_status_codes):
    assert response.status_code in expected_status_codes, (
        f"Nieoczekiwany kod odpowiedzi: {response.status_code}, oczekiwano: {expected_status_codes}"
    )