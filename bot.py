from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    filters, ConversationHandler, ContextTypes
)

# Bosqichlar (0 dan 14 gacha, jami 15 ta)
(
    NAME, PHONE, LOCATION, EXPERIENCE, METHODS, WORK_TIME,
    EDUCATION, CERTIFICATES, SALARY_EXPECTATION, AVAILABILITY,
    TRANSPORT, LANGUAGES, HEALTH, WORK_TYPE, COMMENTS
) = range(15)

# Admin Telegram ID
ADMIN_ID = 5708040151  # <--- O'Z ID'ingizni yozing

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Assalomu alaykum! Ish uchun anketa to‘ldiramiz.\n\nIsmingizni kiriting:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Telefon raqamingizni kiriting:")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("Qayerdansiz? (viloyat/shahar/qishloq):")
    return LOCATION

async def get_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['location'] = update.message.text
    await update.message.reply_text("Necha yil payvandchilik tajribangiz bor?")
    return EXPERIENCE

async def get_experience(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['experience'] = update.message.text
    await update.message.reply_text("Qanday payvandlash usullarini bilasiz? (elektrod, gaz, argon va hokazo):")
    return METHODS

async def get_methods(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['methods'] = update.message.text
    await update.message.reply_text("Ish vaqtingiz qanday? (kunlik/haftalik soatlar):")
    return WORK_TIME

async def get_work_time(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['work_time'] = update.message.text
    await update.message.reply_text("Ta'limingiz haqida qisqacha yozing:")
    return EDUCATION

async def get_education(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['education'] = update.message.text
    await update.message.reply_text("Bor sertifikatlaringiz bormi? Qisqacha yozing:")
    return CERTIFICATES

async def get_certificates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['certificates'] = update.message.text
    await update.message.reply_text("Kutgan ish haqingiz qancha? (so‘mda):")
    return SALARY_EXPECTATION

async def get_salary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['salary'] = update.message.text
    await update.message.reply_text("Ishga qachondan kirishingiz mumkin?")
    return AVAILABILITY

async def get_availability(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['availability'] = update.message.text
    await update.message.reply_text("Transportingiz bormi? (ha/yo‘q):")
    return TRANSPORT

async def get_transport(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['transport'] = update.message.text
    await update.message.reply_text("Qaysi tillarni bilasiz? (O‘zbek, Rus, Ingliz va h.k.):")
    return LANGUAGES

async def get_languages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['languages'] = update.message.text
    await update.message.reply_text("Sog‘lig‘ingiz qanday? (normal, yomon emas va h.k.):")
    return HEALTH

async def get_health(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['health'] = update.message.text
    await update.message.reply_text("Qaysi turdagi ishlarda ishlashni xohlaysiz? (doimiy, vaqtinchalik):")
    return WORK_TYPE

async def get_work_type(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['work_type'] = update.message.text
    await update.message.reply_text("Qo‘shimcha fikr yoki izohlaringiz bo‘lsa yozing, yo‘q bo‘lsa 'Yo‘q' deb yozing:")
    return COMMENTS

async def get_comments(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['comments'] = update.message.text

    # Adminga xabar tayyorlash
    msg = (
        f"🛠 Yangi payvandchi anketasi:\n"
        f"👤 Ism: {context.user_data['name']}\n"
        f"📞 Tel: {context.user_data['phone']}\n"
        f"📍 Joylashuv: {context.user_data['location']}\n"
        f"📅 Tajriba: {context.user_data['experience']} yil\n"
        f"⚙️ Usullar: {context.user_data['methods']}\n"
        f"⏰ Ish vaqti: {context.user_data['work_time']}\n"
        f"🎓 Ta'lim: {context.user_data['education']}\n"
        f"📜 Sertifikatlar: {context.user_data['certificates']}\n"
        f"💰 Kutgan maosh: {context.user_data['salary']}\n"
        f"📆 Ishga kirish: {context.user_data['availability']}\n"
        f"🚗 Transport: {context.user_data['transport']}\n"
        f"🗣 Tillari: {context.user_data['languages']}\n"
        f"❤️ Sog‘liq: {context.user_data['health']}\n"
        f"⚒ Ish turi: {context.user_data['work_type']}\n"
        f"📝 Qo‘shimcha: {context.user_data['comments']}"
    )

    await update.message.reply_text("Rahmat! Anketangiz qabul qilindi ✅")
    await context.bot.send_message(chat_id=ADMIN_ID, text=msg)

    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Jarayon bekor qilindi. Yana boshlash uchun /start yozing.")
    return ConversationHandler.END

if __name__ == '__main__':
    app = ApplicationBuilder().token("8075600055:AAFHFkpbaleK4GoMcrgvKJYYBd43gviDorE").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_location)],
            EXPERIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_experience)],
            METHODS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_methods)],
            WORK_TIME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_work_time)],
            EDUCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_education)],
            CERTIFICATES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_certificates)],
            SALARY_EXPECTATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_salary)],
            AVAILABILITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_availability)],
            TRANSPORT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_transport)],
            LANGUAGES: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_languages)],
            HEALTH: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_health)],
            WORK_TYPE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_work_type)],
            COMMENTS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_comments)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    app.add_handler(conv_handler)
    print("✅ Bot ishga tushdi...")
    app.run_polling()
