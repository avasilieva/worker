#!/bin/usr/env python

import redis, os


path = os.environ["REDISPATH"]
password = os.environ["PASS"]

host, port = path.split(":")

r = redis.StrictRedis(host=host, port=port, db=0, password=password)

while( True ):
  key = r.randomkey()
  print(key, r.get(key))
  r.delete(key)
end

