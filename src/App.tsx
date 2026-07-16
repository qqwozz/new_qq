import { useState, useEffect, useCallback, useMemo, useRef } from 'react'

type Lang = 'ru' | 'en'

const t: Record<Lang, Record<string, string>> = {
  ru: {
    name: 'Дима Киселев',
    role: 'Backend-разработчик',
    stack: 'Python · Go · C++',
    location: 'Москва, Россия',
    bio: 'Backend-разработчик. Создаю микросервисы, API и high-load системы на Python, Go и C++. Чистая архитектура, производительность, надёжность.',
    skillsLabel: 'Основной стек',
    backend: 'Бэкенд',
    backendVal: 'Python (FastAPI, Django) · Go · C++ · gRPC · REST',
    data: 'Данные',
    dataVal: 'PostgreSQL · Redis · SQLite',
    infra: 'Инфраструктура',
    infraVal: 'Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD',
    tools: 'Инструменты',
    toolsVal: 'Git · Postman · VS Code · HTMX',
    expLabel: 'Опыт',
    yandex: 'Backend-разработчик (стажёр) — Яндекс',
    yandexMeta: 'Стажировка · Янв 2024 — Май 2024 · Москва',
    y1: 'Разработка и сопровождение микросервисов для поисковой инфраструктуры Яндекса',
    y2: 'Проектирование и реализация gRPC API для обработки запросов в распределённой системе',
    y3: 'Написание модульных и интеграционных тестов, покрытие кода >80%',
    y4: 'Оптимизация производительности серверных компонентов, снижение latency на 15%',
    vtb: 'Backend-разработчик (стажёр) — ВТБ',
    vtbMeta: 'Стажировка · Сен 2024 — Дек 2024 · Москва',
    v1: 'Разработка микросервисов для обработки платёжных операций в банковской системе',
    v2: 'Реализация REST API для интеграции с внутренними системами банка',
    v3: 'Работа с PostgreSQL, проектирование схем хранения финансовых данных',
    v4: 'Контейнеризация сервисов с Docker, настройка CI/CD пайплайнов',
    projectsLabel: 'Избранные проекты',
    p1: 'Крипто-биржа с C++ matching engine',
    p1d1: 'Высокопроизводительная крипто-биржа с торговым ядром на C++. Архитектура из 6 микросервисов: API Gateway, User, Account, Order, Portfolio и Matching Engine',
    p1d2: 'Обрабатывает 1000+ ордеров/сек с латентностью <100мс',
    p1d3: 'Matching engine на C++ с Price-Time Priority, limit и market ордера',
    p1d4: 'JWT аутентификация, React фронтенд',
    p2: 'Микросервис платежей',
    p2d1: 'Платёжная система с мультивалютными счетами и конвертацией по реальным курсам (200+ валют)',
    p2d2: 'C++ антифрод-движок проверяет velocity <1мс, Python скоринг блокирует подозрительные транзакции',
    p2d3: 'ACID-транзакции с идемпотентностью, JWT + OTP аутентификация',
    p3: 'Интернет-магазин одежды',
    p3d1: 'Полнофункциональный e-commerce с каталогом, фильтрацией, умной корзиной и приёмом платежей через Stripe',
    p3d2: 'Корзина без перезагрузки (HTMX), фильтрация по категориям, размерам, цене',
    p3d3: 'Production-ready Docker (Nginx + Gunicorn)',
    code: 'Код',
    alsoText: 'AutoAdmin — API + Telegram-бот для записей (Go, SQLite). AI Chat Bot — NLP чат-бот на GigaChat (Python, Streamlit).',
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
    czLang: 'Чешский',
    czLvl: 'A1',
    footerMeta: 'Дима Киселев · Москва · 2026',
  },
  en: {
    name: 'Dima Kiselev',
    role: 'Backend Developer',
    stack: 'Python · Go · C++',
    location: 'Moscow, Russia',
    bio: 'Backend developer. I build microservices, APIs, and high-load systems with Python, Go, and C++. Clean architecture, performance, reliability.',
    skillsLabel: 'Core Stack',
    backend: 'Backend',
    backendVal: 'Python (FastAPI, Django) · Go · C++ · gRPC · REST',
    data: 'Data',
    dataVal: 'PostgreSQL · Redis · SQLite',
    infra: 'Infrastructure',
    infraVal: 'Docker · Linux · Nginx · Gunicorn · GitHub Actions CI/CD',
    tools: 'Tools',
    toolsVal: 'Git · Postman · VS Code · HTMX',
    expLabel: 'Experience',
    yandex: 'Backend Developer (intern) — Yandex',
    yandexMeta: 'Internship · Jan 2024 — May 2024 · Moscow',
    y1: 'Developed and maintained microservices for Yandex search infrastructure',
    y2: 'Designed and implemented gRPC API for request handling in a distributed system',
    y3: 'Wrote unit and integration tests with >80% code coverage',
    y4: 'Optimized server component performance, reduced latency by 15%',
    vtb: 'Backend Developer (intern) — VTB',
    vtbMeta: 'Internship · Sep 2024 — Dec 2024 · Moscow',
    v1: 'Developed microservices for payment processing in a banking system',
    v2: 'Implemented REST API for integration with internal bank systems',
    v3: 'Worked with PostgreSQL, designed schemas for financial data storage',
    v4: 'Containerized services with Docker, set up CI/CD pipelines',
    projectsLabel: 'Selected Projects',
    p1: 'Crypto exchange with C++ matching engine',
    p1d1: 'High-performance crypto exchange with C++ trading core. Architecture of 6 microservices: API Gateway, User, Account, Order, Portfolio and Matching Engine',
    p1d2: 'Handles 1000+ orders/sec with <100ms latency',
    p1d3: 'Matching engine in C++ with Price-Time Priority, limit and market orders',
    p1d4: 'JWT authentication, React frontend',
    p2: 'Payment microservice',
    p2d1: 'Payment system with multi-currency accounts and real-time conversion (200+ currencies)',
    p2d2: 'C++ anti-fraud engine checks velocity <1ms, Python scoring blocks suspicious transactions',
    p2d3: 'ACID transactions with idempotency, JWT + OTP authentication',
    p3: 'Online clothing store',
    p3d1: 'Full-featured e-commerce with catalog, filtering, smart cart and Stripe payments',
    p3d2: 'HTMX no-reload cart, filtering by categories, sizes, price',
    p3d3: 'Production-ready Docker (Nginx + Gunicorn)',
    code: 'Source',
    alsoText: 'AutoAdmin — API + Telegram bot for appointments (Go, SQLite). AI Chat Bot — NLP chatbot on GigaChat (Python, Streamlit).',
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
    czLang: 'Czech',
    czLvl: 'A1',
    footerMeta: 'Dima Kiselev · Moscow · 2026',
  },
}

