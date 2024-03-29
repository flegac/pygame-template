from my_game.features.move.position import Position
from my_game.features.move.speed import Speed
from python_ecs.ecs import System


class MoveSystem(System):
    def __init__(self):
        super().__init__([Position, Speed])

    def update(self, position: Position, speed: Speed) -> None:
        position.x += speed.x
        position.y += speed.y
