
from vkbottle.bot import Bot, Message

from config import VK_TOKEN

from keyboards.main import get_main_keyboard
from keyboards.services import (
    get_services_keyboard,
    get_category_keyboard,
    get_service_keyboard,
)

from data.demo_data import DEMO_SERVICES
from data.demo_texts import (
    DEMO_NOTICE,
    WELCOME_TEXT,
    SECTION_TEXTS,
)


bot = Bot(token=VK_TOKEN)


# Фотографии, загруженные в сообщество VK
LOCATION_MAIN = "photo-243018616_456239021"
LOCATION_ENTRANCE = "photo-243018616_456239022"


# Адрес студии на Яндекс Картах
YANDEX_MAPS_URL = (
    "https://yandex.ru/maps/?text="
    "%D0%9A%D1%83%D0%B7%D0%BD%D0%B5%D1%86%D0%BA"
    "%2C%20%D1%83%D0%BB%D0%B8%D1%86%D0%B0"
    "%20%D0%9A%D0%B0%D0%BB%D0%B8%D0%BD%D0%B8%D0%BD%D0%B0"
    "%2C%20197"
)


async def send_section(message: Message, section: str):
    text = SECTION_TEXTS[section]

    if section in ("services", "booking"):
        text += f"\n\n━━━━━━━━━━━━━━━━━━\n\n{DEMO_NOTICE}"

    if section == "services":
        await message.answer(
            text,
            keyboard=get_services_keyboard()
        )
        return

    await message.answer(
        text,
        keyboard=get_main_keyboard()
    )


async def send_location(message: Message):
    # Первая фотография — общий вид здания
    await message.answer(
        "📍 КАК НАС НАЙТИ\n\n"
        "Студия красоты и здоровья «ЭДЕМ»\n\n"
        "📌 Адрес:\n"
        "г. Кузнецк, ул. Калинина, 197\n\n"
        "🏢 Второй этаж, направо.\n\n"
        "Вход в студию обозначен жёлтыми баннерами.\n"
        "Посмотрите на фотографии, чтобы легко найти нужную дверь.\n\n"
        f"🗺 Яндекс Карты:\n{YANDEX_MAPS_URL}",
        attachment=LOCATION_MAIN,
    )

    # Вторая фотография — вход в студию
    await message.answer(
        "🚪 КАК ПРОЙТИ В СТУДИЮ\n\n"
        "1. Найдите жёлтую дверь с баннерами.\n"
        "2. Поднимитесь на второй этаж.\n"
        "3. На втором этаже поверните направо.\n\n"
        "Будем рады видеть вас в студии «ЭДЕМ»!",
        attachment=LOCATION_ENTRANCE,
        keyboard=get_main_keyboard()
    )


async def show_category(message: Message, category: str):
    services = DEMO_SERVICES.get(category)

    if not services:
        await message.answer(
            "Категория не найдена.",
            keyboard=get_services_keyboard()
        )
        return

    await message.answer(
        f"📂 {category.upper()}\n\n"
        "Выберите интересующую процедуру:",
        keyboard=get_category_keyboard(category)
    )


async def show_service(message: Message, service_name: str):
    for category, services in DEMO_SERVICES.items():
        for service in services:
            if service["name"].lower() == service_name.lower():
                response = (
                    f"✨ {service['name']}\n\n"
                    f"{service['description']}\n\n"
                    f"💰 Стоимость: {service['price']} ₽\n"
                    f"⏱ Продолжительность: {service['duration']} минут"
                )

                await message.answer(
                    response,
                    keyboard=get_service_keyboard()
                )
                return

    await message.answer(
        "Не удалось найти эту процедуру.",
        keyboard=get_services_keyboard()
    )


@bot.on.message()
async def handle_message(message: Message):
    text = (message.text or "").strip()
    normalized_text = text.lower()

    # Приветствие
    if normalized_text in ["начать", "старт", "привет", "/start"]:
        await message.answer(
            WELCOME_TEXT,
            keyboard=get_main_keyboard()
        )
        return

    # Главное меню
    if normalized_text in ["⬅️ главное меню", "главное меню"]:
        await message.answer(
            WELCOME_TEXT,
            keyboard=get_main_keyboard()
        )
        return

    # Возврат к категориям
    if normalized_text in ["⬅️ к категориям", "к категориям"]:
        await send_section(message, "services")
        return

    # Раздел «Как нас найти»
    if "как нас найти" in normalized_text:
        await send_location(message)
        return

    # Выбор категории
    category = next(
        (
            name
            for name in DEMO_SERVICES
            if normalized_text == f"📂 {name}".lower()
            or normalized_text == name.lower()
        ),
        None
    )

    if category:
        await show_category(message, category)
        return

    # Выбор процедуры
    service_name = next(
        (
            service["name"]
            for services in DEMO_SERVICES.values()
            for service in services
            if normalized_text == f"💆 {service['name']}".lower()
            or normalized_text == service["name"].lower()
        ),
        None
    )

    if service_name:
        await show_service(message, service_name)
        return

    # Основные разделы
    if "записаться" in normalized_text:
        await send_section(message, "booking")
    elif "услуги" in normalized_text:
        await send_section(message, "services")
    elif "мои записи" in normalized_text:
        await send_section(message, "my_bookings")
    elif "о студии" in normalized_text:
        await send_section(message, "about")
    elif "связаться" in normalized_text:
        await send_section(message, "contact")
    else:
        await message.answer(
            "Не совсем понял ваш запрос.\n\n"
            "Пожалуйста, воспользуйтесь кнопками меню.",
            keyboard=get_main_keyboard()
        )


if __name__ == "__main__":
    print("EDEM VK DEMO запущен!")
    bot.run()

