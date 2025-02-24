# ✅ Test tworzenia rezerwacji bez wymaganych pól
def test_create_booking_missing_fields(booking):
    from common.utils import invalid_booking_payload, validate_error_response

    payload = invalid_booking_payload(missing_fields=["lastname", "totalprice"])
    response = booking.create_booking(payload)
    validate_error_response(response, expected_status_codes=[400, 500])


def test_create_booking_invalid_data(booking):
    from common.utils import invalid_booking_payload, validate_error_response

    payload = invalid_booking_payload(invalid_types={"totalprice": "sto", "depositpaid": "yes"})
    response = booking.create_booking(payload)
    print("Response Body:", response.json())
    validate_error_response(response, expected_status_codes=[200, 400])

    if response.status_code == 200:
        data = response.json().get("booking", {})
        assert data.get("totalprice") is not None, "API zaakceptowało None dla totalprice"
        assert isinstance(data.get("totalprice"), int), "totalprice nie jest typu int"
        assert isinstance(data.get("depositpaid"), bool), "depositpaid nie jest typu bool"


def test_update_booking_no_auth(booking, create_booking):
    from common.utils import valid_booking_payload

    payload = valid_booking_payload()
    response = booking.update_booking(create_booking, payload, token="")  # Brak tokena
    assert response.status_code == 403


def test_delete_booking_invalid_token(booking, create_booking):
    invalid_token = "fake_token_123"
    response = booking.delete_booking(create_booking, invalid_token)
    assert response.status_code == 403


def test_get_nonexistent_booking(booking):
    nonexistent_booking_id = 999999  # Zakładamy, że taki ID nie istnieje
    response = booking.get_booking(nonexistent_booking_id)
    assert response.status_code == 404