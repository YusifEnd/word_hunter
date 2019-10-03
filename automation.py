# import sqlite3
# from words import sozler
#
# con = sqlite3.connect("oyun.db")
# kursor = con.cursor()

# con_gamer = sqlite3.connect("gamer.db")
# kursor_gamer = con2.cursor()

# OLMAYAN TABLE'NI ELAVE ETMEK UCUN:
# def create_table_finds():
#     kursor.execute("CREATE TABLE IF NOT EXISTS finds(soz TEXT)")
#     con.commit()
#
# create_table_finds()


# BAZADA OLMAYAN TAPILMALI YENI SOZLERI ELAVE ETMEK UCUN:
# kursor.execute("SELECT * FROM words")
# baza_words = []
# for i in kursor.fetchall():
#     baza_words.append(*i)
#
# for z in sozler:
#     if z not in baza_words:
#         kursor.execute("INSERT INTO words VALUES(?)", [z])
#         con.commit()
# con.close()


# BAZADA OLMAYAN ESAS 8 HERFLI YENI SOZLERI ELAVE ETMEK UCUN:
# kursor.execute("SELECT * FROM finds")
# baza_finds = []
# for i in kursor.fetchall():
#     baza_finds.append(*i)
#
# for z in sozler:
#     if len(z) == 8:
#       if z not in baza_finds:
#         kursor.execute("INSERT INTO finds VALUES(?)", [z])
#         con.commit()
# con.close()
















