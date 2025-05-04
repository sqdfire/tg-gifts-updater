from pathlib import Path


SESSION_NAME: str = "#"

API_ID: int = # Ur API_ID
API_HASH: str = "#"


CHECK_INTERVAL: float = 90.

DATA_FILEPATH: Path = Path(__file__).parent / "star_gifts.json"
NOTIFY_CHAT_ID: int = - #with minus notify chat id
NOTIFY_AFTER_STICKER_DELAY: float = 1.
NOTIFY_AFTER_TEXT_DELAY: float = 2.
TIMEZONE: str = "UTC"


NOTIFY_TEXT: str = """\
{title}

№ {number} (<code>{id}</code>)
{total_amount}{available_amount}
💎 Price: {price} ⭐️
♻️ Convert price: {convert_price} ⭐️
"""

NOTIFY_TEXT_TITLES: dict[bool, str] = {
    True: "🔥 A new limited gift has appeared",
    False: "❄️ A new gift has appeared"
}

NOTIFY_TEXT_TOTAL_AMOUNT: str = "\n🎯 Total amount: {total_amount}"
NOTIFY_TEXT_AVAILABLE_AMOUNT: str = "\n❓ Available amount: {available_amount} ({same_str}{available_percentage}%, updated at {updated_datetime} UTC)\n"


GIFT_TEXT: str = "🎁 Gift №{number} ({id})"
GIFT_HIDE_MY_NAME: bool = True
