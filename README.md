## Trybe Project 31 - Job Insights


## PROJECT OVERVIEW

  This is project #1 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project analyzes data related to the Jobs market. Project tasks are incorporared in a Web App. Unit tests are also part of the tasks for the application. There is also a bonus task to code a feature for the app. The data was extracted from [Glassdoor](https://www.glassdoor.com.br/) and obtained through [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data). Stack: Python3, Pytest, Flask/Jinja2.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  * tasks 13 are bonus tasks

  *description* | *status*
  --- | :---:
  1 - Implement a function read | :heavy_check_mark:
  2 - Implement a function get_unique_job_types | :heavy_check_mark:
  3 - Implement a function get_unique_industries | :heavy_check_mark:
  4 - Implement a function get_max_salary | :heavy_check_mark:
  5 - Implement a function get_min_salary | :heavy_check_mark:
  6 - Implement a function filter_by_job_type | :heavy_check_mark:
  7 - Implement a function filter_by_industry | :heavy_check_mark:
  8 - Implement a function matches_salary_range | :heavy_check_mark:
  9 - Implement a function filter_by_salary_range | :heavy_check_mark:
  10 - Implement a test to count_ocurrences function | :heavy_check_mark:
  11 - Implement a test to read_brazilian_file function | :heavy_check_mark:
  12 - Implement a test to sort_by function | :heavy_check_mark:
  13.1 - Create a route /job receiving index param | :heavy_check_mark:
  13.2 - Create a view job, receiving index param | :heavy_check_mark:
  13.3 - Implement view job so that it returns status code 200 to valid jobs | :heavy_check_mark:
  13.4 - Implement view job that returns the exact HTML of a job's page | :heavy_check_mark:
</details>

<details>
  <summary><strong>How to Execute the Tests</strong></summary>

  To execute the tests, first check if you have the virtual environment up and running.

  <strong>To Execute All tests:</strong> ```$ python3 -m pytest```

  the file `pyproject.toml` already correctly configures pytest. However, in case you have issues with that and want a complete explicit output, the command is:

  ```bash
  python3 -m pytest -s -vv
  ```

  In case you need to execute just one test file, use the command:

  ```bash
  python3 -m pytest tests/filename.py
  ```

  In case you need to execute just one test function, use the command:

  ```bash
  python3 -m pytest -k test_function_name
  ```

  If you wish that the tests stop from being executed when the first error happens, use the param `-x`

  ```bash
  python3 -m pytest -x tests/filename.py
  ```

  To execute a specific test of a file, type the command:

  ```bash
  python3 -m pytest tests/filename.py::test_function_name
  ```
</details>

## HOW TO RUN THE APP

  1. clone the repository

   - `git clone git@github.com:thiagoguarino/trybe-project31-job-insights.git`
  
  2. enter the project's folder 

   - `cd trybe-project31-job-insights`

  3. create and open the project's virtual environment

  - `python3 -m venv .venv && source .venv/bin/activate`
  
  4. install dependencies

  - `python3 -m pip install -r dev-requirements.txt`

  5. To execute the app

  - `flask run`  
