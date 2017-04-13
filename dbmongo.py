from flask import Blueprint, request, jsonify, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
import config
import math
from flask import current_app
import numpy as np
import scipy.misc as spy
import derivatives

Race = -1
T1 =-1
T2 = -1
gender = ''

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('localhost:27017')
db = client.test_database

form_db = Blueprint('form_db',__name__)

# def ar_calculator(One_AR_RR,Race,T1,T2,gender):
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

def ar_calculator_derivative_r(One_AR_RR):
    One_ARxRR_r = One_AR_RR;
    One_ARxRR_p = One_AR_RR[1];
    One_ARxRR_d = One_AR_RR[2];

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

@form_db.route('/saveUserInfo',methods=['POST'])
def updateForm():
    try:
        json_data = request.json['info']
        current_app.logger.info(json_data)  # the jaon_data is 'dict'
        ### declear input variable ###
        global Race
        global T1
        global gender
        global T2
        # Race = -1
        # T1 =-1
        BMI_male = -1
        BMI_female = -1
        Veg = -1
        posi = [0,0,0,0]
        No_NSaids = -1
        hrs_Xrcise = 0
        interval = 0
        Rel_CRC = 0
        Rel_Trend = 0
        AbsRisk = [0,0,0]
        CI = [0,0,0]
        ModerXrcis = 0
        VigrXrcis = [0,0,0] #women
        No_Strogn = 0 #women
        BMI30YesStrgn = 0 #women
        No_IBupro = -1 #man
        Cigarets = 0 #man
        CigYr = [0,0,0,0] #man
        ### translate the form data into input ###
        if json_data['demographics']['hispanic'] == 3:
            Race = 3
        else:
            Race = json_data['demographics']['race']

        T1 = json_data['demographics']['age']

        height = json_data['demographics']['height_feet']*12 + json_data['demographics']['height_inches']
        weight = json_data['demographics']['weight']
        BMI = (weight/(height*height))*703

        if json_data['diet']['vegetables_serving'] <= 4:
            Veg = 1
        else:
            Veg = 0

        if json_data['medical_history']['colon_sigmo'] == -1:
            posi[json_data['medical_history']['polyp']] = 1
        else:
            posi[json_data['medical_history']['colon_sigmo']] = 1

        No_IBupro = json_data['medications']['NoIBuprofen']

        if No_IBupro == 0:
            No_NSaids = json_data['medications']['No_NSaids(IBuprofen)']
        else:
            No_NSaids = json_data['medications']['No_NSaids(NoIBuprofen)']

        if No_IBupro == -9:
            No_IBupro = 0
        if No_NSaids == -9:
            No_NSaids = 0

        if json_data['physical_activity']['vigorous_activity_months'] == 0:
            VigrXrcis[0] = 1
            if json_data['physical_activity']['moderate_activity_months'] == 0:
                hrs_Xrcise = 3
            else:
                tmp_hrs = json_data['physical_activity']['moderate_activity_hours']
                if tmp_hrs <= 2:
                    hrs_Xrcise = 2
                elif tmp_hrs <= 4:
                    hrs_Xrcise = 1
                else:
                    hrs_Xrcise = 0
        else:
            if json_data['physical_activity']['moderate_activity_months'] == 0:
                tmp_hrs = json_data['physical_activity']['vigorous_activity_hours']
                if tmp_hrs <= 2:
                    hrs_Xrcise = 2
                elif tmp_hrs <= 4:
                    hrs_Xrcise = 1
                else:
                    hrs_Xrcise = 0
            else:
                vig_temp = json_data['physical_activity']['vigorous_activity_hours']
                mod_temp = json_data['physical_activity']['moderate_activity_hours']
                if vig_temp <= 2:
                    VigrXrcis[1] = 1
                elif vig_temp <= 4:
                    VigrXrcis[2] = 1
                else:
                    pass
                tmp_hrs = vig_temp + mod_temp
                if tmp_hrs <= 2:
                    hrs_Xrcise = 2
                elif tmp_hrs <= 4:
                    hrs_Xrcise = 1
                else:
                    hrs_Xrcise = 0

        if json_data['family']['cancer_relatives'] == -1:
            if json_data['family']['num_cancer_relatives'] == 2:
                Rel_CRC = 1
                Rel_Trend = 2

            else: # -8 / 
                Rel_CRC = 1
                Rel_Trend = 1
        else:
            Rel_CRC = 0
            Rel_Trend = 0

        gender = json_data['demographics']['gender']
        #Rel_Trend
         ### male input only ###
        if gender == 'Male':
            if BMI <= 24.9:
                BMI_male = 0
            elif BMI <=29.9:
                BMI_male = 1
            else:
                BMI_male = 2

            if json_data['male_miscellaneous']['somke'] != -1:
                CigYr[0] = 1
                Cigarets = 0
            else:
                if json_data['male_miscellaneous']['start_time'] == 0:
                    CigYr[0] = 1
                    Cigarets = 0
                else:
                    Cigarets = json_data['male_miscellaneous']['Num_Cigs']
                    if json_data['male_miscellaneous']['current_smoke'] == 'yes':
                        interval = T1 - json_data['male_miscellaneous']['start_time']
                    else:
                        interval = json_data['male_miscellaneous']['time_quit'] - json_data['male_miscellaneous']['start_time']
                    if interval >= 35:
                        CigYr[2] = 1
                    elif interval >= 15:
                        CigYr[1] = 1
                    elif interval > 0:
                        CigYr[3] = 1
                    else:
                        CigYr = [0,0,0,0]

            # input_data = [Race,posi[0],posi[1],posi[2],No_IBupro,Rel_CRC,hrs_Xrcise,CigYr[0],CigYr[1],CigYr[2],Veg,Cigarets,BMI_male,posi[1],posi[2],posi[3],No_NSaids,Rel_Trend]
            input_data = [1,0,1,0,1,1,3,0,1,0,1,3,2,1,0,0,1,2]
            # input_data = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
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

            # derivative
            dAbsRsk_5 = derivatives.calculate_derivate(T1,T1+5,Race,gender,One_AR_RR)
            dAbsRsk_10 = derivatives.calculate_derivate(T1,T1+10,Race,gender,One_AR_RR)
            dAbsRsk_life = derivatives.calculate_derivate(T1,90,Race,gender,One_AR_RR)
            # partern_Indx
            sigmod = 0
            for i in posi:
                if i == 1:
                    break
                sigmod += 1
            Cig_Yr = 0
            if CigYr[0] == 1:
                Cig_Yr = 0
            if CigYr[1] == 1:
                Cig_Yr = 2
            if CigYr[2] == 1:
                Cig_Yr = 3
            if CigYr[3] == 1:
                Cig_Yr = 1
            Patrn_Indx = (Rel_Trend+1) + 3*Cigarets + 4*3*No_IBupro + 2*4*3*No_NSaids + 2*2*4*3*(sigmod) + 4*2*2*4*3*(BMI_male) + 3*4*2*2*4*3*(Veg) +  2*3*4*2*2*4*3*(Cig_Yr) + 4*2*3*4*2*2*4*3*(hrs_Xrcise)
            Cov = config.wrkCov_male[Patrn_Indx - 1]

            # wrkCov
            final_wrkCov_5 = dAbsRsk_5[0]*dAbsRsk_5[0]*Cov[0] + dAbsRsk_5[1]*dAbsRsk_5[1]*Cov[1] + 2*dAbsRsk_5[1]*dAbsRsk_5[2]*Cov[3] + dAbsRsk_5[2]*dAbsRsk_5[2]*Cov[2]
            CI[0] = CI_calculator(final_wrkCov_5,AbsRisk[0])

            final_wrkCov_10 = dAbsRsk_10[0]*dAbsRsk_10[0]*Cov[0] + dAbsRsk_10[1]*dAbsRsk_10[1]*Cov[1] + 2*dAbsRsk_10[1]*dAbsRsk_10[2]*Cov[3] + dAbsRsk_10[2]*dAbsRsk_10[2]*Cov[2]
            CI[1] = CI_calculator(final_wrkCov_10,AbsRisk[1])

            final_wrkCov_life = dAbsRsk_life[0]*dAbsRsk_life[0]*Cov[0] + dAbsRsk_life[1]*dAbsRsk_life[1]*Cov[1] + 2*dAbsRsk_life[1]*dAbsRsk_life[2]*Cov[3] + dAbsRsk_life[2]*dAbsRsk_life[2]*Cov[2]
            CI[2] = CI_calculator(final_wrkCov_life,AbsRisk[2])


        ### female input only ###
        if gender == 'Female':
            if BMI <= 30:
                BMI_female = 0
            else:
                BMI_female = 1

            if json_data['female_miscellaneous']['periods'] == -1:
                if json_data['female_miscellaneous']['last_period'] == -1:
                    No_Strogn = json_data['female_miscellaneous']['female_hormones']
                else:
                    No_Strogn = 0
            else:
                No_Strogn = 0

            BMI30YesStrgn = (BMI >= 30) * (1 - No_Strogn)


            # input_data = [Race,posi[0],posi[1],posi[2],No_Strogn,Rel_CRC,No_NSaids,VigrXrcis[0],VigrXrcis[1],VigrXrcis[2],BMI_female,hrs_Xrcise,Veg,No_NSaids,posi[1],posi[2],posi[3],No_Strogn,Rel_Trend,BMI_female,BMI30YesStrgn]
            input_data = [1,0,0,1,1,1,1,1,0,0,1,3,1,1,0,1,0,1,2,1,0]
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

            # derivative
            dAbsRsk_5 = derivatives.calculate_derivate(T1,T1+5,Race,gender,One_AR_RR)
            dAbsRsk_10 = derivatives.calculate_derivate(T1,T1+10,Race,gender,One_AR_RR)
            dAbsRsk_life = derivatives.calculate_derivate(T1,90,Race,gender,One_AR_RR)

            # partern_Indx
            sigmod = 0
            for i in posi:
                if i == 1:
                    break
                sigmod += 1
            Pattrn_ID  =  2*2*2*4*2*3*1*hrs_Xrcise + 2*2*4*2*3*1*No_Strogn + 2*4*2*3*1*Veg + 4*2*3*1*BMI_female + 2*3*1*sigmod + 3*1*No_NSaids + 1*Rel_Trend + 1*1
            Cov = config.wrkCov_female[Pattrn_ID - 1]
            # current_app.logger.info(Pattrn_ID)
            # current_app.logger.info(Cov)

            # wrkCov

        current_app.logger.info(AbsRisk)
        # current_app.logger.info(CI)


        return jsonify(status='OK',message='send to back_end successfully')
    except Exception as e:
        return str(e)

