import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

KEYWORDS = ["کمونیسم", "استالین", "لنین", "مارکس", "انقلاب", "پرولتاریا", "سرمایه‌داری", "رفقا", "بورژوازی"]

@dp.message()
async def handle(message: types.Message):
    if not message.text:
        return
    txt = message.text.lower()
    if any(k in txt for k in KEYWORDS):
        try:
            resp = await client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": f"به عنوان یک کمونیست زد خنده‌دار ایرانی، با طنز جواب بده:\n\n{message.text}"}],
                temperature=0.9,
                max_tokens=150
            )
            await message.reply(resp.choices[0].message.content)
        except:
            await message.reply("رفقا، حزب مشغول شارژه ☭")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
