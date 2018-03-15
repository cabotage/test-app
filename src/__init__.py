import sys
import os

sys.stderr.write(f"{os.environ.get('ENV_VAR')}\n")
