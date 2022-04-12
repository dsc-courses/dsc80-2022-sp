---
layout: home
title: Home
nav_exclude: false
nav_order: 1
---

# {{ site.tagline }} <img src='favicon.ico' style='vertical-align: text-top' width=37>
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }

{{ site.staffersnobio }}

[Zoom Link](https://ucsd.zoom.us/j/92137281308){: .btn .btn-blue } [Recordings](https://podcast.ucsd.edu){: .btn .btn-green } [Assignment Solutions](https://campuswire.com/c/G325FA25B/feed/508){: .btn .btn-purple }

{% for module in site.modules %}
{{ module }}
{% endfor %}