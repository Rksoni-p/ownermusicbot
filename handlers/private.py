import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/86aa550f64231113c8162.jpg",
        caption=f"""**𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐝𝐯𝐚𝐧𝐜𝐞 🥀𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦 𝐌𝐮𝐬𝐢𝐜 🎶 𝐁𝐨𝐭 𝐑𝐮𝐧 𝐎𝐧 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 🥀 𝐕𝐩𝐬 💫𝐒𝐞𝐫𝐯𝐞𝐫 🌎 𝐅𝐞𝐞𝐥 ❤️ 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 𝐌𝐮𝐬𝐢𝐜 🎧 𝐈𝐧 𝐕𝐜 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐝 𝐁𝐲 = [SWEAT❤️](https://t.me/classy_network)

𝐂𝐫𝐞𝐚𝐭𝐨𝐫 :- [✨ 𝐊𝐈𝐍𝐆💜](https://t.me/I_AM_KING_OP)
𝐒𝐮𝐩𝐩𝐨𝐫𝐭 :- [✨ 𝐐𝐔𝐄𝐄𝐍 ❤️🎸](https://t.me/payalsahu1)
𝐃𝐢𝐬𝐜𝐮𝐬𝐬 :- [✨ 𝐆𝐑𝐎𝐔𝐏 🎧](https://t.me/freinnd)
𝐒𝐨𝐮𝐫𝐜𝐞  :- [✨ 𝐍𝐄𝐓𝐖𝐎𝐑𝐊 🌍](https://t.me/FROZY_BLOOD_BASHER)
𝐂𝐨𝐦𝐦𝐚𝐧𝐝 :- [✨ 𝐂𝐔𝐓𝐄 🚩](https://t.me/I_AM_KING_OP)
𝐅𝐞𝐞𝐋𝐢𝐧𝐠'𝐒 :- [✨ 𝗝𝗼𝗶𝗻 ❤️🥀](https://t.me/FROZY_BLOOD_BASHER)

𝐈𝐟 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 𝐀𝐧𝐲 𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧𝐬 𝐀𝐧𝐝 𝐇𝐞𝐥𝐩 𝐓𝐡𝐞𝐧 𝐃𝐦 𝐌𝐲 𝐁𝐨𝐬𝐬 = [𝗠𝗿 OWNER ❤️](https://t.me/I_AM_KING_OP)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🥀 Jᴏɪɴ Hᴇʀᴇ & Sᴜᴘᴘᴏʀᴛ ✨", url=f"https://t.me/freinnd")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/1cecce7c41d4f3fc5f0fc.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 GO TO MY GROUP  💞", url=f"https://t.me/freinnd")
                ]
            ]
        ),
    )
