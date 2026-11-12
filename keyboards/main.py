
from vkbottle import Keyboard, KeyboardButtonColor, Text


def get_main_keyboard():
    keyboard = Keyboard(one_time=False)

    keyboard.add(
        Text("📅 Записаться"),
        color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("✨ Услуги"),
        color=KeyboardButtonColor.POSITIVE
    )

    keyboard.row()

    keyboard.add(
        Text("📋 Мои записи"),
        color=KeyboardButtonColor.PRIMARY
    )
    keyboard.add(
        Text("🏛 О студии"),
        color=KeyboardButtonColor.SECONDARY
    )

    keyboard.row()

    keyboard.add(
        Text("📍 Как нас найти"),
        color=KeyboardButtonColor.SECONDARY
    )
    keyboard.add(
        Text("💬 Связаться"),
        color=KeyboardButtonColor.SECONDARY
    )

    return keyboard.get_json()


