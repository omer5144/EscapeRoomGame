import pygame

from src.consts import strings, items, backgrounds, colors
from src.consts.objects import ObjectNames, ObjectFiles
from src.scenes import Scene


# this is an abstract ptouch class
class PtouchNoteAbstract(Scene):
    def __init__(self, note_text: str, **kwargs):
        self.note_text = note_text
        super(PtouchNoteAbstract, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                                 background_name=backgrounds.PTOUCH_NOTE_BACKGROUND, **kwargs)
        self.add_object(ObjectNames.DOWN_ARROW, ObjectFiles.DOWN_ARROW, 420, 410, 150, 80)

    def render(self):
        super(PtouchNoteAbstract, self).render()

        text_surface = pygame.font.Font(None, 100).render(self.note_text, True, colors.BLACK)
        rotated_text_surface = pygame.transform.rotate(text_surface, 12)
        self.screen.blit(rotated_text_surface, (280, 270))

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectNames.DOWN_ARROW:
            from src.scenes import LeftTeamRoom
            return LeftTeamRoom


class PtouchNoteFirst(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteFirst, self).__init__(note_text=strings.PTOUCH_SENTENCES[0], **kwargs)

class PtouchNoteSecond(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteSecond, self).__init__(note_text=strings.PTOUCH_SENTENCES[1], **kwargs)

class PtouchNoteThird(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteThird, self).__init__(note_text=strings.PTOUCH_SENTENCES[2], **kwargs)

class PtouchNoteFourth(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteFourth, self).__init__(note_text=strings.PTOUCH_SENTENCES[3], **kwargs)


class PtouchNoteFifth(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteFifth, self).__init__(note_text=strings.PTOUCH_SENTENCES[4], **kwargs)

class PtouchNoteSixth(PtouchNoteAbstract):
    def __init__(self, **kwargs):
        super(PtouchNoteSixth, self).__init__(note_text=strings.PTOUCH_SENTENCES[5], **kwargs)