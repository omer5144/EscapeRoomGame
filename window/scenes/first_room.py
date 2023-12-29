import pygame
from pygame import Surface, Rect
from pygame.event import Event

from consts import colors, strings
from window import Header, Footer
from window.scenes import Scene


class FirstRoom(Scene):
    key_rect: Rect

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(FirstRoom, self).__init__(screen, width, height, x, y, header, footer, strings.FIRST_ROOM_NAME)

        self.key_rect = pygame.Rect(200, 200, 50, 50)

    def render(self):
        super(FirstRoom, self).render()

        pygame.draw.rect(self.screen, colors.BLACK, self.key_rect)

    def handle_events(self, events: list[Event]) -> type | None:
        super(FirstRoom, self).handle_events(events)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if self.key_rect.collidepoint(event.pos):
                        from window.scenes import second_room
                        return second_room.SecondRoom
