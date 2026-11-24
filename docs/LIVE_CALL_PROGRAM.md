# Dev Workflows Live Call: Pull Requests & Code Review

**Duration:** 60 minutes
**Audience:** developers who already use Git and GitHub, but have little experience with team review workflows
**Core message:** *A good review starts with the author, not the reviewer. AI is a first filter, never the approver.*

---

## At a glance

| Time | Block | Format |
|---|---|---|
| 0–5 | Hook: which PR would you review today? | Discussion |
| 5–15 | The PR as the author's product | Talk + examples |
| 15–27 | Reviewing as a reviewer | Live in GitHub |
| 27–45 | AI review: what it catches, what it misses | Live demo |
| 45–52 | Wiring it into the workflow | Live in GitHub |
| 52–60 | Q&A and takeaways | Discussion |

---

## 0–5 min · Hook

Show two pull requests side by side:

1. A huge PR: 40 files, title "fix stuff", empty description.
2. A small, focused PR with a clear title, context and testing steps.

Ask the audience: *"Which one would you review today, and which one would you postpone for a week?"*

The answer is obvious, and that is the point: reviewability is something the author creates.

---

## 5–15 min · The PR as the author's product

**Size and scope.** One purpose per PR. Aim for roughly 400 changed lines or fewer; beyond that, review quality drops sharply. Refactorings and features go in separate PRs.

**Title and description.** The description answers three questions: *what* changed, *why* it changed, and *how* to test it. Link the ticket. Show the repository's `.github/pull_request_template.md` as an example.

**Draft PRs.** Open a PR as a draft to get early feedback on direction before polishing.

**Self-review.** Before clicking "Ready for review", read your own diff in the GitHub UI. Authors catch a surprising number of issues (debug output, leftover TODOs, unrelated changes) simply by seeing the diff the way the reviewer will.

**Green CI is necessary, not sufficient.** Passing tests only prove what the tests check.

---

## 15–27 min · Reviewing as a reviewer

**What to look for, in order of importance:**

1. **Correctness:** does it do what the ticket asks? Edge cases, error paths.
2. **Security:** input validation, authorization, secrets, injection.
3. **Design:** is this the right place and the right abstraction? Will it be maintainable?
4. **Readability:** naming, structure, comments where intent is not obvious.
5. **Style:** ideally zero human comments here, because linters and formatters should handle it.

**GitHub features to demo live:**

- Inline comments and multi-line comments
- **Suggested changes** (the author applies them with one click)
- The three review outcomes: *Comment*, *Approve*, *Request changes*
- "Viewed" checkboxes to track progress through large diffs

**Comment conventions** that make intent explicit:

| Prefix | Meaning |
|---|---|
| `blocking:` | Must be fixed before merge |
| `question:` | I don't understand; please explain (may lead to a change) |
| `suggestion:` | Optional improvement |
| `nit:` | Tiny, non-blocking detail |
| `praise:` | Something done well, worth saying out loud |

**Tone.** Comment on the code, not the person. Ask questions instead of giving orders: *"What happens if `code` is empty?"* works better than *"This is wrong."*

---

## 27–45 min · AI review demo (the core of the session)

**Setup:** this repository contains a feature branch with a pull request that adds coupon codes to orders. An AI reviewer (GitHub App) is installed on the repository.

**Script:**

1. Open the PR and briefly read the description together. Ask the audience to spot problems in the diff themselves for two minutes.
2. Let the AI review run (or show its result) and walk through the comments.
3. Sort every finding into one of three columns, together with the audience:

| Caught by AI | Missed by AI | False positive / noise |
|---|---|---|
| | | |

4. Reveal the original ticket for the feature and check the PR against its acceptance criteria. Discuss: *could the AI have known this?*
5. **Optional second pass:** add a team style guide for the AI reviewer, re-run the review and compare. Lesson: an AI reviewer is only as good as the context it gets.

**Key takeaways from the demo:**

- AI is fast and tireless at pattern-type issues (security smells, common bugs, style).
- AI does not know your requirements unless they are written down where it can read them.
- AI comments still need a human to judge them: some are wrong, some are noise.
- Never merge because "the bot approved".

---

## 45–52 min · Wiring it into the workflow

**Recommended pipeline:**

```
push → CI (lint + tests) → AI review → human review → merge
```

**GitHub settings to show:**

- **Branch protection / rulesets** on `main`: require a PR, at least one approving review, and passing status checks
- **CODEOWNERS:** automatically request reviews from the people responsible for a path
- **Dismiss stale approvals** when new commits are pushed

**Discussion prompt:** AI review speeds up the first feedback loop, but research on large numbers of AI-assisted PRs also shows more review "smells" when AI is involved. Where is the balance between speed and quality in your team?

---

## 52–60 min · Q&A and takeaways

### Author checklist

- [ ] The PR does one thing and is small enough to review in one sitting
- [ ] Title and description explain what, why and how to test
- [ ] I reviewed my own diff in the GitHub UI
- [ ] Tests cover failure paths, not only the happy path
- [ ] No secrets, debug output or commented-out code

### Reviewer checklist

- [ ] I understand the requirement (I read the ticket)
- [ ] Correctness and edge cases first, style last
- [ ] Authorization and input validation checked
- [ ] Every comment is labeled (`blocking`, `nit`, …)
- [ ] I respond within one working day

---

## Facilitator preparation

- [ ] Push both branches to a fresh GitHub repository and open the demo PR
- [ ] Install and test the AI review app on that repository **a few days before** the call (pricing and free tiers in this space change often)
- [ ] Do a full dry run; AI output is not deterministic, so keep screenshots of a good run as a backup
- [ ] Prepare the "bad PR vs good PR" example for the hook
- [ ] Have the ticket text ready to reveal during the demo
