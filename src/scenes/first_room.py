import pygame
from pygame import Surface, Rect
from pygame.event import Event

from src.consts import strings, colors
from src.base import Header, Footer
from src.scenes import Scene


class FirstRoom(Scene):
    key_rect: Rect

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(FirstRoom, self).__init__(screen, width, height, x, y, header, footer, strings.FIRST_ROOM_NAME)

        self.key_rect = pygame.Rect(200, 200, 50, 50)

    def render(self):
        super(FirstRoom, self).render()

        pygame.draw.rect(self.screen, colors.BLACK, self.key_rect)

    def on_mouse_left_button_down_without_item(self, event: Event) -> type | None:
        super(FirstRoom, self).on_mouse_left_button_down_without_item(event)

        if self.key_rect.collidepoint(event.pos):
            from src.scenes import SecondRoom
            return SecondRoom

    def on_mouse_left_button_down_with_item(self, event: Event, item_name: str) -> None:
        super(FirstRoom, self).on_mouse_left_button_down_with_item(event, item_name)

        self.set_title(f"You can't use {item_name} on that")

    def on_mouse_right_button_down(self, event: Event) -> None:
        super(FirstRoom, self).on_mouse_right_button_down(event)

        self.add_item('santa')
