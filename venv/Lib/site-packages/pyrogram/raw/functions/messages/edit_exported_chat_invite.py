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


class EditExportedChatInvite(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0x2e4ffbe``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        link: ``str``
        revoked (optional): ``bool``
        expire_date (optional): ``int`` ``32-bit``
        usage_limit (optional): ``int`` ``32-bit``

    Returns:
        :obj:`messages.ExportedChatInvite <pyrogram.raw.base.messages.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "link", "revoked", "expire_date", "usage_limit"]

    ID = 0x2e4ffbe
    QUALNAME = "functions.messages.EditExportedChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", link: str, revoked: Union[None, bool] = None, expire_date: Union[None, int] = None, usage_limit: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.link = link  # string
        self.revoked = revoked  # flags.2?true
        self.expire_date = expire_date  # flags.0?int
        self.usage_limit = usage_limit  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditExportedChatInvite":
        flags = Int.read(data)
        
        revoked = True if flags & (1 << 2) else False
        peer = TLObject.read(data)
        
        link = String.read(data)
        
        expire_date = Int.read(data) if flags & (1 << 0) else None
        usage_limit = Int.read(data) if flags & (1 << 1) else None
        return EditExportedChatInvite(peer=peer, link=link, revoked=revoked, expire_date=expire_date, usage_limit=usage_limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.revoked else 0
        flags |= (1 << 0) if self.expire_date is not None else 0
        flags |= (1 << 1) if self.usage_limit is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(String(self.link))
        
        if self.expire_date is not None:
            data.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            data.write(Int(self.usage_limit))
        
        return data.getvalue()
