from mkart.models.position import Position


class PositionService:

    def __init__(self, last_laps):
        self._last_laps = last_laps

    def get_positions(self):
        position_number = 1
        positions = []

        last_laps = self._last_laps

        for last_lap in last_laps:
            duration = last_lap['duration']
            lap = last_lap['lap']

            position = Position(
                position_number,
                lap.driver,
                lap.number,
                duration
            )
            positions.append(position)
            position_number += 1

        return positions
