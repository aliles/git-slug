from __future__ import absolute_import, division, print_function
import logging
import sys
import time

import begin
import pygit2

from git_slug.version import __version__
from git_slug.wordnet import WordNet


@begin.start
@begin.logging
def main(pretty='{c.hex} {w.verb} {w.noun}'):
    """Generate code name for each commit based on the commit's hash.
    """
    logging.debug("Loading Git repository ... %f", time.time())
    repo = pygit2.Repository('.git')
    last = repo[repo.head.target]
    logging.debug("Loading Wordnet database ... %f", time.time())
    wordnet = WordNet()
    logging.debug("Walking Git repository ... %f", time.time())
    for commit in repo.walk(last.id, pygit2.GIT_SORT_TOPOLOGICAL):
        wordnet.seed(int(commit.hex, 16))
        logging.info(pretty.format(c=commit, w=wordnet))
        sys.stdout.flush()
