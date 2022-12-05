def solution(scriptByExtension):
    return sorted([[key, value] for (value, key) in scriptByExtension.items()])
