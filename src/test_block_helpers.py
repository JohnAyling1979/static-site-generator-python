import unittest

from block_helpers import block_to_block_type
from block_type import BlockType

class TestBlockHelpers(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("This is a paragraph"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("##This is a heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```This is a code block"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- This is a list"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. This is an ordered list"), BlockType.ORDERED_LIST)