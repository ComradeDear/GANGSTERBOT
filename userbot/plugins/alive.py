import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


ALIVE_IMG = Config.ALIVE_PHOTTO
if ALIVE_IMG is None:
  ALIVE_IMG = "https://telegra.ph/file/5ecab2ff600f6300a3023.jpg"

@borg.on(admin_cmd(pattern="alive")
#@borg.on(events.NewMessage(pattern=r"\.alive(.*)",incoming=True))

        return
    mentions = "**πΎπΈβπΎπππΌβ-πΉππ is oNlIne**"
    mentions = "**ππΈπππΌβ**"     : {DEFAULTUSER}\n"
    mentions = "**ββπΈββπΌπ** "             : [join](https://t.me/gangsterbot_channel)\n"
    mentions = "** ππββπβπ πΎβππβ**"                         : [join](https://t.me/gangsterbot_support)\n"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
