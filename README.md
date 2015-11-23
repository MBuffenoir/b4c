#Description 

Battle 4 coins (B4C) is a bitcoins monetized starcraft II match platform.
Users can register and link a Starcraft 2 player profile to their account.

Match are proposed by the players themselves. They define how much bitcoins they engage in the match and the winner takes it all.

The platform propose an escrow service to solve eventual disputes. We use blizzard API to check the match history of the players [https://dev.battle.net/io-docs].

All matches are free to enter.

Revenue can be generated from ads, streams and sponsors. TBD.

#Tech stack

##Back end
Django (+ tastypie eventually) is used to create a public API and an admin interface.
Crossbar will provide real-time communications.

##Front end
Django templating + autobahn library or AngularJS creates a SPA relying on the API.

# License

MIT


