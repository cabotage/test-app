import sys
import os

print(f"{os.environ.get('ENV_VAR')}", file=sys.stderr)
