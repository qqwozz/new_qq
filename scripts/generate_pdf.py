#!/usr/bin/env python3
"""
Генератор PDF-резюме для Димы Киселева.
Запуск: pip install reportlab && python scripts/generate_pdf.py
Выход: public/qq/Dima_Kiselev_Resume.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# ─── Настройки ───
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "public", "qq", "Dima_Kiselev_Resume.pdf")
INK = HexColor("#1A1A1A")
MUTED = HexColor("#5C5A55")
LIGHT = HexColor("#8A8780")
BG = HexColor("#FFFFFF")
W, H = A4

# ─── Шрифты ───
# Используем встроенные шрифты (Helvetica для латиницы, для кириллицы нужен шрифт)
# Если нужна кириллица — замени на путь к .ttf шрифту с поддержкой кириллицы
FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"


def draw_line(c, x, y, width):
    c.setStrokeColor(HexColor("#E8E5DE"))
    c.setLineWidth(0.5)
    c.line(x, y, x + width, y)


def section_title(c, y, title):
    c.setFont(FONT, 8)
    c.setFillColor(LIGHT)
    c.drawCentredString(W / 2, y, title.upper())
    draw_line(c, 50 * mm, y - 4 * mm, W - 100 * mm)
    return y - 12 * mm


def experience_entry(c, y, title, meta, bullets):
    c.setFont(FONT_BOLD, 11)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, title)
    y -= 5 * mm
    c.setFont(FONT, 9)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, meta)
    y -= 7 * mm
    c.setFont(FONT, 9.5)
    c.setFillColor(HexColor("#2C2A26"))
    for bullet in bullets:
        c.drawCentredString(W / 2, y, f"•  {bullet}")
        y -= 5 * mm
    return y - 5 * mm


def project_entry(c, y, title, meta, bullets, stack):
    c.setFont(FONT_BOLD, 11)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, title)
    y -= 5 * mm
    c.setFont(FONT, 9)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, meta)
    y -= 7 * mm
    c.setFont(FONT, 9.5)
    c.setFillColor(HexColor("#2C2A26"))
    for bullet in bullets:
        c.drawCentredString(W / 2, y, f"•  {bullet}")
        y -= 5 * mm
    y -= 2 * mm
    c.setFont(FONT, 8)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, stack)
    return y - 8 * mm


def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)
    y = H - 30 * mm

    # ─── Header ───
    c.setFont(FONT_BOLD, 28)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, "Dima Kiselev")
    y -= 8 * mm
    c.setFont(FONT, 11)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, "Backend Developer  ·  Python · Go · C++  ·  Moscow, Russia")
    y -= 6 * mm
    c.setFont(FONT, 9)
    c.drawCentredString(W / 2, y, "github.com/qqwozz  ·  t.me/onixxed  ·  offconix@gmail.com  ·  leetcode.com/u/oonixxxxx/")
    y -= 10 * mm
    draw_line(c, 50 * mm, y, W - 100 * mm)
    y -= 10 * mm

    # ─── Experience ───
    y = section_title(c, y, "Experience")
    y = experience_entry(c, y,
        "Backend Developer (intern) — VTB",
        "Internship · Sep 2024 — Dec 2024 · Moscow",
        [
            "Built a payment processing microservice — handles 500+ transactions/min",
            "Implemented REST API integrating with 4 internal bank systems, 99.9% uptime",
            "Designed PostgreSQL schemas for financial data storage, optimized queries — 30% latency reduction",
            "Set up CI/CD pipelines and Docker containerization, deploy time reduced from 40 to 5 minutes",
        ]
    )

    # ─── Education ───
    y = section_title(c, y, "Education")
    y = experience_entry(c, y,
        "Faculty of Information Technology",
        "Bachelor's · 2020 — 2024",
        ["High-load systems development, algorithms and data structures"]
    )
    y = experience_entry(c, y,
        "Additional courses",
        "2023 — present",
        ["Algorithmic Trading (Coursera), System Design (Educative), Go (Udemy)"]
    )

    # ─── Projects ───
    y = section_title(c, y, "Selected Projects")
    y = project_entry(c, y,
        "QW Pay",
        "Payment microservice · 2024",
        [
            "Payment system with multi-currency accounts and real-time conversion (200+ currencies)",
            "C++ anti-fraud engine checks velocity <1ms, Python scoring blocks suspicious transactions",
            "ACID transactions with idempotency, JWT + OTP authentication",
        ],
        "Go · C++ · Python · PostgreSQL · Redis · Docker"
    )
    y = project_entry(c, y,
        "ENF Shop",
        "Online clothing store · 2024",
        [
            "Full-featured e-commerce with catalog, filtering, smart cart and Stripe payments",
            "HTMX no-reload cart, filtering by categories, sizes, price",
            "Production-ready Docker (Nginx + Gunicorn)",
        ],
        "Django · PostgreSQL · Redis · HTMX · Stripe · Docker"
    )

    # ─── Skills ───
    y = section_title(c, y, "Core Stack")
    c.setFont(FONT, 9.5)
    c.setFillColor(HexColor("#2C2A26"))
    skills = [
        ("Backend", "Python (FastAPI, Django) · Go · C++ · gRPC · REST"),
        ("Data", "PostgreSQL · Redis · SQLite"),
        ("Infrastructure", "Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD"),
        ("Tools", "Git · Postman · VS Code · HTMX"),
    ]
    for label, value in skills:
        c.setFont(FONT_BOLD, 9)
        c.setFillColor(MUTED)
        c.drawString(50 * mm, y, label.upper())
        c.setFont(FONT, 9.5)
        c.setFillColor(HexColor("#2C2A26"))
        c.drawString(80 * mm, y, value)
        y -= 6 * mm

    # ─── Languages ───
    y -= 5 * mm
    y = section_title(c, y, "Languages")
    c.setFont(FONT, 9.5)
    c.setFillColor(HexColor("#2C2A26"))
    c.drawCentredString(W / 2, y, "Russian — C2, native  ·  English — B1")

    c.save()
    print(f"PDF saved to: {os.path.abspath(OUTPUT)}")


if __name__ == "__main__":
    generate()