@form_db.route('/update',methods=['POST'])
def updateUser():
    try:
        user_data = request.json['info']
        # current_app.logger.info(user_data)
        # current_app.logger.info(session['id'])
        age = user_data['age']
        phoneNum = user_data['phone']
        email = user_data['email']
        fname = user_data['fname']
        lname = user_data['lname']
        userId = session['id']
        current_app.logger.info(userId)
        if db.testUser.find_one({'id' : userId}) != None:
            current_app.logger.info("find it")
            db.testUser.update_one({'id': userId},{'$set':{'fname':fname,'lname':lname,'email':email,'age':age,'phone':phoneNum}})
        else:
            current_app.logger.info("insert it")
            db.testUser.insert_one(
                {
                'id': userId,
                'fname': fname,
                'lname':lname,
                'email':email,
                'age':age,
                'phone':phoneNum
                })
        return jsonify(status='OK',message='update successfully')
    except Exception as e:
        return jsonify(status='ERROR',message=str(e))
@form_db.route('/getUserInfo',methods=['GET'])
def sendUserInfo():
    try:
        if db.testUser.find_one({'id' : session['id']}) != None:
            data = db.testUser.find_one({'id': session['id']})
            current_app.logger.info(data)
            #return jsonify(status='OK',message=JSONEncoder().encode(data))
            return JSONEncoder().encode(data)
        else:
            return jsonify(status='ERROR',message='update failed')
        # db.testUser.drop()
    except Exception as e:
        return str(e)