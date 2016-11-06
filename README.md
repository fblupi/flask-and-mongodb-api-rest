# flask-and-mongodb-api-rest
My first API REST using Flask and MongoDB (http://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_RESTAPI_with_Flask.php).

## Configuration

* Install MongoDB:
```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```
* Install PyMongo:
```
pip install pymongo
```

## Running

* Start MongoDB:
```
sudo service mongodb Start
```
* Run virtualenv:
```
virtualenv -p python3 venv
source venv/bin/activate
```
* Run our app:
```
pip install Flask-PyMongo
python mongo.py
```
