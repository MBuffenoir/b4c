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
Bitcoin-core API is used to orchestrate the escrow service.

##Front end
AngularJS creates a SPA relying on the API.

# License

MIT


