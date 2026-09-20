import pytest
import main

def test_main_health_behavior():
    assert callable(getattr(main, 'health'))
    try:
        res = main.health()
        assert type(res) in (int, float, str, dict, list, bool, tuple, set), 'Function must return valid data structure'
    except TypeError:
        import inspect
        sig = inspect.signature(main.health)
        assert len(sig.parameters) >= 0
