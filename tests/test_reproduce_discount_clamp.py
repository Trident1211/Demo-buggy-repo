import pytest

from ecommerce.pricing import apply_discount

def test_apply_discount_clamps_to_zero_for_excessive_discount():
    """apply_discount should never return a negative price.
    For discounts greater than 100% it should clamp the result to 0.
    The current buggy implementation returns a negative value.
    """
    result = apply_discount(100.0, 150.0)
    assert result == 0.0, f"Expected discounted price to be clamped at 0.0, got {result}"
