from src.pre_built.sorting import sort_by


# file authorship: thiago guarino
def test_sort_by_criteria():
    mocked_jobs = [
        {"date_posted": "2022-01-12", "min_salary": 4000, "max_salary": 8000},
        {"date_posted": "2022-03-13", "min_salary": 2000, "max_salary": 6000},
        {"date_posted": "2022-05-16", "min_salary": 9000, "max_salary": 9500},
    ]

    criteria = ["date_posted", "min_salary", "max_salary"]

    # 0) criteria date_posted, 1) criteria min_salary, 2) criteria max_salary
    expected = [
        [mocked_jobs[2], mocked_jobs[1], mocked_jobs[0]],  # (0)
        [mocked_jobs[1], mocked_jobs[0], mocked_jobs[2]],  # (1)
        [mocked_jobs[2], mocked_jobs[0], mocked_jobs[1]],  # (2)
    ]

    sort_by(mocked_jobs, criteria[1])

    assert mocked_jobs == expected[1]
