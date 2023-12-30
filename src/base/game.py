import asyncio

import pygame
import sys

from pygame.event import Event

from src.consts import strings, items
from src.base import Window, Header, Body, Footer
from src.context.game_context import GameContext

pygame.init()


class Game(Window):
    is_running: bool

    header_height: int
    body_height: int
    footer_height: int

    header: Header
    body: Body
    footer: Footer

    game_context: GameContext

    def __init__(self, width: int, header_height: int, body_height, footer_height,
                 x: int, y: int, scenes_types: set[type], first_scene_type: type):
        super(Game, self).__init__(
            pygame.display.set_mode((width, header_height + body_height + footer_height)), width,
            header_height + body_height + footer_height, x, y)

        self.game_context = GameContext()

        self.is_running = True

        self.header_height = header_height
        self.body_height = body_height
        self.footer_height = footer_height

        self.header = Header(self.screen, self.width, self.header_height, self.x, self.__header_y)
        self.footer = Footer(self.screen, self.width, self.footer_height, self.x, self.__footer_y,
                             items.ITEMS_MAX_COUNT)
        self.body = Body(self.game_context, self.screen, self.width, self.body_height, self.x, self.__body_y,
                         scenes_types, first_scene_type, self.header, self.footer)

        pygame.display.set_caption(strings.WINDOW_CAPTION)

    def render(self) -> None:
        super(Game, self).render()

        self.body.render()
        self.header.render()
        self.footer.render()

    def handle_events(self, events: list[Event]) -> None:
        super(Game, self).handle_events(events)

        self.header.handle_events(events)
        self.body.handle_events(events)
        self.footer.handle_events(events)

    def on_quit(self, event: Event) -> None:
        super(Game, self).on_quit(event)

        self.stop()

    async def start(self) -> None:
        while self.is_running:
            self.render()
            pygame.display.flip()

            events = pygame.event.get()
            self.handle_events(events)
            await asyncio.sleep(0)

        pygame.quit()
        sys.exit()

    def stop(self) -> None:
        self.is_running = False

    @property
    def __header_y(self) -> int:
        return self.y

    @property
    def __body_y(self) -> int:
        return self.y + self.header_height

    @property
    def __footer_y(self) -> int:
        return self.y + self.header_height + self.body_height
