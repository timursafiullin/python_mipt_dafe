from subprocess import check_output, DEVNULL, CalledProcessError
from os import remove

# test from Preview
with open("test2_p.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity=2)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
"""
    )
output = check_output(["python", "./test2_p.py"]).decode().replace("\r", "")
remove("./test2_p.py")
assert (
    output
    == """call func for name: Mr.White
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
Hello, Mr.White!
call func for name: Saul Goodman
Hello, Saul Goodman!
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
"""
), "Preview test did not pass"
print("Preview test passed")

# test 1 (capacity = 1)
with open("test2_1.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity=1)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
"""
    )
output = check_output(["python", "./test2_1.py"]).decode().replace("\r", "")
remove("./test2_1.py")
assert (
    output
    == """call func for name: Mr.White
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
call func for name: Mr.White
Hello, Mr.White!
call func for name: Saul Goodman
Hello, Saul Goodman!
call func for name: Mr.White
Hello, Mr.White!
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
"""
), "Capacity=1 test did not pass"
print("1 test passed")

# test 2 (capacity = 5, normal algorithm)
with open("test2_2.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity=5)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mike"))
print(get_greeting("Mike"))
print(get_greeting("Alex"))
print(get_greeting("Mama"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mama"))
print(get_greeting("Mr.White"))
print(get_greeting("Mr.White"))
print(get_greeting("Papa"))
print(get_greeting("Mike"))
"""
    )
output = check_output(["python", "./test2_2.py"]).decode().replace("\r", "")
remove("./test2_2.py")
assert (
    output
    == """call func for name: Mr.White
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
Hello, Mike!
Hello, Mike!
call func for name: Alex
Hello, Alex!
call func for name: Mama
Hello, Mama!
Hello, Mr.White!
call func for name: Saul Goodman
Hello, Saul Goodman!
Hello, Mama!
Hello, Mr.White!
Hello, Mr.White!
call func for name: Papa
Hello, Papa!
call func for name: Mike
Hello, Mike!
"""
), "Normal algorithm test did not pass"
print("2 test passed")

# test 3 (check if capacity < 1 returns error)
with open("test2_3.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity=0)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
"""
    )
try:
    output = (
        check_output(["python", "./test2_3.py"], stderr=DEVNULL)
        .decode()
        .replace("\r", "")
    )
    raise AssertionError("capacity<1 test did not pass")
except CalledProcessError:
    pass
remove("./test2_3.py")
print("3 test passed")

# test 4 (check if capacity is not Real returns error)
with open("test2_4.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity="asd")
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
"""
    )
try:
    output = (
        check_output(["python", "./test2_4.py"], stderr=DEVNULL)
        .decode()
        .replace("\r", "")
    )
    raise AssertionError("capacity<1 test did not pass")
except CalledProcessError:
    pass
remove("./test2_4.py")
print("4 test passed")

# test 5 (check if capacity rounds)
with open("test2_5.py", "w") as f:
    f.write(
        """
from cache import lru_cache
@lru_cache(capacity=2.4)
def get_greeting(name: str) -> str:
    greeting = f"Hello, {name}!"
    print(f"call func for name: {name}")
    return greeting
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
print(get_greeting("Mr.White"))
print(get_greeting("Saul Goodman"))
print(get_greeting("Mr.White"))
print(get_greeting("Mike"))
"""
    )
output = check_output(["python", "./test2_5.py"]).decode().replace("\r", "")
remove("./test2_5.py")
assert (
    output
    == """call func for name: Mr.White
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
Hello, Mr.White!
call func for name: Saul Goodman
Hello, Saul Goodman!
Hello, Mr.White!
call func for name: Mike
Hello, Mike!
"""
), "capacity round test did not pass"
print("5 test passed")
