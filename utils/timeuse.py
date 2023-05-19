"""Функция-декоратор для измерения времени работы сортировок массива."""
from time import perf_counter
from typing import Tuple


def timedelta_to_msm(duration: float) -> Tuple[int, int, float]:
    minutes = int(duration // 60)
    seconds = int((duration % 60) // 1)
    milisec = (duration % 1)
    return minutes, seconds, milisec


def time_use(func):
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        execution_time = perf_counter() - start_time
        print(
            f'Время сортировкой {func.__name__}: {execution_time}',
            'Минут: {} секунд: {} доля секунды: {}'.format(
                *timedelta_to_msm(execution_time)
            ),
            sep='\n'
        )
        return result
    return wrapper


if __name__ == '__main__':
    ...
