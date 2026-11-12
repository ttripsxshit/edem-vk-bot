
from vkbottle import Keyboard, KeyboardButtonColor, Text

from data.demo_data import DEMO_SERVICES


def get_services_keyboard():
    """Клавиатура со списком категорий."""

    keyboard = Keyboard(one_time=False)

    for category in DEMO_SERVICES:
        keyboard.add(
            Text(f"📂 {category}"),
            color=KeyboardButtonColor.PRIMARY
        )
        keyboard.row()

    keyboard.add(
        Text("⬅️ Главное меню"),
        color=KeyboardButtonColor.SECONDARY
    )

    return keyboard.get_json()


def get_category_keyboard(category: str):
    """Клавиатура со списком процедур выбранной категории."""

    keyboard = Keyboard(one_time=False)

    for service in DEMO_SERVICES[category]:
        keyboard.add(
            Text(f"💆 {service['name']}"),
            color=KeyboardButtonColor.POSITIVE
        )
        keyboard.row()

    keyboard.add(
        Text("⬅️ К категориям"),
        color=KeyboardButtonColor.SECONDARY
    )
    keyboard.row()

    keyboard.add(
        Text("⬅️ Главное меню"),
        color=KeyboardButtonColor.SECONDARY
    )

    return keyboard.get_json()


def get_service_keyboard():
    """Клавиатура на странице отдельной процедуры."""

    keyboard = Keyboard(one_time=False)

    keyboard.add(
        Text("⬅️ К категориям"),
        color=KeyboardButtonColor.PRIMARY
    )
    keyboard.row()

    keyboard.add(
        Text("⬅️ Главное меню"),
        color=KeyboardButtonColor.SECONDARY
    )

    return keyboard.get_json()
