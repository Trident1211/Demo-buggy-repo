def test_paginate_returns_full_page_items():
    from api.pagination import paginate
    items = list(range(1, 6))  # [1, 2, 3, 4, 5]
    result = paginate(items, page=1, per_page=5)
    # The pagination should return all 5 items; current buggy implementation drops the last one.
    assert len(result["items"]) == 5, f"Expected 5 items, got {len(result['items'])}: {result['items']}"
    assert result["items"] == items, f"Expected full list {items}, got {result['items']}"
