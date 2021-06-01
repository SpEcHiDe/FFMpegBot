#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Telegram Terminal Bot
# CopyLeft AGPLv3 (C) 2020 The Authors
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client,
    filters
)

from termbot import (
    AUTH_USERS,
    NO_CMD_RUNNING,
    TERMINATE_CMD_TRIGGER,
    TERMINATE_HELP_GNIRTS,

    aktifperintah
)

from termbot.helper_funcs.hash_msg import hash_msg


@Client.on_message(filters.command([TERMINATE_CMD_TRIGGER]) & filters.chat(AUTH_USERS))
async def terminate_cmd_t(client, message):
    if message.reply_to_message is None:
        await message.reply_text(TERMINATE_HELP_GNIRTS, quote=True)
        return
    if hash_msg(message.reply_to_message) in aktifperintah:
        try:
            aktifperintah[hash_msg(message.reply_to_message)].process.terminate()
        except Exception:
            await message.reply_text("Could not Terminate!", quote=True)
        else:
            del aktifperintah[hash_msg(message.reply_to_message)]
            await message.reply_to_message.edit("Terminated!")
    else:
        await message.reply_text(NO_CMD_RUNNING, quote=True)
