import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.INFO)

SESSION = environ.get("SESSION", "")
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)

    try:
        await client.approve_all_chat_join_requests(Id)
        await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    except FloodWait as t:
        await asyncio.sleep(t.value)
        await client.approve_all_chat_join_requests(Id)
        await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    except Exception as e:
        logging.error(str(e))
        # Fallback option
        try:
            join_requests = [request async for request in client.get_chat_join_requests(Id)]
            for request in join_requests:
                await client.approve_chat_join_request(Id, request.from_user.id)
                await asyncio.sleep(1)
            await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
        except Exception as e:
            logging.error(str(e))

logging.info("Bot Started....")
User.run()
