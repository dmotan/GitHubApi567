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

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

