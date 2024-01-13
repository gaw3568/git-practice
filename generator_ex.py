def gen():
    print('gen start')
    yield 1
    print("a")
    yield 2
    print("b")
    yield 3
    return 'done'

g = gen()

print(g)

try:
    for _ in range(5):
        print(f"출력 : {next(g)}")
except StopIteration as e :
    print(e.value)