import pygame
from pygame import Surface

from src.consts import sizes, strings, colors, backgrounds
from src.base import Window


class Header(Window):
    background: Surface

    title_surface: Surface

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, title: str = strings.DEFAULT_HEADER_TITLE):
        super(Header, self).__init__(screen, width, height, x, y)

        if backgrounds.HEADER_BACKGROUND:
            self.background = pygame.transform.scale(
                pygame.image.load(f'resources/images/{backgrounds.HEADER_BACKGROUND}'), (self.width, self.height))
        else:
            self.background = pygame.Surface((self.width, self.height))
            self.background.fill(colors.BLUE)

        self.set_title(title)

    def render(self) -> None:
        super(Header, self).render()

        self.screen.blit(self.background, (self.x, self.y))

        self.screen.blit(self.title_surface, (self.x + self.__title_x_padding, self.y + sizes.TITLE_Y_PADDING))

    def set_title(self, title: str) -> None:
        self.title_surface = pygame.font.Font(None, self.__font_height).render(title, True, colors.BLACK)
        self.render()

    @property
    def __font_height(self) -> int:
        return self.height - sizes.TITLE_Y_PADDING * 2

    @property
    def __title_x_padding(self) -> int:
        return (self.width - self.title_surface.get_width()) // 2
