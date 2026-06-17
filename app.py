import random
import math

import random


def generate_excuse():
    who = ["The dog", "My grandma", "His turtle", "My bird"]
    what = ["ate", "pissed on", "crushed", "broke"]
    when = [
        "before the class",
        "right in time",
        "when I finished",
        "during my lunch",
        "while I was praying",
    ]

    # Selecciona un elemento aleatorio de cada lista
    random_who = random.choice(who)
    random_what = random.choice(what)
    random_when = random.choice(when)

    # Une las partes para formar la oración
    excuse = f"{random_who} {random_what} my homework {random_when}."
    return excuse


# Imprime la excusa generada en la consola
print(generate_excuse())
