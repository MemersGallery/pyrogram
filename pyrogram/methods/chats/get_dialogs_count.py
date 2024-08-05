#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
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

import pyrogram
from pyrogram import raw


class GetDialogsCount:
    async def get_dialogs_count(
        self: "pyrogram.Client",
        pinned_only: bool = False,
        chat_list: int = 0
    ) -> int:
        """Get the total count of your dialogs.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            pinned_only (``bool``, *optional*):
                Pass True if you want to count only pinned dialogs.
                Defaults to False.
            
            chat_list (``int``, *optional*):
                Chat list in which to search messages; Only Main (0) and Archive (1) chat lists are supported. Defaults to (0) Main chat list.

        Returns:
            ``int``: On success, the dialogs count is returned.

        Example:
            .. code-block:: python

                count = await app.get_dialogs_count()
                print(count)
        """

        if pinned_only:
            return len((await self.invoke(raw.functions.messages.GetPinnedDialogs(folder_id=chat_list))).dialogs)
        else:
            r = await self.invoke(
                raw.functions.messages.GetDialogs(
                    offset_date=0,
                    offset_id=0,
                    offset_peer=raw.types.InputPeerEmpty(),
                    limit=1,
                    hash=0,
                    folder_id=chat_list
                )
            )

            if isinstance(r, raw.types.messages.Dialogs):
                return len(r.dialogs)
            else:
                return r.count
