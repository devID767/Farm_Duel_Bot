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


class ExportChatInvite(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0x14b9bcd7``

    Parameters:
        peer: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        legacy_revoke_permanent (optional): ``bool``
        expire_date (optional): ``int`` ``32-bit``
        usage_limit (optional): ``int`` ``32-bit``

    Returns:
        :obj:`ExportedChatInvite <pyrogram.raw.base.ExportedChatInvite>`
    """

    __slots__: List[str] = ["peer", "legacy_revoke_permanent", "expire_date", "usage_limit"]

    ID = 0x14b9bcd7
    QUALNAME = "functions.messages.ExportChatInvite"

    def __init__(self, *, peer: "raw.base.InputPeer", legacy_revoke_permanent: Union[None, bool] = None, expire_date: Union[None, int] = None, usage_limit: Union[None, int] = None) -> None:
        self.peer = peer  # InputPeer
        self.legacy_revoke_permanent = legacy_revoke_permanent  # flags.2?true
        self.expire_date = expire_date  # flags.0?int
        self.usage_limit = usage_limit  # flags.1?int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "ExportChatInvite":
        flags = Int.read(data)
        
        legacy_revoke_permanent = True if flags & (1 << 2) else False
        peer = TLObject.read(data)
        
        expire_date = Int.read(data) if flags & (1 << 0) else None
        usage_limit = Int.read(data) if flags & (1 << 1) else None
        return ExportChatInvite(peer=peer, legacy_revoke_permanent=legacy_revoke_permanent, expire_date=expire_date, usage_limit=usage_limit)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.legacy_revoke_permanent else 0
        flags |= (1 << 0) if self.expire_date is not None else 0
        flags |= (1 << 1) if self.usage_limit is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        if self.expire_date is not None:
            data.write(Int(self.expire_date))
        
        if self.usage_limit is not None:
            data.write(Int(self.usage_limit))
        
        return data.getvalue()
