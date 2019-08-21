ALPHABET = list('abcdefghijklmnopqrstuvwxyz')


def coun_alb(c_str: str) -> int:
    """Посчитывает сумму прдложения по системе a-1, b-2, c-3(номер буквы в ахлфавите) и так далее."""
    raw_str = c_str.lower().split()
    raw_str = "".join(raw_str)

    summary = 0
    for l in raw_str:
        summary += (ALPHABET.index(l) if l in ALPHABET else -1) + 1

    return summary


print(coun_alb('NEW YORK STOCK EXCHANGE INCORPORATED'))
