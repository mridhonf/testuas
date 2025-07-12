import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Visualisasi Biaya Persediaan (EOQ Breakdown)")

# Input pengguna
D = st.number_input("Kebutuhan per tahun (D)", min_value=1, value=12000)
S = st.number_input("Biaya pemesanan per pesanan (S)", min_value=1, value=100000)
H = st.number_input("Biaya penyimpanan per unit per tahun (H)", min_value=1, value=2500)

# Perhitungan EOQ
EOQ = np.sqrt((2 * D * S) / H)

# Rentang nilai Q (jumlah pemesanan)
Q_range = np.linspace(100, D, 200)

# Perhitungan biaya-biaya
biaya_pemesanan = (D / Q_range) * S
biaya_penyimpanan = (Q_range / 2) * H
total_biaya = biaya_pemesanan + biaya_penyimpanan

# Visualisasi
fig, ax = plt.subplots()
ax.plot(Q_range, biaya_pemesanan, label="Biaya Pemesanan", color='blue')
ax.plot(Q_range, biaya_penyimpanan, label="Biaya Penyimpanan", color='green')
ax.plot(Q_range, total_biaya, label="Total Biaya", color='orange')
ax.axvline(EOQ, color='red', linestyle='--', label=f'EOQ ≈ {EOQ:.0f}')

ax.set_xlabel("Jumlah Pemesanan per Order (Q)")
ax.set_ylabel("Biaya (Rp)")
ax.set_title("Kurva Komponen Biaya Persediaan")
ax.legend()
st.pyplot(fig)

# Output numerik
st.markdown("### 🔍 Ringkasan:")
st.write(f"**EOQ (Jumlah Optimal per Order):** {EOQ:.2f} unit")
