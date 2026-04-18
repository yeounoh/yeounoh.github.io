---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* **Cornell University**, BS in ECE & ME in CS
* **Brown University**, CS PhD
* *Add your years here*

Work experience
======
* **Google**, AI and Data Systems Research
* *Add your roles and dates here*
* *Add previous experience at startups and large companies*

Skills
======
* Data Systems
* AI Systems & Data Agents
* Data Science
* Software Engineering

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* *Add professional service (e.g., PC member, reviewing) and leadership roles here*
