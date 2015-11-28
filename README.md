#Description 

Battle 4 coins (B4C) is a bitcoins monetized starcraft II match platform. It could easily be extended to any Blizzard Game and further on to any (video or not) game ...
Users can link a Starcraft 2 player profile to their account.

Match are proposed by the players themselves. They define how much bitcoins they engage in the match pot and the winner takes it all.

The platform propose an escrow service to solve eventual disputes. It uses blizzard API to check the match history of the players [https://dev.battle.net/io-docs].

All matches are free to enter.

#Tech stack

##Back end
Django (+ tastypie eventually) is used to create a public API and an admin interface.
Crossbar will provide real-time communications.

##Front end
Django templating + autobahn library or AngularJS creates a SPA relying on the API.

# General worflow

### Players profile

- Starcraft id + name to be able to be located by opponent on the inGame chat system
- Pot address
- Receiving bitcoin address
- Race, level, portrait ... (all SC related goodies, see blizzard api result for details)
- Number of games played
- Lost dispute number (updated by the site admin) -> A user with many games played and a low lost dispute should be a reliable opponent.

### Matches

A match is proposed by a registered player. Anyone can propose to be a challenger, the creator of the match review the profile of his proposed opponents and pick one (if there is more than one). Players must agree on a time to play the games (approximation).

We must implement a search engine for player to look for games they are interested in (by pot size, by league, by opponent name, etc ...)

As of now, disconnection will be treated as a game loss !

- Matches can have the following status: open / pending / cancelled / finished

Once 2 opponents are matched:

- A new private / pubkey is generated server side (from a master BIP44 seed)
- A 2 of 3 multisig address is generated using: server-side address, players 1 pot address, player 2 pot address.
- Each player must send the pot amount to the multisig address (so if proposed pot is of 50mBTC each player sends 50 mBTC)
- Each player receive a transaction they must sign and upload (Electrum > Load Transaction > sign). This will be used to send them coins once the match winner is decided.
- They must add each other as Friend in Game and play their match according to the conditions chosen (Best of 3, 5 ,7).
- The match starts once each players click on startmatch button

Once the match has been played and the winner is known.

- server fetch match history from bizzard API and set the winner of the match.
- server sign a tx to the winner receiving address of choice
- server broadcast tx

### Useful links & softwares

+ Bitcore
+ Electrum
+ Bitcoin-core
+ [https://coinb.in/]

# License

MIT


