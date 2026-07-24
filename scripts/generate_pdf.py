#!/usr/bin/env python3
"""
Генератор PDF-резюме для Димы Киселева.
Запуск: python scripts/generate_pdf.py
Выход: public/qq/Dima_Kiselev_Resume.pdf
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "public", "qq", "Dima_Kiselev_Resume.pdf")

INK = HexColor("#1A1A1A")
MUTED = HexColor("#5C5A55")
LIGHT = HexColor("#8A8780")
SOFT = HexColor("#2C2A26")
LINE_COLOR = HexColor("#E8E5DE")
W, H = A4

# ─── Register fonts (Cyrillic support) ───
FONT_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont("Arial", f"{FONT_DIR}/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", f"{FONT_DIR}/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Italic", f"{FONT_DIR}/ariali.ttf"))
pdfmetrics.registerFont(TTFont("Times", f"{FONT_DIR}/times.ttf"))
pdfmetrics.registerFont(TTFont("Times-Bold", f"{FONT_DIR}/timesbd.ttf"))
pdfmetrics.registerFont(TTFont("Times-Italic", f"{FONT_DIR}/timesi.ttf"))

# Use Times for headings (serif), Arial for body (sans-serif)
HFONT = "Times"
HFONT_BOLD = "Times-Bold"
BFONT = "Arial"
BFONT_BOLD = "Arial-Bold"
BFONT_ITALIC = "Arial-Italic"


def line(c, x, y, width):
    c.setStrokeColor(LINE_COLOR)
    c.setLineWidth(0.4)
    c.line(x, y, x + width, y)


def section(c, y, title):
    y -= 2 * mm
    c.setFont(BFONT, 8)
    c.setFillColor(LIGHT)
    c.drawCentredString(W / 2, y, title.upper())
    line(c, 50 * mm, y - 3 * mm, W - 100 * mm)
    return y - 10 * mm


def job(c, y, title, meta, bullets):
    c.setFont(HFONT_BOLD, 11)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, title)
    y -= 5 * mm
    c.setFont(BFONT, 9)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, meta)
    y -= 6 * mm
    for b in bullets:
        c.setFont(BFONT, 9.5)
        c.setFillColor(SOFT)
        c.drawCentredString(W / 2, y, f"•  {b}")
        y -= 5 * mm
    return y - 4 * mm


def project(c, y, title, meta, bullets, stack):
    c.setFont(HFONT_BOLD, 12)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, title)
    y -= 5 * mm
    c.setFont(BFONT, 9)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, meta)
    y -= 6 * mm
    for b in bullets:
        c.setFont(BFONT, 9.5)
        c.setFillColor(SOFT)
        c.drawCentredString(W / 2, y, f"•  {b}")
        y -= 5 * mm
    y -= 2 * mm
    c.setFont(BFONT, 8)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, stack)
    return y - 8 * mm


def skill_row(c, y, label, value):
    c.setFont(BFONT_BOLD, 9)
    c.setFillColor(MUTED)
    c.drawString(50 * mm, y, label.upper())
    c.setFont(BFONT, 9.5)
    c.setFillColor(SOFT)
    c.drawString(82 * mm, y, value)
    return y - 5.5 * mm


def generate():
    c = canvas.Canvas(OUTPUT, pagesize=A4)

    # ─── Header ───
    y = H - 28 * mm
    c.setFont(HFONT_BOLD, 28)
    c.setFillColor(INK)
    c.drawCentredString(W / 2, y, "Дима Киселев")
    y -= 8 * mm
    c.setFont(BFONT, 11)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, "Backend Developer  ·  Python · Go · C++ · Rust  ·  Москва, Россия")
    y -= 6 * mm
    c.setFont(BFONT, 8.5)
    c.setFillColor(MUTED)
    c.drawCentredString(W / 2, y, "github.com/qqwozz  ·  t.me/onixxed  ·  offconix@gmail.com  ·  leetcode.com/u/oonixxxxx/")
    y -= 8 * mm
    line(c, 50 * mm, y, W - 100 * mm)
    y -= 10 * mm

    # ─── Experience ───
    y = section(c, y, "Опыт")
    y = job(c, y,
        "Backend-разработчик (стажёр) — ВТБ",
        "Стажировка · Сен 2024 — Дек 2024 · Москва",
        [
            "Разрабатывал высоконагруженный API-шлюз на Go (Gin, gRPC) — >1000 RPS",
            "Разбор 10+ инцидентов L2: анализ логов в ELK, 2 решения внесены в базу знаний",
            "Дашборды в Grafana (CPU, память, latency) и алерты в Prometheus",
            "Оптимизация SQL-запросов (JOIN, оконные функции) для PostgreSQL и Oracle",
            "5+ Python-скриптов для сбора логов — сокращение ручной проверки на 40%",
            "Техническая документация, спринты и задачи в Jira/Confluence",
        ]
    )

    # ─── Education ───
    y = section(c, y, "Образование")
    y = job(c, y,
        "Факультет информационных технологий",
        "Бакалавр · 2025 — н.в.",
        ["Разработка высоконагруженных систем, алгоритмы и структуры данных"]
    )
    y = job(c, y,
        "Дополнительные курсы",
        "2022 — н.в.",
        ["Яндекс Лицей · IT Школа Samsung · Популярный курс по Git · Популярный курс по Go"]
    )

    # ─── Projects ───
    y = section(c, y, "Проекты")
    y = project(c, y,
        "QW Pay",
        "Микросервис платежей · 2024",
        [
            "Платёжная система с мультивалютными счетами и конвертацией (200+ валют)",
            "C++ антифрод-движок проверяет velocity <1мс, Python скоринг блокирует транзакции",
            "ACID-транзакции с идемпотентностью, JWT + OTP аутентификация",
        ],
        "Go · C++ · Python · PostgreSQL · Redis · Docker"
    )
    y = project(c, y,
        "ENF Shop",
        "Интернет-магазин одежды · 2024",
        [
            "E-commerce с каталогом, фильтрацией, умной корзиной и Stripe",
            "Корзина без перезагрузки (HTMX), фильтрация по категориям",
            "Production-ready Docker (Nginx + Gunicorn)",
        ],
        "Django · PostgreSQL · Redis · HTMX · Stripe · Docker"
    )
    y = project(c, y,
        "AutoAdmin",
        "API + Telegram-бот · 2024",
        [
            "API + Telegram-бот для записи клиентов на услуги с расписанием и подписками",
            "Чистая архитектура, JWT-аутентификация, SQLite, Docker",
        ],
        "Go · SQLite · Telegram Bot API · JWT · Docker"
    )
    y = project(c, y,
        "OAuth 2.0",
        "Авторизация · 2024",
        [
            "Реализация OAuth 2.0 авторизации с поддержкой Authorization Code Flow",
            "Go бэкенд, Shell-скрипты для автоматизации, HTML фронтенд",
        ],
        "Go · Shell · HTML"
    )

    # ─── Skills ───
    y = section(c, y, "Стек")
    y = skill_row(c, y, "Бэкенд", "Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST")
    y = skill_row(c, y, "Данные", "PostgreSQL · Redis · SQLite · Celery")
    y = skill_row(c, y, "Инфра", "Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD")
    y = skill_row(c, y, "Инструменты", "Git · Postman · VS Code · HTMX")

    # ─── Languages ───
    y -= 3 * mm
    y = section(c, y, "Языки")
    c.setFont(BFONT, 9.5)
    c.setFillColor(SOFT)
    c.drawCentredString(W / 2, y, "Русский — C2, родной  ·  Английский — B1")

    c.save()
    print(f"PDF: {os.path.abspath(OUTPUT)}")


if __name__ == "__main__":
    generate()
