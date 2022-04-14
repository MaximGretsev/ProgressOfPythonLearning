a: int = 1233
a_: list = [int(item) for item in str(a)]

set_: set = set(a_)

print(len(a_) == len(set_))

