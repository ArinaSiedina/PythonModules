import importlib

print("\nREAGENT STATUS: Loading reagents...\n", "Checking dependencies:", sep="\n")
libraries: list[tuple[str, str]] = [
    ("pandas", "Data manipulation ready"),
    ("numpy", "Numerical computation ready"),
]
all_installed: bool = True

for name, desc in libraries:
    try:
        library = importlib.import_module(name)

        print(f"[OK] {name} {library.__version__} - {desc}")
    except ModuleNotFoundError:
        print(
            f"[MISSING] {name}",
            f" Install with pip: python -m pip install {name}",
            f" Install with Poetry: poetry add {name}",
            sep="\n",
            end="\n\n",
        )
        all_installed = False

print(
    "\npip vs Poetry:",
    "requirements.txt declares what to install; "
    "pip resolves it at install time.",
    "pyproject.toml declares the same constraints, "
    "and Poetry pins the resolved",
    "versions in poetry.lock so every install is identical.",
    sep="\n",end="\n\n"
)
if all_installed:
    print("All reagents present and accounted for.")
