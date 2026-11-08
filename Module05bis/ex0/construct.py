import os
import sys
import sysconfig

global_py: str = sys.base_prefix
current_py: str = sys.prefix
is_venv: bool = global_py != current_py

print(
    "\nLABORATORY STATUS:",
    "The laboratory is sealed" if is_venv else "You are working in the open",
    end="\n\n",
)
print(
    f"Current Python: {sys.executable}",
    "\nVirtual Environment:",
    os.path.basename(current_py) if is_venv else "None detected",
    end="\n",
)
if is_venv:
    print(
        f"Environment Path: {current_py}\n",
        "SUCCESS: You are working in an isolated environment!",
        "Safe to install reagents without affecting the global system.\n",
        f"Reagent installation path:\n{sysconfig.get_path('purelib')}",
        sep="\n",
    )
else:
    print(
        "\nWARNING: You are in the global environment!",
        "Every reagent you install here leaks into the whole system.\n",
        "To seal the laboratory, run:",
        "python3 -m venv lab_env",
        "source lab_env/bin/activate\n",
        "Then run this program again.",
        sep="\n",
    )
