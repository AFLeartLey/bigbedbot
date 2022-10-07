import re
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group,Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.broadcast.exceptions import ExecutionStop
from graia.broadcast.builtin.decorators import Depend
from graia.ariadne.message.parser.base import StartsWith

from modules.keyword import fileio as kwio

channel = Channel.current()

def checkAdmin():
    adminid = 2043118307
    async def checkAdmin_deco(app: Ariadne,group: Group,member: Member):
        if member.id != adminid:
            await app.send_message(
                group,
                MessageChain("你叫什么 你是bot管理？")
            )
            return ExecutionStop
    return Depend(checkAdmin_deco)

@channel.use(ListenerSchema(listening_events=[GroupMessage],decorators=[checkAdmin]))
async def get_sentence(app:Ariadne,member: Member, group:Group, message: Annotated[MessageChain,StartsWith("添加保留字")]):
    rawmsg = message.display
    if(member.id != 2043118307):
        return await app.send_message(
                group,
                MessageChain("你叫什么 你是bot管理？")
            )
    kwio.add(rawmsg)
    return await app.send_message(group,MessageChain(f"ok done"))