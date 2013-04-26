#!/usr/bin/env python
# Git clone all my gists

import json
import urllib
from subprocess import call
from urllib import urlopen
import os
USER = os.environ['USER']

def download_gists(page):
    u = urlopen('https://api.github.com/users/' + USER + '/gists?page=' + page + '&per_page=100')
    gists = json.load(u)

    for gist in gists:
        call(['git', 'clone', gist['git_pull_url']])

download_gists('1')
download_gists('2')
download_gists('3')
download_gists('4')
download_gists('5')
download_gists('6')
download_gists('7')
download_gists('8')
download_gists('9')
download_gists('10')
