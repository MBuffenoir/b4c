#How to install a web app on a swarm cluster on google compute engine (GCE)

We use:
docker engine (>= 1.9) / machine / compose / hub
gcloud command line tool

##Setting up google cloud

We will use gcloud, a tool by google to manage instances in our google cloud engine account. Let's install it and login with:

    $ curl -sSL https://sdk.cloud.google.com | bash
    $ gcloud auth login

Select a project > create project. From now in we will use this project ID

    $ export PROJECT_ID=<your-project-id>

##Setting up the Swaaaaaaaarm

###Creating a discovery service on a machine out of the cluster

    $ docker-machine create --driver google \
        --google-project  \
        --google-zone europe-west1-b \
        --google-machine-type f1-micro \
        consul-master

Connect to it:

    $ eval $(docker-machine env consul-master)

Start consul with:

    $ docker run --name consul-master --restart=always -p 8500:8500 -d progrium/consul -server -bootstrap -ui-dir /ui

Finally add a firewall rule to allow our swarm node to communicate with the consul server on the port 8500:
    
    $ gcloud compute --project $PROJECT_ID firewall-rules create "consul" --allow tcp:8500  --network "default" --source-tags "docker-machine"

###Creating the swarm master

We need instances on which to install swarm. Let's first create the master with:
    
    $ docker-machine create --driver google \
        --google-project $PROJECT_ID \
        --google-zone europe-west1-b \
        --google-machine-type n1-standard-1  \
        --swarm \
        --swarm-master \
        --swarm-discovery="consul://$(docker-machine ip consul-master):8500" \
        --engine-opt="cluster-store=consul://$(docker-machine ip consul-master):8500" \
        --engine-opt="cluster-advertise=eth0:2376" \
        swarm-master

To connect to the master use:
    
    $ docker-machine ssh swarm-master

And enter our env (note the --swarm`):

    $ eval $(docker-machine env --swarm swarm-master)

Here I got an issue, the machine swarm port were not opened correctly on the GCE firewall, this solved the issue (See [https://github.com/docker/machine/issues/1432]):

    gcloud compute firewall-rules create swarm-machines --allow tcp:3376 --source-ranges 0.0.0.0/0 --target-tags docker-machine --project $PROJECT_ID

After this I could use the `docker-machine env` command without issue.

###Creating a swarm node

    $ docker-machine create --driver google \
        --google-project $PROJECT_ID  \
        --google-zone europe-west1-b \
        --google-machine-type n1-standard-1 \
        --swarm \
        --swarm-discovery="consul://$(docker-machine ip consul-master):8500" \
        --engine-opt="cluster-store=consul://$(docker-machine ip consul-master):8500" \
        --engine-opt="cluster-advertise=eth0:2376" \
        swarm-node-1

Of course you can create as many nodes as needed.

More driver option are available: [https://docs.docker.com/machine/drivers/gce/].

Change the machine-type according to your needs / budget.

You can then test the nodes instances by connection to them with:

    $ docker-machine ssh swarm-node-1

Or from the swarm master list the machine registered on consul:

    $ docker run swarm list consul://$(docker-machine ip consul-master):8500

###Networking

Using the new --x-networking argument of the docker-compose command we can now create an overlay network, that will be used by all the container describe in our compose file:

    docker-compose --x-networking up -d 

##Scaling

    docker-compose scale=3 <app name>
    docker-compose up --force-recreate -d



