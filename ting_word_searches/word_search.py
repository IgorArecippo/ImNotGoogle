def exists_word(word, instance):
    result = []

    for file_data in instance.queue:
        file_name = file_data["nome_do_arquivo"]
        lines = file_data["linhas_do_arquivo"]

        occurrences = []
        for i, line in enumerate(lines, start=1):
            if word.lower() in line.lower():
                occurrences.append({"linha": i, "conteudo": line})

        if occurrences:
            result.append({
                "palavra": word,
                "arquivo": file_name,
                "ocorrencias": occurrences
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
