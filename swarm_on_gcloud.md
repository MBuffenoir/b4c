#How to install a web app on a swarm cluster on google compute engine (GCE)

We use:
docker engine / machine / compose / hub
gcloud command line tool

##Setting up google cloud

We will use gcloud, a tool by google to manage instances in our google cloud engine account. Let's install it and login with:

    $ curl -sSL https://sdk.cloud.google.com | bash
    $ gcloud auth login

Select a project > create project. From now in we will use this project ID

    $ export PROJECT_ID=<your-project-id>
    $ gcloud config set project $PROJECT_ID

##Setting up the Swaaaaaaaarm

First we will generate our swarm token on our local machine with:

    $ docker run swarm create

Write dowm the token returned by this command and put it in an ENV variable:

    $ export SWARM_TOKEN=<token>

We need some instances on which to install swarm. Let's first creat the master with:
    
    $ docker-machine create --driver google \
        --google-project $PROJECT_ID \
        --google-zone europe-west1-b \
        --google-machine-type f1-micro \
        --swarm \
        --swarm-master \
        --swarm-discovery token://$SWARM_TOKEN \
        swarm-master

To connect to the master use:
    
    $ docker-machine ssh swarm-master

And enter our env (note the --swarm`):

    $ eval $(docker-machine env --swarm swarm-master)

Here I got an issue, the machine port were not opened correctly on the GCE firewall, this solved the issue (See [https://github.com/docker/machine/issues/1432]):

    gcloud compute firewall-rules create swarm-machines --allow tcp:3376 --source-ranges 0.0.0.0/0 --target-tags docker-machine --project $PROJECT_ID

After this I could use the machine env without issue.

Now, we are going to creato two swarm nodes with

    $ docker-machine create --driver google \
        --google-project $PROJECT_ID  \
        --google-zone europe-west1-c \
        --google-machine-type n1-standard-1 \
        --swarm \
        --swarm-discovery token://$SWARM_TOKEN \
        swarm-node-0

and

    $ docker-machine create --driver google \
        --google-project $PROJECT_ID  \
        --google-zone europe-west1-d \
        --google-machine-type n1-standard-1 \
        --swarm \
        --swarm-discovery token://$SWARM_TOKEN \
        swarm-node-1

More driver option are available: [https://docs.docker.com/machine/drivers/gce/].

Change the machine-type according to your needs / budget.

You can then test the nodes instances by connection to them with:

    $ docker-machine ssh swarm-agent0
    $ docker-machine ssh swarm-agent1

##Networking

In order to use the docker 1.9 networking capabilities we need to modify our docker-engine options:

    $ docker-machine ssh swarm-master
    $ sudo vi /etc/default/docker

Add the following options: 

    --cluster-store
    --cluster-advertise

Restart your docker engine with:

    $ sudo service docker restart

TODO: We should be able to provision this from the start with GCE startup-scripts.

From this point you can run docker-compose up -d from your laptop to see your cluster being populated with containers :-)



