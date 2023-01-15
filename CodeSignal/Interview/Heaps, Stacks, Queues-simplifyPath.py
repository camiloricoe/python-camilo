def solution(a):
    st = ['/']
    a = a.split("/")
    for i in a:
        if i == '..':
            if len(st) > 1:
                st.pop()
            else:
                continue
        elif i == '.':
            continue
        elif i != '':
            st.append("/" + str(i))
    if len(st) == 1:
        return "/"

    return "".join(st[1:])
