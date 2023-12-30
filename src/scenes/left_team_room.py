from src.consts import strings, items, backgrounds
from src.consts.objects import ObjectNames, ObjectFiles
from src.scenes import Scene
from src.context.left_team_room_context import LeftTeamRoomContext


class LeftTeamRoom(Scene):
    def __init__(self, **kwargs):
        super(LeftTeamRoom, self).__init__(scene_context_type=LeftTeamRoomContext, scene_name=strings.FIRST_ROOM_NAME,
                                           background_name=backgrounds.LEFT_ROOM_BACKGROUND, **kwargs)

        self.add_object(ObjectNames.AVIV_TABLE, ObjectFiles.LEFT_OFFICE_TABLE, 170, 260, 250, 150)
        self.add_object(ObjectNames.ADI_TABLE, ObjectFiles.RIGHT_OFFICE_TABLE, 530, 260, 250, 150)

        self.add_object(ObjectNames.ADI_CHARACTER, ObjectFiles.ADI_CHARACTER, 650, 220, 90,
                        80, 360-6)

        self.add_object(ObjectNames.PTOUCH_CLOSET, ObjectFiles.LEFT_CLOSET, 0, 150, 170, 290)

        self.add_object(ObjectNames.PTOUCH_NOTES[0], ObjectFiles.PTOUCH_NOTE, 55, 330, 40, 30)
        self.add_object(ObjectNames.PTOUCH_NOTES[1], ObjectFiles.PTOUCH_NOTE, 55, 350, 40, 30)
        self.add_object(ObjectNames.PTOUCH_NOTES[2], ObjectFiles.PTOUCH_NOTE, 55, 370, 40, 30)

        self.add_object(ObjectNames.PTOUCH_NOTES[3], ObjectFiles.PTOUCH_NOTE, 105, 320, 40, 30)
        self.add_object(ObjectNames.PTOUCH_NOTES[4], ObjectFiles.PTOUCH_NOTE, 105, 340, 40, 30)
        self.add_object(ObjectNames.PTOUCH_NOTES[5], ObjectFiles.PTOUCH_NOTE, 105, 360, 40, 30)

        self.add_object(ObjectNames.RIGHT_ARROW, ObjectFiles.RIGHT_ARROW, 920, 260, 70, 80)


    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name in ObjectNames.PTOUCH_NOTES:
            return self._on_pressed_on_ptouch_note(object_name)
        elif object_name == ObjectNames.RIGHT_ARROW:
            from src.scenes import MiddleTeamRoomBack
            return MiddleTeamRoomBack
        elif object_name == ObjectNames.ADI_CHARACTER:
            self._on_pressed_on_adi_character()


    def _on_pressed_on_ptouch_note(self, object_name: str) -> None:
        ptouch_num = ObjectNames.PTOUCH_NOTES.index(object_name)
        from src.scenes import PTOUCH_SCENES
        return PTOUCH_SCENES[ptouch_num]

    def _on_pressed_on_adi_character(self):
        if self.scene_context.is_omer_adam_playing():
            self.set_title("...")
        else:
            self.set_title("lalala")


