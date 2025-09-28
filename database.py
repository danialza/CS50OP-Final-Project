import firebase_admin
from firebase_admin import credentials,firestore
from project import get_data

cred = credentials.Certificate("myexpenses-e895a-firebase-adminsdk-fbsvc-785f9e567f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

get_data_info = get_data()
data_to_database = db.collection("my_expenses").add(get_data_info)
print(f"\n✅ Data successfully added to Firebase with Document ID: {data_to_database[1].id}")

# data_to_table = data_to_database.document()
# data_to_table.set(get_data())


# testdata = {
#     "num":"1",
#     "name":"danial",
#     "last_name":"Za"
# }

# mydata_to_firebase = db.collection("mydata").document("First User").set(testdata)


# read_data = db.collection("cities")
# datasss = read_data.stream()
# data_khas = read_data.document("LA").get()
# print(data_khas.to_dict())

# for data in datasss:
#     print(f"{data.id} is {data.to_dict()}")
