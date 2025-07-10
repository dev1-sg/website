import requests
from jinja2 import Template

base_images = next(iter(requests.get("https://api.dev1-sg.com/v1/public/images/base").json().values()))
base_images = sorted(base_images, key=lambda x: x["image_name"].lower())
ci_images = next(iter(requests.get("https://api.dev1-sg.com/v1/public/images/ci").json().values()))
ci_images = sorted(ci_images, key=lambda x: x["image_name"].lower())

template = Template("""\
---
position: 3
title: Docker Resources
slug: docker-resources
---

## Docker Resources


### [docker-base-images](https://github.com/dev1-sg/docker-base-images)


|#|Image|Group|URI|Latest Tag|Size(MB)|SHA256|Source|Last Push|
|---|---|---|---|---|---|---|---|---|
{% for image in base_images -%}
|{{ loop.index }}|[{{ image.image_name.split('/')[-1] }}](https://gallery.ecr.aws/dev1-sg/{{ image.image_name }})|{{ image.image_group }}|{{ image.uri }}|{{ image.latest_tag }}|{{ image.size_mb }} MB|{{ image.latest_sha }}|[https://github.com/dev1-sg/docker-base-images/tree/main/src/{{ image.image_name.split('/')[-1] }}](https://github.com/dev1-sg/docker-base-images/tree/main/src/{{ image.image_name.split('/')[-1] }})|{{ image.last_push }}|
{% endfor -%}


### [docker-ci-images](https://github.com/dev1-sg/docker-ci-images)


|#|Image|Group|URI|Latest Tag|Size(MB)|SHA256|Source|Last Push|
|---|---|---|---|---|---|---|---|---|
{% for image in ci_images -%}
|{{ loop.index }}|[{{ image.image_name.split('/')[-1] }}](https://gallery.ecr.aws/dev1-sg/{{ image.image_name }})|{{ image.image_group }}|{{ image.uri }}|{{ image.latest_tag }}|{{ image.size_mb }} MB|{{ image.latest_sha }}|[https://github.com/dev1-sg/docker-ci-images/tree/main/src/{{ image.image_name.split('/')[-1] }}](https://github.com/dev1-sg/docker-ci-images/tree/main/src/{{ image.image_name.split('/')[-1] }})|{{ image.last_push }}|
{% endfor -%}

""")

print(template.render(base_images=base_images, ci_images=ci_images))
