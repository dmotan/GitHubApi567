# -*- coding: utf-8 -*-
"""
Created on Mar 6 2021
The primary goal of this file is to demonstrate a simple unittest implementation
for the getGithubData function.

@author: Diaeddin Motan
"""

import unittest
from unittest import mock
from unittest.mock import patch, Mock
from githubApi567 import getGithubData

class TestGetGithub(unittest.TestCase):

    @mock.patch('requests.get')
    def testGetGithubData(self, mockedRequest):
        # Working part
        mockedRequest.return_value.text = '{ "message": "Not Found", "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"}'
        response = getGithubData('richkempinskiiiiiiiii')
        self.assertEqual(response, 'richkempinskiiiiiiiii does not exists')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

