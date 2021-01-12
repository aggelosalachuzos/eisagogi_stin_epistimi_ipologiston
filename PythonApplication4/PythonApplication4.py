
import string 
import random
#gia na xorisei to keimeno se triades
def splitTextToTriplet(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 3]) for i in range(0, len(words), 3)]
    return(grouped_words)

#gia eisodo arxeiou 
file =open('text4.txt' , 'r')
data =file.read()
print(splitTextToTriplet(data))
 
 #gia random string generaton
length=100
randomstr = ''.join(random.choices(string.ascii_letters+string.digits,k=length))
print("this is a random string!!: ",randomstr)

