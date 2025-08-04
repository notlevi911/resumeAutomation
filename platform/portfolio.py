import os
import subprocess

def update_resume(filepath):
    print("🖥️ Updating portfolio repo with new resume...")

    repo_url = "https://x-access-token:{}@github.com/notlevi911/Portolio-Website.git".format(os.getenv("GH_TOKEN"))

    # Clone the portfolio repo
    subprocess.run(["git", "clone", repo_url])
    os.chdir("Portolio-Website")

    # Copy the new resume to replace old one
    subprocess.run(["cp", f"../{filepath}", "Resume (1).pdf"])

    subprocess.run(["git", "add", "Resume (1).pdf"])
    subprocess.run(["git", "config", "user.name", "resume-bot"])
    subprocess.run(["git", "config", "user.email", "resume-bot@example.com"])
    subprocess.run(["git", "commit", "-m", "🔄 Auto-updated resume from resume-sync repo"], check=False)
    subprocess.run(["git", "push"])
