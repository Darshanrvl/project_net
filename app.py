import subprocess
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

def git(args):
    try:
        return subprocess.check_output(
            ["git"] + args,
            stderr=subprocess.STDOUT,
            text=True
        ).strip()
    except Exception:
        return "N/A"

@app.get("/", response_class=PlainTextResponse)
def root():
    commit_id = git(["rev-parse", "HEAD"])
    commit_msg = git(["log", "-1", "--pretty=%B"])
    return f"Hello, World\n\nLatest Git commit ID: {commit_id}\nLatest Git commit message: {commit_msg}"
