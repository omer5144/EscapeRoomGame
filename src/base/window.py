from abc import ABC, abstractmethod

import pygame
from pygame import Surface
from pygame.event import Event


class Window(ABC):
    screen: Surface
    width: int
    height: int
    x: int
    y: int

    def __init__(self, screen: Surface, width: int, height: int, x: int, y):
        self.screen = screen

        self.width = width
        self.height = height

        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> None: ...

    def handle_events(self, events: list[Event]) -> type | None:
        for event in events:
            match event.type:
                case pygame.QUIT:
                    return self.on_quit(event)
                case pygame.MOUSEBUTTONDOWN:
                    return self.on_mouse_button_down(event)
                case pygame.KEYDOWN:
                    return self.on_key_down(event)

    def on_quit(self, event: Event) -> None:
        pass

    def on_mouse_button_down(self, event: Event) -> type | None:
        match event.button:
            case 1:
                return self.on_mouse_left_button_down(event)
            case 3:
                return self.on_mouse_right_button_down(event)

    def on_mouse_left_button_down(self, event: Event) -> None:
        pass

    def on_mouse_right_button_down(self, event: Event) -> None:
        pass

    def on_key_down(self, event: Event) -> None:
        pass
