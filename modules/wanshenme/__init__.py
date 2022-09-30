from logging.config import listen
from queue import Empty
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import StartsWith,MatchContent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from pydantic import ListMaxLengthError

import modules.wanshenme.fileio as wfio
from random import choice

channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def add_wanshenme(app:Ariadne, group:Group, message: Annotated[MessageChain, StartsWith(["+玩","加玩"])]):
    rawmsg = message.display
    res = wfio.write(rawmsg)
    if res == 1:
        return await app.send_message(
            group,
            f"{rawmsg} 已经有了，这么喜欢玩？"
        )
    elif res == 2:
        return await app.send_message(
            group,
            "empty string now allowed!!2"
        )
    await app.send_message(
        group,
        MessageChain(f"work done in idk how long it is seconds")
    )

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def wanshenme(app:Ariadne, group:Group, message: Annotated[MessageChain, StartsWith(["玩what","玩什么"])]):
    #匹配包含的暂时不想写 要不来个人帮我写吧
    await app.send_message(
        group,
        MessageChain(choice(wfio.get()))
    )
