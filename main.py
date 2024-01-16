import asyncio

from src.consts import sizes, sounds
from src.base import Game
from src.scenes import FirstRoom, SecondRoom, LastRoom


async def main() -> None:
    await Game(sizes.WIDTH, sizes.HEADER_HEIGHT, sizes.BODY_HEIGHT, sizes.FOOTER_HEIGHT, 0, 0,
               {FirstRoom, SecondRoom, LastRoom}, FirstRoom, sounds.BACKGROUND_MUSIC).start()


if __name__ == "__main__":
    asyncio.run(main())
