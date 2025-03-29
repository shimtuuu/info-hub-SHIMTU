# 🎮 InfoHub-Zodak

InfoHub-Zodak — это Django-платформа для загрузки, просмотра и скачивания игр. Поддерживает авторизацию через Google, Telegram и email, а также восстановление пароля.

---

## 🚀 Возможности

- 🔐 Регистрация и вход (Google, Telegram, email)
- 🧩 Восстановление пароля
- 🎮 Загрузка и просмотр игр (с обложками и описанием)
- 📥 Скачать игру (торрент или прямая ссылка)
- 🛠️ Красивый Bootstrap-интерфейс
- ⚙️ Админка с превью обложек и фильтрами

---

## 🔧 Установка

```bash
git clone https://github.com/shimtuuu/info-hub-SHIMTU.git
cd info-hub-SHIMTU
python -m venv venv
source venv/bin/activate  # или venv\Scripts\activate на Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Локальные логины

- Email: используйте регистрацию
- Google: настроено через OAuth
- Telegram: работает через Telegram Login Widget

---

## ⚙️ Управление

Админ-панель: [http://localhost:8000/admin/](http://localhost:8000/admin/)  
Создай суперпользователя:

```bash
python manage.py createsuperuser
```

---

## 📦 Авторизация через Telegram

В файле `telegram_auth/views.py` используется проверка подписи через Bot Token. Вы можете заменить токен на свой.

---

## 💬 Контакты

Разработчик: [Shimtu](https://github.com/shimtuuu)