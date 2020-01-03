from bs4 import BeautifulSoup
import time
import concurrent.futures
import pickle

def procesa_html(movie_html, diccionario):#ERROR
    soup = BeautifulSoup(movie_html, "html.parser")
    titulo = soup.title.text #cambio titulo = soup.title.string
    # print(titulo)
    resumen = soup.findAll("div", class_="inline canwrap")
    # print(resumen[0].text)
    descripcion = resumen[0].text
    descripcion.replace(",", "")
    wordlist = descripcion.split(" ")
    for word in wordlist:
        if word in diccionario:
            lista = diccionario[word]
            diccionario_peliculas= diccionario[word]
          #  if titulo not in diccionario_peliculas:
           #     diccionario_peliculas[titulo] = descripcion
           # diccionario[word] = diccionario_peliculas
            lista.append([titulo, descripcion])
            diccionario[word] = lista

        else:
            #diccionario_peliculas = dict()
            lista = list()
            lista.append([titulo, descripcion])
            diccionario[word] = lista


def procesa_lista(movie_list):
    diccionario = dict()
    hilos = []  # hilos = list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        for movie in movie_list:
            with open(movie + ".html", "r",encoding="UTF-8") as archivo:
                html = archivo.read()
            e = executor.submit(procesa_html, html, diccionario)
            hilos.append(e)
    return diccionario


def main():#Procesa lista
    inicio = time.time()
    movie_list = ["tt0087182", "tt1130884", "tt0330373", "tt0475293", "tt1438254", "tt0172495", "tt0803096"]

    diccionario_movies = procesa_lista(movie_list)

    #usuario_palabra = input("Palabra a buscar?")
    #print(diccionario_movies["Hogwarts"])
    #tiempo = time.time() - inicio
    #print("tiempo en segundos: %f" % tiempo)
    print(len(diccionario_movies))
    print(type(diccionario_movies))
    for k, v in diccionario_movies.items():
        print(type(k))
        print(type(v))

    with open("diccionariooo.pkl","wb")as archivo:#leer el archivo

        pickle.dump(diccionario_movies,archivo,protocol=pickle.HIGHEST_PROTOCOL)
        print("El archivo diccionario fue escrito")
        print(len(diccionario_movies))

    with open("diccionariooo.pkl", "rb")as archivo:

        d = pickle.load(archivo)
        print(d)
        word = input("Introduce una palabra: ")
        if (word in d):
            res = d[word]
            for r in res:
                print(r[0])  # titulo
                print(r[1])  # descripcion








# def main():
# inicio = time.time()
# print(diccionario["Thanos'"])
# tiempo = time.time() - inicio
# print("tiempo en segundos: %f" %tiempo)


if __name__ == "__main__":
   main()
