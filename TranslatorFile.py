#188 file translator
from translate import Translator

with open("translate.txt","r+",encoding="utf-8") as myFile:
    fileTxt = myFile.read()
    #print(f"1....{fileTxt}")

    translator = Translator(to_lang="ja")
    translation = translator.translate(fileTxt)
    #print(f"2.....{translation}")
    #this is to write in the same text file
    #myFile.write(f"\n{translation}")

    #to write in new txt file
    with open("transJapan.txt","w",encoding="utf-8") as writeFile:
        writeFile.write(translation)

