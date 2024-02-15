from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="YouTube", url="https://youtu.be/..."),
      InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=...")
    ]
  ]
)