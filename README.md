# WEB-Shop-Beta
sudo apt install python3-venv
python3 -m venv venv
source venv/bin/activate
pip install django
pip install sorl-thumbnail
pip install python-slugify
pip install pillow
python3 manage.py makemigrations
python3 manage.py migrate
http://127.0.0.1:8001/ 