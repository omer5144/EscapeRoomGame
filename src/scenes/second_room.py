import pygame
from pygame.event import Event

from src.consts import strings, colors
from src.scenes import Scene


class SecondRoom(Scene):
    code_input: str

    def __init__(self, **kwargs):
        super(SecondRoom, self).__init__(scene_name=strings.SECOND_ROOM_NAME, **kwargs)

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
