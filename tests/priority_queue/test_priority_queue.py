import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    # Test enqueue with priority
    file1 = {
        "nome_do_arquivo": "arquivo1.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3", "linha4"],
    }
    file2 = {
        "nome_do_arquivo": "arquivo2.txt",
        "qtd_linhas": 7,
        "linhas_do_arquivo": ["linha1",
                              "linha2",
                              "linha3",
                              "linha4", "linha5", "linha6", "linha7"],
    }
    file3 = {
        "nome_do_arquivo": "arquivo3.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": ["linha1", "linha2", "linha3"],
    }

    priority_queue.enqueue(file1)
    priority_queue.enqueue(file2)
    priority_queue.enqueue(file3)

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(7)

    assert len(priority_queue) == 3
    assert priority_queue.dequeue() == file3
    assert priority_queue.dequeue() == file1
    assert priority_queue.dequeue() == file2
