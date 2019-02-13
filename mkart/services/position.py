from mkart.models.position import Position


class PositionService:

    def __init__(self, last_laps):
        self._last_laps = last_laps

    def _get_delay_after_winner(self, winner, loser):
        if winner.finished_laps != loser.finished_laps:
            return (winner.duration + loser.duration) - winner.duration

        return loser.duration - winner.duration

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

    def get_time_drivers_after_winner(self):
        positions = []
        drivers_positions = self.get_positions()
        winer_position = drivers_positions[0]
        drivers_positions.pop(0)
        for position in drivers_positions:
            position.delay_after_winner = self._get_delay_after_winner(winer_position, position)  # noqa
            positions.append(position)

        return positions
