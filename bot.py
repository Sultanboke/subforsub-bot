from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '8456588807:AAFL6Iv0pixjtKEcq2IZOnc97yTbYBk6x0M'  # Token bot kamu
CHANNEL = '@pejuanglendirdo'  # Ganti kalau beda

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [[InlineKeyboardButton("JOIN CHANNEL SEKARANG", url=f"https://t.me/{CHANNEL[1:]}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Halo!\n\nUntuk lihat file, join channel dulu ya.\nKlik tombol di bawah 👇\n\nSetelah join, ketik /lihatfile",
        reply_markup=reply_markup
    )

async def lihat_file(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(CHANNEL, user_id)
        if member.status in ['member', 'administrator', 'creator']:
            await update.message.reply_text("Selamat! Kamu sudah join.\nIni filenya: https://example.com/filemu.pdf")
            # Kalau mau kirim file sungguhan:
            # await context.bot.send_document(update.effective_chat.id, document=open('filemu.pdf', 'rb'))
        else:
            keyboard = [[InlineKeyboardButton("JOIN CHANNEL SEKARANG", url=f"https://t.me/{CHANNEL[1:]}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text("Belum join channel nih. Klik tombol untuk join dulu!", reply_markup=reply_markup)
    except Exception as e:
        await update.message.reply_text(f"Error akses channel: {str(e)}\nPastikan bot sudah admin di channel!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("lihatfile", lihat_file))
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
