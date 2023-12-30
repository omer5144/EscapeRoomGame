import asyncio

from src.consts import sizes
from src.base import Game
from src.scenes import (FirstRoom, SecondRoom, LastRoom, LeftTeamRoom, RightTeamRoom, MiddleTeamRoomBack, PTOUCH_SCENES,
                        MiddleTeamRoomFront, IftachComputer)


async def main() -> None:
    ptouch_scenes = set(PTOUCH_SCENES)
    scene = {LeftTeamRoom, MiddleTeamRoomBack, RightTeamRoom, MiddleTeamRoomFront, IftachComputer}
    all_scenes = scene.union(ptouch_scenes)

    example_scenes = {FirstRoom, SecondRoom, LastRoom}

    await Game(sizes.WIDTH, sizes.HEADER_HEIGHT, sizes.BODY_HEIGHT, sizes.FOOTER_HEIGHT, 0, 0,
               all_scenes, MiddleTeamRoomBack).start()


if __name__ == "__main__":
    asyncio.run(main())
