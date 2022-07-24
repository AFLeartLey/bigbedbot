from tkinter import Grid
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import modules.wanshenme_fileio as wfio
from random import randint

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def add_wanshenme(app: Ariadne,group: Group,message: MessageChain):
    rawmsg = message.display
    if rawmsg.startswith("+玩") or rawmsg.startswith("加玩"):
        wanshenme_list:list[str] = wfio.getlist()
        rawmsg = rawmsg[2:]

        while(rawmsg != "" and rawmsg[0] == " "):
            rawmsg = rawmsg[1:]
        if(rawmsg == ""):
            await app.send_message(group,MessageChain(f"empty string not allowed, minus 2 social credit"))
            return

        if (rawmsg+'\n') in wanshenme_list:
            await app.send_message(group,MessageChain(f"youle"))
            return

        wfio.add_wanshenme(rawmsg)
        await app.send_message(group,MessageChain(f"jiale"))

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def wanshenme(app: Ariadne,group: Group,message: MessageChain):
    rawmsg = message.display
    if rawmsg == "玩什么" or rawmsg == "wanshenme":
        wanshenme_list:list[str] = wfio.getlist()
        if len(wanshenme_list) == 0:
            await app.send_message(
                group,
                MessageChain(f"meiyou!")
            )
        k = randint(0,len(wanshenme_list)-1)
        await app.send_message(
            group,
            MessageChain(
                wanshenme_list[k][0:len(wanshenme_list[k])-1]
            )
        )