# AI reviewer: Gemini Code Assist on GitHub

This repository uses **Gemini Code Assist** as its AI pull request reviewer. It is a GitHub App: once installed, it posts a summary and inline review comments on pull requests.

> Product details (pricing, limits, commands, config options) change often. If something below does not match what you see, the official documentation wins: search for "Gemini Code Assist GitHub".

## 1. Check whether it is already installed

- **Repository settings:** open *Settings → GitHub Apps* (or *Settings → Integrations*). If `gemini-code-assist` is listed, it is installed.
- **On a pull request:** if `gemini-code-assist[bot]` has commented on recent PRs, it is active.

If it is installed, skip to [section 3](#3-use-it-on-a-pull-request).

## 2. Install it

You need admin rights on the repository (or on the organization that owns it).

1. Open <https://github.com/apps/gemini-code-assist> and click **Install**. It is also listed in the GitHub Marketplace under "Gemini Code Assist".
2. Choose the account or organization that owns the repository.
3. Under **Repository access**, select **Only select repositories** and pick this repository. Avoid granting access to all repositories unless you mean to.
4. You are redirected to a Google page. Sign in with a Google account, accept the terms and confirm the connection.

The free consumer version is enough for this demo. Organizations that need enterprise controls use the paid version, which is set up through Google Cloud.

## 3. Use it on a pull request

**Automatic review.** For every pull request opened *after* installation, the bot posts:

1. a summary of the changes, and
2. a code review with inline comments, each labeled with a severity (critical, high, medium, low).

Pull requests that were already open when the app was installed are not reviewed automatically. Trigger them by hand (see below).

**Commands.** Post these as a regular comment on the pull request:

| Command | What it does |
|---|---|
| `/gemini review` | Runs a full code review of the current state of the PR |
| `/gemini summary` | Posts a summary of the PR |
| `/gemini help` | Lists the available commands |
| `@gemini-code-assist <question>` | Asks the bot a question, in the PR conversation or as a reply to one of its comments |

A review usually takes a few minutes. Re-run `/gemini review` after you push new commits; it does not re-review every push on its own.

**Treat its comments like any reviewer's.** Apply the useful ones (many come as GitHub *suggested changes* you can commit with one click), reply to or resolve the rest. Some comments will be wrong or irrelevant. The AI review is a first pass, not an approval: a human still reviews and approves before merge.

## 4. Give it context (optional)

The bot reads configuration from a `.gemini/` folder at the root of the repository, on the **default branch** (`main`). Changes on a feature branch have no effect until they are merged.

**`.gemini/styleguide.md`**: your team's review rules in plain Markdown, for example "money is always `Decimal`" or "every view that reads an order checks the owner". The bot reviews against these in addition to its general checks. The more specific the rules, the more useful the review.

**`.gemini/config.yaml`**: behavior settings, for example:

```yaml
have_fun: false                    # no poems or jokes in summaries
code_review:
  disable: false
  comment_severity_threshold: MEDIUM   # hide LOW-severity comments
  max_review_comments: -1              # -1 = no limit
  pull_request_opened:
    summary: true
    code_review: true
ignore_patterns:
  - "**/migrations/**"
```

After adding or changing either file on `main`, run `/gemini review` on an open PR to see the effect.

## 5. Uninstall or pause

- **Pause:** set `code_review.disable: true` in `.gemini/config.yaml`.
- **Remove:** *Settings → GitHub Apps → gemini-code-assist → Configure*, then remove the repository from its access list or uninstall the app.
