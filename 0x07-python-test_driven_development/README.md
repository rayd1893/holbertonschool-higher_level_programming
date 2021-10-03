# 🖥️ Tests in Python
## Task 0: Integers addition
**0-main.py:**

```Python
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
	print(add_integer(4, "School"))
except Exception as e:
        print(e)
try:
	print(add_integer(None))
except Exception as e:
        print(e)
```

__Execute:__

```sh
./0-main.py

python3 -m doctest -v ./tests/0-add_integer.txt

python3 -c 'print(__import__("0-add_integer").__doc__)'

python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
```