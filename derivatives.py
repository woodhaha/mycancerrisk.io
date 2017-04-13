#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

import config
import math
from flask import current_app
import scipy.misc as spy


T1 = 0
T2 = 0
Race = 0
gender = ''
One_ARxRR_r = 0
One_ARxRR_p = 0
One_ARxRR_d = 0

def ar_calculator_r(One_AR_RR):
    One_ARxRR_r = One_AR_RR

    race = ['white','black','hispanic','asian']
    Strt_j      = T1 - 49;
    End_j       = T2 - 50;

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

def ar_calculator_p(One_AR_RR):
    One_ARxRR_p = One_AR_RR

    race = ['white','black','hispanic','asian']
    Strt_j      = T1 - 49;
    End_j       = T2 - 50;

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

def ar_calculator_d(One_AR_RR):
    One_ARxRR_d = One_AR_RR

    race = ['white','black','hispanic','asian']
    Strt_j      = T1 - 49;
    End_j       = T2 - 50;

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

def calculate_derivate(t1,t2,race,sex,One_AR_RR):
    global T1
    global T2
    global Race
    global gender
    global One_ARxRR_r
    global One_ARxRR_p
    global One_ARxRR_d

    T1 = t1
    T2 = t2
    Race = race
    gender = sex
    dAbsRsk = [0,0,0]

    One_ARxRR_p = One_AR_RR[1]
    One_ARxRR_d = One_AR_RR[2]
    One_AR_RR_r = One_AR_RR[0]
    dAbsRsk[0] = spy.derivative(ar_calculator_r, One_AR_RR_r, dx = 1e-6)

    One_ARxRR_r = One_AR_RR[0]
    One_ARxRR_d = One_AR_RR[2]
    One_AR_RR_p = One_AR_RR[1]
    dAbsRsk[1] = spy.derivative(ar_calculator_p, One_AR_RR_p, dx = 1e-6)

    One_ARxRR_r = One_AR_RR[0]
    One_ARxRR_p = One_AR_RR[1]
    One_AR_RR_d = One_AR_RR[2]
    dAbsRsk[2] = spy.derivative(ar_calculator_d, One_AR_RR_d, dx = 1e-6)

    return dAbsRsk
