# Verify before claiming

## Check the source first

- Open the policy, account page, file, live record, or tool result that holds the fact before you state it.

- Read the exact field that answers the question, such as the account number, the insured name, the file type, or the download state, instead of relying on a file name or a remembered summary.

- Treat a request, a plan, and an instruction as unconfirmed until the source record shows the result.

- Ask the user for the missing source when no record can be opened, and say plainly that the fact is still unconfirmed.

## Report status only after confirmation

- Say a task is done only after the link, the live profile, the file, or the tool result confirms it.

- Say a job is running only after the tool confirms it started, and name what confirmed it in the same message.

- Use the words pending, attempted, or unconfirmed when the check has not finished, and never upgrade those words to done or running.

- Keep one claim per check, so a confirmed part never carries an unconfirmed part with it.

## Correct a reversed claim at once

- State the correction in the next message when a check reverses an earlier claim, and name the fact that was wrong and the fact that replaces it.

- Update the record, the list, or the sheet that carried the wrong fact in the same move, so a later task does not reuse it.

- Do not restate the old claim while correcting it, and do not soften the correction into a new guess.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Read the source twice when two records disagree, and report the disagreement instead of picking one record silently.

- Break a broad question into one check per fact, so each answer has its own source.

- Pause a chain of dependent tasks when the first check fails, and resume only after the corrected fact is confirmed.
