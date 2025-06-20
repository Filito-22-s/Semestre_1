digimones = [
    {
        "id": 1,
        "name": "Agumon",
        "type": "Reptile",
        "images": "https://digi-api.com/images/digimon/w/Agumon.png"
   },
   {
       "id": 2,
       "name": "Airdramon",
       "type": "Mythical Beast",
       "images": "https://digi-api.com/images/digimon/w/Airdramon.png",
   }
]
for digimon in digimones:
    print (f"\n {digimon}")
    print ("--------------------------------------------------------------------------------------------------------------------------")
    print (digimon["id"])
    print (digimon["name"])
    print (digimon["type"])
    print (digimon["images"])