#Description 

Battle 4 coins (B4C) is a bitcoins monetized starcraft II match platform.
Users can register and link a Starcraft 2 player profile to their account.

Match are proposed by the players themselves. They define how much bitcoins they engage in the match and the winner takes it all.

The platform propose an escrow service to solve eventual disputes.
Revenue model is based on a small fee taken on each match (a small percentil).

#Tech stack

##Back end
Django + tastypie are used to create a public API and an admin interface.
Crossbar will provide real-time communications.

##Front end
AngularJS creates a SPA relying on the API.

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
	# to create the env:
	docker-machine create b4c -d virtualbox

	# to use this env
	eval "$(docker-machine env b4c)"

	# to get the ip address to connect to
	docker ip b4c
	```

# License

MIT


