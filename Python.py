import pandas as pd

# Читаем, игнорируя ошибки
df = pd.read_excel("WBmoscow.xlsx", engine='openpyxl', dtype=str)

# Убираем #NAME? и прочий мусор
df = df.replace('#NAME?', '').fillna('')

# Сохраняем чистый файл
df.to_excel("WBmoscowDB.xlsx", index=False)