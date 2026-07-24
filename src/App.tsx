import { useState, useEffect, useCallback, useRef } from 'react'

type Lang = 'ru' | 'en'

const t: Record<Lang, Record<string, string>> = {
  ru: {
    name: 'Дима Киселев',
    role: 'Backend-разработчик',
    stack: 'Python · Go · C++ · Rust',
    location: 'Москва, Россия',
    bio: 'Пишу код, который работает быстро и не ломается. Микросервисы, API, high-load — Python, Go, C++, Rust. Банковская инфраструктура в ВТБ.',
    skillsLabel: 'Основной стек',
    backend: 'Бэкенд',
    backendVal: 'Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST',
    data: 'Данные',
    dataVal: 'PostgreSQL · Redis · SQLite · Celery',
    infra: 'Инфраструктура',
    infraVal: 'Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD',
    tools: 'Инструменты',
    toolsVal: 'Git · Postman · VS Code · HTMX · OAuth 2.0 · Stripe API',
    expLabel: 'Опыт',
    vtb: 'Backend-разработчик (стажёр) — ВТБ',
    vtbMeta: 'Стажировка · Сен 2024 — Дек 2024 · Москва',
    v1: 'Разрабатывал высоконагруженный API-шлюз на Go (Gin, gRPC) — >1000 RPS',
    v2: 'Разбор 10+ инцидентов L2: анализ логов в ELK, выявление первопричин, 2 решения внесены в базу знаний',
    v3: 'Дашборды в Grafana (CPU, память, latency) и алерты в Prometheus с пороговыми значениями',
    v4: 'Оптимизация SQL-запросов (JOIN, оконные функции) для PostgreSQL и Oracle, проверка целостности после миграций',
    v5: '5+ Python-скриптов для автоматического сбора логов — сокращение ручной проверки на 40%',
    v6: 'Техническая документация, регламенты мониторинга, спринты и задачи в Jira/Confluence',
    eduLabel: 'Образование',
    edu1: 'Факультет информационных технологий',
    edu1Meta: 'Бакалавр · 2025 — н.в.',
    edu1d: 'Разработка высоконагруженных систем, алгоритмы и структуры данных',
    edu2: 'Дополнительные курсы',
    edu2Meta: '2022 — н.в.',
    edu2d: 'Яндекс Лицей · IT Школа Samsung · Популярный курс по Git · Популярный курс по Go',
    projectsLabel: 'Избранные проекты',
    p2: 'Микросервис платежей',
    p2d1: 'Платёжная система с мультивалютными счетами и конвертацией по реальным курсам (200+ валют)',
    p2d2: 'C++ антифрод-движок проверяет velocity <1мс, Python скоринг блокирует подозрительные транзакции',
    p2d3: 'ACID-транзакции с идемпотентностью, JWT + OTP аутентификация',
    p3: 'Интернет-магазин одежды',
    p3d1: 'Полнофункциональный e-commerce с каталогом, фильтрацией, умной корзиной и приёмом платежей через Stripe',
    p3d2: 'Корзина без перезагрузки (HTMX), фильтрация по категориям, размерам, цене',
    p3d3: 'Production-ready Docker (Nginx + Gunicorn)',
    p4: 'AutoAdmin',
    p4d1: 'API + Telegram-бот для записи клиентов на услуги с расписанием и подписками',
    p4d2: 'Чистая архитектура, JWT-аутентификация, SQLite, Docker',
    p5: 'OAuth 2.0',
    p5d1: 'Реализация OAuth 2.0 авторизации с поддержкой Authorization Code Flow',
    p5d2: 'Go бэкенд, Shell-скрипты для автоматизации, HTML фронтенд',
    code: 'Код',
    alsoText: 'AI Chat Bot — NLP чат-бот на GigaChat (Python, Streamlit). Perl Log Analyzer — анализатор логов (Perl).',
    alsoMore: 'Все проекты на',
    contactLabel: 'Связаться',
    contactHeadline: 'Давайте создадим\nчто-нибудь вместе.',
    contactSub: 'Открыт для проектов и сотрудничества.',
    contactEmail: 'Написать',
    downloadCv: 'Скачать резюме',
    langLabel: 'Языки',
    ruLang: 'Русский',
    ruLvl: 'C2, родной',
    enLang: 'Английский',
    enLvl: 'B1',
    footerMeta: `Дима Киселев · Москва · ${new Date().getFullYear()}`,
  },
  en: {
    name: 'Dima Kiselev',
    role: 'Backend Developer',
    stack: 'Python · Go · C++ · Rust',
    location: 'Moscow, Russia',
    bio: 'I write code that runs fast and doesn\'t break. Microservices, APIs, high-load — Python, Go, C++, Rust. Built banking infrastructure at VTB.',
    skillsLabel: 'Core Stack',
    backend: 'Backend',
    backendVal: 'Python (FastAPI, Django, Aiogram) · Go (Gin) · C++ · Rust · gRPC · REST',
    data: 'Data',
    dataVal: 'PostgreSQL · Redis · SQLite · Celery',
    infra: 'Infrastructure',
    infraVal: 'Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD',
    tools: 'Tools',
    toolsVal: 'Git · Postman · VS Code · HTMX · OAuth 2.0 · Stripe API',
    expLabel: 'Experience',
    vtb: 'Backend Developer (intern) — VTB',
    vtbMeta: 'Internship · Sep 2024 — Dec 2024 · Moscow',
    v1: 'Built high-load API gateway on Go (Gin, gRPC) — handling >1000 RPS',
    v2: 'Resolved 10+ L2 incidents: ELK log analysis, root cause identification, 2 solutions added to knowledge base',
    v3: 'Grafana dashboards (CPU, memory, latency) and Prometheus alerts with threshold values',
    v4: 'Optimized complex SQL queries (JOINs, window functions) for PostgreSQL and Oracle, post-migration data integrity checks',
    v5: '5+ Python scripts for automated log collection — reduced manual review time by 40%',
    v6: 'Technical documentation, monitoring runbooks, sprint planning and Jira/Confluence task tracking',
    eduLabel: 'Education',
    edu1: 'Faculty of Information Technology',
    edu1Meta: "Bachelor's · 2020 — 2024",
    edu1d: 'High-load systems development, algorithms and data structures',
    edu2: 'Additional courses',
    edu2Meta: '2022 — present',
    edu2d: 'Yandex Lyceum · IT School Samsung · Popular Git Course · Popular Go Course',
    projectsLabel: 'Selected Projects',
    p2: 'Payment microservice',
    p2d1: 'Payment system with multi-currency accounts and real-time conversion (200+ currencies)',
    p2d2: 'C++ anti-fraud engine checks velocity <1ms, Python scoring blocks suspicious transactions',
    p2d3: 'ACID transactions with idempotency, JWT + OTP authentication',
    p3: 'Online clothing store',
    p3d1: 'Full-featured e-commerce with catalog, filtering, smart cart and Stripe payments',
    p3d2: 'HTMX no-reload cart, filtering by categories, sizes, price',
    p3d3: 'Production-ready Docker (Nginx + Gunicorn)',
    p4: 'AutoAdmin',
    p4d1: 'API + Telegram bot for client appointment scheduling with subscriptions',
    p4d2: 'Clean architecture, JWT auth, SQLite, Docker',
    p5: 'OAuth 2.0',
    p5d1: 'OAuth 2.0 authorization implementation with Authorization Code Flow',
    p5d2: 'Go backend, Shell automation scripts, HTML frontend',
    code: 'Source',
    alsoText: 'AI Chat Bot — NLP chatbot on GigaChat (Python, Streamlit). Perl Log Analyzer — log analysis (Perl).',
    alsoMore: 'All projects on',
    contactLabel: 'Contact',
    contactHeadline: "Let's build\nsomething together.",
    contactSub: 'Open to projects and collaboration.',
    contactEmail: 'Get in touch',
    downloadCv: 'Download CV',
    langLabel: 'Languages',
    ruLang: 'Russian',
    ruLvl: 'C2, native',
    enLang: 'English',
    enLvl: 'B1',
    footerMeta: `Dima Kiselev · Moscow · ${new Date().getFullYear()}`,
  },
}

