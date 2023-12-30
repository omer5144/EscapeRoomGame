import pygame
from pygame.event import Event

from src.consts import strings, items, backgrounds
from src.consts.objects import ObjectFiles, ObjectNames
from src.scenes import Scene
from src.consts import colors


class IftachComputer(Scene):
    code_input: str
    def __init__(self, **kwargs):

        super(IftachComputer, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                             background_name=backgrounds.COMPUTER_SCREEN, **kwargs)
        self.add_object(ObjectNames.DOWN_ARROW, ObjectFiles.DOWN_ARROW, 430, 410, 100, 80)

        self.code_input = strings.COMPUTER_PASSWORD_PLACEHOLDER

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectNames.DOWN_ARROW:
            from src.scenes import MiddleTeamRoomBack
            return MiddleTeamRoomBack

    def render(self):
        super(IftachComputer, self).render()

        self.code_input = strings.COMPUTER_PASSWORD_PLACEHOLDER

        text_surface = pygame.font.Font(None, 36).render(f"Username: {strings.IFTACH_USERNAME}", True, colors.GREEN)
        self.screen.blit(text_surface, (300, self.y + 70))
        text_surface = pygame.font.Font(None, 36).render(f"Password:", True, colors.GREEN)
        self.screen.blit(text_surface, (300, self.y + 130))

        text_input = pygame.font.Font(None, 36).render(self.code_input, True, colors.GREEN)
        self.screen.blit(text_input, (420, self.y + 200))

    def on_key_down(self, event: Event) -> type | None:
        super(IftachComputer, self).on_key_down(event)

        if self.code_input == strings.COMPUTER_PASSWORD_PLACEHOLDER:
            self.code_input = ""

        if event.key == pygame.K_BACKSPACE:
            self.code_input = self.code_input[:-1]
        elif event.key == pygame.K_RETURN:
            if self.code_input == "1234":
                pass
                # TODO unlock computer
            else:
                self.code_input = ""
        elif event.unicode.isdigit() and len(self.code_input) < 4:
            self.code_input += event.unicode




