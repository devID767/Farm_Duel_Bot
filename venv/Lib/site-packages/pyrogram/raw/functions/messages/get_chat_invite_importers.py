#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetChatInviteImporters(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0x26fb7289``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        link: ``str``
        offset_date: ``int`` ``32-bit``
        offset_user: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        limit: ``int`` ``32-bit``

    Returns:
        :obj:`messages.ChatInviteImporters <pyrogram.raw.base.messages.ChatInviteImporters>`
    """

    __slots__: List[str] = ["peer", "link", "offset_date", "offset_user", "limit"]

    ID = 0x26fb7289
    QUALNAME = "functions.messages.GetChatInviteImporters"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str, offset_date: int, offset_user: "raw.base.InputUser", limit: int) -> None:
        self.peer = peer  # InputPeer
        self.link = link  # string
        self.offset_date = offset_date  # int
        self.offset_user = offset_user  # InputUser
        self.limit = limit  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetChatInviteImporters":
        # No flags
        
        peer = TLObject.read(data)
        
        link = String.read(data)
        
        offset_date = Int.read(data)
        
        offset_user = TLObject.read(data)
        
        limit = Int.read(data)
        
        return GetChatInviteImporters(peer=peer, link=link, offset_date=offset_date, offset_user=offset_user, limit=limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.peer.write())
        
        data.write(String(self.link))
        
        data.write(Int(self.offset_date))
        
        data.write(self.offset_user.write())
        
        data.write(Int(self.limit))
        
        return data.getvalue()
