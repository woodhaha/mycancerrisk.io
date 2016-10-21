from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from flask import current_app

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
        current_app.logger.info(user_data)
        return jsonify(status='OK',message='get user Info')
    except Exception as e:
        return str(e)