import streamlit as st
import pandas as pd
import joblib
import numpy as np

model = joblib.load('./model/lung_cancer.pkl')

def main():    
    st.title('Form Lung Cancer Prediction')
    st.header('Answer The Following Questions Based On Your Medical History:')

    st.markdown('---')

    st.write('Menurut Anda, dari rentang 1 sampai 10, seberapa mengganggu berat badan Anda dalam beraktivitas sehari-hari?')
    obesity = st.slider('Rentang 1: Sama Sekali Tidak Mengganggu | Rentang 10: Tidak Dapat Beraktivitas Secara Normal', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan pengalaman Anda, dari rentang 1 sampai 10, apakah Anda pernah mengalami batuk berdarah? Jika iya, seberapa sering Anda batuk berdarah?')
    coughing_of_blood = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Kronis', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Menurut Anda, dari rentang 1 sampai 10, seberapa sering Anda meminum alkohol dalam sehari-hari?')
    alcohol_use = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Gak Alkohol Gak Minum (nb: Bukan banyaknya alkohol yang diminum dalam sehari)', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan riwayat medis Anda, dari rentang 1 sampai 10, apakah Anda memiliki alergi yang dapat memengaruhi pernapasan? Jika iya, seberapa parah?')
    dust_allergy = st.slider('Rentang 1: Tidak Punya | Rentang 10: Kronis', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan keseharian Anda, dari rentang 1 sampai 10, seberapa sering Anda menjaga pola makan Anda 4 sehat 5 Sempurna?')
    balanced_diet = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Setiap Hari', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan pengalaman Anda, apakah Anda dikelilingi oleh perokok? Jika iya, dari rentang 1 sampai 10 seberapa sering Anda dikelilingi oleh perokok? (bagi perokok aktif dapat memberikan skala keseringan yang disesuaikan)')
    passive_smoker = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Setiap Waktu', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan riwayat medis Anda, dari rentang 1 sampai 10, apakah keluarga Anda terdapat riwayat terkena kanker paru-paru? Jika iya, seberapa sering Anda merasa mengalami gejala kanker paru-paru, seperti batuk berdarah?')
    genetic_risk = st.slider('Rentang 1: Tidak Ada | Rentang 10: Saya Sering Merasa Mengalami Gejala Kanker Paru-paru (Batuk Berdarah)', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Apakah Anda memiliki atau melakukan pekerjaan atau aktivitas berbahaya setiap harinya yang dapat melukai diri Anda? Jika iya, dari rentang 1 sampai 10 seberapa berbahayanya bagi tubuh? ')
    occupational_hazards = st.slider('Rentang 1: Tidak Ada | Rentang 10: Nyawa Taruhannya', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan pengalaman Anda, dari rentang 1 sampai 10, seberapa sering Anda merasa sakit di dada?')
    chest_pain = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Hampir Setiap Waktu', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan pengalaman Anda, dari rentang 1 sampai 10, seberapa sering Anda terpapar polusi udara?')
    air_pollution = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Setiap Detiknya', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan pengalaman Anda, dari rentang 1 sampai 10, seberapa sering Anda merasa kelelahan?')
    fatigue = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Setiap Waktu Tanpa Terkecuali', min_value=1, max_value=10)

    st.markdown('---')

    st.write('Berdasarkan riwayat kesehatan Anda, dari rentang 1 sampai 10, seberapa parah penyakit pada paru-paru Anda sebelumnya?')
    chronic_lung_disease = st.slider('Rentang 1: Tidak Pernah | Rentang 10: Sekarat', min_value=1, max_value=10)

    st.markdown('---')

    if st.button('Predict'):
        prediction = predict_lung_cancer(obesity, coughing_of_blood, alcohol_use, dust_allergy, balanced_diet, passive_smoker, genetic_risk, occupational_hazards, chest_pain, air_pollution, fatigue, chronic_lung_disease)
        prediction = prediction - 0.66030176

        if prediction >= 0 and prediction < 1:
            prediction = 'Low Risk'
            st.success(f'The model predicts: {prediction}')
        elif prediction >= 1 and prediction < 2:
            prediction = 'Medium Risk'
            st.warning(f'The model predicts: {prediction}')
        else:
            prediction = 'High Risk'
            st.error(f'The model predicts: {prediction}')

def predict_lung_cancer(obesity, coughing_of_blood, alcohol_use, dust_allergy, balanced_diet, passive_smoker, 
                        genetic_risk, occupational_hazards, chest_pain, air_pollution, fatigue, chronic_lung_disease):
    
    input_data = pd.DataFrame([[obesity, coughing_of_blood, alcohol_use, dust_allergy, balanced_diet, passive_smoker, 
                                genetic_risk, occupational_hazards, chest_pain, air_pollution, fatigue, chronic_lung_disease]],
                                columns=['Obesity', 'Coughing of Blood', 'Alcohol use', 'Dust Allergy', 
                                        'Balanced Diet', 'Passive Smoker', 'Genetic Risk', 
                                        'OccuPational Hazards', 'Chest Pain', 'Air Pollution', 
                                        'Fatigue', 'chronic Lung Disease'])
    
    prediction = model.predict(input_data)
    
    return prediction

if __name__ == '__main__':
    main()