install-python:
	uv python install 3.10

init:
	uv venv --python 3.10
	uv init && rm hello.py
	uv tool install black

install:
	. .venv/bin/activate
	# uv pip install --all-extras --requirement pyproject.toml
	# uv pip sync requirements.txt
	uv add -r requirements.txt

delete:
	rm uv.lock pyproject.toml .python-version && rm -rf .venv

run:
	uv run streamlit run app.py &