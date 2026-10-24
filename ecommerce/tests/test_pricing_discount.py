import pytest
from ecommerce.pricing import apply_discount

def test_apply_discount_clamps_negative_to_zero():
    """apply_discount should never return a negative price.
    For discounts greater than 100% it should clamp the result to 0.
    """
    result = apply_discount(100.0, 150.0)
    assert result == 0.0, f"Expected discounted price to be 0.0, got {result}"
