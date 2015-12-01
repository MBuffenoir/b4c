#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os, drest
from __future__ import print_function

# To debug one can do in his shell: 
# export DREST_DEBUG=1
# You need to specify an api key with:
# export APIKEY='your_api_key'

class BlizzardApi:

    def __init__(self, apikey, region='eu'):
        self.baseurl = 'https://%s.api.battle.net' % region
        self.apikey  = apikey

    def get_player_profile(self, id, name):
        """
        return user battle.net sc2 profile
        :param id: an integer, the user's id
        :param name: a string, the user's name
        :parem region: a string, the user region
        """

        self.api = drest.api.API(self.baseurl, ignore_ssl_validation=False, trailing_slash=True)

        try:
            r = self.api.make_request('GET', '/sc2/profile/%s/1/%s/' %(id,name), params=dict(locale='en_GB', apikey=self.apikey))
            if r.status != 200 and r.status != 201:
                return False
            return r.data
        except Exception as e:
            print('unable to connect to Blizzard Api: ' + e)
            return False

    def get_player_match_history(self, id, name):
        """
        return user battle.net last matches
        """

        self.api = drest.api.API(self.baseurl, ignore_ssl_validation=False, trailing_slash=False)

        try:
            r = self.api.make_request('GET', '/sc2/profile/%s/1/%s/matches' %(id,name), params=dict(apikey=self.apikey, locale='en_GB'))        
            print(r.status)
            if r.status != 200 and r.status != 201:
                return False
            return r.data
        except Exception as e:
            print('unable to connect to Blizzard Api: ' + e)
            return False

    def get_player_ladders(self, id, name):
        """
        return user battle.net current ladders infos
        """

        self.api = drest.api.API(self.baseurl, ignore_ssl_validation=False, trailing_slash=False)

        try:
            r = self.api.make_request('GET', '/sc2/profile/%s/1/%s/matches/ladders' %(id,name), params=dict(locale='en_GB', apikey=self.apikey))
            if r.status != 200 and r.status != 201:
                return False
            return r.data
        except Exception as e:
            print('unable to connect to Blizzard Api: ' + e)
            return False


# exemples

# B = BlizzardApi(os.environ['APIKEY'])

# result = B.get_player_profile(241726, 'LaLu')

# print(result)

# result = B.get_player_match_history(241726, 'LaLu')

# print(result)

# result = B.get_player_ladders(241726, 'LaLu')

# print(result)