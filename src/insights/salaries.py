from typing import Union, List, Dict
from src.insights.jobs import read


# file authorship: thiago guarino
def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    max_salary_list = list()

    for job in jobs_data:
        if job["max_salary"].isnumeric():
            max_salary_list.append((int(job["max_salary"])))

    max_salary = max(set(max_salary_list))

    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_data = read(path)
    min_salary_list = list()

    for job in jobs_data:
        if job["min_salary"].isnumeric():
            min_salary_list.append((int(job["min_salary"])))

    min_salary = min(set(min_salary_list))

    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists (1)
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers (2)
        If `job["min_salary"]` is greather than `job["max_salary"]` (3)
        If `salary` isn't a valid integer (4)
    """
    try:
        job_min_salary = int(job["min_salary"])
        job_max_salary = int(job["max_salary"])

        if (job_min_salary > job_max_salary):
            raise ValueError

        if int(salary) in range(job_min_salary, (job_max_salary+1)):
            return True

    except (ValueError, TypeError, KeyError):
        # KeyError- trata (1), TypeError- trata (2), (4), ValueError- trata (3)
        raise ValueError
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_on_salary_range_list = list()

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_on_salary_range_list.append(job)
        except ValueError:
            pass

    return jobs_on_salary_range_list
