# py-imports-demo
this was created only for demonstration purposes related to https://github.com/CYB3RMX/Qu1cksc0pe/pull/58

when you run `main.py`, you should get:
```
C:\SOMEPATH\py-imports-demo>python main.py
Running main.py
Running target.py, with __name__: mod.target
```

when running `target.py` directly:
```
C:\SOMEPATH\py-imports-demo>cd mod
C:\SOMEPATH\py-imports-demo\mod>python target.py
Running target.py, with __name__: __main__
Traceback (most recent call last):
  File "C:\SOMEPATH\py-imports-demo\mod\target.py", line 3, in <module>
    from .utils import stub
ImportError: attempted relative import with no known parent package
```

importing the utility module as `.utils` when running with `__name__` `mod.target` works, because python knows we are inside the `mod` package, therefore `.utils` must refer to the local `mod.utils` module.
However, as you can see, when running the target module directly, you'll get an error.
This is caused by the fact that when running this way, Python isn't aware it's running in a package at all (as evidenced by the value of `__name__`).
That arguably makes sense to some degree, but has quite annoying implications. AFAIK, there is no way to craft location-agnostic imports (without multiple attempts and catching `ImportError`s along the way) OR stooping to `sys.path` hacks. https://stackoverflow.com/questions/16981921/relative-imports-in-python-3.

this also works, but you probably wouldn't want to force invocations to adhere to this scheme:
```
C:\SOMEPATH\py-imports-demo>python -m mod.target
Running target.py, with __name__: __main__
```
