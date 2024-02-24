import random

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji

from keyboards import reply

from filters.is_admine import IsAdmin
from filters.is_digit_or_float import ChackForDigit

router = Router()

@router.message(CommandStart(), IsAdmin(5122684923))
async def start(message: Message):
  await message.answer("Hello, AIOgram 3.x", reply_markup=reply.main)

@router.message(Command("pay"))
async def pay_the_order(message: Message, command: CommandObject) -> None:
  await message.answer("You have successfully paid for the item!")

@router.message(Command(commands=["rn","random-number"]))
async def get_random_number(message: Message, command: CommandObject):
  a, b = [int(n) for n in command.args.split("-")]
  rnum = random.randint(a, b)

  await message.reply(f"Random number: {rnum}")

@router.message(F.text == "play")
async def play_games(message: Message):
  x = await message.answer_dice(DiceEmoji.DICE)
  print(x.dice.value)  

@router.message(Command("test"))
async def test(message: Message, bot: Bot):
  await bot.send_message(message.chat.id, "test") 

@router.message()
async def echo(message: Message):
  await message.answer(f"I don't understand you:)")