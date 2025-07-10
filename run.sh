#!/usr/bin/env sh

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python3 scripts/generate_docs_docker_resources.py > website/docs/3._containerization/3._docker-resources.md
python3 scripts/generate_docs_intro_gh_repos_resources.py > website/docs/1._intro.md
