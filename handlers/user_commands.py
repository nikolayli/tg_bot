import random

from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji

from keyboards import reply

router = Router()

@router.message(CommandStart())
async def start(message: Message):
  await message.answer("Hello, AIOgram 3.x", reply_markup=reply.main)

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