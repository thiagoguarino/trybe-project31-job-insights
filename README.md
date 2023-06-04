## Project 31 - Job Insights


## PROJECT OVERVIEW

  This is project #1 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project analyzes data related to the Jobs market. Project tasks are incorporared in a Web App. Unit tests are also part of the tasks for the application. There is also a bonus task to code a feature for the app.

  The data was extracted from [Glassdoor](https://www.glassdoor.com.br/) and obtained through [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data).

  Stack: Python3, Flask/Jinja2, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  *Nome* | *Avaliação*
  --- | :---:
  1 - Implemente a função read | :heavy_check_mark:
  2 - Implemente a função get_unique_job_types | :heavy_check_mark:
  3 - Implemente a função get_unique_industries | :heavy_check_mark:
  4 - Implemente a função get_max_salary | :heavy_check_mark:
  5 - Implemente a função get_min_salary | :heavy_check_mark:
  6 - Implemente a função filter_by_job_type | :heavy_check_mark:
  7 - Implemente a função filter_by_industry | :heavy_check_mark:
  8 - Implemente a função matches_salary_range | :heavy_check_mark:
  9 - Implemente a função filter_by_salary_range | :heavy_check_mark:
  10 - Implemente um teste para a função count_ocurrences | :heavy_check_mark:
  11 - Implemente um teste para a função read_brazilian_file | :heavy_check_mark:
  12 - Implemente um teste para a função sort_by | :heavy_check_mark:
  13.1 - Crie a rota /job recebendo o parâmetro index | :heavy_check_mark:
  13.2 - Crie a view job, recebendo o parâmetro index | :heavy_check_mark:
  13.3 - Implemente view job para que ela retorne status code 200 para jobs válidos | :heavy_check_mark:
  13.4 - Implemente view job de forma a retornar o HTML exato de uma página de job | :heavy_check_mark:
</details>

<details>
  <summary><strong>How to execute the Tests</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
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
