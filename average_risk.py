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
Race = 0
T1 = 0
gender = ''
T2 = 0
def ar_calculator(One_AR_RR):
    One_ARxRR_r = One_AR_RR[0]
    One_ARxRR_p = One_AR_RR[1]
    One_ARxRR_d = One_AR_RR[2]

    race = ['white','black','hispanic','asian']
    Strt_j      = T1 - 49;
    End_j       = T2 - 50;

    AbsRsk_5        = 0
    AbsRsk_10        = 0
    AbsRsk_life      = 0
    AbsRsk           = 0
    S_j_1       = 1

    jth         = Strt_j

    while jth <= End_j:
        index = math.floor((jth-1)/5)
        Rect_H1 = config.Hazrd[gender]["Rect_H1"][race[Race-1]][index]
        Prxm_H1 = config.Hazrd[gender]["Prxm_H1"][race[Race-1]][index]
        Dist_H1 = config.Hazrd[gender]["Dist_H1"][race[Race-1]][index]
        H2 = config.Hazrd[gender]["H2"][race[Race-1]][index]
        SumHaz = One_ARxRR_r * Rect_H1 + One_ARxRR_p * Prxm_H1 + One_ARxRR_d * Dist_H1
        Surv_This = math.exp(- SumHaz - H2)
        AbsRsk    = AbsRsk + (SumHaz/(SumHaz+H2))*(1-Surv_This)*S_j_1
        S_j_1     = S_j_1*Surv_This
        jth       = jth + 1

    return AbsRsk

def ABSRisk_male(input_data):
    global Race
    global T1
    global gender
    global T2

    AbsRisk = [0,0,0]
    Xstar_r = input_data[1:7]
    Xstar_p = input_data[7:18]
    Xstar_d = input_data[12:18]
    RR = [0,0,0]
    for i in range(6):
        RR[0] += Xstar_r[i] * config.man_Rect_Beta[i]
        RR[2] += Xstar_d[i] * config.man_Dist_Beta[i]
    for j in range(11):
        RR[1] += Xstar_p[j] * config.man_Prxm_Beta[j]
    for k in range(3):
        RR[k] = math.exp(RR[k])
    One_AR_RR = [0,0,0]
    for m in range(3):
        One_AR_RR[m] = RR[m] * config.male_One_AR[m]

    # AbsRisk
    T2 = T1 + 5
    AbsRisk[0] = ar_calculator(One_AR_RR)
    T2 = T1 + 10
    AbsRisk[1] = ar_calculator(One_AR_RR)
    T2 = 90
    AbsRisk[2] = ar_calculator(One_AR_RR)

    return AbsRisk

def ABSRisk_female(input_data):
    global Race
    global T1
    global gender
    global T2

    AbsRisk = [0,0,0]
    Xstar_r = input_data[1:11]
    Xstar_p = input_data[11:19]
    Xstar_d = input_data[13:21]
    RR = [0,0,0]
    for i in range(8):
        RR[1] += Xstar_p[i] * config.feman_Prxm_Beta[i]
        RR[2] += Xstar_d[i] * config.feman_Dist_Beta[i]
    for j in range(10):
        RR[0] += Xstar_r[j] * config.feman_Rect_Beta[j]
    for k in range(3):
        RR[k] = math.exp(RR[k])
    One_AR_RR = [0,0,0]
    if T1 < 65:
        for m in range(3):
            One_AR_RR[m] = RR[m] * config.femal_One_AR_l65[m]
    else:
        for m in range(3):
            One_AR_RR[m] = RR[m] * config.femal_One_AR_g65[m]

    # AbsRisk
    T2 = T1 + 5
    AbsRisk[0] = ar_calculator(One_AR_RR)
    T2 = T1 + 10
    AbsRisk[1] = ar_calculator(One_AR_RR)
    T2 = 90
    AbsRisk[2] = ar_calculator(One_AR_RR)

    return AbsRisk


