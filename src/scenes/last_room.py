import pygame
from pygame import Surface, Rect
from pygame.event import Event

from src.consts import strings, colors
from src.base import Header, Footer
from src.scenes import Scene


class LastRoom(Scene):
    key_rect: Rect

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(LastRoom, self).__init__(screen, width, height, x, y, header, footer, strings.LAST_ROOM_NAME)

        self.key_rect = pygame.Rect(300, 300, 50, 50)

    def render(self):
        super(LastRoom, self).render()

        pygame.draw.rect(self.screen, colors.BLUE, self.key_rect)
