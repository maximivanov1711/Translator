from yandex.Translater import Translater
import requests


def translate(key:str, text:str, lang:str):
    tr = requests.post('https://translate.yandex.net/api/v1.5/tr.json/translate', data={
        'lang': lang, 
        'key': key,
        'text': text,
        'format': 'plain'
    }).json()
    return tr


api_key = 'trnsl.1.1.20200122T172626Z.6f6ffd5b19a2216e.858ec74093cfc88f1ce0e66286cb55423c5832a2'
debug = False


def main():
    while True:
        request = input('->').strip()
        
        if request.startswith('/перевод'):
            text = request[9:] 
            tr = translate(api_key, text, 'ru')
            if debug: print('Debug:',tr)
            print('перевод ->', tr['text'][0])
        
        elif request.startswith('/translate'):
            text = request[11:]
            tr = translate(api_key, text, 'en')
            if debug: print('Debug:',tr)
            print('перевод ->', tr['text'][0])
        
        elif request == '/stop':
            break


if __name__ == '__main__':
    main()


