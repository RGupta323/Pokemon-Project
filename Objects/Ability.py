from Data.PokeAPI import get_json


class Ability:
    def __init__(self, name, url):
        self.name, self.url = name, url
        self.json = get_json(self.name);
        get_effect = lambda json_input : [entry['short_effect'] for entry in json_input if(entry['language']['name']=='en')][0]
        self.effect = get_effect()