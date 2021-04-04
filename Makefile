install: python-install
full-reset: repo-pull docker-reset

python-install:
	python3 -m venv venv && \
	. venv/bin/activate && \
	pip install --upgrade pip && \
	pip install -r requirements.txt && \
	echo "App is installed. Run 'make serve' to run the server."

serve:
	. venv/bin/activate && \
	FLASK_APP=flaskr FLASK_ENV=development \
	APP_SETTINGS=flaskr.config.DevelopmentConfig \
	flask run --extra-files flaskr/templates/base.html:flaskr/templates/index.html:flaskr/static/css/chuck.css

docker-reset:
	echo "Stopping container..." && \
	docker stop chuckquotes || true && \
	echo "Deleting container..." && \
	docker rm chuckquotes || true && \
	echo "Deleting image..." && \
	docker rmi chuckquotes || true && \
	echo "Rebuilding image..." && \
	docker build --tag chuckquotes . && \
	echo "Running new image in new container..." && \
	docker run -d --name chuckquotes --publish 5052:5052 chuckquotes && \
	echo "Set restart on failure..." && \
	docker update --restart=on-failure chuckquotes

repo-pull:
	git pull origin master
