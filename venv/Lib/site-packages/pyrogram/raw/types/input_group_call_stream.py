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


class InputGroupCallStream(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputFileLocation`.

    Details:
        - Layer: ``126``
        - ID: ``0xbba51639``

    Parameters:
        call: :obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`
        time_ms: ``int`` ``64-bit``
        scale: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["call", "time_ms", "scale"]

    ID = 0xbba51639
    QUALNAME = "types.InputGroupCallStream"

    def __init__(self, *, call: "raw.base.InputGroupCall", time_ms: int, scale: int) -> None:
        self.call = call  # InputGroupCall
        self.time_ms = time_ms  # long
        self.scale = scale  # int

    @staticmethod
    def read(data: BytesIO, *args: Any) -> "InputGroupCallStream":
        # No flags
        
        call = TLObject.read(data)
        
        time_ms = Long.read(data)
        
        scale = Int.read(data)
        
        return InputGroupCallStream(call=call, time_ms=time_ms, scale=scale)

    def write(self) -> bytes:
        data = BytesIO()
        data.write(Int(self.ID, False))

        # No flags
        
        data.write(self.call.write())
        
        data.write(Long(self.time_ms))
        
        data.write(Int(self.scale))
        
        return data.getvalue()
