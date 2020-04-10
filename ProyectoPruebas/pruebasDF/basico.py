import pandas as pd

print("INICIO")
datosDF = pd.read_csv(filepath_or_buffer="D:\\GITHUB_REPOS\\myrepo0\\ProyectoPruebas\\pruebasDF\\datos.csv", sep=',')
print(datosDF.head())
print("FIN")

