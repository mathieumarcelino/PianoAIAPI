# app.py - a minimal flask api using flask_restful
from gevent import monkey
monkey.patch_all()

import tflearn
import pickle
import os

os.environ['TMPDIR'] = '/home/mathieu/tmp'

from tflearn.data_utils import *

from threading import Thread
from threading import Lock
from queue import Queue

from flask import Flask, jsonify
from gevent import pywsgi
from flask_restful import Resource, Api
from flask_cors import CORS
from flask import Response
from flask import request

app = Flask(__name__)
app.config.update(
        TESTING=False,
        DEBUG=False,
        ENV='production')
api = Api(app)
CORS(app)

maxlen = 25

class ModelLoader:
    _base = None
    _char_idx = None
    _g = None
    _m = None
    _thread = None
    _inputQueue = Queue()
    _outputQueue = Queue()
    _queueLock = Lock()
    _isStopped = False

    def __init__(self, name):
        self._thread = Thread(name=self._base, target=self.thread_run)
        self._base = name
        self._thread.start()

    def thread_run(self):
        self._base = self._base
        print("loading "+"char_idx_"+self._base+".pickle")
        self._char_idx = pickle.load(open("model/"+self._base+"/char_idx_"+self._base+".pickle", 'rb'))
        print("loading "+self._base+".txt")
        # _,_,self._char_idx = textfile_to_semi_redundant_sequences(self._base+".txt", seq_maxlen=maxlen, redun_step=3, pre_defined_char_idx=self._char_idx)
        self._g = tflearn.input_data([None, maxlen, len(self._char_idx)])
        self._g = tflearn.lstm(self._g, 512, return_seq=True)
        self._g = tflearn.dropout(self._g, 0.5)
        self._g = tflearn.lstm(self._g, 512, return_seq=True)
        self._g = tflearn.dropout(self._g, 0.5)
        self._g = tflearn.lstm(self._g, 512)
        self._g = tflearn.dropout(self._g, 0.5)
        self._g = tflearn.fully_connected(self._g, len(self._char_idx), activation='softmax')
        self._g = tflearn.regression(self._g, optimizer='adam', loss='categorical_crossentropy', learning_rate=0.001)
        self._m = tflearn.SequenceGenerator(self._g, dictionary=self._char_idx,
                                      seq_maxlen=maxlen,
                                      clip_gradients=5.0,
                                      checkpoint_path="model/"+self._base+"/model_"+self._base)
        print("Loading "+"model/"+self._base+"/"+self._base+'.tfl')
        self._m.load("model/"+self._base+"/"+self._base+'.tfl')
        while not self._isStopped:
            data = self._inputQueue.get()
            self._queueLock.acquire(blocking=True)

    def fstring(self,seed=''):
        rand = " " + random_sequence_from_textfile("model/"+self._base+".txt", maxlen)
        s = '{:25.25}'.format(seed + rand)
        print("using seed\n"+s)
        return s

    def generate(self,seed, size=100, temperature=0.5):
        return self._m.generate(size, temperature, seq_seed=self.fstring(seed))


modelMusic = ModelLoader('music')

# m.fit(X, Y, validation_set=0.1, batch_size=128, n_epoch=1, run_id='contes')

@app.route('/music/g/<seed>/<size>/<temp>')
def cgentemp(seed=None, size=None, temp=None):
    try:
        s = int(size)
    except ValueError:
        s = 100
    try:
        t = float(temp)
    except ValueError:
        t = 0.5
    return modelMusic.generate(seed,s,t)

if __name__ == '__main__':
    from gunicorn.app.wsgiapp import run
    run()
