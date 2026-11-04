import json
import random 

prodotti = [
  ("Monitor", "Samsung Odissey G5"),
  ("SSD", "Samsung 990 EVO 2TB"),
  ("Mouse", "Logitech MX Master 3S"),
  ("Tastiera", "Keychron K2"),
  ("RAM", "Corsair Vengeance 32GB"),
  ("CPU", "AMD Ryzen 7 9800x"),
]

offers = []

for cateoria, nome in random.sample(prodotti, 4): 
  prezzo = random.randint(50, 500)

  offers.append({
    "categoria": categoria,
    "nome": nome,
    "prezzo": f"{prezzo}€",
    "sconto": f"-{sconto}%"
  })

with open("offers.json", "w", encoding= "utf-8") as f:
  json.dump(offers, f, indent=2, ensure_ascii=False)

print("offers.json aggiornato!")
