# Dependency maintenance

`requirements.txt` contains the application dependencies used by the Docker image.
`requirements.full.txt` also includes the notebook environment and requires Python
3.11 or later. The overlapping application pins are kept consistent.

Create a new virtual environment outside the repository's checked-in `.venv`:

```sh
python3.11 -m venv ../fake-news-env
../fake-news-env/bin/python -m pip install -r requirements.full.txt -r requirements.txt
../fake-news-env/bin/python -m pip check
../fake-news-env/bin/python -m unittest discover -s tests -v
../fake-news-env/bin/python -m pip install pip-audit
../fake-news-env/bin/python -m pip_audit -r requirements.full.txt
../fake-news-env/bin/python -m pip_audit -r requirements.txt
```

The tests exercise HTTP chunk parsing, Markdown nesting, Flask cookie-cache
headers, notebook HTML export, and the application's classifier pipeline.
They do not import `app.py`, which starts a server and an infinite loop at import
time. They do not validate the saved production models or deployed service.

Do not reuse the repository's checked-in `.venv`: changing requirement pins does
not update that environment. Rebuild the deployment to use the new dependencies.
The existing Docker runtime remains Python 3.10; the notebook tests run on 3.11.

Dependabot groups security updates and checks weekly for routine updates.
GitHub Actions verifies installation, regression tests, and both requirements
audits before review. No updates are automatically merged.
