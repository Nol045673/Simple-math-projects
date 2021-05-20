from telethon import TelegramClient

api_id = xxxxxxx
api_hash = 'XXXXXXXXXXXXXX'
client = TelegramClient('anon', api_id, api_hash)

async def main():
    await client.send_message('+XXXXXXXXXX', 'Hello, friend!')

with client:
    client.loop.run_until_complete(main())
