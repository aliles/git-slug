from __future__ import absolute_import, division, print_function
import logging
import string
import sys
import time

import begin
import pygit2
import jinja2

from git_slug.version import __version__
from git_slug.wordnet import WordNet
from git_slug import filters


@begin.start
@begin.logging
def main(pretty='oneline', tautogram=False):
    """Generate code name for each commit based on the commit's hash.
    """
    logging.debug("Loading Jinja2 template ... %f", time.time())
    loader = jinja2.PackageLoader('git_slug', 'templates')
    env = jinja2.Environment(loader=loader)
    env.filters['localtime'] = filters.localtime
    env.filters['gmtime'] = filters.gmtime
    env.filters['tsformat'] = filters.tsformat
    template = env.get_template(pretty)
    logging.debug("Loading Git repository ... %f", time.time())
    repo = pygit2.Repository('.git')
    last = repo[repo.head.target]
    logging.debug("Loading Wordnet database ... %f", time.time())
    wordnet = WordNet()
    logging.debug("Walking Git repository ... %f", time.time())
    for commit in repo.walk(last.id, pygit2.GIT_SORT_TOPOLOGICAL):
        wordnet.seed(int(commit.hex, 16))
        if tautogram:
            prefix = wordnet.choice(string.lowercase)
            wordnet.filter_fn = lambda word: word[0] == prefix
        logging.info(template.render(commit=commit, wordnet=wordnet))
        sys.stdout.flush()
