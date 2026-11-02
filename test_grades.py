import pytest
from grades import compute_final_grade, remark


# Test 1: Normal grade calculation
def test_normal_grade():
    assert compute_final_grade(80, 85, 90) == 85.5


# Test 2: Perfect scores
def test_perfect_grade():
    assert compute_final_grade(100, 100, 100) == 100


# Test 3: Zero scores
def test_zero_grade():
    assert compute_final_grade(0, 0, 0) == 0


# Test 4: Grade below passing
def test_boundary_74_99():
    assert remark(74.99) == "FAILED"


# Test 5: Exact passing grade
def test_boundary_75():
    assert remark(75) == "PASSED"


# Test 6: Failed remark
def test_remark_failed():
    assert remark(60) == "FAILED"


# Test 7: Passed remark
def test_remark_passed():
    assert remark(90) == "PASSED"


# Test 8: Invalid scores
@pytest.mark.parametrize("score", [-1, 101])
def test_invalid_scores(score):
    with pytest.raises(ValueError):
        compute_final_grade(score, 80, 90)
