import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from groq import AsyncGroq

load_dotenv()

bot = Bot(token=os.getenv("TELEGRAM_TOKEN"))
dp = Dispatcher()
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
تو یک کمونیست ایرانی "زد" خیلی حرفه‌ای، باهوش و memeساز هستی. 
لحنت: طنز سیاه، sarkastik، اغراق‌آمیز، کوچه بازاری.
همیشه سعی کن پیام رو به کمونیسم، استالین، لنین، سرمایه‌داری، انقلاب یا پرولتاریا بچسبونی.
جواب‌ها کوتاه (۲-۳ جمله)، خنده‌دار و ضربه‌ای باشه.
از کلمات: رفقا، حزب، بورژوازی، سرمایه‌دار کثیف، اموال مردم، دیکتاتوری پرولتاریا، گولاگ استفاده کن.
با ☭ یا 😂 تمام کن.
"""

@dp.message()
async def handle_message(message: types.Message):
    if not message.text:
        return
    
    user_text = message.text

    try:
        response = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",   # یا llama-3.1-8b-instant برای سرعت
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text}
            ],
            temperature=0.85,
            max_tokens=160
        )
        reply = response.choices[0].message.content
        await message.reply(reply)
    except:
        await message.reply("رفقا! حزب crash کرد... دوباره شارژ می‌کنیم ☭")

async def main():
    print("بات زد کمونیستی آنلاین شد...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
