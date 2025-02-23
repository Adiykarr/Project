import pytest
from area import calculate_area_square  

def test_calculate_area_square_valid():
    assert calculate_area_square(5) == 25

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)