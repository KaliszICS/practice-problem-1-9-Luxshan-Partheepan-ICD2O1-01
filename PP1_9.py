

def q1(): 
  print('"Hello World"')



def q2(): 
  word = input("Input a word: ")
  print(word.lower())  
  print(word.upper())  



def q3(): 
  words = input("Input a word that is at least 5 letters long: ")
  print(words[1:4])


def q4(): 
  letterwitho = input("Input a word: ")
  alotofsplicedletters = word[:1] + word[1:2] + word[2:3] + word[3:4] + word[4:5] + word[5:6] + word[6:7]
  therealletterwitho = alotofsplicedletters.index('o')
  print(therealletterwitho)

def q5(): 
  longword = input("Input a word: ")
  print(len(longword))



#Do not alter the following code
#Comment out the following code when running your tests

#q1()
#q2()
#q3()
#q4()
#q5()
