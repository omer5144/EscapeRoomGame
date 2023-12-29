from abc import abstractmethod
from typing import Callable

import pygame
from pygame import Surface
from pygame.event import Event

from consts import colors, strings
from window import Window, Header, Footer


class Scene(Window):
    image: Surface

    header: Header
    footer: Footer

    scene_name: str

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer,
                 scene_name: str):
        super(Scene, self).__init__(screen, width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

        self.header = header
        self.footer = footer

        self.scene_name = scene_name

    def render(self) -> None:
        super(Scene, self).render()

        self.set_text(strings.SCENE_TITLE_FORMAT.format(scene_name=self.scene_name))

        self.image.fill(colors.RED)
        self.screen.blit(self.image, (self.x, self.y))

    def resize(self, width: int, height: int, x: int, y: int) -> None:
        super(Scene, self).resize(width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

    @abstractmethod
    def handle_events(self, events: list[Event]) -> type | None: ...

    def set_text(self, text: str) -> None:
        self.header.set_text(text)
