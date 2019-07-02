# Hubertus - Reviermanagement und Jagdtagebuch

## todo

- Revier:
  - /revierList
    - GET > get all Reviere für einen User
    - POST > create new Revier
  - /revier/<int:id>
    - PUT > change data
    - DELETE > delete data
- Tagebuch:
  - /tagebuch
    - GET > get all Tagebucheinträge
    - POST > create new Tagebucheintrag
  - /tagebuch/eintrag/<int:id>
    - PUT > update data
    - delete > delete data

## Installation

1. Linux Server (vorzugsweise Ubuntu)
    1. Docker installieren
    2. Docker-Compose installieren
2. Backend-Repository klonen
`git clone https://github.com/WagnerJM/opus:_xml.git`
3. In das Verzeichnis wechseln
`cd quality`
4. Client-Repo klonen
`git clone https://github.com/WagnerJM/opus_xml_client.git client`
5. .env Datei erstellen
    `python start.py`
    Dabei werden verschiedene Daten abgefragt die für die App notwendig sind und eine .env Datei erstellt
6. Container bauen und starten
`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`

7. Erstelle die Datenbank schemas
Zweites Terminalfenster öffnen und  dort folgendes eingeben.

```docker

docker-compose exec server flask db init

docker-compose exec server flask db migrate

docker-compose exec server flask db upgrade

```

Nachdem das fertig ist, kann mit der App gearbeitet werden.

Der Dienst ist über die <http://Server-IP:8080> erreichbar.
