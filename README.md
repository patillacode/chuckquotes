# randomchuck
An API that returns a random json formatted Chuck Norris quote on request.
And a WEB that renders a random json formatted Chuck Norris quote on request.

[Web Demo](http://chuckquotes-patillacode.rhcloud.com/)

[API Demo](http://chuckquotes-patillacode.rhcloud.com/api)

Developed with Flask/Python

## Install
`pip install -r requirements`

## Run
`cd app`

`python random_chuck_server.py -h --port PORT --host HOST`

## Test
`curl -i -X GET http://127.0.0.1:8080/`
