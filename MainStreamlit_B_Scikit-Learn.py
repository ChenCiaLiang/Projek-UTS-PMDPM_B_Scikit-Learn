import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import os

with st.sidebar:
    selected = option_menu('Proyek UTS ML 24/25',
                            ['Klasifikasi',
                            'Regresi', 'Catatan'],
                            default_index=0)
    
if selected == 'Klasifikasi':
    model = r'BestModel_CLF_GBT_Scikit-Learn.pkl'

    if os.path.exists(model):
        with open(model, 'rb') as f:
            loaded_model = pickle.load(f)
    
        st.title("Prediksi Jenis Rumah")
        st.write("Aplikasi ini membantu user untuk mengecek jenis rumah yang ingin dibeli")

        squaremeters = st.number_input("Luas", min_value=0)
        numberofrooms = st.number_input("Jumlah Kamar", min_value=0)
        hasyard = st.selectbox("Apakah Memiliki Halaman?", ["yes", "no"])
        haspool = st.selectbox("Apakah Memiliki Kolam Renang?", ["yes", "no"])
        floors = st.number_input("Jumlah Lantai", min_value=0)
        citycode = st.number_input("Kode Kota", min_value=0)
        citypartrange = st.number_input("Rentang Partisi Kota", min_value=0)
        numprevowners = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
        made = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)
        isnewbuilt = st.selectbox("Apakah Baru Dibangun?", ["yes", "no"])
        hasstormprotector = st.selectbox("Apakah Memiliki Pelindung Badai?", ["yes", "no"])
        basement = st.number_input("luas Basement", min_value=0)
        attic = st.number_input("attic", min_value=0)
        garage = st.number_input("Luas Garasi", min_value=0)
        hasstorageroom = st.selectbox("Apakah Memiliki Ruang Penyimpanan?", ["yes", "no"])
        hasguestroom = st.number_input("Jumlah Kamar Tamu", min_value=0)

        
        if hasyard == "yes":
            input_hasyard = 1
        else:
            input_hasyard =0
        
        if haspool == "yes":
            input_haspool = 1
        else:
            input_haspool =0
        
        if isnewbuilt == "yes":
            input_isnewbuilt = 1
        else:
            input_isnewbuilt =0
        
        if hasstormprotector == "yes":
            input_hasstormprotector = 1
        else:
            input_hasstormprotector =0
        
        if hasstorageroom == "yes":
            input_hasstorageroom = 1
        else:
            input_hasstorageroom =0

        input_data = [squaremeters, numberofrooms, input_hasyard, input_haspool, floors, citycode, citypartrange,
                        numprevowners, made, input_isnewbuilt, input_hasstormprotector, basement, attic, garage,
                        input_hasstorageroom, hasguestroom]

        st.write("Data yang akan diinput ke model")
        st.write(input_data)

        if st.button("Prediksi"):
            model_prediction = model.predict(input_data)
            outcome = {'Basic':'Basic', 'Luxury':'Luxury', 'Middle':'Middle'}
            st.write(f"Property tersebut merupakan kelas :  **{outcome[model_prediction[0]]}**")
    else:
        st.error("Model tidak ditemukan")


if selected == 'Regresi':
    model = r'BestModel_REG_SVR_Scikit-Learn.pkl'

    if os.path.exists(model):
        with open(model, 'rb') as f:
            loaded_model = pickle.load(f)

        st.title("Prediksi Harga Rumah")
        st.write("Aplikasi ini membantu user untuk mengecek estimasi harga rumah")

        squaremeters = st.number_input("Luas", min_value=0)
        numberofrooms = st.number_input("Jumlah Kamar", min_value=0)
        hasyard = st.selectbox("Apakah Memiliki Halaman?", ["yes", "no"])
        haspool = st.selectbox("Apakah Memiliki Kolam Renang?", ["yes", "no"])
        floors = st.number_input("Jumlah Lantai", min_value=0)
        citycode = st.number_input("Kode Kota", min_value=0)
        citypartrange = st.number_input("Rentang Partisi Kota", min_value=0)
        numprevowners = st.number_input("Jumlah Pemilik Sebelumnya", min_value=0)
        made = st.number_input("Tahun Dibuat", min_value=1900, max_value=2024)
        isnewbuilt = st.selectbox("Apakah Baru Dibangun?", ["yes", "no"])
        hasstormprotector = st.selectbox("Apakah Memiliki Pelindung Badai?", ["yes", "no"])
        basement = st.number_input("luas Basement", min_value=0)
        attic = st.number_input("attic", min_value=0)
        garage = st.number_input("Luas Garasi", min_value=0)
        hasstorageroom = st.selectbox("Apakah Memiliki Ruang Penyimpanan?", ["yes", "no"])
        hasguestroom = st.number_input("Jumlah Kamar Tamu", min_value=0)

        
        if hasyard == "yes":
            input_hasyard = 1
        else:
            input_hasyard =0
        
        if haspool == "yes":
            input_haspool = 1
        else:
            input_haspool =0
        
        if isnewbuilt == "yes":
            input_isnewbuilt = 1
        else:
            input_isnewbuilt =0
        
        if hasstormprotector == "yes":
            input_hasstormprotector = 1
        else:
            input_hasstormprotector =0
        
        if hasstorageroom == "yes":
            input_hasstorageroom = 1
        else:
            input_hasstorageroom =0

        input_data = [squaremeters, numberofrooms, input_hasyard, input_haspool, floors, citycode, citypartrange,
                        numprevowners, made, input_isnewbuilt, input_hasstormprotector, basement, attic, garage,
                        input_hasstorageroom, hasguestroom]

        st.write("Data yang akan diinput ke model: ")
        st.write(input_data)

        if st.button("Prediksi"):
            model_prediction = model.predict(input_data)
            formatted_price = "${:,.2f}".format(model_prediction[0])
            st.write(f"Hasil prediksi model: {formatted_price}")
    else:
        st.error("Model tidak ditemukan")

if selected == 'Catatan':
    st.title('Catatan')
    st.write('''1. Untuk memunculkan sidebar agar tidak error ketika di run, silahkan install library streamlit option menu
            di terminal dengan perintah "pip install streamlit-option-menu".''')
    st.write('2. Menu yang dibuat ada 2 yaitu Klasifikasi dan Regresi.')
    st.write('3. Inputan nya apa aja, sesuaikan dengan arsitektur code anda pada notebook.')
    st.write('4. Referensi desain streamlit dapat di akses pada https://streamlit.io/.')
    st.write('5. Link streamlit desain ini dapat di akses pada https://apputs-6qzfvr4ufiyzhj84mrfkt7.streamlit.app/.')
    st.write('''6. Library pada file requirements yang dibutuhkan untuk deploy online di github ada 5 yaitu streamlit, scikit-learn, pandas, numpy, streamlit-option-menu.''')
