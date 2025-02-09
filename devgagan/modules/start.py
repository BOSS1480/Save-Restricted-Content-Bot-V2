from pyrogram import filters
from devgagan import app
from config import OWNER_ID
from devgagan.core.func import subscribe
import asyncio
from devgagan.core.func import *
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.raw.functions.bots import SetBotInfo
from pyrogram.raw.types import InputUserSelf

from pyrogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
 
@app.on_message(filters.command("set"))
async def set(_, message):
    if message.from_user.id not in OWNER_ID:
        await message.reply("You are not authorized to use this command.")
        return
     
    await app.set_bot_commands([
        BotCommand("start", "🚀 Start the bot"),
        BotCommand("batch", "🫠 Extract in bulk"),
        BotCommand("login", "🔑 Get into the bot"),
        BotCommand("logout", "🚪 Get out of the bot"),
        BotCommand("token", "🎲 Get 3 hours free access"),
        BotCommand("adl", "👻 Download audio from 30+ sites"),
        BotCommand("dl", "💀 Download videos from 30+ sites"),
        BotCommand("freez", "🧊 Remove all expired user"),
        BotCommand("pay", "₹ Pay now to get subscription"),
        BotCommand("status", "⟳ Refresh Payment status"),
        BotCommand("transfer", "💘 Gift premium to others"),
        BotCommand("myplan", "⌛ Get your plan details"),
        BotCommand("add", "➕ Add user to premium"),
        BotCommand("rem", "➖ Remove from premium"),
        BotCommand("session", "🧵 Generate Pyrogramv2 session"),
        BotCommand("settings", "⚙️ Personalize things"),
        BotCommand("stats", "📊 Get stats of the bot"),
        BotCommand("plan", "🗓️ Check our premium plans"),
        BotCommand("terms", "🥺 Terms and conditions"),
        BotCommand("speedtest", "🚅 Speed of server"),
        BotCommand("get", "🗄️ Get all user IDs"),
        BotCommand("lock", "🔒 Protect channel from extraction"),
        BotCommand("gcast", "⚡ Broadcast message to bot users"),
        BotCommand("help", "❓ If you're a noob, still!"),
        BotCommand("cancel", "🚫 Cancel batch process")
    ])
 
    await message.reply("✅ Commands configured successfully!")
 
 
 
 
help_pages = [
    (
        "📝 **סקירה של פקודות הבוט (1/2)**:\n\n"
        "1. **/add userID**\n"
        "> הוסף משתמש לפרימיום (רק למנהל)\n\n"
        "2. **/rem userID**\n"
        "> הסר משתמש מפרימיום (רק למנהל)\n\n"
        "3. **/transfer userID**\n"
        "> העבר פרימיום למטרה העיקרית האהובה שלך עבור משווקים (רק לחברי פרימיום)\n\n"
        "4. **/get**\n"
        "> קבל את כל מזהי המשתמשים (רק למנהל)\n\n"
        "5. **/lock**\n"
        "> נעל את הערוץ מפני הוצאה (רק למנהל)\n\n"
        "6. **/dl link**\n"
        "> הורד סרטונים (לא זמין בגרסה 3 אם אתה משתמש)\n\n"
        "7. **/adl link**\n"
        "> הורד אודיו (לא זמין בגרסה 3 אם אתה משתמש)\n\n"
        "8. **/login**\n"
        "> התחבר לבוט לגישה לערוץ פרטי\n\n"
        "9. **/batch**\n"
        "> הוצאה קבוצתית להודעות (לאחר ההתחברות)\n\n"
    ),
    (
        "📝 **סקירה של פקודות הבוט (2/2)**:\n\n"
        "10. **/logout**\n"
        "> התנתק מהבוט\n\n"
        "11. **/stats**\n"
        "> קבל סטטיסטיקות על הבוט\n\n"
        "12. **/plan**\n"
        "> בדוק תוכניות פרימיום\n\n"
        "13. **/terms**\n"
        "> תנאים והגבלות\n\n"
        "14. **/cancel**\n"
        "> בטל תהליך קבוצתי בהמשך\n\n"
        "15. **/myplan**\n"
        "> קבל פרטים על התוכניות שלך\n\n"
        "16. **/session**\n"
        "> צור סשן Pyrogram V2\n\n"
        "17. **/settings**\n"
        "> 1. SETCHATID : כדי להעלות ישירות לקבוצה או לערוץ או לדו-שיח של משתמש השתמש בזה עם -100[chatID]\n"
        "> 2. SETRENAME : כדי להוסיף תג מותאם אישית או שם משתמש לערוצים שלך\n"
        "> 3. CAPTION : כדי להוסיף כותרת מותאמת אישית\n"
        "> 4. REPLACEWORDS : יכול לשמש למילים שנמחקו דרך REMOVE WORDS\n"
        "> 5. RESET : על מנת להחזיר את הדברים לברירת המחדל\n\n"
        "> אתה יכול להגדיר תצוגה מקדימה מותאמת אישית, סימן מים ל-PDF, סימן מים לסרטון, כניסה מבוססת סשן, וכו' מתוך ההגדרות\n\n"
        "**__מנוהל על ידי צוות @bot_sratim_sdarot__**"
    )
]
 
 
async def send_or_edit_help_page(_, message, page_number):
    if page_number < 0 or page_number >= len(help_pages):
        return
 
     
    prev_button = InlineKeyboardButton("◀️", callback_data=f"help_prev_{page_number}")
    next_button = InlineKeyboardButton("▶️", callback_data=f"help_next_{page_number}")
 
     
    buttons = []
    if page_number > 0:
        buttons.append(prev_button)
    if page_number < len(help_pages) - 1:
        buttons.append(next_button)
 
     
    keyboard = InlineKeyboardMarkup([buttons])
 
     
    await message.delete()
 
     
    await message.reply(
        help_pages[page_number],
        reply_markup=keyboard
    )
 
 