if __name__ == "__main__":
    # input_data[0] is Race, range from 1 to 4
    race = ['white','black','hispanic','asian']

    input_data = np.zeros((100,21),dtype=np.int)
    gender = "Female"
    logger.info("Female")
    ABR = np.zeros((3),dtype=np.int)
    for i in range(50,76):
        T1 = i
        for r in range(4):
            ABR_5 = 0
            ABR_10 = 0
            ABR_life = 0
            Race = r
            for j in range(100): # each case of 100 input data
                input_data[j][0] = r
            for a in range(100): # Posi 0,1,2,3
                if a < 27:
                    input_data[a][1] = 1
                elif a <= 33:
                    input_data[a][3] = 1
                    input_data[a][15] = 1
                else:
                    input_data[a][2] = 1
                    input_data[a][14] = 1
            for b in range(48): #  No strogn
                input_data[b][4] = 1
                input_data[b][17] = 1
            for c in range(100): # rel
                if c < 89:
                    input_data[c][5] = 0
                    input_data[c][18] = 0
                elif c < 99:
                    input_data[c][5] = 1
                    input_data[c][18] = 1
                else:
                    input_data[c][5] = 1
                    input_data[c][18] = 2
            for d in range(59): # no_said
                input_data[d][6] = 1
                input_data[d][13] = 1
            for e in range(100): # exercise
                if e < 17:
                    input_data[e][11] = 0
                elif e < 54:
                    input_data[e][11] = 1
                    input_data[e][9] = 1
                elif e < 63:
                    input_data[e][11] = 2
                    input_data[e][8] = 1
                else:
                    input_data[e][11] = 3
                    input_data[e][7] = 1
            for f in range(22): # BMI
                input_data[f][10] = 1
                input_data[f][19] = 1
            for g in range(88): # veg
                input_data[g][12] = 1
            for h in range(100): # BMI30YesStrgn
                input_data[h][20] = input_data[h][10] * input_data[h][4]
            for k in range(100): # calculate all
                ABR = ABSRisk_female(input_data[k])
                ABR_5 += ABR[0]
                ABR_10 += ABR[1]
                ABR_life += ABR[2]
            logger.info("Age:" + str(i))
            logger.info("Race:" + race[Race])
            logger.info(ABR_5/100)
            logger.info(ABR_10/100)
            logger.info(ABR_life/100)

    input_data = np.zeros((100,18),dtype=np.int)
    gender = "Male"
    logger.info("Male")
    ABR = np.zeros((3),dtype=np.int)
    for i in range(50,76):
        T1 = i
        for r in range(4):
            ABR_5 = 0
            ABR_10 = 0
            ABR_life = 0
            Race = r
            for j in range(100): # each case of 100 input data
                input_data[j][0] = r
            for a in range(100): # Posi 0,1,2,3
                if a < 43:
                    input_data[a][1] = 1
                elif a < 55:
                    input_data[a][3] = 1
                    input_data[a][14] = 1
                else:
                    input_data[a][2] = 1
                    input_data[a][13] = 1
            for b in range(52): #  No Bulofn
                input_data[b][4] = 1
            for c in range(100): # rel
                if c < 91:
                    input_data[c][5] = 0
                    input_data[c][17] = 0
                elif c < 99:
                    input_data[c][5] = 1
                    input_data[c][17] = 1
                else:
                    input_data[c][5] = 1
                    input_data[c][17] = 2
            for d in range(100): # exercise
                if d < 22:
                    input_data[d][6] = 0
                elif d < 37:
                    input_data[d][6] = 1
                elif d < 73:
                    input_data[d][6] = 2
                else:
                    input_data[d][6] = 3
            for e in range(100): # ci_year
                input_data[e][8] = 1
            for f in range(91): # veg
                input_data[f][10] = 1
            for g in range(100): # cigs/d
                if g < 29:
                    input_data[g][11] = 0
                elif g < 43:
                    input_data[g][11] = 1
                elif g < 65:
                    input_data[g][11] = 2
                else:
                    input_data[g][11] = 3
            for h in range(100): # BMI
                if h < 31:
                    input_data[h][12] = 0
                elif h < 80:
                    input_data[h][12] = 1
                else:
                    input_data[h][12] = 2
            for l in range(52): # no_said
                input_data[l][16] = 1
            for k in range(100): # calculate all
                ABR = ABSRisk_male(input_data[k])
                ABR_5 += ABR[0]
                ABR_10 += ABR[1]
                ABR_life += ABR[2]
            logger.info("Age:" + str(T1))
            logger.info("Race:" + race[Race])
            logger.info(ABR_5/100)
            logger.info(ABR_10/100)
            logger.info(ABR_life/100)

    # logger.info(input_data)
    # logger.info(input_data[7])


