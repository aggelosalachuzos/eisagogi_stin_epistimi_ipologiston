file = open('text13.txt' , 'r')
d = file.read()

data = d.split()
print(data)

for word1 in data:
    for word2 in data:
     if len(word1)+len(word2)==20:
         print(word1+word2)
         print(len(word1+word2))

         

            
