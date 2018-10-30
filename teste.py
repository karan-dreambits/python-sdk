#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../lib')
from lib.meli import Meli

_acccess_token = 'APP_USR-0000000000000000-103006-sdklhsuioghksjfghksjhgklzjgklsflbkjhslgslbjspfvpsfjlsjglksfjblsglj-000000000'

meli = Meli(client_id=0000000000000000, client_secret="1234567890abcdefghijklmnopqrst")

print("meli-> {0}".format(meli))
print("meli.dir-> {0}".format(dir(meli)))
print("meli.client_id-> {0}".format(meli.client_id))
print("meli.client_secret-> {0}".format(meli.client_secret))
print("meli.expires_in-> {0}".format(meli.expires_in))
print("meli.access_token-> {0}".format(meli.access_token))
print("meli.AUTH_URL-> {0}".format(meli.AUTH_URL))
print("meli.API_ROOT_URL-> {0}".format(meli.API_ROOT_URL))
print()
# print("meli.make_path()-> {0}".format(meli.make_path()))
# print("meli.options()-> {0}".format(meli.options()))
# print("meli.auth_url()-> {0}".format(meli.auth_url()))

user_me = meli.get('users/me',params={'access_token':_acccess_token})

print()
print("user_me reponse_code-> {0}".format(user_me))
print("user_me content-> {0}".format(user_me.content))
print("user_me text-> {0}".format(user_me.text))

item = meli.getItemByID('MLB1075298550')
print("item reponse_code-> {0}".format(item))
print("item content-> {0}".format(item.content))
