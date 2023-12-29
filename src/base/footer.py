import pygame
from pygame import Surface, Rect
from pygame.event import Event

from src.consts import sizes, items, colors
from src.base import Window


class Footer(Window):
    image: Surface

    item_list: list[str]

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, items_max_count: int):
        super(Footer, self).__init__(screen, width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

        self.item_list = [items.NO_ITEM] * items_max_count

    def render(self) -> None:
        super(Footer, self).render()

        self.image.fill(colors.BLUE)
        self.screen.blit(self.image, (self.x, self.y))

        for index, item in enumerate(self.item_list):
            pygame.draw.rect(self.screen, colors.BLACK, self.__get_item_cube_rect(index))
            pygame.draw.rect(self.screen, colors.GRAY, self.__get_item_content_rect(index))

            if item != items.NO_ITEM:
                item_image = pygame.image.load(f'resources/items/{item}.png')
                self.screen.blit(
                    pygame.transform.scale(item_image, (self.__item_content_size, self.__item_content_size)),
                    (self.__item_content_x(index), self.__item_content_y))

    def handle_events(self, events: list[Event]) -> None:
        super(Footer, self).handle_events(events)

    def add_item(self, item: str) -> bool:
        for i in range(len(self.item_list)):
            if self.item_list[i] == items.NO_ITEM:
                self.item_list[i] = item
                return True
        return False

    @property
    def __item_cube_size(self) -> int:
        return self.height - sizes.ITEMS_Y_PADDING * 2

    @property
    def __item_content_size(self) -> int:
        return self.__item_cube_size - 2 * sizes.ITEM_CONTENT_MARGIN

    @property
    def __items_x_padding(self) -> int:
        return (self.width - self.__item_cube_size * len(self.item_list) - sizes.ITEMS_X_MARGIN * (
                len(self.item_list) + 1)) // 2

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
