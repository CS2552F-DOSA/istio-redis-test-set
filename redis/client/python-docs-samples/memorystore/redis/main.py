# Copyright 2018 Google Inc.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# [START memorystore_main_py]

# # Part 1 counter test
# With this part, curl localhost will get the counter result.
# import logging
# import os

# from flask import Flask
# import redis

# app = Flask(__name__)

# # redis_host = os.environ.get('REDISHOST', 'localhost')
# # redis_port = int(os.environ.get('REDISPORT', 6379))
# # redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

# redis_host = "redis"
# redis_port = "6379"
# redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

# @app.route('/')
# def index():
#     value = redis_client.incr('counter', 1)
#     return 'Visitor number: {}'.format(value)


# @app.errorhandler(500)
# def server_error(e):
#     logging.exception('An error occurred during a request.')
#     return """
#     An internal error occurred: <pre>{}</pre>
#     See logs for full stacktrace.
#     """.format(e), 500


# if __name__ == '__main__':
#     # This is used when running locally. Gunicorn is used to run the
#     # application on Google App Engine. See entrypoint in app.yaml.
#     app.run(host='127.0.0.1', port=8080, debug=True)

# [END memorystore_main_py]


# Part 2 normal access for redis
# Simple test for redis write and read.
# Two options: normal redis client and asyncio-redis

REDIS_HOST = "redis"
REDIS_TEST_HOST = "redis-test"

REDIS_PORT = "6379"
REDIS_TEST_PORT = "6379"

# Normal redis client
# Referring to https://redislabs.com/lp/python-redis/

import redis
import os
import time

# HOST = os.getenv('CLIENT_PROXY', "http://localhost:9001")

print("\n************* client begin *************\n")

r = redis.Redis(
    host= REDIS_HOST,
    port= REDIS_PORT)
print("set foo in redis, foo -> bar redis")
r.set('foo', 'bar redis')
value = r.get('foo')
print("getted value for foo in redis: ", value)
print("\n\n")

r_test = redis.Redis(
    host= REDIS_TEST_HOST,
    port= REDIS_TEST_PORT)
print("set foo in redis-test, foo -> bar redis-test")
r_test.set('foo', 'bar redis-test')
value = r_test.get('foo')
print("getted value for foo in redis: ", value)



print("\n************* client end *************\n")
time.sleep(3)