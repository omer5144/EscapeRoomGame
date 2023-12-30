from src.consts import strings, items, backgrounds
from src.consts.objects import ObjectFiles, ObjectNames
from src.scenes import Scene


class MiddleTeamRoomFront(Scene):
    def __init__(self, **kwargs):

        super(MiddleTeamRoomFront, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                                  background_name=backgrounds.MIDDLE_ROOM_FRONT_BACKGROUND, **kwargs)

        self.add_object(ObjectNames.NOAM_TABLE, ObjectFiles.RIGHT_OFFICE_TABLE, 580, 280, 250, 150)

        self.add_object(ObjectNames.DOWN_ARROW, ObjectFiles.DOWN_ARROW, 440, 410, 100, 80)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectNames.DOWN_ARROW:
            from src.scenes import MiddleTeamRoomBack
            return MiddleTeamRoomBack

