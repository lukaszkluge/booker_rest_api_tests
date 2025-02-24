import pytest

@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", [
    ("Alice", "Smith", 200, False, "2025-03-01", "2025-03-05", "Dinner"),
    ("Bob", "Johnson", 150, True, "2025-04-10", "2025-04-15", "Breakfast"),
    ("Charlie", "Brown", 300, False, "2025-05-20", "2025-05-25", "Parking"),
])
def test_create_booking(booking, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {"checkin": checkin, "checkout": checkout},
        "additionalneeds": additionalneeds
    }
    response = booking.create_booking(payload)
    assert response.status_code == 200
    assert "bookingid" in response.json()


@pytest.mark.parametrize("firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds", [
    ("Updated", "User", 300, True, "2025-04-01", "2025-04-10", "Lunch"),
    ("Modified", "Client", 250, False, "2025-06-01", "2025-06-05", "Spa Access")
])
def test_update_booking(booking, get_token, create_booking, firstname, lastname, totalprice, depositpaid, checkin, checkout, additionalneeds):
    payload = {
        "firstname": firstname,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {"checkin": checkin, "checkout": checkout},
        "additionalneeds": additionalneeds
    }
    response = booking.update_booking(create_booking, payload, get_token)
    assert response.status_code == 200


@pytest.mark.parametrize("use_valid_token", [True, False])
def test_delete_booking(booking, get_token, create_booking, use_valid_token):
    token = get_token if use_valid_token else "invalid_token"
    response = booking.delete_booking(create_booking, token)
    if use_valid_token:
        assert response.status_code == 201
    else:
        assert response.status_code == 403