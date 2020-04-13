from translate import Translator
# by using this with construct you do not have to manually close the file
translate = Translator(to_lang='ja')
with open('test.txt', mode='r') as file:
    translated = translate.translate(file.read())
    print(translated)




