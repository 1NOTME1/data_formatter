from datetime import datetime

def konwertuj_date(data_str):
    formaty = [
        '%d.%m.%Y',
        '%d-%m-%Y',
        '%Y-%m-%d'
    ]
    
    for format in formaty:
        try:
            data = datetime.strptime(data_str.strip(), format)
            return data.strftime('%Y-%m-%d')
        except ValueError:
            continue
    return ''  


def przetworz_plik(plik_txt, plik_wyjsciowy):
    with open(plik_txt, 'r', encoding='utf-8') as plik:
        daty = plik.readlines()

    nowe_daty = []
    for data in daty:
        if data.strip():  # Sprawdź, czy linia nie jest pusta
            nowe_daty.append(konwertuj_date(data))
        else:
            nowe_daty.append('')  # Dodaj pustą linię

    with open(plik_wyjsciowy, 'w', encoding='utf-8') as plik:
        for data in nowe_daty:
            plik.write(data + '\n')

if __name__ == '__main__':
    sciezka_do_pliku = r'C:\Users\USER_NAME\Desktop\daty.txt'  # Podmień na ścieżkę do Twojego pliku
    sciezka_do_pliku_wyjsciowego = r'C:\Users\USER_NAME\\nowe_daty.txt'  # Podmień na ścieżkę, gdzie chcesz zapisać przetworzone daty
    przetworz_plik(sciezka_do_pliku, sciezka_do_pliku_wyjsciowego)
