# CYBER F  v.1.0

**Консольный инструмент для пробива по слитым базам**  
Dev by Xttabee / https://github.com/RenatDEV888/CyberF

## Информация

Простой, но мощный консольный пробив по твоим базам в формате `.csv` / `.xlsx`.  
Ищет по телефону, ФИО, ИНН, TG @username, VK, email, паспорту, городу+имени и т.д.  
Поддерживает сколько угодно баз в папке `bases/`.  

Screenshot 2026-03-08 170944.png

## Функционал
- Автозагрузка всех `.csv` и `.xlsx` из папки `bases/`
- Поиск по любому тексту (телефон, ФИО, ник, ИНН, город + имя и т.п.)
- Поддержка почти всех популярных полей:
  - phone, full_name, first_name, last_name
  - inn, ogrn, pass_nomer
  - telegram_username, username, account_id
  - vk_url, facebook.com, instagram.com, twitter.com
  - email, city, region, country, adres, index
  - operator, male, marital_status, birth_date, age
- Красивый цветной вывод с разделителями
- Радужный ASCII-арт при запуске
- Команды:
  - `reload` — перечитать все базы (можно добавлять файлы на лету)
  - `list` — показать список баз и количество записей в каждой
  - `q` / `exit` / `quit` — выход

## Как запустить

1. Установи зависимости

```bash
aiogram==3.13.1
pandas
openpyxl
python-dotenv
colorama
pyinstaller
