print(f"Running target.py, with __name__: {__name__}")

from .utils import stub

# this would work for direct execution:
# from utils import stub

# the suggestion to just avoid relative imports doesn't work for me:
# from mod.utils import stub
