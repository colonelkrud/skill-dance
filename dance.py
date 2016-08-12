from opsdroid.skills import match_regex
import random

@match_regex(r'.*dance.*')
def dance(opsdroid, message):
    gifs = ["http://i.imgur.com/lnvJm9a.gif",
            "http://i.imgur.com/DyzcWlX.gif",
            "http://i.imgur.com/Cj7pp8k.gif"]
    message.respond(random.choice(gifs))
