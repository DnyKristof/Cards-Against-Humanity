import json
from translate import Translator
import re
translator = Translator(to_lang="hu")
regex = r"\bMYMEMORY\b"

with open("translations/eng/CAH Base Set Full.json","r",encoding="utf8") as f:
    eng = json.load(f)

hun = {"white" : [],"black" : []}
restofeng = {"white" : [],"black" : []}

i = 1

for card in eng["white"]:
    translation = translator.translate(card["text"])
    if re.search(regex,translation):
        restofeng["white"].append(card["text"])
        print(str(i)+". : "+card["text"])
        i+=1
        with open("translations/eng/CAH Base Sett Partitial.json","w") as f:
            f.write(json.dumps(restofeng))
    else:
        kartya = {"hun" : translation,"eng" : card["text"]}
        hun["white"].append(kartya)
        print(str(i)+". : "+kartya["hun"]+" / "+kartya["eng"])
        i+=1
        with open("translations/hu/EEK Alapszett részleges.json","w") as f:
            f.write(json.dumps(hun))
