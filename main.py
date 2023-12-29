import asyncio

from consts import sizes
from window import Game
from window.scenes import FirstRoom, SecondRoom, LastRoom


async def main() -> None:
    assert sizes.HEADER_HEIGHT >= 2 * sizes.TEXT_Y_PADDING, "header height is not compatible with what it includes"
    assert sizes.FOOTER_HEIGHT >= 2 * sizes.SLOTS_Y_PADDING, "header height is not compatible with what it includes"

    await Game(sizes.WIDTH, sizes.HEADER_HEIGHT, sizes.BODY_HEIGHT, sizes.FOOTER_HEIGHT, 0, 0,
               {FirstRoom, SecondRoom, LastRoom}, FirstRoom).start()


if __name__ == "__main__":
    asyncio.run(main())
