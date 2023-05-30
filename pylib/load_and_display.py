import pylib.utils.filetools as fu  # Module de la fonction chargeant les informations de séries.
import pylib.mediatheque as media  # Module contenant les objets liés à la gestion des médias
from pylib.utils import cli
from pathlib import Path
import os.path


def load_data_from_file(path:str, shows:dict=None) -> dict[str, media.TvShow]:
    """
    Charge les informations d'une série à partir de sources de données et retourne un dictionnaire de séries

    :param path: Chemin vers la source de données, peut être un fichier (csv) ou un répertoire contenant des fichiers selon le pattern attendu.
    :param shows: Dictionnaire de séries à compléter. La valeur par défaut est à None car mutable.
    :return: Un dictionnaire [str:TvShow] de séries où la clef est le titre de la série.
    """
    if not os.path.isfile(path):
        raise ValueError(f"Path not to file : {path}")

    my_episodes = fu.load_from_csv(path)

    shows = shows.copy() if shows else {} # La copie permet de respecter l'idiome enseigné.

    for show_name, season, number, title, duration, year in my_episodes:  # *other premt de récupérer d'autres données
        if show_name not in shows:
            shows[show_name] = media.TvShow(show_name)

        show = shows[show_name]

        try:
            show.add_episode(title, number, season, year, duration)
        except ValueError:
            print(f"Episode {title} for {show_name} exists")

    return shows


if __name__ == "__main__":
    # La ligne suivante utilse la variable `__file__`pour déterminer le chemin
    # du module afin de construire le chemin vers le fichier csv.
    file_path = Path(__file__).parent.parent / "assets" / "showslist.csv"
    #print(file_path)

    shows = load_data_from_file(file_path)
    cli.display_shows(shows)