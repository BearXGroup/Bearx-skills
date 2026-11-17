# Browser account identity check

## Confirm the account before acting

- Open the own profile in the browser session before any post, delete, comment reply, verification claim, or account check.

- Read the handle shown in the profile interface and compare it character by character with the intended account for that task.

- Stop the action when the shown handle differs from the intended handle, even when the session looks usable and the task looks ready.

- Treat a login screen, a security challenge screen, or a start screen as no proof about the account, and report the exact screen instead of claiming the account is unavailable or that nothing needs doing.

- Verify the handle again after any reload, account list change, or session change, because a browser session can change accounts without warning.

## Switch accounts without losing a working session

- State what a switch would lose before leaving a working session, and keep a way back to that session when one exists.

- Switch only through the profile account list, and choose the saved entry for the intended account.

- Sign in with the saved login for the intended account only when that account is not already in the saved list.

- Open the own profile again after the switch and confirm the intended handle is now shown before acting.

- Stop the switch at a real block, such as a drag CAPTCHA, a passkey prompt, or a code on the phone of the user, and report that block with the intended and observed handles.

## Report identity exactly

- Report the intended handle and the observed handle for every browser publishing action, deletion, and verification claim.

- Report a result as not done when the intended account could not be entered, even when another account in the same session was available.

- Never post, delete, or claim a verification from an account that is not the intended account.

- Keep each destination separate in the report, because one destination can be correct while another destination used the wrong account.

- Correct the record when a wrong account action is found, and name the action that must be redone from the intended account.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing reels and checking the live post.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page video posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Use a platform connector instead of the browser when the connector can do the same action from a named account.

- Ask the user to complete a real block once, and queue the remaining account checks behind that single approval instead of repeating the same login attempt.

- Keep one intended account per routine step, so a later step cannot silently reuse the session left by an earlier step.