@app.on_message(filters.command("help"))
async def help(client, message):
    join = await subscribe(client, message)
    if join == 1:
        return
 
     
    await send_or_edit_help_page(client, message, 0)
 
 
@app.on_callback_query(filters.regex(r"help_(prev|next)_(\d+)"))
async def on_help_navigation(client, callback_query):
    action, page_number = callback_query.data.split("_")[1], int(callback_query.data.split("_")[2])
 
    if action == "prev":
        page_number -= 1
    elif action == "next":
        page_number += 1
 
     
    await send_or_edit_help_page(client, callback_query.message, page_number)
 
     
    await callback_query.answer()
 
 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
 
@app.on_message(filters.command("terms") & filters.private)
async def terms(client, message):
    terms_text = (
        "> 📜 **תנאים והגבלות** 📜\n\n"
        "✨ אנו לא אחראים למעשים של המשתמשים, ואנו לא מקדמים תוכן המוגן בזכויות יוצרים. אם משתמש כלשהו עוסק בפעילויות כאלה, זו אחריותו בלבד.\n"
        "✨ עם הרכישה, אנו לא מבטיחים את זמינותו, הפסקתו או לתוקפן של התוכנית. __ההרשאה וההשעיה של משתמשים הן לפי שיקול דעתנו; אנו שומרים על הזכות להשעות או להרשות משתמשים בכל עת.__\n"
        "✨ התשלום אלינו **__לא מבטיח__** הרשאה לפקודת /batch. כל ההחלטות בנוגע להרשאה מתקבלות לפי שיקול דעתנו ומצב רוחנו.\n"
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 צפה בתוכניות", callback_data="see_plan")],
            [InlineKeyboardButton("💬 צור קשר עם המנהל", url="https://t.me/boss148bot")],
        ]
    )
    await message.reply_text(terms_text, reply_markup=buttons)
 
 
@app.on_message(filters.command("plan") & filters.private)
async def plan(client, message):
 
    plan_text = (
        "> 💰מחיר פרימיום\n\n המחיר הוא 30 ש\"ח לחודש דרך פייפאל.\n"
        "📥 מגבלת הורדה: משתמשים יכולים להוריד עד 100,000 קבצים בפקודת batch אחת.\n"
        "🛑 קבוצתית: תוכל לקבל שני מצבים /bulk ו-/batch.\n"
        "   - משתמשים מתבקשים להמתין שההליך יתקף באופן אוטומטי לפני שהמשתמשים יתחילו בהורדות או העלאות כלשהן.\n\n"
        "📜 תנאים והגבלות: לפרטים נוספים ולתנאים והגבלות המלאים, אנא שלח /terms או לחץ על ראה תנאים👇\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 צפה בתוכניות", callback_data="see_terms")],
            [InlineKeyboardButton("💬 צור קשר עם המנהל", url="https://t.me/boss148bot")],
        ]
    )
    await message.reply_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_plan"))
async def see_plan(client, callback_query):
    plan_text = (
        "> 💰מחיר פרימיום\n\n המחיר הוא 30 ש\"ח לחודש דרך פייפאל.\n"
        "📥 מגבלת הורדה: משתמשים יכולים להוריד עד 100,000 קבצים בפקודת batch אחת.\n"
        "🛑 קבוצתית: תוכל לקבל שני מצבים /bulk ו-/batch.\n"
        "   - משתמשים מתבקשים להמתין שההליך יתקף באופן אוטומטי לפני שהמשתמשים יתחילו בהורדות או העלאות כלשהן.\n\n"
        "📜 תנאים והגבלות: לפרטים נוספים ולתנאים והגבלות המלאים, אנא שלח /terms או לחץ על ראה תנאים👇\n"
    )
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📜 צפה בתוכניות", callback_data="see_terms")],
            [InlineKeyboardButton("💬 צור קשר עם המנהל", url="https://t.me/boss148bot")],
        ]
    )
    await callback_query.message.edit_text(plan_text, reply_markup=buttons)
 
 
@app.on_callback_query(filters.regex("see_terms"))
async def see_terms(client, callback_query):
    terms_text = (
        "> 📜 **תנאים והגבלות** 📜\n\n"
        "✨ אנו לא אחראים למעשים של המשתמשים, ואנו לא מקדמים תוכן המוגן בזכויות יוצרים. אם משתמש כלשהו עוסק בפעילויות כאלה, זו אחריותו בלבד.\n"
        "✨ עם הרכישה, אנו לא מבטיחים את זמינותו, הפסקתו או לתוקפן של התוכנית. __ההרשאה וההשעיה של משתמשים הן לפי שיקול דעתנו; אנו שומרים על הזכות להשעות או להרשות משתמשים בכל עת.__\n"
        "✨ התשלום אלינו **__לא מבטיח__** הרשאה לפקודת /batch. כל ההחלטות בנוגע להרשאה מתקבלות לפי שיקול דעתנו ומצב רוחנו.\n"
     
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("📋 צפה בתוכניות", callback_data="see_plan")],
            [InlineKeyboardButton("💬 צור קשר עם המנהל", url="https://t.me/boss148bot")],
        ]
    )
    await callback_query.message.edit_text(terms_text, reply_markup=buttons)
 
 
