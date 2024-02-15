from aiogram import Router, F
from aiogram.types import Message

from keyboards import reply, inline, builders, fabrics
from data.subloader import get_json

router = Router()

@router.message(F.text.lower().in_(["hi", "hello"]))
async def greetings(message: Message):
  await message.reply("Hellooooo!")

@router.message()
async def echo(message: Message):
  msg = message.text.lower()
  smiles = await get_json("smiles.json")

  if msg == "links":
    await message.answer("Here are your links: ", reply_markup=inline.links)
  elif msg == "special buttons":
    await message.answer("Special buttons", reply_markup=reply.spec)
  elif msg == "calculator":
    await message.answer("Enter an expression:", reply_markup=builders.calc())
  elif msg == "emoticons":
    await message.answer(f"{smiles[0][0]} <b>{smiles[0][1]}</b>", reply_markup=fabrics.paginator())