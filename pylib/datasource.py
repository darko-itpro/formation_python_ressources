"""
Ce module est une source de données pour les différents exercices.

Ces données sont hétéroclytes, évidemment, dans un "vrai" projet, elles seraient organisées par
arborescence fonctionnelle.
"""

import random
random.seed()

def load_students_list():
    return ["Paul", "Michel", "Ducobu", "Marie", "Paddle", "Carmen", "Marysa"]

def load_grades(course:str):
    if course == "math":
        return [12, 15, 8, 17, 15, 6, 9]
    elif course == "english":
        return [9, 14, 17, 15, 8, 12, 13]
    else:
        raise ValueError("No course found")

def load_season(user=None) -> list:
    """
    Fonction permettant d'accéder à la saison d'une série. Sans paramètre (ou avec `None`, retourne
    la liste des titres de la saison. Avec, retourne une liste d'épisodes sous forme de
    n-uplet.

    Le nombre d'épisodes vus/non vus est aléatoire. Lors de la génération de la liste, chaque
    épisode a 80 % de chances d'être vu. Dès qu'un épisode n'a pas été vu, les suivants sont tous
    non-vus. Un épisode non vu a 60 % de chances de ne pas avoir la clef `viewed`.

    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par un
    n-uplet contenant les éléments `title`, `duration` et `viewed`. Si l'épisode n'a pas été vu,
    cette dernière peut être absente.
    """
    from pathlib import Path
    file_path = Path(__file__).resolve().parent.parent / "assets" / "bbts12.csv"

    with open(file_path) as bbt_file:
        bbt_file.readline()

        if user is None:
            return [_process_line(line)[3] for line in bbt_file]
        else:
            episodes = [_for_user(*_process_line(line)) for line in bbt_file]
            _randomize_viewed(episodes)

            return episodes


def _randomize_viewed(season: list) -> None:
    """
    Ajoute de manière aléatoire une clef `viewed` à une liste d'épisodes.

    Un épisode a 80% de chance d'être vu. Dès qu'un épisode n'est pas vu, les suivants sont
    également non-vus. Un épisode non-vu a 60% de chances de ne pas avoir la clef `viewed`.

    :param season: Une liste de dictionnaires
    """
    is_viewed = True


    for index, episode in enumerate(season):
        if random.random() > 0.8:
            is_viewed = False

        if is_viewed:
            episode = (*episode, True)
        else:
            if random.random() > 0.6:
                episode= (*episode, False)

        season[index] = episode

def _process_line(episode_line: str):
    """
    Extrait et transtype les données à partir d'une ligne type csv.

    :param episode_line: Une ligne type csv
    :return: Un N-uplet (nom saison, saison, numéro d'épisode, titre d'épisode, durée, année)
    """
    show, season, episode, title, duration, year = episode_line.rstrip().split(';')
    return show, int(season), int(episode), title, int(duration), int(year)


def _for_user(show, season, episode, title, duration, year):
    episode = (title, duration)
    return episode