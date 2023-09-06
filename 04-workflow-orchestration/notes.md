# Workflow Orchestration

## 01. Metaflow - Local
```bash
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install metaflow
pip install pylint
pip install kubernetes
```

```bash
python first_flow.py run
```

```bash
python card_flow.py card view my_decorated_func
```

```bash
python artifact_flow.py run
```

```python
from metaflow import Flow
run_artifacts = Flow("ArtifactFlow").latest_run.data
run_artifacts.dataset
```


https://stackoverflow.com/questions/66333474/postgresql-helm-chart-with-initdbscripts

```bash
metaflow configure kubernetes
```