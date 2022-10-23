import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dataFromDB(secretKeyJson):
    if not firebase_admin._apps:   # 初期済みでない場合は初期化処理を行う
        # 下のsecretKeyJsonはダウンロードした秘密鍵のパスを入れてください
        cred = credentials.Certificate(secretKeyJson)
        firebase_admin.initialize_app(cred) 
    db = firestore.client()
    doc_ref = db.collection("datas")
    docs = doc_ref.stream()

    date = []
    temperature = []
    humidity = []

    for doc in docs:
        dict = doc.to_dict() 
        date.append(dict["date"])
        temperature.append(dict["temperature"])
        humidity.append(dict["humidity"])
        
    data = {"date": date, 
            "temperature": temperature, 
            "humidity": humidity
            }
        #xsprint(data) 
        #Cloud Firestoreのtempcontrol-fd850/datas/にあるドキュメントのデータをドキュメントごとに配列でまとめた配列を返す

    return data