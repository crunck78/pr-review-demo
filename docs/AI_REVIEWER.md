# AI reviewer: CodeRabbit on GitHub

This repository uses **CodeRabbit** as its AI pull request reviewer. It is a GitHub App: once installed, it posts a summary and inline review comments on pull requests.

> Product details (pricing, limits, commands, config options) change often. If something below does not match what you see, the official documentation wins: <https://docs.coderabbit.ai>.

## 1. Check whether it is already installed

- **Account settings:** open <https://github.com/settings/installations> (or the organization's *Settings → GitHub Apps*). If **CodeRabbit** is listed and this repository is in its access list, it is installed.
- **On a pull request:** if `coderabbitai[bot]` has commented on recent PRs, it is active.

If it is installed, skip to [section 3](#3-use-it-on-a-pull-request).

## 2. Install it

You need owner rights on the repository. Reviews are free for public repositories.

1. Open <https://app.coderabbit.ai/login> and click **Login with GitHub**, then **Authorize coderabbitai**.
2. Select the account that owns the repository (for a personal repository, your own user name).
3. Under **Choose repository access**, pick **Only select repositories** and select this repository.
4. Click **Install & Authorize**.

## 3. Use it on a pull request

**Automatic review.** Every new pull request gets:

1. a summary of the changes (walkthrough), and
2. a code review with inline comments, many with a ready-to-commit suggested change.

When you push new commits to a reviewed PR, CodeRabbit reviews just those commits automatically.

Pull requests that were already open when the app was installed may not be reviewed automatically. Trigger them by hand.

**Commands.** Post one per comment on the pull request, at the start of the comment:

| Command | What it does |
|---|---|
| `@coderabbitai review` | Reviews the commits pushed since its last review |
| `@coderabbitai full review` | Reviews every file in the PR again from scratch |
| `@coderabbitai summary` | Regenerates the PR summary |
| `@coderabbitai pause` / `resume` | Stops / restarts automatic reviews on this PR |
| `@coderabbitai help` | Lists all commands |
| `@coderabbitai <question>` | Asks a question, in the PR conversation or as a reply to one of its comments |

**Treat its comments like any reviewer's.** Apply the useful ones, reply to or resolve the rest. Some comments will be wrong or irrelevant. The AI review is a first pass, not an approval: a human still reviews and approves before merge.

## 4. Give it context (optional)

**Team review rules in `.coderabbit.yaml`.** A file at the repository root lets you write review instructions per path, in plain language:

```yaml
reviews:
  path_instructions:
    - path: "**/*.py"
      instructions: |
        - Money is always `Decimal`, never `float`.
        - Every view that reads an order checks that it belongs to `request.user`.
```

By default CodeRabbit reads this file from the **pull request's own branch** (for PRs from collaborators), so a rule change takes effect on the PR that contains it. After changing it, run `@coderabbitai full review` to review the whole PR with the new rules.

**Existing guideline files.** CodeRabbit also reads common AI instruction files automatically, for example `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` and `.github/copilot-instructions.md`.

The more specific the rules, the more useful the review.

## 5. Pause or uninstall

- **One PR:** `@coderabbitai pause`, or put `@coderabbitai ignore` in the PR description.
- **Remove:** <https://github.com/settings/installations> → **CodeRabbit** → **Configure**, then remove the repository from its access list or uninstall the app.
