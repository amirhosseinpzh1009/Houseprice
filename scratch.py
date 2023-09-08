import streamlit as st
import pandas as pd
import numpy as np
from collections import ChainMap
import joblib
import pickle
st.write("# Price of houses in Tehran :chart_with_upwards_trend::house_with_garden:")

def user_input():
    st.sidebar.markdown('''# :orange[Features] :bar_chart:''')
    st.sidebar.divider()
    st.sidebar.markdown("***If you choose 0 for a feature that means the feature doesn't exist and If you choose 1 for a feature that means the feature exist***")
    st.sidebar.divider()
    area = st.sidebar.number_input(':orange[Area]', step=10, value=70)
    room = st.sidebar.slider(':orange[Room]', min_value=0, max_value=6, step=1)
    parking = st.sidebar.slider(':orange[Parking]', min_value=0, max_value=1, step=1)
    warehouse = st.sidebar.slider(':orange[Warehouse]', min_value=0, max_value=1, step=1)
    elevator = st.sidebar.slider(':orange[Elevator]', min_value=0, max_value=1, step=1)
    regions = ['Abazar',
 'Abbasabad',
 'Abuzar',
 'Afsarieh',
 'Ahang',
 'Air force',
 'Ajudaniye',
 'Alborz Complex',
 'Aliabad South',
 'Amir Bahador',
 'Amirabad',
 'Amirieh',
 'Andisheh',
 'Aqdasieh',
 'Araj',
 'Atabak',
 'Azadshahr',
 'Azarbaijan',
 'Azari',
 'Baghestan',
 'Bahar',
 'Baqershahr',
 'Beryanak',
 'Boloorsazi',
 'Central Janatabad',
 'Chahardangeh',
 'Chardangeh',
 'Chardivari',
 'Chidz',
 'Damavand',
 'Darabad',
 'Darakeh',
 'Darband',
 'Daryan No',
 'Dehkade Olampic',
 'Dezashib',
 'Dolatabad',
 'Dorous',
 'East Ferdows Boulevard',
 'East Pars',
 'Ekbatan',
 'Ekhtiarieh',
 'Elahieh',
 'Elm-o-Sanat',
 'Enghelab',
 'Eram',
 'Eskandari',
 'Fallah',
 'Farmanieh',
 'Fatemi',
 'Feiz Garden',
 'Firoozkooh',
 'Firoozkooh Kuhsar',
 'Garden of Saba',
 'Gheitarieh',
 'Ghiyamdasht',
 'Ghoba',
 'Gholhak',
 'Gisha',
 'Golestan',
 'Haft Tir',
 'Hakimiyeh',
 'Hashemi',
 'Hassan Abad',
 'Hekmat',
 'Heravi',
 'Heshmatieh',
 'Hor Square',
 'Islamshahr',
 'Islamshahr Elahieh',
 'Javadiyeh',
 'Jeyhoon',
 'Jordan',
 'Kahrizak',
 'Kamranieh',
 'Karimkhan',
 'Karoon',
 'Kazemabad',
 'Keshavarz Boulevard',
 'Khademabad Garden',
 'Khavaran',
 'Komeil',
 'Koohsar',
 'Kook',
 'Lavizan',
 'Mahallati',
 'Mahmoudieh',
 'Majidieh',
 'Malard',
 'Marzdaran',
 'Mehrabad',
 'Mehrabad River River',
 'Mehran',
 'Mirdamad',
 'Mirza Shirazi',
 'Moniriyeh',
 'Narmak',
 'Nasim Shahr',
 'Nawab',
 'Naziabad',
 'Nezamabad',
 'Niavaran',
 'North Program Organization',
 'Northern Chitgar',
 'Northern Janatabad',
 'Northern Suhrawardi',
 'Northren Jamalzadeh',
 'Ostad Moein',
 'Ozgol',
 'Pakdasht',
 'Pakdasht KhatunAbad',
 'Parand',
 'Parastar',
 'Pardis',
 'Pasdaran',
 'Persian Gulf Martyrs Lake',
 'Pirouzi',
 'Pishva',
 'Punak',
 'Qalandari',
 'Qarchak',
 'Qasr-od-Dasht',
 'Qazvin Imamzadeh Hassan',
 'Railway',
 'Ray',
 'Ray - Montazeri',
 'Ray - Pilgosh',
 'Razi',
 'Republic',
 'Robat Karim',
 'Rudhen',
 'Saadat Abad',
 'SabaShahr',
 'Sabalan',
 'Sadeghieh',
 'Safadasht',
 'Salehabad',
 'Salsabil',
 'Sattarkhan',
 'Seyed Khandan',
 'Shadabad',
 'Shahedshahr',
 'Shahr-e-Ziba',
 'ShahrAra',
 'Shahrake Apadana',
 'Shahrake Azadi',
 'Shahrake Gharb',
 'Shahrake Madaen',
 'Shahrake Qods',
 'Shahrake Quds',
 'Shahrake Shahid Bagheri',
 'Shahrakeh Naft',
 'Shahran',
 'Shahryar',
 'Shams Abad',
 'Shoosh',
 'Si Metri Ji',
 'Sohanak',
 'Southern Chitgar',
 'Southern Janatabad',
 'Southern Program Organization',
 'Southern Suhrawardi',
 'Tajrish',
 'Tarasht',
 'Taslihat',
 'Tehran Now',
 'Tehransar',
 'Telecommunication',
 'Tenant',
 'Thirteen November',
 'Vahidieh',
 'Vahidiyeh',
 'Valiasr',
 'Vanak',
 'Velenjak',
 'Villa',
 'Water Organization',
 'Waterfall',
 'West Ferdows Boulevard',
 'West Pars',
 'Yaftabad',
 'Yakhchiabad',
 'Yousef Abad',
 'Zafar',
 'Zaferanieh',
 'Zargandeh',
 'Zibadasht']
    region = st.sidebar.selectbox(':orange[Regions]', options = regions)

    values = [0] * len(regions)
    reg = dict(zip(regions, values))
    reg[str(region)] = 1
    data = {"Area": area, "Room": room, "Parking": parking, "Warehouse": warehouse, "Elevator":elevator}
    merged_dic = dict(ChainMap(reg, data))
    features = pd.DataFrame(merged_dic, index=[0])
    return features

df = user_input()

parking = df["Parking"][0]
warehouse = df["Warehouse"][0]
elevator = df["Elevator"][0]
area = df["Area"][0]
room = df["Room"][0]

st.divider()

if parking == 1:
    p = "Has parking"
else:
    p = "Doesn't have parking"
if warehouse == 1:
    w = "Has warehouse"
else:
    w = "Doesn't have warehouse"
if elevator == 1:
    e = "Has elevator"
else:
    e = "Doesn't have elevator"
header = df.columns.tolist()
for i in range(5, len(header)):
    h = str(header[i])
    if df[h][0] == 1:
        r = h

new_dic = {"Area": area, "Room":room, "Parking": p, "Warehouse": w, "Elevator": e, "Region":r}
features_show = pd.DataFrame(new_dic, index=[0])
st.markdown("## Your target house :arrow_down_small:")
st.table(features_show)
st.divider()
st.markdown("## Prediction the price of target your house:moneybag:")
model = joblib.load('regression_model.joblib')

t = st.sidebar.button("Predict")

if t:
 prediction = model.predict(df)
 st.write('### Our Prediction is (Toman): ', prediction)
 st.divider()











