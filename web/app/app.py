
import os
import socket
import uuid
from flask import request
from flask import Flask
from redis import Redis
from flask import jsonify
import json
import ast
import threading
import logging
import time
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)
app = Flask(__name__)
redis = Redis(host=os.environ.get('REDIS_HOST', 'redis'), port=6379)
@app.route('/')
def hostnameprint():
    redis.incr('hits')
    return '%s.\n' % (socket.gethostname())

@app.route('/counter/<uuid>',methods = ['GET'])
def counterget(uuid):

    return json.dumps(redis.hgetall(str(uuid).encode('ascii', 'ignore')))+ "\n"

@app.route('/counter/<uuid>/stop',methods = ['POST'])
def counterstop(uuid):
    currentVal = redis.hgetall(str(uuid))
    redis.delete(str(uuid))
    redis.lrem('counter-list',1, str(uuid))
    return "deleted "+str(uuid)+ " \n"


def incrementCounter(lock,uuid):
    while True:
        with lock:
            #logging.debug('Lock acquired')
            currentVal = redis.hgetall(str(uuid))
            if 'current' in currentVal and 'to' in currentVal:
                if int(currentVal['current'])+1 <= int(currentVal['to']):
                    redis.hmset(uuid,{"current":int(currentVal['current'])+1,"to":int(currentVal['to'])})
                else:
                    redis.delete(str(uuid))
                    redis.lrem('counter-list',1, str(uuid))
                    break
            else:
                break
        time.sleep(1)


def remove_uni(s):
    """remove the leading unicode designator from a string"""
    s2 = s
    if s.startswith("u'"):
        s2 = s.replace("u'", "'", 1)
    elif s.startswith('u"'):
        s2 = s.replace('u"', '"', 1)
    return s2

@app.route('/counter/',methods = ['POST','GET'])
def counterpost():
    counterlist = []
    if request.method == 'POST':
        uuid.uuid4()
        to = request.form.get('to')
        uuidval = str(uuid.uuid4())
        redis.hmset(uuidval,{"current":0,"to":int(to)})
        redis.rpush('counter-list',uuidval)
        lock = threading.Lock()
        w = threading.Thread(target=incrementCounter, args=(lock,uuidval))
        w.start()
        return  uuidval +"\n"
    else:
        for i,v in enumerate(redis.lrange( "counter-list", 0, -1 )):
            counterlist.append(remove_uni(str(v)))
        return jsonify(result=counterlist)
