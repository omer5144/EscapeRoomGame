from src.consts import strings, items, backgrounds
from src.consts.objects import ObjectFiles, ObjectNames
from src.scenes import Scene


class MiddleTeamRoomBack(Scene):
    def __init__(self, **kwargs):

        super(MiddleTeamRoomBack, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                                 background_name=backgrounds.MIDDLE_ROOM_BACK_BACKGROUND, **kwargs)

        self.add_object(ObjectNames.IFTACH_TABLE, ObjectFiles.LEFT_OFFICE_TABLE, 100, 230, 250, 150)
        self.add_object(ObjectNames.SPARE_TABLE, ObjectFiles.RIGHT_OFFICE_TABLE, 560, 230, 250, 150)

        self.add_object(ObjectNames.RIGHT_ARROW, ObjectFiles.RIGHT_ARROW, 920, 260, 70, 80)
        self.add_object(ObjectNames.LEFT_ARROW, ObjectFiles.LEFT_ARROW, 10, 260, 70, 85)
        self.add_object(ObjectNames.DOWN_ARROW, ObjectFiles.DOWN_ARROW, 440, 410, 100, 80)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        pass

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectNames.RIGHT_ARROW:
            from src.scenes import RightTeamRoom
            return RightTeamRoom
        elif object_name == ObjectNames.LEFT_ARROW:
            from src.scenes import LeftTeamRoom
            return LeftTeamRoom
        elif object_name == ObjectNames.DOWN_ARROW:
            from src.scenes import MiddleTeamRoomFront
            return MiddleTeamRoomFront
