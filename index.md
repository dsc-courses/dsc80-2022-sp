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

This is the website for a past version of DSC 80. However, you can access all course content by clicking the links below, or by accessing the course [**GitHub repository**](https://github.com/dsc-courses/dsc80-2022-sp/).

All podcasts 🎥 (lecture recordings) are available on YouTube [**at this link**](https://youtube.com/playlist?list=PLDNbnocpJUhYy_qYOS_CV4zmigqC6AOhv).

{% for module in site.modules %}
{{ module }}
{% endfor %}