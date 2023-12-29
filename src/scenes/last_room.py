from pygame import Surface, Rect

from src.consts import strings, objects
from src.base import Header, Footer
from src.scenes import Scene


class LastRoom(Scene):
    key_rect: Rect

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(LastRoom, self).__init__(screen, width, height, x, y, header, footer, strings.LAST_ROOM_NAME)

        self.add_object(objects.TROPHY_OBJECT, 100, 0, 100, 100)
