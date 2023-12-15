from typing import Callable

from pygame import Surface
from pygame.event import Event

from window import Window, Header, Footer
from window.rooms import Room


class Body(Window):
    rooms: dict[type, Room]
    current_room: type

    def __init__(self, screen: Surface, width: int, height: int, x: int, y, rooms_types: set[type],
                 first_room_type: type, header: Header, footer: Footer):
        super(Body, self).__init__(screen, width, height, x, y)

        self.rooms = {room_type: room_type(self.screen, self.width, self.height, self.x, self.y,
                                           header, footer) for
                      room_type in
                      rooms_types}
        self.current_room = first_room_type

    def render(self) -> None:
        super(Body, self).render()

        self.rooms[self.current_room].render()

    def resize(self, width: int, height: int, x: int, y: int) -> None:
        super(Body, self).resize(width, height, x, y)

        for room in self.rooms.values():
            room.resize(self.width, self.height, self.x, self.y)

    def handle_events(self, events: list[Event]) -> None:
        super(Body, self).handle_events(events)

        next_room = self.rooms[self.current_room].handle_events(events)
        if next_room:
            self.current_room = next_room
