import pygame
from pygame import Surface, Rect
from pygame.event import Event

from consts import colors, strings
from base import Header, Footer
from scenes import Scene


class LastRoom(Scene):
    key_rect: Rect

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(LastRoom, self).__init__(screen, width, height, x, y, header, footer, strings.LAST_ROOM_NAME)

        self.key_rect = pygame.Rect(300, 300, 50, 50)

    def render(self):
        super(LastRoom, self).render()

        pygame.draw.rect(self.screen, colors.BLUE, self.key_rect)

    def handle_events(self, events: list[Event]) -> None:
        super(LastRoom, self).handle_events(events)
