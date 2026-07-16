# Thang Le Viet Resume

LaTeX source for my resume as an AI Engineer (LLM Agents & AI for Software Engineering).

## Resume

- [View PDF](resume.pdf)
- [Source](resume.tex)

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error resume.tex
pdflatex -interaction=nonstopmode -halt-on-error resume.tex
```

The second pass updates PDF outline metadata.

## Structure

- `resume.tex` - main LaTeX document
- `TLCresume.sty` - resume styling
- `sections/` - resume content sections
- `figs/` - image assets
- `resume.pdf` - generated resume
