# from datetime import datetime, timedelta
# import requests
# from env import settings
# from sqlalchemy import Column, create_engine, Integer, String, Float, DateTime
# from sqlalchemy.orm import DeclarativeBase, sessionmaker

# host = settings.DATABASE_CONFIG['host']
# database = settings.DATABASE_CONFIG['database']
# user = settings.DATABASE_CONFIG['user']
# password = settings.DATABASE_CONFIG['password']
# port = settings.DATABASE_CONFIG['port']
# serviceKey = settings.DATABASE_CONFIG['serviceKey']
# api_end = settings.DATABASE_CONFIG['api_end']

# engine = create_engine("mysql+pymysql://{}:{}@{}/{}".format(user, password, host, database), echo=True)
# Session = sessionmaker(bind=engine)
# session = Session()

# date_data = datetime.today() - timedelta(1)
# date_str = date_data.strftime("%Y%m%d")

# class Base(DeclarativeBase):
#     pass


# class SnowData(Base):
#     __tablename__ = "data_entry"

#     pageNo = Column(Integer, primary_key=True)
#     stnIds = Column(String(255))
#     date = Column(DateTime)
#     ddMefs = Column(Float)
#     ddMes = Column(Float)
#     stnNm = Column(String(255))


# Base.metadata.create_all(engine)


# class SaveData(object):
#     def __init__(self):
#         self.url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
#         self.params = {
#             "serviceKey": serviceKey,
#             "pageNo": "1",
#             "numOfRows": "1",
#             "dataType": "JSON",
#             "dataCd": "ASOS",
#             "dateCd": "DAY",
#             "startDt": date_str,
#             "endDt": date_str,
#             "stnIds": "108",
#         }

#         response = requests.get(self.url, params=self.params)
#         self.data = response.json()

#         for item in self.data['response']['body']['items']['item']:
#             ddMes_str = item.get('ddMes')
#             ddMes = float(ddMes_str) if ddMes_str else 0.0

#             ddMefs_str = item.get('ddMefs')
#             ddMefs = float(ddMefs_str) if ddMefs_str else 0.0

#             stnNm = item.get('stnNm')

#             new_entry = SnowData(
#                 stnIds=item.get('stnId'),
#                 date=date_str,
#                 ddMes=ddMes,
#                 ddMefs=ddMefs,
#                 stnNm=stnNm
#             )
#             session.add(new_entry)
#         session.commit()
#         session.close()

#     def stnIds_num(api_end):
#         response = requests.get(api_end)
#         stnIds_num_datas = response.json()

#         stnIds_numbers = [num_data('stnIds_number') for num_data in stnIds_num_datas]

#         # return stnIds_numbers

#     def table_ins_data(self):
#         ddMes = self.data["response"]["body"]["items"]["item"][0]["ddMes"]
#         ddMefs = self.data["response"]["body"]["items"]["item"][0]["ddMefs"]
#         if ddMefs == '':
#             ddMefs = 0

#         if ddMes == '':
#             ddMes = 0


# if __name__ == "__main__":
#     save_data_obj = SaveData()
#     save_data_obj.table_ins_data()
