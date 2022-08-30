import pandas
# библиотека работы с exlel файлпами
import openpyxl
df = pandas.read_excel("BOOK_KEEP.xlsx")

df= df.fillna(0)

# выбор столбца
print(df['ПРОДУКТЫ'].sum())
seria = df["Unnamed: 0"]
print (seria)
print(type(seria))

list = seria.tolist()
print (list)
