# This script tests if ascii project works as intended.
# I chose 'n!' as a test input and tested behavious of
# three important functions of the project.


import sys
from pathlib import Path

# add ascii-art-project-1 dir to PYTHONPATH to enable imports
project_path = Path(__file__).resolve().parent.parent.parent / "ascii-art-project-1"
sys.path.insert(0, str(project_path))

# import required functions to test
from main import create_dict, convert_char_to_ascii, join_chars
import unittest


# define test inputs and outputs as constants
# n! is a test word to convert to ascii
TEST_WORD = "n!"
TEST_ASCII_RAW = [
    "\n",
    "        \n",
    "        \n",
    " _ __   \n",
    "| '_ \\  \n",
    "| | | | \n",
    "|_| |_| \n",
    "        \n",
    "        \n",
    "\n",
    " _  \n",
    "| | \n",
    "| | \n",
    "| | \n",
    "|_| \n",
    "(_) \n",
    "    \n",
    "    \n",
]
JOIN_CHARS_DESIRED_OUTPUT = (
    "         _  \n"
    "        | | \n"
    " _ __   | | \n"
    "| '_ \\  | | \n"
    "| | | | |_| \n"
    "|_| |_| (_) \n"
    "            \n"
    "            "
)
TEST_ASCII_DICT = {
    "n": [
        "        ",
        "        ",
        " _ __   ",
        "| '_ \\  ",
        "| | | | ",
        "|_| |_| ",
        "        ",
        "        ",
    ],
    "!": [" _  ", "| | ", "| | ", "| | ", "|_| ", "(_) ", "    ", "    "],
}
TEST_ASCII_TEXT_LIST = [
    [
        "        ",
        "        ",
        " _ __   ",
        "| '_ \\  ",
        "| | | | ",
        "|_| |_| ",
        "        ",
        "        ",
    ],
    [" _  ", "| | ", "| | ", "| | ", "|_| ", "(_) ", "    ", "    "],
]


class TestFunctions(unittest.TestCase):
    def test_create_dict(self):
        self.assertDictEqual(
            create_dict(ascii_raw=TEST_ASCII_RAW, int_repr=[ord("n"), ord("!")]),
            TEST_ASCII_DICT,
        )

    def test_convert_char_to_ascii(self):
        self.assertEqual(
            convert_char_to_ascii(word=TEST_WORD, ascii_dict=TEST_ASCII_DICT),
            TEST_ASCII_TEXT_LIST,
        )

    def test_join_chars(self):
        self.assertEqual(
            join_chars(ascii_text_list=TEST_ASCII_TEXT_LIST), JOIN_CHARS_DESIRED_OUTPUT
        )
