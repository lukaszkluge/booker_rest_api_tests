FROM python:3.11-slim
# Ustawienie katalogu roboczego
WORKDIR /Python_POM_API_Docker

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
#  Domyślne polecenie: uruchomienie testów
CMD ["pytest", "--maxfail=5", "--disable-warnings", "--html=report.html"]