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


class GetExportedChatInvites(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0xa2b5a3f6``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        admin_id: :obj:`InputUser <pyrogram.raw.base.InputUser>`
        limit: ``int`` ``32-bit``
        revoked (optional): ``bool``
        offset_date (optional): ``int`` ``32-bit``
        offset_link (optional): ``str``

    Returns:
        :obj:`messages.ExportedChatInvites <pyrogram.raw.base.messages.ExportedChatInvites>`
    """

    __slots__: List[str] = ["peer", "admin_id", "limit", "revoked", "offset_date", "offset_link"]

    ID = 0xa2b5a3f6
    QUALNAME = "functions.messages.GetExportedChatInvites"

    def __init__(self, *, peer: "raw.base.InputPeer", admin_id: "raw.base.InputUser", limit: int, revoked: Union[None, bool] = None, offset_date: Union[None, int] = None, offset_link: Union[None, str] = None) -> None:
        self.peer = peer  # InputPeer
        self.admin_id = admin_id  # InputUser
        self.limit = limit  # int
        self.revoked = revoked  # flags.3?true
        self.offset_date = offset_date  # flags.2?int
        self.offset_link = offset_link  # flags.2?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GetExportedChatInvites":
        flags = Int.read(data)
        
        revoked = True if flags & (1 << 3) else False
        peer = TLObject.read(data)
        
        admin_id = TLObject.read(data)
        
        offset_date = Int.read(data) if flags & (1 << 2) else None
        offset_link = String.read(data) if flags & (1 << 2) else None
        limit = Int.read(data)
        
        return GetExportedChatInvites(peer=peer, admin_id=admin_id, limit=limit, revoked=revoked, offset_date=offset_date, offset_link=offset_link)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.revoked else 0
        flags |= (1 << 2) if self.offset_date is not None else 0
        flags |= (1 << 2) if self.offset_link is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(self.admin_id.write())
        
        if self.offset_date is not None:
            data.write(Int(self.offset_date))
        
        if self.offset_link is not None:
            data.write(String(self.offset_link))
        
        data.write(Int(self.limit))
        
        return data.getvalue()
