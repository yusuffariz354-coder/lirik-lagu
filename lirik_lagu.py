import time

# Lirik lagu Indonesia Raya
lirik = [
    "INDONESIA RAYA\n",
    "Indonesia tanah airku,",
    "Tanah tumpah darahku.",
    "Di sanalah aku berdiri,",
    "Jadi pandu ibuku.\n",
    "Indonesia kebangsaanku,",
    "Bangsa dan tanah airku.",
    "Marilah kita berseru,",
    "Indonesia bersatu.\n",
    "Hiduplah tanahku, hiduplah negeriku,",
    "Bangsaku, rakyatku, semuanya.",
    "Bangunlah jiwanya, bangunlah badannya,",
    "Untuk Indonesia Raya.\n",
    "Indonesia Raya, merdeka, merdeka,",
    "Tanahku, negeriku yang kucinta.",
    "Indonesia Raya, merdeka, merdeka,",
    "Hiduplah Indonesia Raya."
]

# Atur tempo karaoke (detik)
tempo = 2  # ganti ke 1.5 kalau mau lebih cepat, 3 kalau mau lambat

# Tampilkan lirik dengan jeda
for baris in lirik:
    print(baris)
    time.sleep(tempo)