function Typewriter({ text, speed = 25 }: { text: string; speed?: number }) {
  const [displayed, setDisplayed] = useState(text)
  const [done, setDone] = useState(true)
  const indexRef = useRef(text.length)
  const prevTextRef = useRef(text)

  useEffect(() => {
    if (prevTextRef.current === text) return
    prevTextRef.current = text
    setDisplayed('')
    setDone(false)
    indexRef.current = 0

    const interval = setInterval(() => {
      indexRef.current++
      if (indexRef.current <= text.length) {
        setDisplayed(text.slice(0, indexRef.current))
      } else {
        setDone(true)
        clearInterval(interval)
      }
    }, speed)

    return () => clearInterval(interval)
  }, [text, speed])

  return (
    <span>
      {displayed}
      {!done && <span className="cursor">|</span>}
    </span>
  )
}

function App() {
  const [lang, setLang] = useState<Lang>('ru')
  const [showTop, setShowTop] = useState(false)
  const s = t[lang]

  useEffect(() => {
    document.documentElement.lang = lang
  }, [lang])

  useEffect(() => {
    const onScroll = () => setShowTop(window.scrollY > 600)
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => window.removeEventListener('scroll', onScroll)
  }, [])

  const observerRef = useRef<IntersectionObserver | null>(null)

  useEffect(() => {
    observerRef.current = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible')
            observerRef.current?.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    )
    return () => observerRef.current?.disconnect()
  }, [])

  useEffect(() => {
    if (!observerRef.current) return
    const timer = setTimeout(() => {
      document.querySelectorAll('.reveal').forEach((el) => observerRef.current!.observe(el))
    }, 50)
    return () => {
      clearTimeout(timer)
      observerRef.current?.disconnect()
    }
  }, [lang])

  const scrollToTop = useCallback(() => {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }, [])

  return (
    <main>
      <nav className="lang-switch" aria-label="Language">
        <button
          className={lang === 'ru' ? 'active' : ''}
          onClick={() => setLang('ru')}
          aria-label="Русский язык"
        >RU</button>
        <span className="sep">/</span>
        <button
          className={lang === 'en' ? 'active' : ''}
          onClick={() => setLang('en')}
          aria-label="English language"
        >EN</button>
      </nav>

      <header className="hero">
        <div className="wrap">
          <div className="hero-grid">
            <div className="hero-text">
              <h1 className="name">{s.name}</h1>
              <p className="role">
                {s.role}<span className="dot">·</span>{s.stack}<span className="dot">·</span>{s.location}
              </p>
              <p className="bio">
                <Typewriter text={s.bio} speed={25} />
              </p>
              <nav className="contact" aria-label="Contacts">
                <a href="https://github.com/qqwozz" target="_blank" rel="noopener noreferrer">GitHub</a>
                <span className="sep" aria-hidden="true">·</span>
                <a href="https://t.me/onixxed" target="_blank" rel="noopener noreferrer">Telegram</a>
                <span className="sep" aria-hidden="true">·</span>
                <a href="https://instagram.com/qqqwozz" target="_blank" rel="noopener noreferrer">Instagram</a>
                <span className="sep" aria-hidden="true">·</span>
                <a href="https://leetcode.com/u/oonixxxxx/" target="_blank" rel="noopener noreferrer">LeetCode</a>
                <span className="sep" aria-hidden="true">·</span>
                <a href="mailto:offconix@gmail.com">Email</a>
              </nav>
              <a href={`${import.meta.env.BASE_URL}qq/Dima_Kiselev_Resume.pdf`} download className="cv-download">
                {s.downloadCv}
              </a>
            </div>
          </div>
        </div>
      </header>

      <section className="skills" aria-labelledby="skills-label">
        <div className="wrap">
          <span className="label reveal" id="skills-label">{s.skillsLabel}</span>
          <dl className="skills-table">
            <div className="skill-row reveal"><dt>{s.backend}</dt><dd>{s.backendVal}</dd></div>
            <div className="skill-row reveal"><dt>{s.data}</dt><dd>{s.dataVal}</dd></div>
            <div className="skill-row reveal"><dt>{s.infra}</dt><dd>{s.infraVal}</dd></div>
            <div className="skill-row reveal"><dt>{s.tools}</dt><dd>{s.toolsVal}</dd></div>
          </dl>
        </div>
      </section>

      <section className="experience" aria-labelledby="exp-label">
        <div className="wrap">
          <span className="label reveal" id="exp-label">{s.expLabel}</span>
          <div className="jobs">
            <article className="job reveal">
              <h2 className="job-title">{s.vtb}</h2>
              <p className="job-meta">{s.vtbMeta}</p>
              <ul className="job-points">
                <li>{s.v1}</li><li>{s.v2}</li><li>{s.v3}</li><li>{s.v4}</li><li>{s.v5}</li><li>{s.v6}</li>
              </ul>
            </article>
          </div>
        </div>
      </section>

      <section className="education" aria-labelledby="edu-label">
        <div className="wrap">
          <span className="label reveal" id="edu-label">{s.eduLabel}</span>
          <div className="edu-items">
            <article className="edu-item reveal">
              <h2 className="edu-title">{s.edu1}</h2>
              <p className="edu-meta">{s.edu1Meta}</p>
              <p className="edu-desc">{s.edu1d}</p>
            </article>
            <article className="edu-item reveal">
              <h2 className="edu-title">{s.edu2}</h2>
              <p className="edu-meta">{s.edu2Meta}</p>
              <p className="edu-desc">{s.edu2d}</p>
            </article>
          </div>
        </div>
      </section>

      <section className="work" aria-labelledby="work-label">
        <div className="wrap">
          <span className="label reveal" id="work-label">{s.projectsLabel}</span>
          <div className="projects">
            <article className="project reveal">
              <h2 className="project-name">
                <a href="https://github.com/qqwozz/qw_pay" target="_blank" rel="noopener noreferrer">QW Pay</a>
              </h2>
              <p className="project-meta">{s.p2}<span className="dot">·</span>2024</p>
              <ul className="project-points">
                <li>{s.p2d1}</li><li>{s.p2d2}</li><li>{s.p2d3}</li>
              </ul>
              <div className="stack">Go<span className="dot">·</span>C++<span className="dot">·</span>Python<span className="dot">·</span>PostgreSQL<span className="dot">·</span>Redis<span className="dot">·</span>Docker</div>
              <div className="project-links">
                <a href="https://github.com/qqwozz/qw_pay" target="_blank" rel="noopener noreferrer">{s.code} <span className="arrow">↗</span></a>
              </div>
            </article>

            <article className="project reveal">
              <h2 className="project-name">
                <a href="https://github.com/qqwozz/enf-shop" target="_blank" rel="noopener noreferrer">ENF Shop</a>
              </h2>
              <p className="project-meta">{s.p3}<span className="dot">·</span>2024</p>
              <ul className="project-points">
                <li>{s.p3d1}</li><li>{s.p3d2}</li><li>{s.p3d3}</li>
              </ul>
              <div className="stack">Django<span className="dot">·</span>PostgreSQL<span className="dot">·</span>Redis<span className="dot">·</span>HTMX<span className="dot">·</span>Stripe<span className="dot">·</span>Docker</div>
              <div className="project-links">
                <a href="https://github.com/qqwozz/enf-shop" target="_blank" rel="noopener noreferrer">{s.code} <span className="arrow">↗</span></a>
              </div>
            </article>

            <article className="project reveal">
              <h2 className="project-name">
                <a href="https://github.com/qqwozz/autoadmin" target="_blank" rel="noopener noreferrer">AutoAdmin</a>
              </h2>
              <p className="project-meta">{s.p4}<span className="dot">·</span>2024</p>
              <ul className="project-points">
                <li>{s.p4d1}</li><li>{s.p4d2}</li>
              </ul>
              <div className="stack">Go<span className="dot">·</span>SQLite<span className="dot">·</span>Telegram Bot API<span className="dot">·</span>JWT<span className="dot">·</span>Docker</div>
              <div className="project-links">
                <a href="https://github.com/qqwozz/autoadmin" target="_blank" rel="noopener noreferrer">{s.code} <span className="arrow">↗</span></a>
              </div>
            </article>

            <article className="project reveal">
              <h2 className="project-name">
                <a href="https://github.com/qqwozz/OAuth_2.0" target="_blank" rel="noopener noreferrer">OAuth 2.0</a>
              </h2>
              <p className="project-meta">{s.p5}<span className="dot">·</span>2024</p>
              <ul className="project-points">
                <li>{s.p5d1}</li><li>{s.p5d2}</li>
              </ul>
              <div className="stack">Go<span className="dot">·</span>Shell<span className="dot">·</span>HTML</div>
              <div className="project-links">
                <a href="https://github.com/qqwozz/OAuth_2.0" target="_blank" rel="noopener noreferrer">{s.code} <span className="arrow">↗</span></a>
              </div>
            </article>
          </div>

          <p className="also-note reveal">
            {s.alsoText}<br />
            {s.alsoMore} <a href="https://github.com/qqwozz" target="_blank" rel="noopener noreferrer">GitHub <span className="arrow">↗</span></a>.
          </p>
        </div>
      </section>

      <section className="languages" aria-labelledby="lang-label">
        <div className="wrap">
          <span className="label reveal" id="lang-label">{s.langLabel}</span>
          <ul className="lang-list">
            <li className="reveal">{s.ruLang} <span className="lvl">— {s.ruLvl}</span></li>
            <li className="reveal">{s.enLang} <span className="lvl">— {s.enLvl}</span></li>
          </ul>
        </div>
      </section>

      <section className="contact-section" aria-labelledby="contact-label">
        <div className="wrap">
          <span className="label reveal" id="contact-label">{s.contactLabel}</span>
          <h2 className="contact-headline reveal">{s.contactHeadline}</h2>
          <p className="contact-sub reveal">{s.contactSub}</p>
          <div className="contact-cta reveal">
            <a href="mailto:offconix@gmail.com" className="cv-download">{s.contactEmail} <span className="arrow right">→</span></a>
            <a href="https://t.me/onixxed" target="_blank" rel="noopener noreferrer" className="cv-download">Telegram <span className="arrow">↗</span></a>
          </div>
        </div>
      </section>

      <footer>
        <div className="wrap">
          <p className="foot-meta">{s.footerMeta}</p>
          <nav className="foot-links" aria-label="Contacts">
            <a href="https://github.com/qqwozz" target="_blank" rel="noopener noreferrer">GitHub</a>
            <a href="https://t.me/onixxed" target="_blank" rel="noopener noreferrer">Telegram</a>
            <a href="https://instagram.com/qqqwozz" target="_blank" rel="noopener noreferrer">Instagram</a>
            <a href="https://leetcode.com/u/oonixxxxx/" target="_blank" rel="noopener noreferrer">LeetCode</a>
            <a href="mailto:offconix@gmail.com">Email</a>
          </nav>
        </div>
      </footer>

      <button
        className={`scroll-top${showTop ? ' visible' : ''}`}
        onClick={scrollToTop}
        aria-label="Scroll to top"
      >
        ↑
      </button>
    </main>
  )
}

export default App
