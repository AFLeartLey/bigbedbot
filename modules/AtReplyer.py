from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.ariadne.message.element import At

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def AtReplyer(app:Ariadne,group:Group,message:MessageChain,event:GroupMessage):
    if At(app.account) in event.message_chain:
        await app.send_message(group,MessageChain(f"嗯。"))
