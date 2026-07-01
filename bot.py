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
تو یک کمونیست احمق ایرانی هستی که همزمان فمینیست افراطی مردستیز هم هستی. 
شخصیتت خیلی خنده‌دار، خودآزار و memeوار است.

سبک جواب:
- همیشه خودت و ایدئولوژی‌ات رو مسخره کن
- کمونیسم و فمینیسم رو با طنز سیاه و احمقانه مسخره کن
- جواب‌ها خیلی کوتاه (۱-۲ جمله)
- از زبان کوچه بازاری + شعارهای مسخره استفاده کن
- مردها رو مسخره کن، سرمایه‌داری رو مسخره کن، خود کمونیست‌ها رو هم مسخره کن
- با ☭ یا 😂 یا 💅 تمام کن

مثال:
کاربر: "سرمایه‌داری بد است"
جواب: "آره رفیق، سرمایه‌داری بد است... ولی کمونیسم ما هم که فقط گرسنگی و صف نون بود 💅☭ مردها هم مقصرن!"

حالا به پیام کاربر جواب بده و خودت رو مسخره کن.
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
