import json
from translate import Translator
import re
translator = Translator(to_lang="hu")
regex = r"\bMYMEMORY\b"

with open("translations/eng/CAH Base Set Full.json","r",encoding="utf8") as f:
    eng = json.load(f)

restofeng = {"white" : [],"black" : []}

with open("translations/hu/EEK Alapszett részleges.json","r",encoding="utf8") as f:
    hun = json.load(f)

i = 1

for card in eng["black"]:
    card=card["text"]
    translation = translator.translate(card)
    if re.search(regex,translation):
        restofeng["black"].append(card)
        print(str(i)+". : "+card)
        i+=1
        with open("translations/eng/CAH Base Sett Partitial.json","w") as f:
            f.write(json.dumps(restofeng))
    else:
        kartya = {"hun" : translation,"eng" : card}
        hun["black"].append(kartya)
        print(str(i)+". : "+kartya["hun"] +" / "+kartya["eng"])
        i+=1
        with open("translations/hu/EEK Alapszett részleges.json","w") as f:
            f.write(json.dumps(hun))    
    
