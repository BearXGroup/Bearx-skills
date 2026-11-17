# Publish once guard

## Check the day before creating

- Read the published record for the account and the day before creating or scheduling anything.

- Stop when the slot, the theme, or the same asset already appears in that record.

- Treat a missing record as a blocker and create the record first rather than guessing that nothing went out.

- Check the live profile when the record is unclear, because a scheduler dashboard can miss a copy that already went live.

## Register each post at once

- Register the account, the slot, the theme, the asset name, and the live link immediately after publication.

- Register a scheduled post at scheduling time with its scheduled time, and update the entry with the live link after it goes out.

- Keep one entry per account per slot per day, and let that entry be the lock that other routines read.

- Never create a one-off routine that overlaps a daily routine on the same day, and put a dated exception inside the daily routine instead.

## Handle retries without duplicating

- Look up the live post and the schedule before retrying any uncertain publish, because the first attempt may have succeeded.

- Never click publish again after an error without counting the scheduled and live entries first.

- Schedule through a scheduler instead of publishing now when the tool has duplicated on immediate publish, and audit the calendar for exactly one entry.

- Archive the extra copy promptly when two copies of the same post appear, and keep the copy recorded in the published record.

## Verify the real profile

- Read the live profile after publication and confirm exactly one copy of the post is present.

- Report a result as clean only after the live profile check, not from the scheduler view alone.

- Remove or archive a duplicate before reporting success, and correct the published record to the kept copy.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing reels and checking the live post.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Space slots by theme and account so parallel routines cannot claim the same theme on the same day.

- Use one daily routine per account per slot instead of adding a parallel catch-up routine.

- Hold a failed post for a later retry window instead of forcing it into another routine's slot.
