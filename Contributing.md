#Developer guidelines

Docker is used to provide a unified development environment.
You will need docker engine and docker compose to run the project. Mac or Windows developers can use docker machine.

See [https://docs.docker.com] for installation manuals.

	# build and launch
	docker-compose up -d

	# rebuild and restart (in case new requirements have been added)
	docker-compose build
	docker-compose stop b4c
	docker-compose rm -f b4c
	docker-compose up -d

	# Create or update database tables
	docker exec b4c_b4c_1 ./manage.py migrate

	# Create superuser (Used once)
	docker exec -it b4c_b4c_1 ./manage.py createsuperuser

	# Consult the logs
	docker-compose logs -f b4c

	# You can now connect to the admin using:
	http://<docker-ip>:8000/admin

##Docker tips

+ Install completion on mac

	```
	brew install bash-completion
	curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker-compose > /usr/local/etc/bash_completion.d/docker-compose
	```

+ Install completion on linux

	```
	curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose
	```

+ Docker machine on a mac

	```
	# to create the env
	docker-machine create b4c -d virtualbox

	# to use this env
	eval "$(docker-machine env b4c)"

	# to get the ip address to connect to
	docker ip b4c
	```