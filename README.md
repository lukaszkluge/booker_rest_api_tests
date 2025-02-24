# RESTful Booker API Test Suite

## 📝 Opis

Automatyczny zestaw testów API dla systemu rezerwacji oparty o RESTful Booker API. Projekt wykorzystuje pytest oraz wzorzec Page Object Model (POM) dla API, zapewniając przejrzystą strukturę i łatwość rozbudowy.

## ⚙️ Wymagania

Python 3.11+

pytest

requests

docker (opcjonalnie dla uruchomienia w kontenerze)

## 📥 Instalacja

## Sklonuj repozytorium
git clone <repo_url>
cd restful_booker_tests

## Utwórz środowisko wirtualne
python -m venv venv <br>
source venv/bin/activate  # Linux/Mac <br>
venv\Scripts\activate    # Windows

## Zainstaluj zależności
pip install -r requirements.txt

## 🧪 Uruchomienie wszystkich testów
pytest

### Uruchomienie wybranego testu
pytest tests/test_booking.py (przykład)

## 🐳 Uruchomienie przez Dockera

Zbuduj obraz:

docker build -t restful-booker-tests .

Uruchom testy:

docker run restful-booker-tests
