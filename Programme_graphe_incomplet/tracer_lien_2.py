def petit_cout(liste,N):
    cout = []
    for i in liste:
        cout.append(i[1])
    petit = min(cout)
    petit_cout = cout.index(petit)
    return petit_cout
