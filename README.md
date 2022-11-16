# coms - coms open messaging system

## about
aim of coms is to provide a secure, lightweight, bloat-free chatroom with zero logginng, total transience and a nice looking tui

## instalation
### client
install virtualenv if needed
```bash
virtualenv venv
source venv/bin/activate
pip3 install -r client/requirements.txt
python3 client/client.py --help
```
### server 
```bash
virtualenv venv
source venv/bin/activate
pip3 install -r server/requirements.txt
python3 server/server.py --help
```
