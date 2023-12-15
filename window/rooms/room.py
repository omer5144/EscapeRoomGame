from abc import abstractmethod
from typing import Callable

import pygame
from pygame import Surface
from pygame.event import Event

from consts import colors, strings
from window import Window, Header, Footer


class Room(Window):
    image: Surface

    header: Header
    footer: Footer

    room_name: str

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer,
                 room_name: str):
        super(Room, self).__init__(screen, width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

        self.header = header
        self.footer = footer

        self.room_name = room_name

    def render(self) -> None:
        super(Room, self).render()

        self.set_text(strings.ROOM_TITLE_FORMAT.format(room_name=self.room_name))

        self.image.fill(colors.RED)
        self.screen.blit(self.image, (self.x, self.y))

    def resize(self, width: int, height: int, x: int, y: int) -> None:
        super(Room, self).resize(width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

    @abstractmethod
    def handle_events(self, events: list[Event]) -> type | None: ...

    def set_text(self, text: str) -> None:
        self.header.set_text(text)
