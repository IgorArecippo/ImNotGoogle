from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(instance.search(item)["nome_do_arquivo"] == path_file
           for item in range(len(instance))):
        return None

    file = txt_importer(path_file)
    info = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }
    instance.enqueue(info)
    print(info)
    return info


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
        return

    path_file = instance.dequeue()["nome_do_arquivo"]
    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
