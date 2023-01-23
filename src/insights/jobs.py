from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
        jobs_data = list(reader)
        return jobs_data


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_data = read(path)
    job_types_list = list()

    for job in jobs_data:
        if job["job_type"]:
            job_types_list.append(job["job_type"])

    unique_job_types = set(job_types_list)

    return unique_job_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    filtered_jobs_list = list()

    for job in jobs:
        if job["job_type"] == job_type:
            filtered_jobs_list.append(job)

    return filtered_jobs_list
