# Copyright (C) 2018 - 2020 MrYacha.
# Copyright (C) 2020 Jeepeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# This file is part of Sophie.

from __future__ import annotations

import re
from typing import Any, Match, Optional, TYPE_CHECKING

from .bases import BaseFormatPlugin
from .document import FILE_TYPES

if TYPE_CHECKING:
    from ..compiler import ParsedNoteModel, RawNoteModel
    from aiogram.api.types import Message, Chat, User


class WebPreview(BaseFormatPlugin):
    __syntax__: str = r"[%|$]PREVIEW"

    @classmethod
    async def validate(cls, message: Message, match: Optional[Match], data: RawNoteModel) -> Any:  # type: ignore
        if match:
            data.__setattr__('web_preview', True)
            if data.text:
                data.text = re.sub('%PREVIEW', '', data.text)

    @classmethod
    async def compile_(
            cls, message: Message, data: RawNoteModel, payload: ParsedNoteModel, chat: Chat, user: Optional[User]
    ) -> Any:
        if preview := getattr(data, 'web_preview', None) and FILE_TYPES not in payload.__fields__:
            payload.__setattr__('disable_web_page_preview', preview)

    @classmethod
    async def decompile(
            cls, message: Message, data: RawNoteModel, payload: ParsedNoteModel, chat: Chat, user: Optional[User]
    ) -> Any:
        if preview := getattr(data, 'web_preview', None) and FILE_TYPES not in payload.__fields__:
            if preview is True and payload.text is not None:
                payload.text += "%PREVIEW"