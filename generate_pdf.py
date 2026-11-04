import json
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
   
)
from reportlab.lib.styles import getSampleStyleSheet

# Cartella output
os.makedirs("offers", exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")

pdf_path = f"offers/offerte_{today}.pdf"
latest_path = "offers/latest_offers.pdf"

# Legge dati 
with open("offers.json", "r", encoding="utf-8") as f:
  offers = json.load(f)

doc = SimpleDocTemplate(pdf_path, pagesize=A4)

style = getSampleStyleSheet()

story = []

title = Paragraph("Tech Deals Daily", style["Title"])
story.append(title)

story.append(
  Paragraph(f"Data report: {today}", style["Normal"])
)

story.append(Spacer(1, 20))

for offer in offers:
  story.appends(
    Paragraph(
      f"<b>{offer['categoria']}</b>",
      style["Heading2"]
    )
  )

story.append(
  Paragraph(
    offer["nome"],
    style["Normal"]
  )
)

story.append(
  Paragraph(
    f"Prezzo: {offer['prezzo']}",
    style["Normal"]
  )
)

story.append(
  Paragraph(
    f"Sconto: {offer['sconto']}",
    style["Normal"]
  )
)

story.append(Spacer(1, 15))

doc.build(story)

# Copia come latest
import shutil
shutil.copy(pdf_path, latest_path)

print("PDF generato!")
