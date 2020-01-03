import requests
import threading
import urllib.request
import time

from bs4 import BeautifulSoup
#from bs4 import bs
def procesa_html(movie_html,diccionario):
    soup = BeautifulSoup(movie_html, "html.parser")
    titulo = soup.title.string
    # print(titulo)
    resumen = soup.findAll("div", class_="inline canwrap")
    # print(resumen[0].text)
    descripcion = resumen[0].text
    descripcion.replace(",", "")
    wordlist = descripcion.split(" ")
    for word in wordlist:
        if word in diccionario:
            lista = diccionario[word]
            lista.append([titulo, descripcion])
            diccionario[word] = lista
        else:
            lista = list()
            lista.append([titulo, descripcion])
            diccionario[word] = lista


def procesa_lista(movie_list):
    diccionario = dict()
    for movie in movie_list:
        with open(movie + ".html","r",encoding = "UTF 8") as archivo:
            html = archivo.read()
        procesa_html(html,diccionario)
    return diccionario

def main():
    inicio = time.time()
    movie_list = ["tt0087182", "tt1130884", "tt0330373", "tt0475293", "tt1438254", "tt0172495", "tt0803096",
                  "tt0086250", "tt0109830", "tt0102926", "tt0816692", "tt0129290", "tt0097165", "tt0119217",
                  "tt0268978", "tt4633694", "tt0088763", "tt0071562", "tt0068646", "tt0468569", "tt4154664",
                  "tt5924572", "tt0068112", "tt0253658", "tt1677720", "tt5311514", "tt0944947", "tt1517451",
                  "tt1343092", "tt0414387", "tt2726560", "tt0281358", "tt4575576", "tt0377092", "tt0458339",
                  "tt0424774", "tt0133093", "tt0816692", "tt1375666", "tt0103064", "tt2911666", "tt0446029",
                  "tt1259521", "tt4633694", "tt2015381", "tt0347149", "tt4154796", "tt0848228", "tt2395427",
                  "tt4154756", "tt1197624", "tt8031422", "tt2724064", "tt4633694", "tt1872181", "tt1612774",
                  "tt0120915", "tt0121765", "tt0121766", "tt0086190", "tt0080684", "tt0076759", "tt2488496",
                  "tt2527336", "tt2527338", "tt0081505", "tt2582802", "tt0099685", "tt0407887", "tt0469494",
                  "tt0944947", "tt1854513", "tt5028340", "tt1477834", "tt0101188", "tt0385880", "tt4158110",
                  "tt1638002", "tt0068646", "tt0361748", "tt3110958", "tt5164214", "tt1477834", "tt0451279",
                  "tt0114327", "tt0088763", "tt0080684", "tt0086190", "tt0109830", "tt4154756", "tt3315342",
                  "tt0088763", "tt5311514", "tt0095327", "tt0110357", "tt0088763", "tt0096874", "tt0099088",
                  "tt2527338", "tt4154664", "tt01207372", "tt0167260", "tt0345950", "tt0110912", "tt2084970"]
    diccionario_movies = procesa_lista(movie_list)
    print(diccionario_movies["SpongeBob"])
    tiempo = time.time() - inicio
    print("tiempo en segundos: %f" %tiempo)

#def main():
#inicio = time.time()
#print(diccionario["Thanos'"])
#tiempo = time.time() - inicio
#print("tiempo en segundos: %f" %tiempo)


if __name__=="__main__":
    main()