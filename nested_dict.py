import collections
d = collections.defaultdict(dict)
import pickle


fin = open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\Iwama_dojos_tidy.txt",'r')

for i in fin:
    i.split('|')
    d[i.split('|')[0]] = {}

fin.close()
fin = open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL\Iwama_dojos_tidy.txt",'r')

for i in fin:
    i.split('|')
    d[i.split('|')[0]][i.split('|')[1].strip()] = i.split('|')[2].strip()

print (d)

pickle_out = open(r"C:\Users\gatesk\Documents\___aaa___PERSONAL//dojodict.pickle", "wb")
pickle.dump(d, pickle_out)
pickle_out.close()