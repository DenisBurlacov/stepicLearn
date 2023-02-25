for n in range(1):
    for k in range(1, 4):
        for m in range(1, 7):
            if 26 * n + 30 * k + 31 * m == 365:
                print('n = ', n, 'k =', k, 'm =', m)
