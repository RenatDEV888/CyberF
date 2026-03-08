# pip install colorama pandas openpyxl tqdm

import sys
from pathlib import Path
import pandas as pd
from colorama import init, Fore, Style
from tqdm import tqdm

init(autoreset=True)

RAINBOW = [
    Fore.RED + Style.BRIGHT,
    Fore.LIGHTRED_EX,
    Fore.YELLOW + Style.BRIGHT,
    Fore.LIGHTYELLOW_EX,
    Fore.GREEN + Style.BRIGHT,
    Fore.LIGHTGREEN_EX,
    Fore.CYAN + Style.BRIGHT,
    Fore.LIGHTCYAN_EX,
    Fore.BLUE + Style.BRIGHT,
    Fore.LIGHTBLUE_EX,
    Fore.MAGENTA + Style.BRIGHT,
    Fore.LIGHTMAGENTA_EX,
]

def rainbow_text(text):
    result = ""
    for i, char in enumerate(text):
        color = RAINBOW[i % len(RAINBOW)]
        result += f"{color}{char}"
    return result + Style.RESET_ALL


ASCII_BANNER = """
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~ ________      ___    ___ ________  _______   ________          ________  ~
# ~|\   ____\    |\  \  /  /|\   __  \|\  ___ \ |\   __  \        |\  _____\ ~
# ~\ \  \___|    \ \  \/  / | \  \|\ /\ \   __/|\ \  \|\  \       \ \  \__/  ~
# ~ \ \  \        \ \    / / \ \   __  \ \  \_|/_\ \   _  _\       \ \   __\ ~
# ~  \ \  \____    \/  /  /   \ \  \|\  \ \  \_|\ \ \  \\  \|       \ \  \_| ~
# ~   \ \_______\__/  / /      \ \_______\ \_______\ \__\ _\        \ \__\  ~
# ~    \|_______|\___/ /        \|_______|\|_______|\|__|\|__|        \|__|  ~
# ~             \|___|/                                                      ~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

def print_rainbow_banner():
    lines = ASCII_BANNER.strip().splitlines()
    for line in lines:
        print(rainbow_text(line))

databases = {}

def load_databases():
    global databases
    databases = {}

    BASE_DIR = Path("bases")
    if not BASE_DIR.exists() or not BASE_DIR.is_dir():
        print(f"{Fore.RED}Папки bases не найдена.{Style.RESET_ALL}")
        return

    print(f"{Fore.CYAN}Сканирую папку: {BASE_DIR.absolute()}{Style.RESET_ALL}")


    files = [f for f in BASE_DIR.glob("*.*") if f.suffix.lower() in [".csv", ".xlsx", ".xls"]]

    if not files:
        print(f"{Fore.RED}В папке bases нет ни одного .csv / .xlsx файла ⛔{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}Найдено файлов: {len(files)}{Style.RESET_ALL}")


    for file in tqdm(
        files,
        desc=f"{Fore.MAGENTA}Загружаю базы{Style.RESET_ALL}",
        unit="файл",
        colour="magenta",
        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}{postfix}]"
    ):
        name = file.stem
        try:
            if file.suffix.lower() == ".csv":
                df = pd.read_csv(file, dtype=str).fillna("")
            else:
                df = pd.read_excel(file, dtype=str).fillna("")

            df.columns = df.columns.str.strip().str.lower()
            databases[name] = df


            tqdm.write(f"{Fore.GREEN} [+] {name:<22} → {len(df):>6} строк{Style.RESET_ALL}")

        except Exception as e:
            tqdm.write(f"{Fore.RED} [ERR] {file.name}: {e}{Style.RESET_ALL}")

    if databases:
        print(f"\n{Fore.LIGHTMAGENTA_EX}Готов к пробиву. Баз загружено ✅: {len(databases)}{Style.RESET_ALL}\n")
    else:
        print(f"{Fore.RED}Ни одной базы не загрузилось.{Style.RESET_ALL}")

def search_in_df(df: pd.DataFrame, query: str) -> pd.DataFrame:
    if not query.strip():
        return pd.DataFrame()

    q = str(query).lower().replace("+", "").replace("-", "").replace(" ", "").strip()

    if len(q) < 3:
        return pd.DataFrame()

    mask = pd.Series(False, index=df.index)

    cols = [
        "phone", "full_name", "first_name", "last_name", "inn", "ogrn",
        "telegram_username", "username", "account_id", "vk_url",
        "facebook.com", "instagram.com", "twitter.com", "email",
        "pass_nomer", "region", "country", "index", "adres", "male", "operator", "role", "photo", "insta_account_id"
    ]

    for col in cols:
        if col in df.columns:
            mask |= df[col].astype(str).str.lower().str.contains(q, na=False)

    parts = query.lower().split()
    if len(parts) >= 2:
        city_part = parts[0]
        name_part = " ".join(parts[1:])
        if "city" in df.columns and "full_name" in df.columns:
            mask |= (
                df["city"].astype(str).str.lower().str.contains(city_part, na=False) &
                df["full_name"].astype(str).str.lower().str.contains(name_part, na=False)
            )

    return df[mask]

def print_person(row, source):
    print(f"{Fore.RED}┌─[ {Fore.CYAN}{source.upper()}{Fore.RED} ]───────{Style.RESET_ALL}")

    fields = [
        ("🙎‍♂️ ФИО", row.get("full_name")),
        ("🙎‍♂️ Имя", row.get("first_name")),
        ("🙎‍♂️ Фамилия", row.get("last_name")),
        ("📷️ Фото", row.get("photo")),
        ("💼 Роль", row.get("role")),
        ("📞 Телефон", row.get("phone")),
        ("☎️ Оператор", row.get("operator")),
        ("👤 Возраст", f"{row.get('age', '')} ({row.get('birth_date', '—')})".strip(" ()")),
        ("♂️ Пол", row.get("male")),
        ("🏢 Город", row.get("city")),
        ("🗾 Регион", row.get("region")),
        ("🌍 Страна", row.get("country")),
        ("💳 ИНН", row.get("inn")),
        ("💳 ОГРН", row.get("ogrn")),
        ("👨‍👩‍👦 Семья", row.get("marital_status")),
        ("📧 TG @", row.get("telegram_username")),
        ("📧 TG username", row.get("username")),
        ("🆔 TG ID", row.get("account_id")),
        ("🛜 VK", row.get("vk_url")),
        ("🛜 FB", row.get("facebook.com")),
        ("🛜 IG", row.get("instagram.com")),
        ("🆔 IN ID", row.get("insta_account_id")),
        ("🛜 TW", row.get("twitter.com")),
        ("📧 Почта", row.get("email")),
        ("🪪 Паспорт", row.get("pass_nomer")),
        ("📫 Адрес", row.get("adres")),
        ("✉️ Индекс", row.get("index")),
    ]

    has = False
    for label, val in fields:
        if val and str(val).strip() not in ["", "nan", "—"]:
            print(f"{Fore.CYAN}│ {label:<12}{Style.RESET_ALL} {val}")
            has = True

    if not has:
        print(f"{Fore.LIGHTBLACK_EX}│ Пусто как в кошельке ☹{Style.RESET_ALL}")

    print(f"{Fore.RED}└───────────────────────────────────────────────┘{Style.RESET_ALL}\n")

def main():
    print("\n" * 2)
    print_rainbow_banner()
    print(
        f"\n{Fore.LIGHTMAGENTA_EX}   CYBER F v1.0   |   Поиск: номер, ФИО, ИНН, email, TG, VK...   "
        f"Developer Xttabee / https://github.com/RenatDEV888/CyberF{Style.RESET_ALL}"
    )
    print(f"{Fore.YELLOW}   reload  |  list  |  q / exit{Style.RESET_ALL}\n")

    load_databases()

    while True:
        try:
            query = input(f"{Fore.LIGHTMAGENTA_EX}darkbase@cyberfuck:~${Style.RESET_ALL} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{Fore.RED}Сессия уничтожена. Выход.{Style.RESET_ALL}")
            sys.exit(0)

        if not query:
            continue

        q = query.lower()

        if q in ["q", "exit", "quit", "выход"]:
            print(f"{Fore.LIGHTMAGENTA_EX}Пробиваем дальше в следующий раз, братан.{Style.RESET_ALL}")
            break

        elif q == "reload":
            print(f"{Fore.CYAN}Перезагрузка баз...{Style.RESET_ALL}")
            load_databases()
            continue

        elif q == "list":
            if databases:
                for name, df in sorted(databases.items()):
                    print(f"{Fore.GREEN}→ {name:<22} {len(df):>6} записей{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Базы отсутствуют ⛔{Style.RESET_ALL}")
            continue


        total = 0
        print(f"{Fore.YELLOW}🔍 Поиск: {query}{Style.RESET_ALL}")

        for name, df in databases.items():
            found = search_in_df(df, query)
            if not found.empty:
                print(f"\n{Fore.CYAN}База → {name.upper()}   [ {len(found)} ]{Style.RESET_ALL}")
                for _, row in found.iterrows():
                    print_person(row, name)
                    total += 1

        if total == 0:
            print(f"{Fore.RED}Ничего не нашлось по «{query}» ⛔{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}Выловлено: {total} записей 🔥{Style.RESET_ALL}\n")


if __name__ == "__main__":
    main()