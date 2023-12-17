import asyncio

import typer

from pyredis.asyncserver import RedisServerProtocol


REDIS_DEFAULT_PORT = 6379


async def main(port=None):
    if port == None:
        port = REDIS_DEFAULT_PORT
    else:
        port = int(port)

    print(f"Starting PyRedis on port: {port}")

    loop = asyncio.get_running_loop()

    server = await loop.create_server(
        lambda: RedisServerProtocol(), "127.0.0.1", REDIS_DEFAULT_PORT
    )

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    typer.run(asyncio.run(main()))