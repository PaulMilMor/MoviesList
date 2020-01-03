from bs4 import BeautifulSoup
import time
import concurrent.futures
import pickle

def main():#Procesa lista
    with open("diccionario.pkl", "rb")as archivo:
        d = pickle.load(archivo)
        word = input("Introduce una palabra: ")
        if (word in d):
            res = d[word]
            for k,v in res.item():
                print(k)

        else:
            print("palabra no encontrada")
    #while(len(llave)>0)

"""
do: 
    llave = input("Introduce una palabra: ")
    if(len(llave==0))
        break
    else
        if(llave in d)
            resultados = d[llave]
"""
if __name__ == "__main__":
   main()
