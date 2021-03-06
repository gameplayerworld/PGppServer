# PGppServer
Lightweight and simple server for PokeGo++. 
Teleports between given locations and reports raids to webhook 
compatible with [PokeAlarm](https://github.com/PokeAlarm/PokeAlarm).

## Installation
```
git clone https://github.com/hzpz/PGppServer.git
cd PGppServer
python3 -m venv pgppserver-venv
source pgppserver-venv/bin/activate
pip install -r requirements.txt
```

## Configuration
See `config.py`:
* `HOST`: IP to bind to, use '0.0.0.0' for all interfaces
* `PORT`: port to listen on
* `MIN_RAID_LEVEL`: minimum raid level to publish to webhook
* `WEBHOOK_URL`: URL of webhook, e.g. 'http://localhost:4000'
* `TELEPORT_DELAY_MINUTES`: time in minutes between teleports
* `LOCATIONS_CSV_FILENAME`: name of the CSV file with locations, see below for details
* `SEEN_RAIDS_FILENAME`: file for cache of seen raids
* `LOG_LEVEL`: logging verbosity

### Locations CSV
Format: `latitude,longitude,name`, e.g. `52.2780709,7.9853899,Osnabrück`. `name` is optional.

### PokeGo++
* Fake Location: on
* Enable Worker Mode: on
* URL: http://{pgppserver}/data
* Enable Location Fetch: on
* URL: http://{pgppserver}/loc

## Start
```
cd PGppServer
source pgppserver-venv/bin/activate
python server.py
```