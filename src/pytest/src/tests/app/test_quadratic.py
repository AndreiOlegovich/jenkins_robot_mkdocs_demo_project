# test_quadratic.py

import pytest
from dev.app.quadratic import quadratic_solve, TYPE_ERROR_TEXT

class TestQuadratic:
    def test_raises_type_error(self):
        with pytest.raises(TypeError) as exc_info:
            quadratic_solve(1, "", 2)
        assert str(exc_info.value) == TYPE_ERROR_TEXT

    def test_result_is_tuple(self):
        res = quadratic_solve(0, 0, 0)
        assert isinstance(res, tuple)

    # Параметризация
    # @pytest.mark.parametrize("args, expected_result",[
    #     ((1, -3, -4), (4, -1)),
    #     ((0, 0, 0), (None, None))
    # ])
    @pytest.mark.parametrize("args, expected_result",[
        pytest.param((1, -3, -4), (4, -1),
                     id="two roots",
                     ),
        pytest.param((1, -2, 1), (1.0, None),
                     id="single root",
                     ),
        pytest.param((0, 0, 0), (None, None),
                     id="no roots",)
    ])
    def test_solution(self, args, expected_result):
        res = quadratic_solve(*args)
        assert res == expected_result
