# -*- coding: utf-8 -*-
"""
Created on Mar 6 2021
The primary goal of this file is to demonstrate a simple unittest implementation
for the getGithubData function.

@author: Diaeddin Motan
"""

import unittest

from githubApi567 import getGithubData

class TestGetGithub(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testGetGithubData(self):
        # Github id does not exist
        self.assertEqual(getGithubData('richkempinskiiiiiiiii'), 'richkempinskiiiiiiiii does not exists')
        # Github id exists
        self.assertNotEqual(getGithubData('dmotan'),'dmotan does not exists')

        commits = {
            'AMP-pets': 2,
            'Basic-Portfolio': 3,
            'Bootstrap-Portfolio': 3,
            'burger': 6,
            'deanEnergySolutions': 1,
            'diya2motan.github.io': 2,
            'Flashcard-Generator': 4,
            'fresh-potatoes': 1,
            'getallaround': 1,
            'GifTastic': 4,
            'github-slideshow': 7,
            'GitHubApi567': 4,
            'Hangman-Game': 5,
            'helloWorld': 2,
            'Here-We-Go': 30,
            'HW-Wireframe': 3,
            'hw1': 1,
            'js-clock': 2,
            'js-drumkit': 2,
            'liri-node-app': 4,
            'mongo-scrape-assignment': 2,
            'myrepo': 1,
            'NYTReact': 1,
            'Portfolio': 1,
            'react-passport': 2,
            'Responsive-Portfolio': 2,
            'sequelizedBurger': 2,
            'Student-Repository': 2,
            'swapi': 2,
            'test': 2
        }

        self.assertEqual(getGithubData('dmotan'),commits)

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

