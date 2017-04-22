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



def CI_calculator(Var_Pi,AbsRsk):
    #variance and 95 CI of ln odds @
    lnOdds      = math.log(AbsRsk/(1-AbsRsk))
    Var_lnOdds  = Var_Pi * (1/math.pow(AbsRsk*(1-AbsRsk),2))
    SE_lnOdds   = math.sqrt(Var_lnOdds)
    CILlnOdds   = lnOdds - 1.96*SE_lnOdds
    CIUlnOdds   = lnOdds + 1.96*SE_lnOdds

    CIL         = math.exp(CILlnOdds)/(1+math.exp(CILlnOdds))
    CIU         = math.exp(CIUlnOdds)/(1+math.exp(CIUlnOdds))

    return [CIL,CIU]

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

def filter_average_risk(input_folder,result):
    # logger.info(result)
    race = ['white','black','hispanic','asian']
    with open(input_folder) as f:
        content = f.read().splitlines()
        n = 0
        temp1=[]
        temp2=[]
        for i in content:
            n += 1
            temp1.append(i)
            if (n % 20) == 0:
                temp2.append(temp1)
                temp1 = []
        # logger.info(temp2[0])
        for j in range(26):
            for k in range(4):
                if k == 0:
                    result['female'][str(j+50)][race[k]] = [temp2[j][2],temp2[j][3],temp2[j][4]]
                if k == 1:
                    result['female'][str(j+50)][race[k]] = [temp2[j][7],temp2[j][8],temp2[j][9]]
                if k == 2:
                    result['female'][str(j+50)][race[k]] = [temp2[j][12],temp2[j][13],temp2[j][14]]
                if k == 3:
                    result['female'][str(j+50)][race[k]] = [temp2[j][17],temp2[j][18],temp2[j][19]]
        for j in range(26,52):
            for k in range(4):
                if k == 0:
                    result['male'][str(j+24)][race[k]] = [temp2[j][2],temp2[j][3],temp2[j][4]]
                if k == 1:
                    result['male'][str(j+24)][race[k]] = [temp2[j][7],temp2[j][8],temp2[j][9]]
                if k == 2:
                    result['male'][str(j+24)][race[k]] = [temp2[j][12],temp2[j][13],temp2[j][14]]
                if k == 3:
                    result['male'][str(j+24)][race[k]] = [temp2[j][17],temp2[j][18],temp2[j][19]]
        with open('./data.json', 'w') as f:
            json.dump(result, f)

if __name__ == "__main__":

    result = {}
    gender = ['male', "female"]
    for i in gender:
        result[i] = {}
        for j in range(50,76):
            result[i][str(j)] = {"white" : [0,0,0],"black" : [0,0,0],"hispanic" : [0,0,0],"asian" : [0,0,0]}
    filter_average_risk('./average_risk.text',result)

        ## CI for women
    # Cov =[4.546208144002, 4.130158086161, 5.266894654875, 3.323549274533, 1.754735743591, 1.431805476943, 4.047989544533]
    # AbsRsk = 0.025101503408076736
    # dAbsRsk_10 = np.array([[0.0016340398582836979, 0.0016990335180433469, 0.0014384855147320241]])
    # dAbsRsk_10_T = np.transpose(dAbsRsk_10)
    # array = [0,0,0,0,0,0,0,0,0]
    # for i in range(6):
    #     array[0] = Cov[i]
    #     for j in range(6):
    #         if j == i:
    #             continue
    #         array[1] = Cov[j]
    #         array[3] = Cov[j]
    #         for k in range(6):
    #             if k == j:
    #                 continue
    #             if k == i:
    #                 continue
    #             array[4] = Cov[k]
    #             for l in range(6):
    #                 if l == i:
    #                     continue
    #                 if l == j:
    #                     continue
    #                 if l == k:
    #                     continue
    #                 array[6] = Cov[l]
    #                 array[2] = Cov[l]
    #                 for m in range(6):
    #                     if m == i:
    #                         continue
    #                     if m == j:
    #                         continue
    #                     if m == k:
    #                         continue
    #                     if m == l:
    #                         continue
    #                     array[5] = Cov[m]
    #                     array[7] = Cov[m]
    #                     for n in range(6):
    #                         if n == i:
    #                             continue
    #                         if n == j:
    #                             continue
    #                         if n == k:
    #                             continue
    #                         if n == l:
    #                             continue
    #                         if n == m:
    #                             continue
    #                         array[8] = Cov[n]
    #                         # cnt += 1
    #                         Cov_array = np.array([[array[0],array[1],array[2]],[array[3],array[4],array[5]],[array[6],array[7],array[8]]])
    #                         final_wrkCov_10 = np.dot(dAbsRsk_10, Cov_array)
    #                         final_wrkCov_10_final = np.dot(final_wrkCov_10, dAbsRsk_10_T)
    #                         CI = CI_calculator(final_wrkCov_10_final,AbsRsk)
    #                         logger.info(CI)



