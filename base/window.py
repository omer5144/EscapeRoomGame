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
    def resize(self, width: int, height: int, x: int, y: int) -> None:
        self.width = width
        self.height = height

        self.x = x
        self.y = y

    @abstractmethod
    def handle_events(self, events: list[Event]) -> type | None: ...

    @property
    def min_width(self) -> int:
        return 0

    @property
    def min_height(self) -> int:
        return 0

