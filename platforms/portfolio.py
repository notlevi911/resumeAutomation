import os
import subprocess
import shutil

def update_resume(filepath):
    print("🖥️ Updating new-portfolio repo with new resume...")

    repo_url = f"https://x-access-token:{os.getenv('GH_TOKEN')}@github.com/notlevi911/new-portfolio.git"
    repo_dir = "new-portfolio"
    target_resume = os.path.join("frontend", "public", "resume.pdf")  # keep same name

    # Remove old clone if exists
    if os.path.exists(repo_dir):
        shutil.rmtree(repo_dir)

    # Clone fresh copy
    subprocess.run(["git", "clone", repo_url])
    os.chdir(repo_dir)

    # Copy Resume (1).pdf into frontend/public as Resume (1).pdf
    shutil.copy(f"../{filepath}", target_resume)

    # Stage changes
    subprocess.run(["git", "add", target_resume])

    # Configure git user
    subprocess.run(["git", "config", "user.name", "resume-bot"])
    subprocess.run(["git", "config", "user.email", "resume-bot@example.com"])

    # Commit (only if there are changes)
    commit_result = subprocess.run(["git", "diff", "--cached", "--quiet"])
    if commit_result.returncode != 0:  # changes exist
        subprocess.run(["git", "commit", "-m", "🔄 Auto-updated resume"])
        subprocess.run(["git", "push"])
        print("✅ Resume (1).pdf updated and pushed to new-portfolio!")
    else:
        print("ℹ️ No changes to commit.")
