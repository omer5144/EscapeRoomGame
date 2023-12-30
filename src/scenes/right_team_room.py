from src.consts import strings, items, backgrounds
from src.consts.objects import ObjectFiles, ObjectNames
from src.scenes import Scene


class RightTeamRoom(Scene):
    def __init__(self, **kwargs):

        super(RightTeamRoom, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                           background_name=backgrounds.RIGHT_ROOM_BACKGROUND, **kwargs)

        self.add_object(ObjectNames.OMER_TABLE, ObjectFiles.LEFT_OFFICE_TABLE, 190, 260, 250, 150)
        self.add_object(ObjectNames.DANI_TABLE, ObjectFiles.RIGHT_OFFICE_TABLE, 550, 260, 250, 150)

        self.add_object(ObjectNames.LEFT_ARROW, ObjectFiles.LEFT_ARROW, 10, 260, 70, 85)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectNames.LEFT_ARROW:
            from src.scenes import MiddleTeamRoomBack
            return MiddleTeamRoomBack
