# chuckquotes
An API that returns a random json formatted Chuck Norris quote on request.
And a WEB that renders a random json formatted Chuck Norris quote on request.

[Web Demo](http://chucknorris.patilla.es)

[API Demo](http://chucknorris.patilla.es/api)

Developed with Flask/Python

## Install
`pip install -r requirements`

## Run
`cd app`

`python random_chuck_server.py -h --port PORT --host HOST`

## Test
`curl -i -X GET http://127.0.0.1:9090/`
