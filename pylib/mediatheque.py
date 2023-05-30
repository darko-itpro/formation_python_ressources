

class MediaValueError(ValueError):
    pass

class TvShow:
    def __init__(self, name: str):
        self.name = name.title()
        self._episodes = []

    def add_episode(self, title: str, number: int, season_number: int, year: int, duration: int):
        new_episode = Episode(title, number, season_number, year, duration)
        if new_episode in self._episodes:
            raise MediaValueError(f"Episode s{season_number}e{number} exists")

        self._episodes.append(new_episode)

    def get_episodes(self, season=None):
        if season is None:
            return self._episodes.copy()
        else:
            return [episode
                    for episode in self._episodes
                    if episode.season_number == season]

    def __str__(self):
        return f"Tv Show {self.name}, ({len(self.episodes)} episodes)"

class Episode:
    def __init__(self, title: str, number: int, season_number: int, year: int, duration: int):
        self.title = title
        self.number = int(number)
        self.season_number = int(season_number)
        self.duration = int(duration)
        self.year = int(year)

    def __str__(self):
        return f"Episode {self.title} s{self.season_number}e{self.number}"

    def __repr__(self):
        return f"Episode({self.title}, {self.number}, {self.season_number})"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (self.number, self.season_number) == (other.number, other.season_number)

class Playlist:
    """
    Classe permétant la gestion d'une playlist. Les épisodes peuvent être redondants.
    """
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def add_episode(self, episode:Episode):
        self.episodes.append(episode)
