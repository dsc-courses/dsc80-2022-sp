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

| 🎉 <span style='color:green'><b>Welcome to the Spring 2022 offering of DSC 80!</b></span> <br>Before class starts on Monday 3/28, make sure to read the [syllabus](syllabus) and make sure you can access Campuswire. See you on Monday! |

{{ site.staffersnobio }}

[Zoom Link](https://ucsd.zoom.us/j/92137281308){: .btn .btn-blue } [Recordings](https://podcast.ucsd.edu){: .btn .btn-green }

{% for module in site.modules %}
{{ module }}
{% endfor %}