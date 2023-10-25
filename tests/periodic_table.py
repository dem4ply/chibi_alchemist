#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from chibi_alchemist.periodic_table import load_all_elements, Element


class Test_periodic_table(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_all_elements_should_work(self):
        elements = load_all_elements()
        for e in elements:
            self.assertIsInstance( e, Element )

    def test_elements_has_info( self ):
        elements = load_all_elements()
        for e in elements:
            self.assertTrue( e.name )
            self.assertTrue( e.symbol )

    def test_elements_neutrons_are_correct( self ):
        elements = load_all_elements()
        by_symbol = { e.symbol: e for e in elements }

        self.assertEqual( by_symbol[ 'Na' ].neutrons, 12 )
        self.assertEqual( by_symbol[ 'Ca' ].neutrons, 20 )
        self.assertEqual( by_symbol[ 'Sn' ].neutrons, 69 )
        self.assertEqual( by_symbol[ 'Fr' ].neutrons, 136 )
        self.assertEqual( by_symbol[ 'Fe' ].neutrons, 30 )
