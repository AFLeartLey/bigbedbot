from logging.config import listen
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import MatchContent
from graia.broadcast.builtin.decorators import Depend
from graia.broadcast.exceptions import ExecutionStop

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

grouplist = [916717813]

def checkgr():
    async def checkgr_depo(app:Ariadne, group:Group):
        if group.id not in grouplist:
            raise ExecutionStop
    return Depend(checkgr_depo)

@channel.use(ListenerSchema(decorators=[Depend(checkgr)],listening_events=[GroupMessage]))
async def getsign(app:Ariadne,group:Group,message:Annotated[MessageChain,MatchContent("签到")]):
    ...
