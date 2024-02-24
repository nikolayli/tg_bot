from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
  inline_keyboard=[
    [
      InlineKeyboardButton(text="YouTube", url="https://youtu.be/..."),
      InlineKeyboardButton(text="Telegram", url="tg://resolve?domain=...")
    ]
  ]
)

sub_channel = InlineKeyboardMarkup (
  inline_keyboard=[
    [
      InlineKeyboardButton(text="Subscribe", url="https://t.me/")
    ]
  ]
)