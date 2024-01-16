from builtins import enumerate
from dataclasses import dataclass

import pygame
from pygame import Surface, Rect
from pygame.event import Event

from src.consts import sizes, items, colors, sounds, backgrounds
from src.base import Window


@dataclass
class Item:
    name: str
    cube_rect: Rect
    content_rect: Rect
    image: Surface | None


class Footer(Window):
    background: Surface

    items_max_count: int
    item_list: list[Item]
    selected_item_index: int | None

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, items_max_count: int):
        super(Footer, self).__init__(screen, width, height, x, y)

        if backgrounds.HEADER_BACKGROUND:
            self.background = pygame.transform.scale(
                pygame.image.load(f'resources/images/{backgrounds.FOOTER_BACKGROUND}'), (self.width, self.height))
        else:
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill(colors.BLUE)

        self.items_max_count = items_max_count
        self.item_list = [
            Item(items.NO_ITEM, self.__get_item_cube_rect(index), self.__get_item_content_rect(index), None) for index
            in range(items_max_count)]
        self.selected_item_index = None

    def render(self) -> None:
        super(Footer, self).render()

        self.screen.blit(self.background, (self.x, self.y))

        for index, item in enumerate(self.item_list):
            pygame.draw.rect(self.screen, colors.GREEN if self.selected_item_index == index else colors.BLACK,
                             item.cube_rect)
            pygame.draw.rect(self.screen, colors.GRAY, item.content_rect)

            if item.image:
                self.screen.blit(item.image, item.content_rect)

    def on_mouse_left_button_down(self, event: Event) -> None:
        super(Footer, self).on_mouse_left_button_down(event)

        for index, item in enumerate(self.item_list):
            if item.cube_rect.collidepoint(event.pos) and self.item_list[index].name != items.NO_ITEM:
                self.selected_item_index = index
                return

        self.selected_item_index = None

    def add_item(self, item_name: str) -> bool:
        for i in range(len(self.item_list)):
            if self.item_list[i].name == items.NO_ITEM:
                self.item_list[i].name = item_name
                self.item_list[i].image = pygame.transform.scale(pygame.image.load(f'resources/images/{item_name}'),
                                                                 (self.__item_content_size, self.__item_content_size))

                self.make_sound(sounds.ADD_ITEM_SOUND)
                return True
        return False

    def use_selected_item(self) -> None:
        if self.selected_item_index is not None:
            for i in range(self.selected_item_index, self.items_max_count - 1):
                self.item_list[i].name = self.item_list[i + 1].name
                self.item_list[i].image = self.item_list[i + 1].image

            self.item_list[-1].name = items.NO_ITEM
            self.item_list[-1].image = None

    @property
    def selected_item(self) -> str | None:
        if self.selected_item_index is not None:
            return self.item_list[self.selected_item_index].name

    @property
    def __item_cube_size(self) -> int:
        return self.height - sizes.ITEMS_Y_PADDING * 2

    @property
    def __item_content_size(self) -> int:
        return self.__item_cube_size - 2 * sizes.ITEM_CONTENT_MARGIN

    @property
    def __items_x_padding(self) -> int:
        return (self.width - self.__item_cube_size * self.items_max_count - sizes.ITEMS_X_MARGIN * (
                self.items_max_count + 1)) // 2

    @property
    def __item_cube_y(self) -> int:
        return self.y + sizes.ITEMS_Y_PADDING

    @property
    def __item_content_y(self) -> int:
        return self.y + sizes.ITEMS_Y_PADDING + sizes.ITEM_CONTENT_MARGIN

    def __item_cube_x(self, index: int) -> int:
        return self.x + self.__items_x_padding + sizes.ITEMS_X_MARGIN + (
                sizes.ITEMS_X_MARGIN + self.__item_cube_size) * index

    def __item_content_x(self, index: int) -> int:
        return self.x + self.__items_x_padding + sizes.ITEMS_X_MARGIN + sizes.ITEM_CONTENT_MARGIN + (
                sizes.ITEMS_X_MARGIN + self.__item_cube_size) * index

    def __get_item_cube_rect(self, index: int) -> Rect:
        return pygame.Rect(self.__item_cube_x(index),
                           self.__item_cube_y,
                           self.__item_cube_size,
                           self.__item_cube_size
                           )

    def __get_item_content_rect(self, index: int) -> Rect:
        return pygame.Rect(self.__item_content_x(index),
                           self.__item_content_y,
                           self.__item_content_size,
                           self.__item_content_size
                           )
