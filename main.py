import asyncio

# Fix for Python 3.14+ where asyncio.get_event_loop() raises RuntimeError if no loop is running
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from bot import Bot

if __name__ == "__main__":
    Bot().run()
