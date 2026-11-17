"""One-command launcher; isolated dependencies, with offline report/check options."""
from pathlib import Path
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main():
    if sys.version_info < (3, 11):
        raise SystemExit("Python 3.11 or later is required; tested on Python 3.13.15.")
    if sys.argv[1:] == ["--report"]:
        return subprocess.call([sys.executable, str(ROOT / "model.py")], cwd=ROOT)
    if sys.argv[1:] == ["--check"]:
        return subprocess.call([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_model.py", "-v"], cwd=ROOT)
    env_python = ROOT / ".venv" / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    if not env_python.exists():
        print("Creating project-only .venv environment...", flush=True)
        subprocess.run([sys.executable, "-m", "venv", str(ROOT / ".venv")], check=True)
    ready = subprocess.run([str(env_python), "-c", "import importlib.metadata as m; assert m.version('streamlit') == '1.66.0'"], capture_output=True)
    if ready.returncode:
        print("Installing requirements (internet required the first time)...", flush=True)
        subprocess.run([str(env_python), "-m", "pip", "install", "-r", str(ROOT / "requirements.txt")], check=True)
    return subprocess.call([str(env_python), "-m", "streamlit", "run", str(ROOT / "app.py"), "--server.address=127.0.0.1", "--server.headless=true", "--browser.gatherUsageStats=false", *sys.argv[1:]], cwd=ROOT)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as error:
        raise SystemExit(f"Setup failed (exit {error.returncode}). Check internet and Python installation, then rerun the same command. The offline result is in outputs/results.md.")
