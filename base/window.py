from abc import ABC, abstractmethod

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

    @abstractmethod
    def handle_events(self, events: list[Event]) -> type | None: ...
