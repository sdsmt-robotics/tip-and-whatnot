We can easily create a package by tossing an empty `__init__.py` into a child directory. You cannot import things from parent directories without appending them to your path with `sys.path.append('..')`.

If we have the following structure

```
module/
    __init__.py
    thing.py
script.py
```

We can import `thing.py` in `script.py` with `from module import thing`.

If we want the contents of `thing.py` visible under the name `module`, we add `from .thing import *` to `module/__init__.py`. This works because `module/__init__.py` is ran whenever we use some form of `import module` in our code. You can also add more things to `__init__.py` files if you need to.

---

We can also easily create submodules within modules too. That's what the files in this repository illustrate.

We have the following file structure:

```
module/
    constants/
        __init__.py
        defines.py
        flags.py
        pins.py
    __init__.py
    internal_script.py
external_script.py
```

Let's start with the `constants/` submodule and build upwards.

The `constants/__init__.py` file tells the Python interpreter that `constants` is a submodule of `module` (itself defined as a module because of `module/__init__.py`).

The three files in `constants/` define bunch of information about our robot. They're split into different files to make it easier to find and change if we need to, but we don't want people who use the `constants` submodule to know about that, so we import their contents in `constants/__init__.py` with relative imports i.e. `from .flags import *`. This lifts the contents of `constants/flags.py` up to the `constants` submodule, effectively flattening it.

At the next level we have scripts inside the `module` module. We can use relative imports to import things in children directories, but not parent directories. I.e. `from . import constants`.

We want the functions and/or constants inside `internal_script.py` to be visible under `module`, so we add `from .internal_script import *` to `module/__init__.py`.

We also want `constants` visible under `module` as `module.constants`, so we add `from . import constants` to `module/__init__.py`.

---

Finally, at the highest level, from outside `module/` we can access all the things just like we normally would.

We can use any of the following

```python
import module
print(module.constants.LED_LEFT)
print(module.constants.flags.LED_LEFT)
module.internal()

from module import constants, internal
print(constants.LED_LEFT)
print(constants.flags.LED_LEFT)
internal()

from module import constants.flags as flags
print(flags.LED_LEFT)

from module.constants import LED_LEFT
# Or: from modules.constants.flags import LED_LEFT
print(LED_LEFT)

import module.constants as constants
import module.internal as internal
print(constants.LED_LEFT)
print(constants.flags.LED_LEFT)
internal()
```

---

Of course, changing the structure of out `__init__.py` files will change how we can use our module/submodules in top-level scripts. For example, if we only had `from . import flags, pins, defines` in `module/constants/__init__.py`, we would be unable to use `from module.constants import LED_LEFT`, and instead be forced to use `from module.constants.flags import LED_LEFT`.

If we chose to do this, we could use `pins.LED_LEFT` *and* `flags.LED_LEFT` instead of `pins.LED_LEFT_PIN` and `flags.LED_LEFT`.