function Typewriter({ text, speed = 30 }: { text: string; speed?: number }) {
  const [displayed, setDisplayed] = useState('')
  const [done, setDone] = useState(false)
  const indexRef = useRef(0)

  useEffect(() => {
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

  const observer = useMemo(() => {
    return new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible')
            observer.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    )
  }, [])

  useEffect(() => {
    const timer = setTimeout(() => {
      document.querySelectorAll('.reveal').forEach((el) => observer.observe(el))
    }, 50)
    return () => {
      clearTimeout(timer)
      observer.disconnect()
    }
  }, [lang, observer])

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
              <a href={`${import.meta.env.BASE_URL}Dima_Kiselev_Resume.pdf`} download className="cv-download">
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
              <h2 className="job-title">{s.yandex}</h2>
              <p className="job-meta">{s.yandexMeta}</p>
              <ul className="job-points">
                <li>{s.y1}</li><li>{s.y2}</li><li>{s.y3}</li><li>{s.y4}</li>
              </ul>
            </article>
            <article className="job reveal">
              <h2 className="job-title">{s.vtb}</h2>
              <p className="job-meta">{s.vtbMeta}</p>
              <ul className="job-points">
                <li>{s.v1}</li><li>{s.v2}</li><li>{s.v3}</li><li>{s.v4}</li>
              </ul>
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
                <a href="https://github.com/qqwozz/QW_Trading_Platform" target="_blank" rel="noopener noreferrer">QW Trading Platform</a>
              </h2>
              <p className="project-meta">{s.p1}<span className="dot">·</span>2024</p>
              <ul className="project-points">
                <li>{s.p1d1}</li><li>{s.p1d2}</li><li>{s.p1d3}</li><li>{s.p1d4}</li>
              </ul>
              <div className="stack">Go<span className="dot">·</span>C++17<span className="dot">·</span>PostgreSQL<span className="dot">·</span>Redis<span className="dot">·</span>gRPC<span className="dot">·</span>Docker<span className="dot">·</span>React</div>
              <div className="project-links">
                <a href="https://github.com/qqwozz/QW_Trading_Platform" target="_blank" rel="noopener noreferrer">{s.code} <span className="arrow">↗</span></a>
              </div>
            </article>

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
            <li className="reveal">{s.czLang} <span className="lvl">— {s.czLvl}</span></li>
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
