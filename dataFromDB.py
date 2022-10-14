import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dataFromDB():
    # 下のファイルは先程ダウンロードした秘密鍵のパスを入れてください
    cred = credentials.Certificate("./tempcontrol-fd850-firebase-adminsdk-f43jn-fe3be151b4.json")
    firebase_admin.initialize_app(cred) 
    db = firestore.client()

    doc_ref = db.collection("datas")
    docs = doc_ref.stream()

    date = []
    temperature = []
    humidity = []

    for doc in docs:
        dict = doc.to_dict() 
        date.append(dict["data"][0])
        temperature.append(dict["data"][1])
        humidity.append(dict["data"][2])

    data = [date, temperature, humidity]
    print(data) 
    #Cloud Firestoreのtempcontrol-fd850/datas/にあるドキュメントのデータをドキュメントごとに配列でまとめた配列を返す
    return data

dataFromDB()