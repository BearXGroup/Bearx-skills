# Check public post text for leaked narration script

## Scan the final public text

- Read the exact final caption description and post text before any publish step.

- Search the text for speaker labels at the start of a line.

- Search for repeated speaker names and for internal narration markers and for long passages copied word for word from a narration script.

- Treat a narration script file as an internal production file and never treat it as a ready caption.

- Flag the text when any speaker label appears or when the text reads like a spoken script rather than a short public caption.

## Rewrite a leaked text

- Stop the publish step when the scan flags the text and do not publish a flagged version to meet a schedule.

- Write a new caption from a short topic summary and keep it separate from the script wording.

- Keep the new caption short and public facing and remove every speaker name that came from the script.

- Show the rewritten text for approval before publishing when approval is part of the workflow.

## Verify before publishing

- Scan the rewritten text again with the same checks before publishing.

- Publish only the version that passes the clean scan.

- Read the live post back after publishing and confirm that no speaker label or script passage reached the public post.

- Remove or correct a live post that still carries a leak and publish the clean version only after it passes the scan again.

## Available connectors

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page posts and checking the live post.

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing feed posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Draft the caption from the topic and the hook before opening the script file so the script cannot become the caption by default.

- Keep narration scripts and public captions in separate files and never copy a whole script file into a caption field.
