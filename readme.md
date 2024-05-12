# Application UserService
## Description 
The main aim of application is simulationg work of publisher (throw messages in broker with delay using paho.mqtt.client) and subscriber (receive messages from publisher) while logging all actions of app.

Also both publisher and subscriber use inner function of generating unique id `get_uuid()`.

## Installation
1. Create directory:
```bash
mkdir user_service
cd user_service
```

2. Create and activate virtual environment (if you need):
```bash
mkdir venv
python3 -m venv venv/
source venv/bin/activate
```

3. Install packages:
```bash
pip install fastapi paho-mqtt 'uvicorn[all]' requests
```

5. Clone git repository:
```bash
git clone -b master https://github.com/PUTENCHIK/user-service.git
cd user-service
```

5. Start app
* Using python script:
```bash
python3 user_service_start.py
```
* Using uvicorn:
```bash
uvinorn user_serice:app --host 0.0.0.0 --port 5001
```

## Usage
Go in browser to `http://{host}:5001/start/{amount}` to start simulation of publishing messages. 

Also you can go to `http://{host}:5001/get_uuid` to get unique id.
