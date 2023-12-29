# EscapeRoomGame
This project is a template for an "Escape Room" game.

## Project Structure
- src - the code
  - base - the base classes for the game
  - consts - the constant variables of the game
  - scenes - the scenes classes
- resources
  - images - the images files to display in the game

### Base Classes
- Window - a generic window in the game, defines the rendering and events handling methods
- Game - the game loop, contains the 3 parts of the window
- header - the header of the screen, contains the title
- body - the middle of the screen, contains the switching scenes
- footer the footer of the screen, contains the collected items

### Consts Modules
- strings - contains all the text strings of the game as constants
- colors - contains all the colors of the game as constants
- sizes - contains all the sizes, dimensions and coordinates of the game as constants
- backgrounds - contains all the scene's backgrounds names of the game as constants
- items - contains all the items (to be collected) names of the game as constants
- objects - contains all the objects (appear in the scenes) of the game as constants

### Scenes Classes
- Scene - the generic scene which every other scene should inherit
- any other scenes you add to the game

## How to add a scene?
To add a simple scene you need to:
1. add a scene file in the scenes package
2. add a scene class in the scene file which inherit the Scene class
3. add the `__init__` method (pass the `kwargs` parameter to the `super().__init__` method)
4. add to the `__init__` method the `scene_name: str`  and `background_name: str` if you don't want to use the default values

An Example:
```python
from src.consts import strings, backgrounds
from src.scenes import Scene

class SimpleScene(Scene):
    def __init__(self, **kwargs):
        super(SimpleScene, self).__init__(scene_name=strings.SIMPLE_SCENE_NAME,
                                          background_name=backgrounds.SIMPLE_SCENE_BACKGROUND,
                                          **kwargs)
```

Now when you have a simple scene with name and background we want to add objects to the scene.
To do that we can use the `self.add_object(object_name: str,x: int, y: int, width: int, height: int) -> None` method

An Example:
```python
from src.consts import strings, objects, backgrounds
from src.scenes import Scene

class ObjectsScene(Scene):
    def __init__(self, **kwargs):

        super(ObjectsScene, self).__init__(scene_name=strings.OBJECT_SCENE_NAME,
                                           background_name=backgrounds.OBJECT_SCENE_BACKGROUND,
                                           **kwargs)

        self.add_object(objects.FIRST_OBJECT, 400, 200, 200, 200)
        self.add_object(objects.SECOND_OBJECT, 650, 250, 100, 100)
```

To finish it up we need to add some logic to the scene, we can use it by overriding the Scene methods:
- `self.on_item_used_on_object(item_name: str, object_name: str)`
- `self.on_pressed_on_object(object_name: str)`

In these methods you can also call the following methods:
- `self.add_item(item_name: str) -> None` to collect a new item to the items list: 
- `self.self.use_selected_item() -> None` - to remove the selected item from the items list
- `self.set_title(title: str) -> None` - to change the header title
- `self.remove_object(object_name: str) -> None` - to remove an object from the scene

You can also move to another scene if your event handler method returns this scene class type
An Example:
```python
from src.consts import strings, objects, items, backgrounds
from src.scenes import Scene

class LogicScene(Scene):
    def __init__(self, **kwargs):

        super(LogicScene, self).__init__(scene_name=strings.LOGIC_SCENE_NAME,
                                         background_name=backgrounds.LOGIC_SCENE_BACKGROUND,
                                         **kwargs)

        self.add_object(objects.FIRST_OBJECT, 400, 200, 200, 200)
        self.add_object(objects.SECOND_OBJECT, 650, 250, 100, 100)

    def on_item_used_on_object(self, item_name: str, object_name: str) -> type | None:
        if item_name == items.FIRST_ITEM and object_name == objects.FIRST_OBJECT:
            self.use_selected_item()
            from src.scenes import SecondRoom
            return SecondRoom

    def on_pressed_on_object(self, object_name: str) -> None:
        if object_name == objects.FIRST_OBJECT:
            self.set_title('You pressed on the first object')
        elif object_name == objects.SECOND_OBJECT:
            self.remove_object(objects.SECOND_OBJECT)
            self.add_item(items.FIRST_ITEM)
            self.set_title('You collect a first item')
```

Finally, to add your scenes to the game you need to send a set with all the scenes classes type to the start method (and the first scene again separately)
```python
import asyncio

from src.consts import sizes
from src.base import Game
from src.scenes import FirstScene, SecondScene, LastScene


async def main() -> None:
    await Game(sizes.WIDTH, sizes.HEADER_HEIGHT, sizes.BODY_HEIGHT, sizes.FOOTER_HEIGHT, 0, 0,
               {FirstScene, SecondScene, LastScene}, FirstScene).start()


if __name__ == "__main__":
    asyncio.run(main())
```