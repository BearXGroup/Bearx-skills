# Strip generated image metadata before posting

## Decide which accounts need a clean file

- Treat an account as no AI mark when the user ordered no AI mention or label for it.

- Check the account rule before you open the image file.

- Keep the generated original apart from the file you will post.

## Strip the metadata before posting

- Open the generated image and save a fresh copy as JPEG at quality 92 with PIL.

- Do not copy EXIF or other embedded metadata into the fresh copy.

- Save the clean copy under a new name and keep the original untouched for reference.

- Use the clean copy as the only file you hand to the posting step.

## Verify the clean file before publishing

- Read the clean file back and confirm it carries no EXIF and no C2PA signal.

- Publish only a file that passes that check.

- Read the live post back after publishing and confirm no AI label appears on it.

- When a live post still shows an AI label, stop and ask the user to confirm that exact post for deletion.

- Delete that post only after the user confirms it, and delete it through a browser task on instagram.com, because the Instagram connector cannot delete a post.

- Confirm the deletion by reading the live profile and confirming the post is gone before doing anything else.

- Check the published record for the account and day before reposting, and repost only when the record shows no live copy for that slot.

- Repost with a fresh clean copy and read the live post back to confirm no AI label appears.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing feed posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Generate the image without embedded signals when the generator offers that choice and still re-encode the result before posting.

- Keep a clean copy beside every generated original so a repost never falls back to the file that carries the signal.
