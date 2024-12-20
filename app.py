import streamlit as st
import joblib
from sklearn.preprocessing import LabelEncoder

# Modeli yükle
model = joblib.load("eniyi.joblib")

# Encoderları oluştur
marka_encoder = LabelEncoder()

# Kategorik değerler
markalar = ["Samsung", "Apple", "Xiaomi", "Huawei", "Oppo", "OnePlus"]

modeller = {
    "Samsung": ["Galaxy S10", "Galaxy S20", "Galaxy S21"],
    "Apple": ["iPhone 10", "iPhone 11", "iPhone 12"],
    "Xiaomi": ["Redmi Note 8", "Redmi Note 9", "Mi 11"],
    "Huawei": ["P30", "P40", "Mate 40"],
    "Oppo": ["A15", "Reno 5", "Find X3"],
    "OnePlus": ["Nord", "8T", "9 Pro"]
}

marka_encoder.fit(markalar)


# Uygulama başlığı
st.title("Telefon Tahmin Uygulaması")

# Marka seçimi
marka = st.selectbox("Marka Seçin", markalar)

# Model seçimi
model_secimi = st.selectbox("Model Seçin", modeller[marka])

# Depolama seçimi
depolama = st.selectbox("Depolama (GB)", [64, 128, 256])

# RAM seçimi
ram = st.selectbox("RAM (GB)", [4, 6, 8, 12])

yas = st.selectbox("Yaş", [0, 1, 2, 3,4])


# Kategorik değerleri encode et
marka_encoded = marka_encoder.transform([marka])[0]


# Modeli encode ederek uygun sayıya çevir
model_index = modeller[marka].index(model_secimi)

# Tahmin için veriyi oluştur
veri = [[marka_encoded, model_index, depolama, ram, yas]]

# Ek özellikleri hesaplama
ram_depolama_ratio = ram / depolama
yas_kare = yas ** 2

# Yeni özellikleri ekle
veri[0].extend([ram_depolama_ratio, yas_kare])

# Tahmini hesapla ve göster
# Tahmini hesapla ve göster
if st.button("Tahmin Yap"):
    tahmin = model.predict(veri)
    tahmin_rounded = round(tahmin[0], 2)  # Tahmini noktadan sonra 1 basamağa yuvarla
    st.success(f"Tahmin Edilen Değer: {tahmin_rounded}")
