from aiogram.types import (
  ReplyKeyboardMarkup,
  KeyboardButton,
  KeyboardButtonPollType
)  

main = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Emoticons"),
      KeyboardButton(text="Links")
    ],
    [
      KeyboardButton(text="Calculator"),
      KeyboardButton(text="Special buttons")
    ]
  ],
  resize_keyboard=True,
  one_time_keyboard=True,
  input_field_placeholder="Select an action from the menu",
  selective=True
)

spec = ReplyKeyboardMarkup(
  keyboard=[
    [
      KeyboardButton(text="Send geolocation", request_location=True),
      KeyboardButton(text="Send contact", request_contact=True),
      KeyboardButton(text="Create an event", request_poll=KeyboardButtonPollType())
    ],
    [
      KeyboardButton(text="back")
    ]
  ],
  resize_keyboard=True
)