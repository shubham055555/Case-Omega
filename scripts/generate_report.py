from pathlib import Path
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from xml.sax.saxutils import escape
import re

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reports" / "final_forensic_report.md"
DOCX_OUT = ROOT / "reports" / "Case_Omega_Final_Report.docx"
PDF_OUT = ROOT / "reports" / "Case_Omega_Final_Report.pdf"

content = SOURCE.read_text(encoding="utf-8")

# ---------- CREATE DOCX ----------
doc = Document()
section = doc.sections[0]
section.top_margin = Inches(0.7)
section.bottom_margin = Inches(0.7)
section.left_margin = Inches(0.8)
section.right_margin = Inches(0.8)

normal = doc.styles["Normal"]
normal.font.name = "Arial"
normal.font.size = Pt(10)

for style_name in ["Heading 1", "Heading 2", "Heading 3"]:
    doc.styles[style_name].font.name = "Arial"
    doc.styles[style_name].font.color.rgb = RGBColor(31, 78, 121)

for line in content.splitlines():
    line = line.strip()

    if not line or line == "---":
        continue

    if line.startswith("# "):
        p = doc.add_heading(line[2:], level=1)
        if len(doc.paragraphs) <= 2:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif line.startswith("## "):
        doc.add_heading(line[3:], level=2)
    elif line.startswith("### "):
        doc.add_heading(line[4:], level=3)
    elif line.startswith("- ") or re.match(r"^\d+\.\s", line):
        text = re.sub(r"^\d+\.\s", "", line)
        text = text[2:] if text.startswith("- ") else text
        doc.add_paragraph(text, style="List Bullet")
    elif line.startswith("|"):
        continue
    else:
        text = line.replace("**", "").replace("`", "")
        doc.add_paragraph(text)

doc.save(DOCX_OUT)

# ---------- CREATE PDF ----------
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(
    name="MainTitle",
    parent=styles["Title"],
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1F4E79"),
    fontSize=19,
    leading=24,
    spaceAfter=14
))
styles.add(ParagraphStyle(
    name="SectionHeading",
    parent=styles["Heading2"],
    textColor=colors.HexColor("#1F4E79"),
    fontSize=13,
    leading=17,
    spaceBefore=10,
    spaceAfter=6
))
styles.add(ParagraphStyle(
    name="BodyTextCustom",
    parent=styles["BodyText"],
    fontSize=9,
    leading=13,
    spaceAfter=6
))

story = []

for line in content.splitlines():
    line = line.strip()

    if not line or line == "---":
        story.append(Spacer(1, 5))
        continue

    if line.startswith("# "):
        story.append(Paragraph(
            escape(line[2:]), styles["MainTitle"]
        ))
    elif line.startswith("## "):
        story.append(Paragraph(
            escape(line[3:]), styles["SectionHeading"]
        ))
    elif line.startswith("### "):
        story.append(Paragraph(
            escape(line[4:]), styles["Heading3"]
        ))
    elif line.startswith("|"):
        continue
    else:
        text = escape(line)
        text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
        text = re.sub(r"`(.*?)`", r"<font name='Courier'>\1</font>", text)
        story.append(Paragraph(text, styles["BodyTextCustom"]))

def add_page_number(canvas, document):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.drawCentredString(
        4.25 * inch, 0.4 * inch,
        f"Case Omega | Page {document.page}"
    )
    canvas.restoreState()

pdf = SimpleDocTemplate(
    str(PDF_OUT),
    pagesize=(8.27 * inch, 11.69 * inch),
    rightMargin=0.65 * inch,
    leftMargin=0.65 * inch,
    topMargin=0.65 * inch,
    bottomMargin=0.65 * inch
)

pdf.build(
    story,
    onFirstPage=add_page_number,
    onLaterPages=add_page_number
)

print("=" * 50)
print("CASE OMEGA - REPORT GENERATION")
print("=" * 50)
print("DOCX created:", DOCX_OUT)
print("PDF created:", PDF_OUT)
print("DOCX size:", DOCX_OUT.stat().st_size, "bytes")
print("PDF size:", PDF_OUT.stat().st_size, "bytes")
print("REPORT GENERATION SUCCESSFUL")
