from my_game.features.move.speed import Speed
from python_ecs.ecs import System


class FrictionSystem(System):
    def __init__(self, ratio: float):
        super().__init__([Speed])
        self.ratio = ratio

    def update(self, speed: Speed) -> None:
        speed.x *= self.ratio
        speed.y *= self.ratio
