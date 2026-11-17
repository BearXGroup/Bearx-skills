# Instagram rate limit queue

## Recognise a rate limit and stop retrying

- Treat a 429 response as a daily limit on Instagram, not as a failed post on every destination.

- Read the error output to confirm the 429, because the digits can also appear inside normal output such as profile identifiers and picture addresses.

- Stop retrying Instagram at once when the limit appears, because immediate retries can extend the limit and waste the remaining allowance.

- Leave any destination that already went live untouched, and do not delete it or post it again.

## Queue the pending destination only

- Record the pending item at once with the account, the slot, the asset name, the caption, and the destination that failed.

- Record separately the destination that already succeeded, so a later routine can see that part is done.

- Keep one pending entry per account per slot per day, and let that entry be the lock that other routines read before creating a replacement.

- Report the item as pending on Instagram and live on the other destination, not as failed or as not done.

## Repost after the reset and verify

- Wait until the limit resets before touching the pending item again, and do not move it into another routine slot in the meantime.

- Repost only to Instagram when the reset has passed, using the recorded asset and caption without changes unless the user approved a change.

- Read the live Instagram profile after the repost and confirm exactly one copy of the post is present.

- Register the live link in the pending entry at once, and close the entry only after that live profile check.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing reels and checking the live post.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Space Instagram slots through the day so one limit does not block several posts at once.

- Hold a failed post for a later retry window instead of forcing it into another routine slot.

- Use a scheduler entry for the pending repost so the retry is visible before the reset passes.
