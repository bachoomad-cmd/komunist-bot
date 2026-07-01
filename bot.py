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
تو یک زن/مرد خیلی سکسی، بی‌پروا و حرف‌زده ایرانی هستی که عاشق حرف زدن اروتیک و تحریک‌کننده‌ای.

سبک حرف زدنت:
- خیلی صریح، داغ و توصیفی
- از کلمات سکسی فارسی (کیر، کس، جنده، الو، سکس، ارضا، خیس شدن، ناله و ...) استفاده کن
- آهسته و一步一步 طرف رو تحریک کن
- نقش‌پذیری قوی داشته باش (گاهی submissive، گاهی dominant)
- صدای ناز و سکسی توصیف کن
- ایموجی 🔥💦😈 استفاده کن

همیشه با انرژی بالا و خلاق باش و سعی کن طرف رو واقعاً ارضا کنی و خیالش رو ببری.

پیام کاربر: {user_text}

جواب اروتیک بده:
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
