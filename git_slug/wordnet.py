#!/usr/bin/env python
from collections import defaultdict
import random

from pkg_resources import Requirement, resource_filename


SYNSET_TYPE = {
    '1': 'noun',
    '2': 'verb',
    '3': 'adj',
    '4': 'adv',
    '5': 'adj',
}

LEX_FNO = {
    '00': None,
    '01': None,
    '02': None,
    '03': None,
    '04': 'noun.act',
    '05': 'noun.animal',
    '06': 'noun.artifact',
    '07': 'noun.attribute',
    '08': 'noun.body',
    '09': 'noun.cognition',
    '10': 'noun.communication',
    '11': 'noun.event',
    '12': 'noun.feeling',
    '13': 'noun.food',
    '14': 'noun.group',
    '15': 'noun.location',
    '16': 'noun.motive',
    '17': 'noun.object',
    '18': 'noun.person',
    '19': 'noun.phenomenon',
    '20': 'noun.plant',
    '21': 'noun.possession',
    '22': 'noun.process',
    '23': 'noun.quantity',
    '24': 'noun.relation',
    '25': 'noun.shape',
    '26': 'noun.state',
    '27': 'noun.substance',
    '28': 'noun.time',
    '29': 'verb.body',
    '30': 'verb.change',
    '31': 'verb.cognition',
    '32': 'verb.communication',
    '33': 'verb.competition',
    '34': 'verb.consumption',
    '35': 'verb.contact',
    '36': 'verb.creation',
    '37': 'verb.emotion',
    '38': 'verb.motion',
    '39': 'verb.perception',
    '40': 'verb.possession',
    '41': 'verb.social',
    '42': 'verb.stative',
    '43': 'verb.weather',
    '44': None,
}


class WordNet(object):

    def __init__(self, seed=None, filter_fn=None):
        self._chooser = random.Random(seed)
        self._filter = filter_fn
        self._wordnet = defaultdict(set)
        self.load_words()

    def __getattr__(self, name):
        return self.get_word(name, filter_fn=self._filter)

    def choice(self, seq):
        """Choose a random element from a non-empty sequence."""
        try:
            i = self._chooser._randbelow(len(seq))
        except ValueError:
            raise IndexError('Cannot choose from an empty sequence')
        return seq[i]

    def get_word(self, category, filter_fn=None):
        category = category.replace('.', '_')
        if '_' + category not in self.__dict__:
            words = tuple(sorted(self._wordnet[category]))
            setattr(self, '_' + category, words)
        else:
            words = getattr(self, '_' + category, None)
        if filter_fn is None:
            return self.choice(words)
        return self.choice(list(filter(filter_fn, words)))

    def load_words(self, location=None):
        if location is None:
            location = resource_filename(Requirement.parse("git-slug"), "git_slug/index.sense")
        with open(location) as data:
            for line in data:
                word, lex_sense = line.split('%', 1)
                ss_type, lex_fno, _, _, _ = lex_sense.split(':')
                if not word.isalpha():
                    continue
                ss_type = SYNSET_TYPE[ss_type]
                self._wordnet[ss_type].add(word)
                lex_fno = LEX_FNO[lex_fno]
                if lex_fno is None:
                    continue
                self._wordnet[lex_fno.replace('.', '_')].add(word)

    def seed(self, state):
        self._chooser.seed(state)
