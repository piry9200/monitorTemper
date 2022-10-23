import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def dateToDB(secretKeyJson, date, temperature, humidity):
    if not firebase_admin._apps:   # 初期済みでない場合は初期化処理を行う
        # 下のsecretKeyJsonはダウンロードした秘密鍵のパスを入れてください
        cred = credentials.Certificate(secretKeyJson)
        firebase_admin.initialize_app(cred) 
        
    db = firestore.client()
    doc_ref = db.collection("datas").document(date)
    doc_ref.set({
        'date': date,
        'temperature': temperature,
        'humidity':humidity
    }
)
