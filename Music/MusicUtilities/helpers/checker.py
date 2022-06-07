from Music import BOT_USERNAME, LOG_GROUP_ID, app
from Music.MusicUtilities.database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "Sən bu qrupda anonim adminsən!\nAdmin icazələri alan hesaba qayıt."
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**Qara Siyahıya alınmış qrup**\n\nBu Qrup @HusuSovetski tərəfindən qara siyahıya alınıdı!.Qara siyahıdan çıxardılması üçün  __SUDO USER__ müraciət et.\nSahibin Listinə bax [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"Bot yoxlanışdadır. Narahatçılıq üçün üzr istəyirik!"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**GBan-lanmış user**\n\nSən bu bot üçün GBan-lanmısan.Müraciət et __SUDO USER__ UNGban edilməsi üçün.\nSahibin listinə bax [From Here](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "Blacklisted Chat", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "Bot yoxlanışdadır. Narahatçılıq üçün üzr istəyirik!",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "You're Gbanned", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
