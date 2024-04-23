"""Test my garden functions."""

__author__ = "730404642"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_edge() -> None:
    """Test add_by_kind with an empty dictionary."""
    garden = {}
    add_by_kind(garden, "flower", "rose")
    assert "flower" in garden, "Edge Case Test Failed."
    assert "rose" in garden["flower"], "Edge Case Test Failed."


def test_add_by_kind_use() -> None:
    """Test add_by_kind with existing category."""
    garden = {"flower": ["daisy"]}
    add_by_kind(garden, "flower", "tulip")
    assert "tulip" in garden["flower"], "Use Case Test Failed."


def test_add_by_date_edge() -> None:
    """Test add_by_date with a new date not in the dictionary."""
    garden = {"April": ["daisy"]}
    add_by_date(garden, "May", "sunflower")
    assert "May" in garden, "Edge Case Test Failed."
    assert "sunflower" in garden["May"], "Edge Case Test Failed."


def test_add_by_date_use() -> None:
    """Test add_by_date with existing date."""
    garden = {"June": ["rose"]}
    add_by_date(garden, "June", "lily")
    assert "lily" in garden["June"], "Use Case Test Failed."


def test_lookup_by_kind_and_date_edge() -> None:
    """Test lookup_by_kind_and_date for a month with no plants."""
    by_kind = {"flower": ["tulip", "rose"]}
    by_date = {"July": ["tulip"]}
    result = lookup_by_kind_and_date(by_kind, by_date, "flower", "August")
    assert result == "No flowers to plant in August.", "Edge Case Test Failed."


def test_lookup_by_kind_and_date_use() -> None:
    """Test lookup_by_kind_and_date for a month with plants."""
    by_kind = {"flower": ["daisy", "rose"]}
    by_date = {"April": ["daisy"]}
    result = lookup_by_kind_and_date(by_kind, by_date, "flower", "April")
    assert result == "Flowers to plant in April: ['daisy']", "Use Case Test Failed."