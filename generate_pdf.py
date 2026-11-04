import json
import os
import shutil
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

styles = getSampleStyleSheet()

story = []

# Copertina

story.append(
    Paragraph(
        "The Best Technology Deals",
        styles["Title"]
    )
)

stoyr.append(
    Paragraph(
        "Le migliori offerte tecnologiche del giorno",
        style["Heading2"]
    )
)
story.append(Spacer(1, 50))

story.append(
    Paragraph(
        f"Offerte analizzate: {len(offers)}",
        styles["Heading3"]
    )
)

story.append(Spacer(1, 10))

story.append(
    Paragraph(
        f"{best_offer['prezzo']} | {best_offer['sconto']}",
        styles["Normal"]
    )
)

story.append(
    Paragraph(
        "Generato automaticamente con GitHub Actions",
        styles["Normal"]
    )
)

story.append(PageBreak())

# TABELLA OFFERTE

story.append(
    Paragraph(
        "Migliori Offerte del Giorno",
        styles["Title"]
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
table = Table(data, colWidths=[90, 200, 80, 80])

table.setStyle(
    TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.darkblue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),

        ('GRID', (0,0), (-1,1), 1, colors.black),
        
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        
        ('BACKGROUND', (0,1), (-1,1), colors.beige)
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

best_offer = max(
    offers,
    key=lambda x: int(
        x["sconto"].replace("-", "").replace("%", "")
    )
)

story.append(
    Paragraph(
        "Offerta del giorno",
        styles["Title"]
    )
)

story.append(Spacer(1, 20))

story.append(
    Paragraph(
        best_offer["nome"],
        styles["Heading1"]
    )
)

story.append(
        Paragraph(
            f"Sconto: {best_offer['sconto']}",
            styles["Normal"]
        )
)

doc.build(story)

shutil.copy(pdf_path, latest_path)

print("PDF generato con successo!")

