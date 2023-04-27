'''Реализация алгоритма проверки возможности составить строку random_note
из символов строки letters.'''


def can_construct(random_note: str, letters: str) -> bool:
    for letter in set(random_note):
        if (
            letter not in letters
            or random_note.count(letter) > letters.count(letter)
        ):
            return False
    return True


if __name__ == '__main__':
    assert can_construct('abba', 'aabbbbccc')
    assert not can_construct('Hello world!', 'aabbbbccc!')
    assert can_construct('Hello world!', 'o!o!odedHeHlll d b!rb erere w')
    assert can_construct('', '')
    assert can_construct('', 'adv')
    assert not can_construct('quant', '')
