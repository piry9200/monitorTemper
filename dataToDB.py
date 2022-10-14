import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dateToDB(date, temperature, humidity):

    # 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
    cred = credentials.Certificate("./tempcontrol-fd850-firebase-adminsdk-f43jn-fe3be151b4.json")
    firebase_admin.initialize_app(cred) 
    db = firestore.client()

    doc_ref = db.collection("datas").document(date)
    doc_ref.set( { "data": [date, temperature, humidity]})

dateToDB("tommorrow", 25, 70)
