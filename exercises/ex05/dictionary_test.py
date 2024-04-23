"""EX06 - Unit Tests on Dictionary."""
 
__author__ = "730404642"

import pytest
from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_normal_case():
    """Tests the expected normal case."""
    assert invert({'a': '1', 'b': '2', 'c': '3'}) == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_normal_case_empty():
    """Tests the expected normal case if the input is empty."""
    assert invert({}) == {}


def test_invert_duplicate_keys():
    """Tests the edge case where there are duplicate keys."""
    assert invert({'a': '1', 'b': '1', 'c': '2'}) != {'1': 'a', '2': 'c'}


def test_favorite_color_normal_case():
    """Tests favorite color where blue is the most common."""
    colors = {'person1': 'blue', 'person2': 'red', 'person3': 'blue', 'person4': 'green'}
    assert favorite_color(colors) == 'blue'


def test_favorite_color_all_equal():
    """Tests favorite color where there are all equal occurances."""
    colors = {'person1': 'blue', 'person2': 'red', 'person3': 'green', 'person4': 'yellow'}
    assert favorite_color(colors) == 'blue'


def test_favorite_color_empty():
    """Tests favorite color where the input is empty."""
    colors = {}
    with pytest.raises(ValueError):
        favorite_color(colors)


def test_count_multiple():
    """Tests count with multiple entries and even some duplicates."""
    elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
    expected = {'apple': 2, 'banana': 3, 'orange': 1}
    assert count(elements) == expected


def test_count_unique():
    """Tests count where all entries are unique."""
    elements = ['apple', 'banana', 'orange']
    expected = {'apple': 1, 'banana': 1, 'orange': 1}
    assert count(elements) == expected


def test_count_empty_list():
    """Tests count when list is empty."""
    elements = []
    expected = {}
    assert count(elements) == expected


def test_alphabetizer_cases():
    """Tests alphabetizer with a list containing lowercase and uppercase."""
    input_list = ['Apple', 'banana', 'Apricot', 'blueberry', 'almond']
    expected_output = {'a': ['Apple', 'Apricot', 'almond'], 'b': ['banana', 'blueberry']}
    assert alphabetizer(input_list) == expected_output


def test_alphabetizer_empty():
    """Test alphabetizer with empty list."""
    assert alphabetizer([]) == {}


def test_alphabetizer_spec_chars():
    """Test alphabetizer with special chars."""
    input_list = ['Apple', '2bananas', '#hashtag', '100days']
    expected_output = {'a': ['Apple'], '2': ['2bananas'], '#': ['#hashtag'], '1': ['100days']}
    assert alphabetizer(input_list) == expected_output


def test_update_attendance_new():
    """Test update_attendance by adding a student to a new day."""
    attendance = {}
    update_attendance(attendance, 'Monday', 'Alice')
    assert attendance == {'Monday': ['Alice']}


def test_update_attendance_exists():
    """Test update_attendance by adding a student to a day that already inputted."""
    attendance = {'Monday': ['Alice']}
    update_attendance(attendance, 'Monday', 'Bob')
    assert attendance == {'Monday': ['Alice', 'Bob']}


def test_update_attendance_duplicates():
    """Test update_attendance duplicates are not added on the same day."""
    attendance = {'Monday': ['Alice']}
    update_attendance(attendance, 'Monday', 'Alice')
    assert attendance == {'Monday': ['Alice']}