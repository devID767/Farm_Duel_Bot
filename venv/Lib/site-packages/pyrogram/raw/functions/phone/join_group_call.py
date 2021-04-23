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


class JoinGroupCall(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0xb132ff7b``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        join_as: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        params: :obj:`DataJSON <pyrogram.raw.base.DataJSON>`
        muted (optional): ``bool``
        invite_hash (optional): ``str``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "join_as", "params", "muted", "invite_hash"]

    ID = 0xb132ff7b
    QUALNAME = "functions.phone.JoinGroupCall"

    def __init__(self, *, call: "raw.base.InputGroupCall", join_as: "raw.base.InputPeer", params: "raw.base.DataJSON", muted: Union[None, bool] = None, invite_hash: Union[None, str] = None) -> None:
        self.call = call  # InputGroupCall
        self.join_as = join_as  # InputPeer
        self.params = params  # DataJSON
        self.muted = muted  # flags.0?true
        self.invite_hash = invite_hash  # flags.1?string

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "JoinGroupCall":
        flags = Int.read(data)
        
        muted = True if flags & (1 << 0) else False
        call = TLObject.read(data)
        
        join_as = TLObject.read(data)
        
        invite_hash = String.read(data) if flags & (1 << 1) else None
        params = TLObject.read(data)
        
        return JoinGroupCall(call=call, join_as=join_as, params=params, muted=muted, invite_hash=invite_hash)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.invite_hash is not None else 0
        data.write(Int(flags))
        
        data.write(self.call.write())
        
        data.write(self.join_as.write())
        
        if self.invite_hash is not None:
            data.write(String(self.invite_hash))
        
        data.write(self.params.write())
        
        return data.getvalue()
