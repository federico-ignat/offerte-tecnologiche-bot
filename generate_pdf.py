import json
import os
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
   
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

# Copertina

story.append(
    Paragraph(
        "TECH DEALS DAY",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        f"Edizione del {today}",
        style["Heading2"]
    )
)

story.append(Spacer(1, 200))

story.append(
    Paragraph(
        "Generato automaticamente con GitHub Actions",
        style["Normal"]
    )
)

story.append(PageBreak())

# TABELLA OFFERTE

story.append(
    Paragraph(
        "Migliori Offerte del Giorno",
        style["Title"]
    )
)

story.append(Spacer(1, 20))

data = [
    ["Categoria", "Prodotto", "Prezzo", "Sconto"]
]

for offer in offers:
    data.append([
        offer["categoria"],
        offer["nome"],
        offer["prezzo"],
        offer["sconto"]
    ] 
    )
table = Table(data, coldWidths=[90, 200, 80, 80])

table.setStyle(
    TableStyle([
        ('BACKGROUND', (0,0), (-1,0), color.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), color.white),

        ('GRID', (0,0), (-1,1), 1, color.black),
        
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        
        ('BACKGROUND', (0,1), (-1,1), color.beige)
    ])
)

story.append(table)

story.append(Spacer(1, 30))

story.append(
    Paragraph(
        f"Numero offerte trovate: {len(offers)}",
        styles["Heading3"]
    )
)

doc.build(story)

shutil.copy(pdf_path, latest_path)

print("PDF generato con successo!")
title = Paragraph("Tech Deals Daily", style["Title"])
story.append(title)

story.append(
  Paragraph(f"Data report: {today}", style["Normal"])
)

story.append(Spacer(1, 20))

for offer in offers:
  story.append(
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
