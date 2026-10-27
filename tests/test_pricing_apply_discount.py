def test_apply_discount_clamps_to_zero():
    from ecommerce.pricing import apply_discount
    result = apply_discount(100, 150)
    assert result == 0, f"Expected discounted price to be 0, got {result}"