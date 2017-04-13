#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

from flask import Blueprint, request, jsonify, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import config
import math
from flask import current_app
import numpy as np
import scipy.misc as spy




def filter_raw(input_folder):
    with open(input_folder) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.split(' ') for x in content]
        result =[]
        for i in content:
            cnt = []
            for j in i:
                if j != '':
                    cnt.append(float(j))
            result.append(cnt[1:8])
        logger.info(result[767])
        with open('./data.json', 'w') as f:
            json.dump(result, f)

if __name__ == "__main__":

    filter_raw('./test.txt')

