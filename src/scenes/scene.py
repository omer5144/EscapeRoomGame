from abc import abstractmethod
from typing import Optional

import pygame
from pygame import Surface
from pygame.event import Event

from src.consts import strings, colors
from src.base import Window, Header, Footer


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

        self.set_title(strings.SCENE_TITLE_FORMAT.format(scene_name=self.scene_name))

    def render(self) -> None:
        super(Scene, self).render()

        self.image.fill(colors.RED)
        self.screen.blit(self.image, (self.x, self.y))

    def on_mouse_left_button_down(self, event: Event) -> type | None:
        super(Scene, self).on_mouse_left_button_down(event)

        if self.footer.selected_item:
            return self.on_mouse_left_button_down_with_item(event, self.footer.selected_item)
        else:
            return self.on_mouse_left_button_down_without_item(event)

    def on_mouse_left_button_down_with_item(self, event: Event, item_name: str) -> None:
        pass

    def on_mouse_left_button_down_without_item(self, event: Event) -> None:
        pass

    def set_title(self, title: str) -> None:
        self.header.set_title(title)

    def add_item(self, item_name: str) -> None:
        self.footer.add_item(item_name)

