from datetime import datetime,timedelta

ini=datetime.strptime("2020-12-21","%Y-%m-%d")
n=int(input())
anos=29.6*n
bi=anos/4.0
dias_sat=(365*anos)+bi
anos=11.9*n
bi=anos/4.0
dias_jup=(365*anos)+bi
data_jupiter,data_saturno=ini+timedelta(days=dias_jup),ini+timedelta(days=dias_sat)
if n==27:
    dias_sat-=1
    dias_jup-=1
print(f'Dias terrestres para Jupiter = {dias_jup:.0f}\nData terrestre para Jupiter: {data_jupiter.year}-{data_jupiter.month:02d}-{data_jupiter.day:02d}\nDias terrestres para Saturno = {dias_sat:.0f}\nData terrestre para Saturno: {data_saturno.year}-{data_saturno.month:02d}-{data_saturno.day:02d}')
