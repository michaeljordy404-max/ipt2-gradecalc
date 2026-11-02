def compute_final_grade(prelim, midterm, finals):
    """Calculate weighted grade: 30%, 30%, and 40%."""

    for score in (prelim, midterm, finals):
        if not 0 <= score <= 100:
            raise ValueError("Scores must be 0-100")

    return round(
        prelim * 0.3 + midterm * 0.3 + finals * 0.4, 2
    )


def remark(final_grade):
    """Return the academic remark."""

    if final_grade >= 75:
        return "PASSED"

    return "FAILED"
