#!/usr/bin/env python3
"""Render resume.txt — an 80-column plain-text resume for raw GitHub viewing.

Mirrors the content of sections/*.tex. Run after editing the LaTeX sources:
    python3 build_txt.py
"""

import textwrap

W = 80


def center(s):
    return s.center(W).rstrip()


def lr(left, right):
    """Left text, right text, flush to the 80-column edge."""
    pad = max(1, W - len(left) - len(right))
    return left + " " * pad + right


def bullets(items):
    # break_on_hyphens=False keeps compounds like "legacy-system" intact.
    return [
        textwrap.fill(
            t,
            width=W,
            initial_indent="  - ",
            subsequent_indent="    ",
            break_on_hyphens=False,
        )
        for t in items
    ]


def wrap(text, indent="  "):
    return textwrap.fill(
        text,
        width=W,
        initial_indent=indent,
        subsequent_indent=indent,
        break_on_hyphens=False,
    )


def section(title):
    return ["", title.upper(), "-" * W, ""]


def job(title, org, dates, items):
    return [lr(title, dates), "  " + org, ""] + bullets(items) + [""]


out = []

# -- Header ------------------------------------------------------------------
out += [
    "=" * W,
    center("THANG LE VIET"),
    center("AI Engineer"),
    "",
    center("Ho Chi Minh City, Viet Nam  |  (+84) 989394637"),
    center("levietthang0512@outlook.com"),
    center("github.com/toreleon  |  linkedin.com/in/thanglv"),
    "=" * W,
]

# -- Summary -----------------------------------------------------------------
out += section("Summary")
out += [
    wrap(
        "AI Engineer with 5 years shipping production ML and LLM systems, "
        "specializing in agentic AI for software engineering. Currently building "
        "enterprise coding agents for code review, bug localization, and codebase "
        "intelligence at FPT AI Center."
    )
]

# -- Experience --------------------------------------------------------------
out += section("Experience")
out += job(
    "AI Engineer",
    "FPT AI Center - AI4SE Lab",
    "Jan 2024 - Present",
    [
        "Led development of a LangGraph-based multi-agent system that automates "
        "code review, code analysis, and bug localization across 50+ "
        "multi-language enterprise repositories",
        "Built Metis, a codebase-intelligence engine that auto-generates technical "
        "wikis via RAG and vector search over large multi-language repositories, "
        "adopted by internal FPT engineering teams",
        "Implemented LLM-as-a-judge pipelines and benchmarked agents on HumanEval, "
        "MBPP, and CodeReviewBench",
        "Developed MCP servers and tool-calling integrations exposing code-analysis "
        "tools to the agents",
        "Designed and shipped production backend services (Python) powering a "
        "mainframe code-analysis and modernization platform that surfaces "
        "legacy-system intelligence to developers",
    ],
)
out += job(
    "AI Engineer",
    "Resonance Technology",
    "Apr 2022 - Oct 2023",
    [
        "Lifted platform user engagement 83.7% by leading R&D on prompt-based LLM "
        "product features",
        "Accelerated SERP clustering 40% and cut memory usage over 5x by "
        "redesigning the core clustering algorithms",
        "Prototyped WriterZen's AI copilot automating end-to-end SEO workflows, "
        "content planning, and competitive analysis",
    ],
)
out += job(
    "Data Scientist",
    "Be Group",
    "Jul 2021 - Apr 2022",
    [
        "Raised top-recommendation click-through from 55% to 70% by building "
        "ranking algorithms for Be Food search",
        "Increased recommendation clicks 8% by designing a personalized drop-off "
        "recommendation model",
        "Automated customer support with a Rasa conversational platform and a "
        "FastText semantic-search engine",
    ],
)
out += job(
    "Research Assistant",
    "NLP@UIT Lab, University of Information Technology",
    "Feb 2020 - Feb 2022",
    [
        "Built COVIDROP, the first Vietnamese numerical-reasoning "
        "reading-comprehension dataset (DROP-based), with annotation guidelines "
        "and labeling tools ensuring high-quality data collection",
        "Implemented and evaluated NAQANet and NumNet baselines to benchmark "
        "Vietnamese numerical reasoning",
    ],
)
out.pop()  # trailing blank before next section rule

# -- Skills ------------------------------------------------------------------
SKILLS = [
    ("Programming & Tools", "Python, TypeScript, SQL, Git, Claude Code, Cursor, Codex"),
    (
        "LLM & Agentic Systems",
        "LLM agents, multi-agent orchestration (LangGraph), RAG, prompt "
        "engineering, fine-tuning (LoRA), LLM evaluation, tool calling, MCP "
        "(Model Context Protocol), OpenAI & Anthropic APIs",
    ),
    (
        "AI for Software Engineering",
        "Agentic code review, bug localization, codebase intelligence, mainframe "
        "modernization",
    ),
    (
        "ML & Data",
        "PyTorch, Hugging Face Transformers, TensorFlow, ranking & recommendation, "
        "semantic search, vector databases",
    ),
    ("MLOps & Infra", "Docker, Kubernetes, FastAPI / REST APIs, cloud (AWS/GCP/Azure)"),
    ("Languages", "Vietnamese (Native), English (C1)"),
]
out += section("Skills")
for label, value in SKILLS:
    out += ["  " + label, wrap(value, indent="      "), ""]
out.pop()

# -- Education ---------------------------------------------------------------
out += section("Education")
out += [
    lr("Master of Science (M.Sc.) in Computer Science", "Sep 2023 - Mar 2026"),
    "  University of Information Technology  |  GPA: 3.7/4.0",
    "",
    lr("Bachelor of Science (B.Sc.) in Data Science", "Sep 2018 - Jan 2022"),
    "  University of Information Technology  |  GPA: 3.6/4.0 (Top 1 in Major)",
]

# -- Publications ------------------------------------------------------------
out += section("Publications")
out += [
    wrap(
        'Van Nguyen, K., Le, T.V. & Do, T.PP. "Numerical reasoning reading '
        'comprehension on Vietnamese COVID-19 news: task, corpus, and challenges." '
        "Neural Computing & Applications 36, 14053-14073 (2024).",
    ),
    "  https://doi.org/10.1007/s00521-024-09744-5",
]

with open("resume.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out).rstrip() + "\n")

print(f"wrote resume.txt ({len(out)} lines, {W}-column)")
