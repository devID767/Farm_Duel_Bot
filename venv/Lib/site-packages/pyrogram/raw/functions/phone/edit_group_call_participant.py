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


class EditGroupCallParticipant(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``126``
        - ID: ``0xd975eb80``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        participant: :obj:`InputPeer <pyrogram.raw.base.InputPeer>`
        muted (optional): ``bool``
        volume (optional): ``int`` ``32-bit``
        raise_hand (optional): ``bool``

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "participant", "muted", "volume", "raise_hand"]

    ID = 0xd975eb80
    QUALNAME = "functions.phone.EditGroupCallParticipant"

    def __init__(self, *, call: "raw.base.InputGroupCall", participant: "raw.base.InputPeer", muted: Union[None, bool] = None, volume: Union[None, int] = None, raise_hand: Union[None, bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.participant = participant  # InputPeer
        self.muted = muted  # flags.0?true
        self.volume = volume  # flags.1?int
        self.raise_hand = raise_hand  # flags.2?Bool

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "EditGroupCallParticipant":
        flags = Int.read(data)
        
        muted = True if flags & (1 << 0) else False
        call = TLObject.read(data)
        
        participant = TLObject.read(data)
        
        volume = Int.read(data) if flags & (1 << 1) else None
        raise_hand = Bool.read(data) if flags & (1 << 2) else None
        return EditGroupCallParticipant(call=call, participant=participant, muted=muted, volume=volume, raise_hand=raise_hand)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.volume is not None else 0
        flags |= (1 << 2) if self.raise_hand is not None else 0
        data.write(Int(flags))
        
        data.write(self.call.write())
        
        data.write(self.participant.write())
        
        if self.volume is not None:
            data.write(Int(self.volume))
        
        if self.raise_hand is not None:
            data.write(Bool(self.raise_hand))
        
        return data.getvalue()
