from logging.config import listen
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import MatchContent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

helpmessage = """
这是一个西八bot
----------功能列表
语录 查一个人的随机语录。
用法：
语录 <人名>
如:
语录 nh

加语录 给一个人添加一条语录。
用法：
加语录 <人名>:<内容>
如：
加语录 ngd:神！

ssibal 一个被我拿来当ping的玩意。
----------
群友什么时候赞助我50
"""
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def get_help(app:Ariadne, group:Group, message: Annotated[MessageChain, MatchContent("帮助页面")]):
    return await app.send_message(
        group,
        MessageChain(helpmessage)
    )
