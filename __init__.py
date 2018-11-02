from opsdroid.matchers import match_regex
import random

@match_regex(r'\bdance\b', case_sensitive=False)
async def dance(opsdroid, config, message):
    gifs = ["http://i.imgur.com/lnvJm9a.gif",
            "http://i.imgur.com/DyzcWlX.gif",
            "http://i.imgur.com/Cj7pp8k.gif"]
    await message.respond(random.choice(gifs))
