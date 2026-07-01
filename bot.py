import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

@dp.message()
async def handle(message: types.Message):
    if not message.text:
        return
    if any(k in message.text.lower() for k in ["کمونیسم", "استالین", "لنین", "مارکس", "انقلاب", "رفقا"]):
        try:
            resp = await client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": f"زد کمونیستی جواب بده:\n{message.text}"}],
                max_tokens=120
            )
            await message.reply(resp.choices[0].message.content)
        except Exception as e:
            await message.reply("رفقا، حزب crash کرد ☭")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
