from src.consts import strings, objects
from src.scenes import Scene


class LastRoom(Scene):
    def __init__(self, **kwargs):
        super(LastRoom, self).__init__(scene_name=strings.LAST_ROOM_NAME, **kwargs)

        self.add_object(objects.TROPHY_OBJECT, 100, 0, 100, 100)
