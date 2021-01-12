from collections import Counter


#gia na paroume san input dictionary
inf = open('text11.txt', 'r')
content = inf.read().splitlines() #gia na ginei list me split stin allagi gramis
inf_dict = dict(i.strip('(').strip(')').split(', ') for i in content) #gia na to kanoume dictionary
print(inf_dict)
print(type(inf_dict))

#gia na metrisoume poses fores xrisimopoieitai 1 kleidi

counter = Counter(inf_dict.keys())
counts_counter = Counter(counter.keys())
print(counts_counter)