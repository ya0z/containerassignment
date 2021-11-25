# This is a Flask application running inside Amazon EC2 Ubuntu 18.04
## Install Python Virtualenv
```
$ sudo apt-get update
$ sudo apt-get install python3-venv
```
## Git-clone this repository
```
$ git clone https://github.com/ya0z/containerassignment.git
```
## Create and run the virtual environment inside the cloned repository
```
$ cd containerassignment
$ python3 -m venv venv
$ source venv/bin/activate
```
## Install Flask, Gunicorn and the required libraries
```
$ pip install -r workshop01/requirements.txt
```
## Run the Gunicorn WSGI server and serve the Flask application
```
$ cd workshop01
$ ../venv/bin/gunicorn -b 0.0.0.0:80 app:app
```
## View the application on the EC2 IP
http://\[public-ip\]/
