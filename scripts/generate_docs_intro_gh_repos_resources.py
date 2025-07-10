import requests
from jinja2 import Template

repos = next(iter(requests.get("https://api.dev1-sg.com/v1/public/repos/gh").json().values()))
repos = sorted(repos, key=lambda x: x["name"].lower())

template = Template("""\
---
position: 1
title: Introduction
slug: intro
---

## Mission

dev1-sg is a devops project to define a vendor-neutral, principle-led meaning of DevOps.

### Repositories

|#|Name|Description|Clone URL|Language|Topics|Last Push|
|---|---|---|---|---|---|---|
{% for repo in repos -%}
|{{ loop.index }}|[{{ repo.name }}]({{ repo.url }})|{{ repo.description or "-" }}|{{ repo.clone_url }}|{{ repo.language or "-" }}|{{ repo.topics | join(", ") }}|{{ repo.last_push or "-" }}|
{% endfor %}

### Contributing

We welcome anyone who would like to get involved.

Be sure to review the [contributing guidelines](https://github.com/dev1-sg/.github/blob/main/CONTRIBUTING.md) and [code of conduct](https://github.com/dev1-sg/.github/blob/main/CODE_OF_CONDUCT.md).

### Security

Reporting a security vulnerability? Check out the project's [security policy](https://github.com/dev1-sg/.github/blob/main/SECURITY.md).

### Support

Looking for help?

Check out the project’s [instructions for getting support](https://github.com/dev1-sg/.github/blob/main/SUPPORT.md).

""")

print(template.render(repos=repos))
