"""
# 2. auto_skelbimai_app
#
# lentelė automobiliai:
# -gamintojas
# -modelis
# -pagaminimo_metai
# -kaina
# -miestas
# ką suprogramuoti? CRUD veiksmai. visų eilučių atvaizdavimas, eilutės
# pridėjimas, eilučių/ės trynimas, eilutės vieno ar keletos duomenų(langelių) redagavimas(keitimas),
# paieška pagal gamintoją(+ modelį), kainą, metus(kiek pavyks)
"""
import os.path
import sqlite3


# auto_gamintojas = "Audi"
# auto_modelis = "A4"
# auto_pagaminimo_metai = "1991-06-05"
# auto_kaina = 2000
# auto_miestas = "Klaipeda"

# auto_ivedimas =


if not os.path.exists("auto_db"):
    print("nera auto_db folderio, sukursim")
    os.mkdir("auto_db")
os.chdir("auto_db")

conn = sqlite3.connect("auto_skelbimai_duomenys.db")
c = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS
Auto_duomenys (
gamintojas text,
modelis text,
metai text,
kaina integer,
miestas text);"""

c.execute(query)
