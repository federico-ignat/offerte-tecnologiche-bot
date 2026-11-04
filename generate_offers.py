import json
import random 

prodotti = [
  ("Monitor", "Samsung Odissey G5"),
  ("SSD", "Samsung 990 EVO 2TB"),
  ("Mouse", "Logitech MX Master 3S"),
  ("Tastiera", "Keychron K2"),
  ("RAM", "Corsair Vengeance 32GB"),
  ("CPU", "AMD Ryzen 7 9800x"),
  ("Notebook", "Lenovo Legion 5"),
  ("Smartphone", "Samsung Galaxy S25")
]

offers = []

for categoria, nome in random.sample(prodotti, 5): 
  prezzo = random.randint(50, 1500)
  sconto = random.randint(10, 50)

  offers.append({
    "categoria": categoria,
    "nome": nome,
    "prezzo": f"{prezzo}€",
    "sconto": f"-{sconto}%"
  })

with open("offers.json", "w", encoding= "utf-8") as f:
  json.dump(offers, f, indent=2, ensure_ascii=False)

print("Offerte generate correttamente!")
