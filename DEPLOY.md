# Деплой

## Пошагово

```bash
# 1. Убедись что всё закоммичено
git status

# 2. Переключись на main
git checkout main

# 3. Замержи свою ветку
git merge feature/resume-polish

# 4. Запушь
git push origin main

# 5. Готово — GitHub Actions задеплоит автоматически
```

Сайт обновится через 1-2 минуты: https://qqwozz.github.io/new_qq/

## Если деплой упал

1. Зайди на https://github.com/qqwozz/new_qq/actions
2. Посмотри логи ошибки
3. Исправь, закоммить, запушь в `main` снова

## Локальная проверка перед деплоем

```bash
npm run dev          # запуск dev-сервера
npm run build        # проверка что билд собирается
npm run preview      # превью продакшн-билда
```
