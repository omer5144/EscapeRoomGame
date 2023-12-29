import pygame
from pygame import Surface
from pygame.event import Event

from src.consts import strings, colors
from src.base import Header, Footer
from src.scenes import Scene


class SecondRoom(Scene):
    code_input: str

    def __init__(self, screen: Surface, width: int, height: int, x: int, y: int, header: Header, footer: Footer):
        super(SecondRoom, self).__init__(screen, width, height, x, y, header, footer, strings.SECOND_ROOM_NAME)

        self.code_input = ""

    def render(self):
        super(SecondRoom, self).render()

        text_surface = pygame.font.Font(None, 36).render(f"Code: {self.code_input}", True, colors.BLACK)
        self.screen.blit(text_surface, (50, self.y + 100))

    def on_key_down(self, event: Event) -> type | None:
        super(SecondRoom, self).on_key_down(event)

        if event.key == pygame.K_BACKSPACE:
            self.code_input = self.code_input[:-1]
        elif event.key == pygame.K_RETURN:
            if self.code_input == "1234":
                from src.scenes import LastRoom
                return LastRoom
            else:
                self.code_input = ""
        elif event.unicode.isdigit() and len(self.code_input) < 4:
            self.code_input += event.unicode
