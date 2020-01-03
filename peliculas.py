import requests
import threading
import time
#import urllib.request
# agregar hilos
inicio = time.time()
def main():

  lista =["tt0087182", "tt1130884", "tt0330373", "tt0475293", "tt1438254", "tt0172495", "tt0803096",
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
  for page in lista:
    t= threading.Thread(target = descarga,args=(page,))
    t.start()
  #descarga(lista)

  print("Listo!")
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