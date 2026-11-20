---
layout: home
permalink: /
title: "AI & Data Systems Research"
redirect_from:
  - /about/
  - /about.html
eyebrow: "AI & Data Systems Research · Google Cloud"
tagline: "Co-designing databases, AI agents, and hardware compilers for scalable intelligent data processing."
bio_summary: "I am a researcher and technical lead at Google Cloud exploring how database systems, large language models, and AI accelerators co-evolve. My recent work spans proxy-based semantic query optimization, agentic Text-to-SQL and multi-agent RL, and native analytical query execution on TPUs—building on earlier leadership in PyTorch/XLA distributed sharding (SPMD & Auto-Sharding) and automated ML model validation (TFX SliceFinder)."
avatar_caption: "Systems, AI & Data Infrastructure"

highlights:
  - index: "01"
    title: "Semantic Data Processing"
    summary: "Scaling LLM-powered SQL operators (AI.IF, AI.RANK) and unstructured document ETL via embedding proxies, multi-objective pipeline rewrites, and workflow-aware agent serving."
    works:
      - title: ">100x AI Query Approximation"
        venue: "SIGMOD '26"
        url: "https://dl.acm.org/doi/10.1145/3802002"
        note: "Lightweight embedding proxies slashing LLM filter cost & latency in BigQuery and AlloyDB."
      - title: "Multi-Objective Agentic Rewrites (MOAR)"
        venue: "PVLDB '26"
        url: "https://doi.org/10.14778/3836663.3836673"
        note: "Joint accuracy–cost global pipeline optimization for DocETL unstructured analytics."
      - title: "Cortex: Agentic Resource Pooling"
        venue: "SAA @ SOSP '25"
        url: "https://arxiv.org/abs/2510.14126"
        note: "Stage isolation and workflow-aware scheduling for multi-turn agent serving."

  - index: "02"
    title: "Optimizing Text-to-SQL"
    summary: "Advancing natural language interfaces for complex enterprise schemas through multi-agent reinforcement learning, query-decomposed table retrieval, and cost–accuracy optimization."
    works:
      - title: "DualSQL: Multi-Agent RL for NL2SQL"
        venue: "arXiv '26"
        url: "https://arxiv.org/abs/2609.18135"
        note: "Jointly optimizing schema linking and SQL generation on a shared backbone with REX & guardrails."
      - title: "PRISM & Fine-Grained Table Retrieval"
        venue: "SIGMOD '26 · AKBC '26"
        url: "https://dl.acm.org/doi/10.1145/3786679"
        note: "Co-optimizing pipeline cost–accuracy frontiers and connectivity-aware multi-table retrieval."
      - title: "CHASE-SQL & Long-Context NL2SQL"
        venue: "ICLR '25 · PVLDB '25"
        url: "https://openreview.net/forum?id=CvGqMD5OtX"
        note: "Multi-path candidate synthesis, preference selection, and extended-context schema grounding."

  - index: "03"
    title: "TPU Data Processing & Compilation"
    summary: "Co-designing relational analytics and hybrid AI execution graphs directly with JAX/XLA compilers and TPU hardware primitives."
    works:
      - title: "TPU-Accelerated Analytical Query Processing"
        venue: "arXiv '26"
        url: "https://arxiv.org/abs/2610.22673"
        note: "Native TPU Accelerator (NTA) executing full TPC-H cleanly across TensorCores and SparseCores."
      - title: "AI Query Compilation"
        venue: "AIDB @ VLDB '26"
        url: "https://arxiv.org/abs/2608.10139"
        note: "Fusing SQL algebra and LLM layers into a single tensor graph (up to 5.3x lower latency, 9.8x throughput on TPUs)."
      - title: "PyTorch/XLA SPMD & Auto-Sharding"
        venue: "PyTorch Conf '23–'24"
        url: "https://pytorch.org/blog/pytorch-xla-spmd/"
        note: "Compiler-driven distributed parallelization for large-scale models on Cloud TPUs."

interests:
  - title: "Semantic & Agentic Data Systems"
    detail: "Approximating, rewriting, and serving LLM-augmented relational and unstructured data pipelines at cloud warehouse scale."
  - title: "Text-to-SQL & Natural Language Interfaces"
    detail: "Multi-agent reinforcement learning, fine-grained schema retrieval, synthetic evaluation, and cost–accuracy optimization."
  - title: "TPU & Accelerator-Native Analytics"
    detail: "Co-designing OLAP operators and hybrid SQL+AI execution with JAX/XLA compilers and specialized hardware accelerators."
  - title: "Data-Centric ML Validation"
    detail: "Automated failure-mode discovery (SliceFinder), data quality metrics, and quantifying uncertainty from unknown examples."

experience:
  - org: "Google Cloud"
    role: "Research & Technical Lead"
    detail: "Leading research on AI data systems, semantic query optimization, NL2SQL, and TPU analytical processing; previously led PyTorch/XLA SPMD & Auto-Sharding."
  - org: "Google Research"
    role: "Student Research Collaborator"
    detail: "Researched and built SliceFinder (ICDE '19, TKDE '20) for automated ML data slicing, integrated into TensorFlow Extended (TFX)."
  - org: "Apple (Core OS)"
    role: "Software Engineer"
    detail: "Architected backend telemetry pipelines for the App Store Connect Power & Performance API (WWDC '20)."
  - org: "Academic Community & Service"
    detail: "VLDB 2026 Industrial Track Program Committee · SIGMOD 2026 Research Session Chair (LLM & Agentic Data Processing)."
---
