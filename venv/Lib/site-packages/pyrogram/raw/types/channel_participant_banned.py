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


class ChannelParticipantBanned(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``126``
        - ID: ``0x50a1dfd6``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        kicked_by: ``int`` ``32-bit``
        date: ``int`` ``32-bit``
        banned_rights: :obj:`ChatBannedRights <pyrogram.raw.base.ChatBannedRights>`
        left (optional): ``bool``
    """

    __slots__: List[str] = ["peer", "kicked_by", "date", "banned_rights", "left"]

    ID = 0x50a1dfd6
    QUALNAME = "types.ChannelParticipantBanned"

    def __init__(self, *, peer: "raw.base.Peer", kicked_by: int, date: int, banned_rights: "raw.base.ChatBannedRights", left: Union[None, bool] = None) -> None:
        self.peer = peer  # Peer
        self.kicked_by = kicked_by  # int
        self.date = date  # int
        self.banned_rights = banned_rights  # ChatBannedRights
        self.left = left  # flags.0?true

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ChannelParticipantBanned":
        flags = Int.read(data)
        
        left = True if flags & (1 << 0) else False
        peer = TLObject.read(data)
        
        kicked_by = Int.read(data)
        
        date = Int.read(data)
        
        banned_rights = TLObject.read(data)
        
        return ChannelParticipantBanned(peer=peer, kicked_by=kicked_by, date=date, banned_rights=banned_rights, left=left)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.left else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.kicked_by))
        
        data.write(Int(self.date))
        
        data.write(self.banned_rights.write())
        
        return data.getvalue()
