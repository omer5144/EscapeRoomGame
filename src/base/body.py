from pygame import Surface
from pygame.event import Event

from src.base import Window, Header, Footer
from src.scenes import Scene


class Body(Window):
    scenes: dict[type, Scene]
    current_scene: type

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, scenes_types: set[type],
                 first_scene_type: type, header: Header, footer: Footer):
        super(Body, self).__init__(screen, width, height, x, y)

        self.scenes = {scene_type: scene_type(self.screen, self.width, self.height, self.x, self.y,
                                              header, footer) for
                       scene_type in
                       scenes_types}
        self.current_scene = first_scene_type

    def render(self) -> None:
        super(Body, self).render()

        self.scenes[self.current_scene].render()

    def handle_events(self, events: list[Event]) -> None:
        super(Body, self).handle_events(events)

        next_scene = self.scenes[self.current_scene].handle_events(events)
        if next_scene:
            self.current_scene = next_scene
