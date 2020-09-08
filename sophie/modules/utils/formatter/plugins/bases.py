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

from typing import Any, List, Optional, TYPE_CHECKING, Type

if TYPE_CHECKING:
    from ..compiler import ParsedNoteModel, RawNoteModel
    from aiogram.api.types import Message, Chat, User


class BaseFormatPlugin:
    __syntax__: Optional[str] = None

    @classmethod
    async def compile_(
            cls, message: Message, data: RawNoteModel, payload: ParsedNoteModel, chat: Chat, user: Optional[User]
    ) -> Any:
        pass

    @classmethod
    async def decompile(
            cls, message: Message, data: RawNoteModel, payload: ParsedNoteModel, chat: Chat, user: Optional[User]
    ) -> Any:
        pass

    @classmethod
    async def validate(cls, *args: Any, **kwargs: Any) -> Any:
        pass


def get_all_plugins() -> List[Type[BaseFormatPlugin]]:
    return BaseFormatPlugin.__subclasses__()