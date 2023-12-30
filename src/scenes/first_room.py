from src.consts import strings, items, backgrounds
from src.scenes import Scene
from src.consts.objects import ObjectFiles


class FirstRoom(Scene):
    def __init__(self, **kwargs):

        super(FirstRoom, self).__init__(scene_name=strings.FIRST_ROOM_NAME,
                                        background_name=backgrounds.FOREST_BACKGROUND, **kwargs)

        self.add_object(ObjectFiles.SANTA_OBJECT, ObjectFiles.SANTA_OBJECT, 400, 200, 200, 200)
        self.add_object(ObjectFiles.SNOWFLAKE_OBJECT, ObjectFiles.SNOWFLAKE_OBJECT, 650, 250, 100, 100)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        if item_name == items.SNOWFLAKE_ITEM and object_name == ObjectFiles.SANTA_OBJECT:
            self.use_selected_item()
            from src.scenes import SecondRoom
            return SecondRoom

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == ObjectFiles.SANTA_OBJECT:
            self.set_title('I want my snowflake')
        elif object_name == ObjectFiles.SNOWFLAKE_OBJECT:
            self.remove_object(ObjectFiles.SNOWFLAKE_OBJECT)
            self.add_item(items.SNOWFLAKE_ITEM)
            self.set_title('This is a special snowflake')
