# coms - coms open messaging system

## about
aim of coms is to provide a secure, lightweight, bloat-free chatroom with zero logginng, total transience and a nice looking tui

## instalation
### client
```bash
# install virtualenv if needed
# pip3 install virtualenv

# create and activate virtual enviroment
virtualenv venv
source venv/bin/activate
# install requirements
pip3 install -r client/requirements.txt

# lauch client
python3 client/client.py --help
```
### server 
```bash
# install virtualenv if needed
# pip3 install virtualenv

# create and activate virtual enviroment
virtualenv venv
source venv/bin/activate
# install requirements
pip3 install -r server/requirements.txt

# start server
python3 server/server.py --help
```
## licensing
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.