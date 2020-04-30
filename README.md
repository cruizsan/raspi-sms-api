# raspi-sms-api
sms api for raspberry (linux)

# Installation
### Python3 et Gunicorn3 et Flask
```
sudo apt install python3 python3-dev python3-pip gunicorn3
pip3 install flask
```

### Gammu (envoi de sms)
```
sudo apt install gammu
gammu-detect > /etc/gammurc
# on test
gammu sendsms TEXT <phoneNumber> -text "monTexte"
```

# Execution
### gunicorn pour lancer un webserver multi worker
```
# -w <x> : nombre de worker/process
# --bind <host:port> : quel adresse communiqué ici localhost/domaine.ltd fonctionne sur le port 8888
# -n <name> : mettre un nom sur le process
# -D : pour daemoniser et faire fonctionner en background
cd raspi-sms-api;
gunicorn3 -w 4 --bind 0.0.0.0:8888 wsgi:app -n rasp_sms_api
# gunicorn3 -w 4 --bind 0.0.0.0:8888 wsgi:app -n rasp_sms_api -D
```

# Exemple
### supposons un domaine apisms.ltd
```
curl -X POST http://apisms.ltd:8888/send/sms -F "number=047276****" -F "text=mon premier sms"
```
