from flask import Blueprint, request, jsonify, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from flask import current_app

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

client = MongoClient('localhost:27017')
db = client.test_database

form_db = Blueprint('form_db',__name__)

@form_db.route('/saveUserInfo',methods=['POST'])
def updateForm():
    try:
        json_data = request.json['info']
        current_app.logger.info(json_data)
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