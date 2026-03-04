# AGENTS.md

## Project Overview

Rune is a curated collection of AI prompts for development, productivity, and creative tasks. Each prompt is stored as a standalone markdown file organized by category.

## Directory Structure

```
prompts/
├── common_agents.md    # Shared agent templates
├── coding/             # Programming & development prompts
├── writing/            # Writing & content creation prompts
└── productivity/       # Workflow & efficiency prompts
```

## File Conventions

### Prompt Files

- Each prompt is a standalone `.md` file
- Filename should be descriptive and use kebab-case (e.g., `read-article.md`)
- Prompts should include:
  - Clear role definition (e.g., "Act as an expert...")
  - Specific goals and constraints
  - Output format instructions
  - Example inputs if applicable

### Style Guidelines

- Use clear, direct language in prompts
- Format output sections with emojis or markdown headers for readability
- Include explicit constraints (e.g., "don't add any extra information")
- Specify output language when necessary

## Adding New Prompts

1. Choose the appropriate category directory (create if needed)
2. Create a new `.md` file with a descriptive name
3. Follow the existing prompt style and structure
4. Update README.md if adding a new category

## Commit Message Format

Follow conventional commits specification:

```
<type>(<scope>): <subject>

<body>
```

### Types

- `feat` — New prompt or feature
- `fix` — Bug fix or correction
- `docs` — Documentation updates
- `refactor` — Restructuring without content changes
- `style` — Formatting, typos, whitespace
- `chore` — Maintenance tasks

### Scope (optional)

- Category name: `coding`, `writing`, `productivity`
- `readme` — README updates
- `agents` — AGENTS.md updates

### Subject Rules

- Use imperative mood ("add" not "added")
- No trailing period
- Lowercase after the colon

### Examples

```
feat(productivity): add project-planning prompt

feat(coding): add code-review prompt with focus on security

fix(writing): correct typos in blog-outline prompt

docs(readme): update directory structure

chore: reorganize prompts into subdirectories
```

## Branch Protection

The `main` branch is protected. All changes must be made via pull requests with at least one approval.
