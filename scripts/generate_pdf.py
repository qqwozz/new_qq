#!/usr/bin/env python3
"""
PDF Resume Generator — Dima Kiselev (RU + EN)
Generates two PDFs: Russian and English versions.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PUBLIC_DIR = os.path.join(SCRIPT_DIR, "..", "public", "qq")

INK = HexColor("#1A1A1A")
SOFT = HexColor("#2C2A26")
MUTED = HexColor("#5C5A55")
LIGHT = HexColor("#8A8780")
BG_LINE = HexColor("#EDEAE2")

W, H = A4
ML = 22 * mm
MR = 22 * mm
MT = 20 * mm
CW = W - ML - MR

FONT_DIR = "C:/Windows/Fonts"
pdfmetrics.registerFont(TTFont("Inter", f"{FONT_DIR}/arial.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Bold", f"{FONT_DIR}/arialbd.ttf"))
pdfmetrics.registerFont(TTFont("Inter-Italic", f"{FONT_DIR}/ariali.ttf"))
pdfmetrics.registerFont(TTFont("Georgia", f"{FONT_DIR}/times.ttf"))
pdfmetrics.registerFont(TTFont("Georgia-Bold", f"{FONT_DIR}/timesbd.ttf"))

S, SB, SI, G, GB = "Inter", "Inter-Bold", "Inter-Italic", "Georgia", "Georgia-Bold"

# ─── Content ───
CONTENT = {
    "ru": {
        "name": "Дима Киселев",
        "role": "Backend-разработчик  ·  Python · Go · C++ · Rust",
        "contact": "github.com/qqwozz  ·  t.me/onixxed  ·  offconix@gmail.com  ·  Москва, Россия",
        "exp_label": "Опыт",
        "exp_title": "Backend-разработчик (стажёр) — ВТБ",
        "exp_meta": "Сен 2025 — Июн 2026",
        "exp_bullets": [
            "Разрабатывал высоконагруженный API-шлюз на Go (Gin, gRPC) — >1000 RPS",
            "Разбор 10+ инцидентов L2: анализ логов в ELK, выявление первопричин, 2 решения внесены в базу знаний",
            "Дашборды в Grafana (CPU, память, latency) и алерты в Prometheus с пороговыми значениями",
            "Оптимизация SQL-запросов (JOIN, оконные функции) для PostgreSQL и Oracle, проверка целостности после миграций",
            "5+ Python-скриптов для автоматического сбора логов — сокращение ручной проверки на 40%",
            "Техническая документация, регламенты мониторинга, спринты и задачи в Jira/Confluence",
        ],
        "proj_label": "Проекты",
        "projects": [
            ("QW Pay", "2024", [
                "Платёжная система с мультивалютными счетами и конвертацией (200+ валют)",
                "C++ антифрод-движок: velocity <1мс, Python скоринг блокирует транзакции",
                "ACID-транзакции, идемпотентность, JWT + OTP аутентификация",
            ], "Go · C++ · Python · PostgreSQL · Redis · Docker"),
            ("ENF Shop", "2024", [
                "E-commerce с каталогом, фильтрацией, умной корзиной и Stripe-платежами",
                "Корзина без перезагрузки (HTMX), фильтрация по категориям, размерам, цене",
                "Production-ready Docker (Nginx + Gunicorn)",
            ], "Django · PostgreSQL · Redis · HTMX · Stripe · Docker"),
            ("AutoAdmin", "2024", [
                "API + Telegram-бот для записи клиентов на услуги с расписанием и подписками",
                "Чистая архитектура, JWT-аутентификация, SQLite, Docker",
            ], "Go · SQLite · Telegram Bot API · JWT · Docker"),
            ("OAuth 2.0", "2024", [
                "Реализация OAuth 2.0 авторизации с поддержкой Authorization Code Flow",
                "Go бэкенд, Shell-скрипты для автоматизации, HTML фронтенд",
            ], "Go · Shell · HTML"),
        ],
        "skills_label": "Стек",
        "skills": [
            ("Бэкенд", "Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST"),
            ("Данные", "PostgreSQL · Redis · SQLite · Celery"),
            ("Инфра", "Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD"),
            ("Инструменты", "Git · Postman · VS Code · HTMX · OAuth 2.0 · Stripe API"),
        ],
        "edu_label": "Образование",
        "edu1_title": "Факультет информационных технологий",
        "edu1_meta": "2025 — н.в.",
        "edu1_desc": "Бакалавр · Высоконагруженные системы, алгоритмы и структуры данных",
        "edu2_title": "Дополнительные курсы",
        "edu2_meta": "2022 — н.в.",
        "edu2_desc": "Яндекс Лицей · IT Школа Samsung · Version Control with Git (Coursera) · Programming with Google Go (Coursera) · Grokking System Design Interview (Educative)",
        "lang_label": "Языки",
        "languages": ["Русский — C2, родной", "Английский — B1"],
    },
    "en": {
        "name": "Dima Kiselev",
        "role": "Backend Developer  ·  Python · Go · C++ · Rust",
        "contact": "github.com/qqwozz  ·  t.me/onixxed  ·  offconix@gmail.com  ·  Moscow, Russia",
        "exp_label": "Experience",
        "exp_title": "Backend Developer (intern) — VTB",
        "exp_meta": "Sep 2025 — Jun 2026",
        "exp_bullets": [
            "Built high-load API gateway on Go (Gin, gRPC) — handling >1000 RPS",
            "Resolved 10+ L2 incidents: ELK log analysis, root cause identification, 2 solutions added to knowledge base",
            "Grafana dashboards (CPU, memory, latency) and Prometheus alerts with threshold values",
            "Optimized complex SQL queries (JOINs, window functions) for PostgreSQL and Oracle, post-migration data integrity checks",
            "5+ Python scripts for automated log collection — reduced manual review time by 40%",
            "Technical documentation, monitoring runbooks, sprint planning and Jira/Confluence task tracking",
        ],
        "proj_label": "Selected Projects",
        "projects": [
            ("QW Pay", "2024", [
                "Payment system with multi-currency accounts and real-time conversion (200+ currencies)",
                "C++ anti-fraud engine: velocity <1ms, Python scoring blocks suspicious transactions",
                "ACID transactions, idempotency, JWT + OTP authentication",
            ], "Go · C++ · Python · PostgreSQL · Redis · Docker"),
            ("ENF Shop", "2024", [
                "E-commerce with catalog, filtering, smart cart and Stripe payments",
                "HTMX no-reload cart, filtering by categories, sizes, price",
                "Production-ready Docker (Nginx + Gunicorn)",
            ], "Django · PostgreSQL · Redis · HTMX · Stripe · Docker"),
            ("AutoAdmin", "2024", [
                "API + Telegram bot for client appointment scheduling with subscriptions",
                "Clean architecture, JWT auth, SQLite, Docker",
            ], "Go · SQLite · Telegram Bot API · JWT · Docker"),
            ("OAuth 2.0", "2024", [
                "OAuth 2.0 authorization implementation with Authorization Code Flow",
                "Go backend, Shell automation scripts, HTML frontend",
            ], "Go · Shell · HTML"),
        ],
        "skills_label": "Core Stack",
        "skills": [
            ("Backend", "Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST"),
            ("Data", "PostgreSQL · Redis · SQLite · Celery"),
            ("Infra", "Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD"),
            ("Tools", "Git · Postman · VS Code · HTMX · OAuth 2.0 · Stripe API"),
        ],
        "edu_label": "Education",
        "edu1_title": "Faculty of Information Technology",
        "edu1_meta": "2025 — present",
        "edu1_desc": "Bachelor's · High-load systems, algorithms and data structures",
        "edu2_title": "Additional courses",
        "edu2_meta": "2022 — present",
        "edu2_desc": "Yandex Lyceum · IT School Samsung · Version Control with Git (Coursera) · Programming with Google Go (Coursera) · Grokking System Design Interview (Educative)",
        "lang_label": "Languages",
        "languages": ["Russian — C2, native", "English — B1"],
    },
}


class ResumeBuilder:
    def __init__(self, lang):
        self.d = CONTENT[lang]
        suffix = "" if lang == "ru" else "_en"
        path = os.path.join(PUBLIC_DIR, f"Dima_Kiselev_Resume{suffix}.pdf")
        self.c = canvas.Canvas(path, pagesize=A4)
        self.y = H - MT
        self.path = path

    def _line(self, y, width=CW, color=BG_LINE, thickness=0.5):
        self.c.setStrokeColor(color)
        self.c.setLineWidth(thickness)
        self.c.line(ML, y, ML + width, y)

    def _text(self, x, y, text, font=S, size=10, color=INK):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawString(x, y, text)

    def _center(self, y, text, font=S, size=10, color=INK):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawCentredString(W / 2, y, text)

    def _right(self, y, text, font=S, size=10, color=MUTED):
        self.c.setFont(font, size)
        self.c.setFillColor(color)
        self.c.drawRightString(W - MR, y, text)

    def header(self):
        self._center(self.y, self.d["name"], GB, 24, INK)
        self.y -= 8 * mm
        self._center(self.y, self.d["role"], S, 10, MUTED)
        self.y -= 5 * mm
        self._center(self.y, self.d["contact"], S, 8.5, LIGHT)
        self.y -= 6 * mm
        self._line(self.y)
        self.y -= 6 * mm

    def section(self, title):
        self.y -= 2 * mm
        self._text(ML, self.y, title.upper(), SB, 8, MUTED)
        self.y -= 1.5 * mm
        self._line(self.y, thickness=0.5)
        self.y -= 5 * mm

    def experience(self):
        self._text(ML, self.y, self.d["exp_title"], SB, 10.5, INK)
        self._right(self.y, self.d["exp_meta"], S, 8.5, MUTED)
        self.y -= 5 * mm
        for b in self.d["exp_bullets"]:
            self._text(ML + 3 * mm, self.y, "·", S, 9, LIGHT)
            self._text(ML + 7 * mm, self.y, b, S, 9, SOFT)
            self.y -= 4.2 * mm
        self.y -= 2 * mm

    def projects(self):
        for title, meta, bullets, stack in self.d["projects"]:
            self._text(ML, self.y, title, SB, 10, INK)
            self._right(self.y, meta, S, 8, MUTED)
            self.y -= 4.5 * mm
            for b in bullets:
                self._text(ML + 3 * mm, self.y, "·", S, 8.5, LIGHT)
                self._text(ML + 7 * mm, self.y, b, S, 8.5, SOFT)
                self.y -= 3.8 * mm
            self.y -= 1 * mm
            self._text(ML + 7 * mm, self.y, stack, SI, 7.5, LIGHT)
            self.y -= 5 * mm

    def skills(self):
        for label, value in self.d["skills"]:
            self._text(ML, self.y, label, SB, 8, MUTED)
            self._text(ML + 42 * mm, self.y, value, S, 8.5, SOFT)
            self.y -= 4.5 * mm
        self.y -= 1 * mm

    def education(self):
        self._text(ML, self.y, self.d["edu1_title"], SB, 9.5, INK)
        self._right(self.y, self.d["edu1_meta"], S, 8, MUTED)
        self.y -= 4 * mm
        self._text(ML + 3 * mm, self.y, self.d["edu1_desc"], S, 8.5, SOFT)
        self.y -= 5 * mm
        self._text(ML, self.y, self.d["edu2_title"], SB, 9.5, INK)
        self._right(self.y, self.d["edu2_meta"], S, 8, MUTED)
        self.y -= 4 * mm
        self._text(ML + 3 * mm, self.y, self.d["edu2_desc"], S, 8, SOFT)
        self.y -= 6 * mm

    def languages(self):
        self._center(self.y, "  ·  ".join(self.d["languages"]), S, 9, SOFT)
        self.y -= 5 * mm

    def build(self):
        self.header()
        self.section(self.d["exp_label"])
        self.experience()
        self.section(self.d["proj_label"])
        self.projects()
        self.section(self.d["skills_label"])
        self.skills()
        self.section(self.d["edu_label"])
        self.education()
        self.section(self.d["lang_label"])
        self.languages()
        self.c.save()
        print(f"PDF: {os.path.abspath(self.path)}")


if __name__ == "__main__":
    ResumeBuilder("ru").build()
    ResumeBuilder("en").build()
    print("Done — both RU and EN PDFs generated.")
