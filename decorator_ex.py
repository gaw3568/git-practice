# 데코레이터 실습
import time


def performance_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st

        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)

        print(f"{et:.5f} {name}({arg_str}) -> {result}")
        return result

    return perf_clocked()


def time_func(seconds):
    time.sleep(seconds)


def sum_func(*numbers):
    return sum(numbers)


none_deco1 = performance_clock(time_func)
none_deco2 = performance_clock(time_func)

