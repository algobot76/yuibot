import asyncio

import hoshino

bot = hoshino.init()
app = bot.asgi

if __name__ == "__main__":
    bot.run(use_reloader=False, loop=asyncio.get_event_loop())
