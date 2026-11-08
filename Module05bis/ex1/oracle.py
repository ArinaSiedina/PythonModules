import os

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

mode = os.getenv("MATRIX_MODE", "development")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL", "INFO")
endpoint = os.getenv("ZION_ENDPOINT")

required = {
    "DATABASE_URL": database,
    "API_KEY": api_key,
    "ZION_ENDPOINT": endpoint,
}

print("ORACLE STATUS: Consulting the configuration...")

print("\nConfiguration loaded:")
print(f" Mode: {mode}")
print(f" Database: {'Connection configured' if database else 'Not configured'}")
print(f" API Access: {'Credentials configured' if api_key else 'Not authenticated'}")
print(f" Log Level: {log_level}")
print(f" Remote Network: {'Endpoint configured' if endpoint else 'Not configured'}")

print("\nConfiguration validation:")

if mode == "development":
    print(" [INFO] Development mode - detailed diagnostics enabled")

    for name, value in required.items():
        if value:
            print(f" [OK] {name} is configured")
        else:
            print(f" [WARNING] {name} is missing - development can continue")

elif mode == "production":
    missing = [name for name, value in required.items() if not value]

    if missing:
        print(" [ERROR] Production configuration is incomplete")
        for name in missing:
            print(f" [MISSING] {name}")
    else:
        print(" [OK] All required production settings are configured")

else:
    print(f" [WARNING] Unknown configuration mode: {mode}")

print("\nConfiguration security check:")
print(" [OK] Secret values are hidden from output")

gitignore_path = os.path.join(os.path.dirname(__file__), ".gitignore")

if os.path.isfile(gitignore_path):
    with open(gitignore_path, "r", encoding="utf-8") as file:
        ignored_files = [line.strip() for line in file]

    if ".env" in ignored_files:
        print(" [OK] .env file listed in .gitignore")
    else:
        print(" [WARNING] .env is not explicitly listed in .gitignore")
else:
    print(" [WARNING] .gitignore file not found")

print(" [OK] Production environment overrides supported")
print("\nThe Oracle sees all configurations.")