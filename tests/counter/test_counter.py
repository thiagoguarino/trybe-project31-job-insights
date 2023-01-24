from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "python"
    word_count = count_ocurrences(path, word)
    assert word_count == 1639
