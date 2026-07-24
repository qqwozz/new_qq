#!/usr/bin/env python3
"""
PDF Resume Generator — Dima Kiselev
Best practices applied:
- One page, clean hierarchy, F-pattern layout
- Quantified achievements, action verbs
- Professional sans-serif fonts, strategic whitespace
- ATS-friendly, no graphics/tables that break parsing
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "..", "public", "qq", "Dima_Kiselev_Resume.pdf")

# ─── Colors ───
INK = HexColor("#1A1A1A")
SOFT = HexColor("#2C2A26")
MUTED = HexColor("#5C5A55")
LIGHT = HexColor("#8A8780")
ACCENT = HexColor("#1A1A1A")
LINE = HexColor("#D4D0C8")
BG_LINE = HexColor("#EDEAE2")

W, H = A4
MARGIN_L = 22 * mm
MARGIN_R = 22 * mm
MARGIN_T = 20 * mm
CONTENT_W = W - MARGIN_L - MARGIN_R

# ─── Fonts ───
FONT_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont("Inter", f"{FONT_DIR}/arial.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bold", f"{FONT_DIR}/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Italic", f"{FONT_DIR}/ariali.ttf"))
pdfmetrics.registerFont(TTFont("Georgia", f"{FONT_DIR}/times.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", f"{FONT_DIR}/timesbd.ttf"))

SANS = "Inter"
SANS_B = "Inter-Bold"
SANS_I = "Inter-Italic"
SERIF = "Georgia"
SERIF_B = "Georgia-Bold"


class ResumeBuilder:
    def __init__(self):
        self.c = canvas.Canvas(OUTPUT, pagesize=A4)
        self.y = H - MARGIN_T

    def _line(self, y, width=CONTENT_W, color=LINE, thickness=0.4):
        self.c.setStrokeColor(color)
        self.c.setLineWidth(thickness)
        self.c.line(MARGIN_L, y, MARGIN_L + width, y)

    def _text(self, x, y, text, font=SANS, size=10, color=INK):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawString(x, y, text)

    def _center(self, y, text, font=SANS, size=10, color=INK):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawCentredString(W / 2, y, text)

    def _right(self, y, text, font=SANS, size=10, color=MUTED):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawRightString(W - MARGIN_R, y, text)

    def header(self):
        # Name
        self._center(self.y, "Дима Киселев", SERIF_B, 24, INK)
        self.y -= 8 * mm

        # Role
        self._center(self.y, "Backend Developer  ·  Python · Go · C++ · Rust", SANS, 10, MUTED)
        self.y -= 5 * mm

        # Contact line
        contacts = "github.com/qqwozz  ·  t.me/onixxed  ·  offconix@gmail.com  ·  Moscow, Russia"
        self._center(self.y, contacts, SANS, 8.5, LIGHT)
        self.y -= 6 * mm

        self._line(self.y, color=BG_LINE, thickness=0.6)
        self.y -= 6 * mm

    def section(self, title):
        self.y -= 2 * mm
        self._text(MARGIN_L, self.y, title.upper(), SANS_B, 8, MUTED)
        self.y -= 1.5 * mm
        self._line(self.y, color=BG_LINE, thickness=0.5)
        self.y -= 5 * mm

    def experience(self, title, meta, bullets):
        # Title + date on same line
        self._text(MARGIN_L, self.y, title, SANS_B, 10.5, INK)
        self._right(self.y, meta, SANS, 8.5, MUTED)
        self.y -= 5 * mm

        for b in bullets:
            self._text(MARGIN_L + 3 * mm, self.y, "·", SANS, 9, LIGHT)
            self._text(MARGIN_L + 7 * mm, self.y, b, SANS, 9, SOFT)
            self.y -= 4.2 * mm

        self.y -= 2 * mm

    def project(self, title, meta, bullets, stack):
        self._text(MARGIN_L, self.y, title, SANS_B, 10, INK)
        self._right(self.y, meta, SANS, 8, MUTED)
        self.y -= 4.5 * mm

        for b in bullets:
            self._text(MARGIN_L + 3 * mm, self.y, "·", SANS, 8.5, LIGHT)
            self._text(MARGIN_L + 7 * mm, self.y, b, SANS, 8.5, SOFT)
            self.y -= 3.8 * mm

        self.y -= 1 * mm
        self._text(MARGIN_L + 7 * mm, self.y, stack, SANS_I, 7.5, LIGHT)
        self.y -= 5 * mm

    def skills_table(self, rows):
        for label, value in rows:
            self._text(MARGIN_L, self.y, label, SANS_B, 8, MUTED)
            self._text(MARGIN_L + 42 * mm, self.y, value, SANS, 8.5, SOFT)
            self.y -= 4.5 * mm

    def languages(self, items):
        self._center(self.y, "  ·  ".join(items), SANS, 9, SOFT)
        self.y -= 5 * mm

    def build(self):
        self.header()

        # ─── Experience ───
        self.section("Опыт")
        self.experience(
            "Backend-разработчик (стажёр) — ВТБ",
            "Сен 2025 — Июн 2026",
            [
                "Разрабатывал высоконагруженный API-шлюз на Go (Gin, gRPC) — >1000 RPS",
                "Разбор 10+ инцидентов L2: анализ логов в ELK, выявление первопричин, 2 решения внесены в базу знаний",
                "Дашборды в Grafana (CPU, память, latency) и алерты в Prometheus с пороговыми значениями",
                "Оптимизация SQL-запросов (JOIN, оконные функции) для PostgreSQL и Oracle, проверка целостности после миграций",
                "5+ Python-скриптов для автоматического сбора логов — сокращение ручной проверки на 40%",
                "Техническая документация, регламенты мониторинга, спринты и задачи в Jira/Confluence",
            ]
        )

        # ─── Projects ───
        self.section("Проекты")
        self.project(
            "QW Pay",
            "2024",
            [
                "Платёжная система с мультивалютными счетами и конвертацией (200+ валют)",
                "C++ антифрод-движок: velocity <1мс, Python скоринг блокирует транзакции",
                "ACID-транзакции, идемпотентность, JWT + OTP аутентификация",
            ],
            "Go · C++ · Python · PostgreSQL · Redis · Docker"
        )
        self.project(
            "ENF Shop",
            "2024",
            [
                "E-commerce с каталогом, фильтрацией, умной корзиной и Stripe-платежами",
                "Корзина без перезагрузки (HTMX), фильтрация по категориям, размерам, цене",
                "Production-ready Docker (Nginx + Gunicorn)",
            ],
            "Django · PostgreSQL · Redis · HTMX · Stripe · Docker"
        )
        self.project(
            "AutoAdmin",
            "2024",
            [
                "API + Telegram-бот для записи клиентов на услуги с расписанием и подписками",
                "Чистая архитектура, JWT-аутентификация, SQLite, Docker",
            ],
            "Go · SQLite · Telegram Bot API · JWT · Docker"
        )
        self.project(
            "OAuth 2.0",
            "2024",
            [
                "Реализация OAuth 2.0 авторизации с поддержкой Authorization Code Flow",
                "Go бэкенд, Shell-скрипты для автоматизации, HTML фронтенд",
            ],
            "Go · Shell · HTML"
        )

        # ─── Skills ───
        self.section("Стек")
        self.skills_table([
            ("Бэкенд", "Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST"),
            ("Данные", "PostgreSQL · Redis · SQLite · Celery"),
            ("Инфра", "Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD"),
            ("Инструменты", "Git · Postman · VS Code · HTMX · OAuth 2.0 · Stripe API"),
        ])
        self.y -= 1 * mm

        # ─── Education ───
        self.section("Образование")
        self._text(MARGIN_L, self.y, "Факультет информационных технологий", SANS_B, 9.5, INK)
        self._right(self.y, "2025 — н.в.", SANS, 8, MUTED)
        self.y -= 4 * mm
        self._text(MARGIN_L + 3 * mm, self.y, "Бакалавр · Высоконагруженные системы, алгоритмы и структуры данных", SANS, 8.5, SOFT)
        self.y -= 5 * mm

        self._text(MARGIN_L, self.y, "Дополнительные курсы", SANS_B, 9.5, INK)
        self._right(self.y, "2022 — н.в.", SANS, 8, MUTED)
        self.y -= 4 * mm
        courses = "Яндекс Лицей · IT Школа Samsung · Version Control with Git (Coursera) · Programming with Google Go (Coursera) · Grokking System Design Interview (Educative)"
        self._text(MARGIN_L + 3 * mm, self.y, courses, SANS, 8, SOFT)
        self.y -= 6 * mm

        # ─── Languages ───
        self.section("Языки")
        self.languages(["Русский — C2, родной", "Английский — B1"])

        self.c.save()
        print(f"PDF: {os.path.abspath(OUTPUT)}")


if __name__ == "__main__":
    ResumeBuilder().build()
