import os
import site
import sys

global_py: str = sys.base_prefix
current_py: str = sys.prefix
is_venv: bool = global_py != current_py
global_locations: list[str] = site.getsitepackages([global_py])
current_locations: list[str] = site.getsitepackages([current_py])

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
print("\nGlobal Python package locations:")
for location in global_locations:
    print(f"  {location}")

print("\nCurrent environment package locations:")
for location in current_locations:
    print(f"  {location}")

if is_venv:
    print(
        f"Environment Path: {current_py}\n",
        "SUCCESS: You are working in an isolated environment!",
        "Safe to install reagents without affecting the global system.\n",
        sep="\n",
    )
else:
    print(
        "\nWARNING: You are in the global environment!",
        "Every reagent you install here leaks into the whole system.\n",
        "To seal the laboratory, run:",
        "On Unix:",
        "python3 -m venv lab_env",
        "source lab_env/bin/activate\n",
        "On Windows (PowerShell):",
        "py -m venv lab_env",
        r".\lab_env\Scripts\Activate.ps1",
        "",
        "Then run this program again.",
        sep="\n",
    )
