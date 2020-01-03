import requests
import threading
import time
import concurrent.futures

#import urllib.request
# agregar hilos
inicio = time.time()
def main():
    #
    with open("lista_peliculas","r") as archivo:
        peliculas = archivo.read()
    lista_peliculas = peliculas.split("\n")

    for page in lista_peliculas:
        t= threading.Thread(target = descarga,args=(page,))
        t.start()
    #descarga(lista)

    print("Listo!")
def procesa_lista(movie_list):
    diccionario = dict()
    hilos = []  # hilos = list()
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        for movie in movie_list:
            with open(movie + ".html", "r",encoding="utf8") as archivo:
                html = archivo.read()
            e = executor.submit(main, html, diccionario)
            hilos.append(e)
    return diccionario

def descarga(codigo):
  URL = "https://www.imdb.com/title/" + codigo
  try:
    #respuesta = urllib.request.urlopen(URL)
    respuesta = requests.get(URL)
    pagina = respuesta.content
    archivo_html = codigo + ".html"
    with open(archivo_html,"wb") as archivo:
      #wb from write byte?
      archivo.write(pagina)
    print("archivo %s guardado" % archivo_html)

  except OSError as e:
    print(archivo_html)
    print(e.strerror)



if __name__=="__main__":
  main()