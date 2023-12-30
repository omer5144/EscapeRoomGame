from src.consts import strings
from src.scenes import Scene
from src.consts.objects import ObjectFiles


class LastRoom(Scene):
    def __init__(self, **kwargs):
        super(LastRoom, self).__init__(scene_name=strings.LAST_ROOM_NAME, **kwargs)

        self.add_object(ObjectFiles.TROPHY_OBJECT, ObjectFiles.TROPHY_OBJECT, 100, 0, 100, 100)
