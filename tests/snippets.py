#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

from chibi_alchemist.snippets import split_elements


class Test_split_elements( unittest.TestCase ):
    def test_should_work( self ):
        split_elements( 'LiBr' )

    def test_should_return_two_elements( self ):
        result = split_elements( 'LiBr' )
        self.assertEqual( len( result ), 2 )

    def test_should_be_a_list( self ):
        result = split_elements( 'LiBr' )
        self.assertIsInstance( result, list )

    def test_should_be_Li_and_Br( self ):
        result = split_elements( 'LiBr' )
        expected = [ 'Li', 'Br' ]
        self.assertEqual( result, expected )

    def test_should_work_with_subfix_amounts( self ):
        result = split_elements( 'SnS3' )
        expected = [ 'Sn', 'S3' ]
        self.assertEqual( result, expected )

    def test_should_work_with_prefix_amounts( self ):
        result = split_elements( 'Sn3S' )
        expected = [ 'Sn3', 'S' ]
        self.assertEqual( result, expected )

    def test_should_work_with_both_amounts( self ):
        result = split_elements( 'Sn3S3' )
        expected = [ 'Sn3', 'S3' ]
        self.assertEqual( result, expected )
