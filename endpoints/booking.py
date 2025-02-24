from endpoints.base_endpoint import BaseEndpoint

class Booking(BaseEndpoint):
    """Klasa obsługująca rezerwacje"""

    def create_booking(self, payload):
        return self.post("/booking", json=payload)

    def get_booking(self, booking_id):
        return self.get(f"/booking/{booking_id}")

    def update_booking(self, booking_id, payload, token):
        headers = {"Cookie": f"token={token}"}
        return self.put(f"/booking/{booking_id}", json=payload, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"/booking/{booking_id}", headers=headers)

