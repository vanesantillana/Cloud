#Usando Librerias
#from collections import Counter
#print(Counter(word_list).most_common())

with open('lorem999.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

def clean(text):
    for char in '-.,;"\'\n':
        text=text.replace(char,' ')
    text = text.lower()
    #Obtengo una lista de palabras
    return text.split()

def imprimir (list):
    for i in list:
        print(i + ' -> ' + str(list[i]))

def wordCount(w_list):
    d = {}
    for word in w_list: 
        d[word] = d.get(word, 0) + 1
    return d

word_list = clean(data)
result = wordCount(word_list)
imprimir(result)