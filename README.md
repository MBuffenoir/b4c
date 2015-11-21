# Description 

Battle 4 coins (B4C) is a bitcoins monetized starcraft II match platform.
Users can register and link a Starcraft 2 player profile to their account.

Match are proposed by the players themselves. They define how much bitcoins they engage in the match and the winner takes it all.

The platform propose an escrow service to solve eventual disputes.
Revenue model is based on a small fee taken on each match (a small percentil).

# Tech stack

## Back end
Django + tastypie are used to create a public API and an admin interface.
Crossbar will provide real-time communications.

## Front end
AngularJS create a SPA relying on the API.

# Developer guidelines

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

	# docker-compose

	# You can now connect to the admin using:
	http://<docker-ip>:8000/admin

