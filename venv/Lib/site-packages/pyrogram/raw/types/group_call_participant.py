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


class GroupCallParticipant(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.GroupCallParticipant`.

    Details:
        - Layer: ``126``
        - ID: ``0x19adba89``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        date: ``int`` ``32-bit``
        source: ``int`` ``32-bit``
        muted (optional): ``bool``
        left (optional): ``bool``
        can_self_unmute (optional): ``bool``
        just_joined (optional): ``bool``
        versioned (optional): ``bool``
        min (optional): ``bool``
        muted_by_you (optional): ``bool``
        volume_by_admin (optional): ``bool``
        is_self (optional): ``bool``
        active_date (optional): ``int`` ``32-bit``
        volume (optional): ``int`` ``32-bit``
        about (optional): ``str``
        raise_hand_rating (optional): ``int`` ``64-bit``
    """

    __slots__: List[str] = ["peer", "date", "source", "muted", "left", "can_self_unmute", "just_joined", "versioned", "min", "muted_by_you", "volume_by_admin", "is_self", "active_date", "volume", "about", "raise_hand_rating"]

    ID = 0x19adba89
    QUALNAME = "types.GroupCallParticipant"

    def __init__(self, *, peer: "raw.base.Peer", date: int, source: int, muted: Union[None, bool] = None, left: Union[None, bool] = None, can_self_unmute: Union[None, bool] = None, just_joined: Union[None, bool] = None, versioned: Union[None, bool] = None, min: Union[None, bool] = None, muted_by_you: Union[None, bool] = None, volume_by_admin: Union[None, bool] = None, is_self: Union[None, bool] = None, active_date: Union[None, int] = None, volume: Union[None, int] = None, about: Union[None, str] = None, raise_hand_rating: Union[None, int] = None) -> None:
        self.peer = peer  # Peer
        self.date = date  # int
        self.source = source  # int
        self.muted = muted  # flags.0?true
        self.left = left  # flags.1?true
        self.can_self_unmute = can_self_unmute  # flags.2?true
        self.just_joined = just_joined  # flags.4?true
        self.versioned = versioned  # flags.5?true
        self.min = min  # flags.8?true
        self.muted_by_you = muted_by_you  # flags.9?true
        self.volume_by_admin = volume_by_admin  # flags.10?true
        self.is_self = is_self  # flags.12?true
        self.active_date = active_date  # flags.3?int
        self.volume = volume  # flags.7?int
        self.about = about  # flags.11?string
        self.raise_hand_rating = raise_hand_rating  # flags.13?long

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "GroupCallParticipant":
        flags = Int.read(data)
        
        muted = True if flags & (1 << 0) else False
        left = True if flags & (1 << 1) else False
        can_self_unmute = True if flags & (1 << 2) else False
        just_joined = True if flags & (1 << 4) else False
        versioned = True if flags & (1 << 5) else False
        min = True if flags & (1 << 8) else False
        muted_by_you = True if flags & (1 << 9) else False
        volume_by_admin = True if flags & (1 << 10) else False
        is_self = True if flags & (1 << 12) else False
        peer = TLObject.read(data)
        
        date = Int.read(data)
        
        active_date = Int.read(data) if flags & (1 << 3) else None
        source = Int.read(data)
        
        volume = Int.read(data) if flags & (1 << 7) else None
        about = String.read(data) if flags & (1 << 11) else None
        raise_hand_rating = Long.read(data) if flags & (1 << 13) else None
        return GroupCallParticipant(peer=peer, date=date, source=source, muted=muted, left=left, can_self_unmute=can_self_unmute, just_joined=just_joined, versioned=versioned, min=min, muted_by_you=muted_by_you, volume_by_admin=volume_by_admin, is_self=is_self, active_date=active_date, volume=volume, about=about, raise_hand_rating=raise_hand_rating)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.muted else 0
        flags |= (1 << 1) if self.left else 0
        flags |= (1 << 2) if self.can_self_unmute else 0
        flags |= (1 << 4) if self.just_joined else 0
        flags |= (1 << 5) if self.versioned else 0
        flags |= (1 << 8) if self.min else 0
        flags |= (1 << 9) if self.muted_by_you else 0
        flags |= (1 << 10) if self.volume_by_admin else 0
        flags |= (1 << 12) if self.is_self else 0
        flags |= (1 << 3) if self.active_date is not None else 0
        flags |= (1 << 7) if self.volume is not None else 0
        flags |= (1 << 11) if self.about is not None else 0
        flags |= (1 << 13) if self.raise_hand_rating is not None else 0
        data.write(Int(flags))
        
        data.write(self.peer.write())
        
        data.write(Int(self.date))
        
        if self.active_date is not None:
            data.write(Int(self.active_date))
        
        data.write(Int(self.source))
        
        if self.volume is not None:
            data.write(Int(self.volume))
        
        if self.about is not None:
            data.write(String(self.about))
        
        if self.raise_hand_rating is not None:
            data.write(Long(self.raise_hand_rating))
        
        return data.getvalue()
