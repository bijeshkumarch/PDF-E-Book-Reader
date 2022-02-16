import os
import PyPDF2
from googletrans import Translator
from gtts import gTTS
from playsound import  playsound

translator= Translator()


# Check for directry Ebook
mdir="Ebook/"
if(os.path.isdir(mdir)):
    pass
else:
    os.mkdir(mdir)

# Read the ebook
book='Eat-That-frog.pdf'
pdfReader=PyPDF2.PdfFileReader(book)
pages=pdfReader.numPages

# Find the language of ebook
def findlang():
    current_language=""
    for i in range(pages):
        page=pdfReader.getPage(i)
        mtext=page.extractText()
        if(mtext==""):
            i+=1
            continue
        current_language=translator.detect(mtext).lang
        break
    return current_language
# Choose destination language
langs=['hi','en','gu','ml','mr','or','pa','ta','te','ur']
print("Select your language from below options")
print("0 : Hindi\n1 : English\n2 : Gujrati\n3 : Malyalam\n4 : Marathi\n5 : Odia\n6 : Punjabi\n7 : Tamil\n8 : Telugu\n9 : Urdu")
choice=0
for i in range(3):
    choice=int(input("Enter your choice : "))
    if(choice<0 or choice>9):
        print("Incorrect choice!\nPlease try again!")
    else:
        break
choose_lang=langs[choice]
current_language=findlang()

# Creating path for specific language
mpath=mdir+book[:-4]+"_"+choose_lang+"/"
if(os.path.isdir(mpath)):
    pass
else:
    os.mkdir(mpath)


i=0
start=0
while(i<pages):
    page=pdfReader.getPage(i)
    mtext=page.extractText()
    if(mtext==""):
        i+=1
        continue

    mtext=translator.translate(mtext,src=current_language,dest=choose_lang)
    mtext=mtext.text

    if(start==0):
        start=i

    sound=mpath+"page"+str(i+1+1)+".mp3"
    if(os.path.exists(sound)):
        pass
    else:
        sound=mpath+"page"+str(i+1)+".mp3"   
        myobj=gTTS(text=mtext,lang=choose_lang,slow=False)
    
        myobj.save(sound)

    if(i>start):
        sound=mpath+"page"+str(i)+".mp3"
        playsound(sound)
    i+=1