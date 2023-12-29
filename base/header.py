import pygame
from pygame import Surface
from pygame.event import Event

from consts import colors, sizes, strings
from window import Window


class Header(Window):
    image: Surface

    text_surface: Surface

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, text: str = strings.DEFAULT_HEADER_TEXT):
        super(Header, self).__init__(screen, width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

        self.set_text(text)

    def render(self) -> None:
        super(Header, self).render()

        self.image.fill(colors.BLUE)
        self.screen.blit(self.image, (self.x, self.y))

        self.screen.blit(self.text_surface, (self.x + self._text_x_padding, self.y + sizes.TEXT_Y_PADDING))

    def resize(self, width: int, height: int, x: int, y: int) -> None:
        super(Header, self).resize(width, height, x, y)

        self.image = pygame.Surface((self.width, self.height))

    def handle_events(self, events: list[Event]) -> None:
        super(Header, self).handle_events(events)

    @property
    def min_width(self) -> int:
        return self.text_surface.get_width()

    @property
    def min_height(self) -> int:
        return self.height

    def set_text(self, text: str) -> None:
        self.text_surface = pygame.font.Font(None, self._font_height).render(text, True, colors.BLACK)

    @property
    def _font_height(self) -> int:
        return self.height - sizes.TEXT_Y_PADDING * 2

    @property
    def _text_x_padding(self) -> int:
        return (self.width - self.text_surface.get_width()) // 2
