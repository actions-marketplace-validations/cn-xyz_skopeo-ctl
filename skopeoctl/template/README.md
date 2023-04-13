Google Containers Registry {{ src_repo }} Mirrors [last sync {{ date }}]
-------

Repository Address: [https://hub.docker.com/u/{{ dest_repo }}/](https://hub.docker.com/u/{{ dest_repo }}/)

Useage
-------

From gcr.io:
```bash
docker pull {{ src_repo }}/image:v1.0.0
```

From docker hub Mirrors:
```bash
docker pull {{ dest_repo }}/image:v1.0.0
```

Total of {{ image_count }}'s {{ src_org }} images

-------

| No  | name | tags count | total size | last sync time |
| --- | ----- | ---------- | ---------- | -------------- |
{%- for index in range(image_count) -%}
{%- set no = index + 1 -%}
{%- set image = images_list[index] -%}
{%- set name = image['name'] -%}
{%- set sync_from = "https://{{ src_org }}/{{ src_repo }}/%s" % name -%}
{%- set docker_hub = "https://hub.docker.com/u/{{ dest_repo }}/%s/tags/" % name -%}
{%- set tags_count = image['tags_count'] -%}
{%- set total_size = image['total_size'] -%}
{%- set date = image['date'] %}
| {{ no }} | {{ name }} | {{ tags_count }} | {{ total_size }} | {{ date }} |
{%- endfor %}

Support
-------

- https://github.com/cn-xyz/image-sync
