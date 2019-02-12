from functools import reduce


class LapService:

    def __init__(self, laps):
        self._laps = laps

    def _get_drivers_id(self):
        return list(set([lap.driver.id for lap in self._laps]))

    def _get_driver_laps(self, driver_id):
        return [lap for lap in self._laps if lap.driver.id == driver_id]

    def _get_last_driver_laps(self, laps):
        laps.sort(key=lambda lap: lap.number, reverse=True)
        return laps[0]

    def _get_race_duration_of_driver(self, laps):
        durations_of_laps = [lap.duration for lap in laps]
        return reduce((lambda x, y: x + y), durations_of_laps)

    def _get_best_lap(self, laps):
        laps.sort(key=lambda lap: lap.duration)
        return laps[0]

    def get_last_laps_duration(self):
        last_laps = []
        drivers_ids = self._get_drivers_id()
        for id in drivers_ids:
            driver_laps = self._get_driver_laps(id)
            last_laps.append({
                'duration': self._get_race_duration_of_driver(driver_laps),
                'lap': self._get_last_driver_laps(driver_laps)
            })

        last_laps.sort(key=lambda x: x['duration'])
        return last_laps

    def get_best_drivers_lap(self):
        drivers_best_lap = []
        drivers_ids = self._get_drivers_id()
        for id in drivers_ids:
            driver_laps = self._get_driver_laps(id)
            best_lap = self._get_best_lap(driver_laps)
            drivers_best_lap.append(best_lap)

        drivers_best_lap.sort(key=lambda x: x.duration)
        return drivers_best_lap

    def get_best_lap_of_race(self):
        return self._get_best_lap(self._laps)
