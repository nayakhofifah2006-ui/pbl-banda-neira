import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ====================================
# KONFIGURASI HALAMAN
# ====================================

st.set_page_config(
    page_title="Monitoring Perairan Banda Neira",
    layout="wide"
)

# ====================================
# JUDUL DAN IDENTITAS
# ====================================

st.title("Monitoring Perairan Banda Neira")

st.markdown("""
### Universitas Islam Bandung

**Mata Kuliah:** Pemodelan dan Simulasi

**Dosen Pengampu:** Yuhka Sundaya

### Kelompok 10

- Naya Khofifah Aulia (10090224012)
- Yulia Yuthika (10090224013)
- Melvina Putri Aprilianti (10090224029)
""")

st.info("""
Lokasi Studi : Perairan Banda Neira, Maluku

Parameter yang Digunakan :
- Sea Surface Temperature (SST)
- Chlorophyll-a

Tujuan :
Menganalisis kondisi perairan dan potensi daerah penangkapan ikan berdasarkan data oseanografi.
""")

st.markdown("---")

# ====================================
# PENDAHULUAN
# ====================================

st.markdown("""
# Banda Neira, Permata Laut Maluku

Banda Neira merupakan salah satu pulau utama di Kepulauan Banda yang terletak di Provinsi Maluku, Indonesia. Wilayah ini dikenal luas karena sejarah perdagangan rempah-rempah dunia serta keindahan lautnya yang menjadi daya tarik wisata bahari.

Selain memiliki nilai sejarah yang tinggi, Banda Neira juga menyimpan potensi sumber daya laut yang sangat besar. Perairan di sekitar Kepulauan Banda menjadi habitat berbagai jenis ikan pelagis maupun ikan karang yang memiliki nilai ekonomi penting bagi masyarakat pesisir.

Dalam bidang kelautan dan perikanan, kondisi lingkungan laut sangat berpengaruh terhadap keberadaan dan persebaran ikan. Salah satu cara untuk memantau kondisi tersebut adalah melalui data satelit yang mampu memberikan informasi secara luas dan berkelanjutan.

Parameter yang umum digunakan dalam analisis perairan adalah Sea Surface Temperature (SST) atau Suhu Permukaan Laut serta Chlorophyll-a. SST digunakan untuk mengetahui kondisi fisik perairan, sedangkan Chlorophyll-a digunakan sebagai indikator keberadaan fitoplankton yang menjadi sumber makanan utama dalam rantai makanan laut.

Melalui aplikasi ini, pengguna dapat melihat visualisasi kondisi perairan Banda Neira berdasarkan data SST dan Chlorophyll-a serta memperoleh gambaran sederhana mengenai potensi daerah penangkapan ikan.
""")

st.markdown("---")

# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("Menu")

menu = st.sidebar.selectbox(
    "Pilih Halaman",
    [
        "Dashboard Monitoring",
        "Panduan Data NOAA",
        "Analisis Potensi Perikanan"
    ]
)

# ====================================
# DASHBOARD
# ====================================

if menu == "Dashboard Monitoring":

    st.header("Dashboard Monitoring Perairan")

    df = pd.read_csv("data_banda_neira.csv")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Rata-rata SST",
            f"{df['SST'].mean():.2f} °C"
        )

    with col2:
        st.metric(
            "Rata-rata Chlorophyll-a",
            f"{df['Chlorophyll'].mean():.2f}"
        )

    with col3:
        st.metric(
            "Jumlah Data",
            len(df)
        )

    st.subheader("Data Pengamatan")

    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Grafik SST")

        fig, ax = plt.subplots()

        ax.plot(
            df["Bulan"],
            df["SST"],
            marker="o"
        )

        ax.set_ylabel("SST (°C)")

        st.pyplot(fig)

    with col2:

        st.subheader("Grafik Chlorophyll-a")

        fig, ax = plt.subplots()

        ax.plot(
            df["Bulan"],
            df["Chlorophyll"],
            marker="o"
        )

        ax.set_ylabel("mg/m³")

        st.pyplot(fig)

# ====================================
# NOAA
# ====================================

elif menu == "Panduan Data NOAA":

    st.header("Panduan Pengambilan Data Satelit NOAA")

    st.markdown("""
## Apa itu NOAA?

National Oceanic and Atmospheric Administration (NOAA) merupakan lembaga pemerintah Amerika Serikat yang menyediakan data kelautan, atmosfer, iklim, dan lingkungan secara terbuka.

Data NOAA banyak digunakan oleh peneliti, mahasiswa, maupun instansi pemerintah untuk memantau kondisi lingkungan laut secara berkala.

### Parameter yang Digunakan

- Sea Surface Temperature (SST)
- Chlorophyll-a
- Ocean Color
- Kecepatan Angin
- Tinggi Gelombang

### Wilayah Pengamatan

Koordinat Banda Neira:

- Latitude : -5 sampai -4
- Longitude : 129 sampai 131

### Langkah Pengambilan Data

**1. Buka NOAA CoastWatch**

https://coastwatch.noaa.gov

**2. Cari Dataset**

Gunakan kata kunci:

- SST
- Sea Surface Temperature
- Chlorophyll-a

**3. Tentukan Area Pengamatan**

Masukkan koordinat Banda Neira.

**4. Tentukan Rentang Waktu**

Contoh:

- Januari 2024
- Desember 2024

**5. Unduh Data**

Format yang direkomendasikan:

- CSV
- NetCDF (.nc)

**6. Analisis Data**

Data yang telah diunduh dapat diolah menggunakan Python, Excel, maupun Streamlit.
""")

    st.success(
        "Data satelit memungkinkan pemantauan kondisi laut secara lebih luas, cepat, dan efisien."
    )

# ====================================
# POTENSI IKAN
# ====================================

elif menu == "Analisis Potensi Perikanan":

    st.header("Analisis Potensi Perikanan")

    df = pd.read_csv("data_banda_neira.csv")

    sst = df["SST"].mean()
    chl = df["Chlorophyll"].mean()

    if 28 <= sst <= 30 and chl >= 0.45:
        status = "Tinggi"
    elif chl >= 0.35:
        status = "Sedang"
    else:
        status = "Rendah"

    st.metric(
        "Potensi Daerah Penangkapan Ikan",
        status
    )

    st.markdown("""
### Interpretasi Hasil

- SST yang stabil menunjukkan kondisi perairan yang baik.
- Chlorophyll-a yang tinggi menandakan produktivitas perairan yang tinggi.
- Produktivitas perairan yang tinggi umumnya berkaitan dengan potensi keberadaan ikan yang lebih besar.
- Kombinasi SST dan Chlorophyll-a dapat digunakan sebagai indikator awal dalam menentukan daerah penangkapan ikan.

Berdasarkan data yang digunakan pada aplikasi ini, kondisi perairan Banda Neira menunjukkan potensi perikanan yang cukup baik.
""")
    st.markdown("""
### Kesimpulan

Berdasarkan data SST dan Chlorophyll-a yang digunakan,
perairan Banda Neira menunjukkan kondisi yang cukup baik
untuk mendukung produktivitas perikanan.

Nilai SST yang berada pada kisaran optimal serta konsentrasi
Chlorophyll-a yang relatif tinggi menunjukkan bahwa wilayah
ini memiliki potensi sebagai daerah penangkapan ikan.
""")