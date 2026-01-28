---
layout: splash
permalink: /
hidden: true
header:
  overlay_color: "#000"
  overlay_filter: "0.5"
  actions:
    - label: "View Resume"
      url: "/about/"
    - label: "Read the Blog"
      url: "/posts/"
excerpt: "Senior Platform Engineer specializing in Kubernetes, cloud infrastructure, and secure CI/CD pipelines. I build and support platforms that developers can be enthusiastic about."

intro:
  - excerpt: "## Featured Projects"

feature_row_k8s:
  - title: "Kubernetes Platform Automation"
    excerpt: "Production-grade Kubernetes cluster automation using Terraform and cloud-init. Automated provisioning with reproducible infrastructure deployment."
    url: "https://github.com/eckslopez/kubernetes-platform-infrastructure"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
  - url: "/platform/engineering/building-production-grade-k3s-cluster-on-spare-capacity/"
    btn_label: "Read Blog Post"
    btn_class: "btn--inverse"

feature_row_postgres:
  - title: "Multi-Tenant PostgreSQL Security"
    excerpt: "Operational guardrails and security isolation for multi-tenant PostgreSQL. Role-per-tenant architecture with connection limits and resource protection."
    url: "https://github.com/eckslopez/pg"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
  - url: "/databases/operations/platform/operational-guardrails-for-multi-tenant-postgres/"
    btn_label: "Read Blog Post"
    btn_class: "btn--inverse"

feature_row_pipelines:
  - title: "Platform Pipelines"
    excerpt: "Reusable GitHub Actions workflows for CI/CD. Centralized pipeline definitions enabling standardized deployment patterns across repositories."
    url: "https://github.com/eckslopez/platform-pipelines"
    btn_label: "View on GitHub"
    btn_class: "btn--primary"
---

{% include feature_row id="intro" type="center" %}

{% include feature_row id="feature_row_k8s" type="left" %}

{% include feature_row id="feature_row_postgres" type="right" %}

{% include feature_row id="feature_row_pipelines" type="left" %}

## Recent Posts

{% for post in site.posts limit:3 %}
### [{{ post.title }}]({{ post.url }})
*{{ post.date | date: "%B %d, %Y" }}*

{{ post.excerpt }}

[Read more →]({{ post.url }}){: .btn .btn--inverse}
{% endfor %}

[View all posts →](/posts/){: .btn .btn--primary .btn--large}
