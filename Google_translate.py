#import the translator module
from googletrans import Translator
trans=Translator()

#get the word from the user
word=input("Enter your word or sentence\n ")

#get the translation
answer=trans.translate(word)

print("The translation is : " + answer.text)
print("The language is : " +answer.src)
