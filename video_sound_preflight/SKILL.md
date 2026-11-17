# Video sound preflight

## Probe the final file

- Probe the final video file for an audio stream before starting any posting step.

- Check for audible sound at the beginning, at the middle, and at the end of the file.

- Reject a file with no audio stream, a muted track, or no audible sound in those checks.

- Treat a script, a caption, or a plan to add music inside an app as no evidence of sound in the file.

- Probe the file again after any edit, export, or format change, because a new export can drop the track.

## Fix a silent file before posting

- Keep a silent file out of every posting queue until a fixed file passes the probe.

- Embed narration or music into the video file itself when posting from a computer, because platform music cannot be relied on to attach during computer posting.

- Keep music audible under any narration, without replacing the narration.

- Delay publication rather than posting a silent file to meet a schedule, and fix the file first.

## Post and verify each destination

- Post only the file that passed the probe, and track each destination separately.

- Verify each live post after publication, and stop the remaining destinations when one destination goes out silent.

- Replace or remove a silent live post promptly, then post the fixed file only after it passes the probe again.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing reels and checking the live post.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page video posts and checking the live post.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

### When available

- These connectors depend on the user's channel or devices. `muse.connector_search` shows which ones this session has.

- [Upload-Post](/opt/hatch/connectors/upload_post_mcp/CONNECTOR.md) for publishing one video across several networks including TikTok.

## Wrong-audio gate — run before EVERY social upload (Xavier's rule, 2026-11-02)

A file can have sound and still carry the WRONG sound. On 2026-11-02 six Facebook reels went up with the FORTE bulletin narration mixed under Xavier's real voice, because a shared working slot (`remotion-app/public/audio.mp3` — a narration file) was reused as a "music bed". The page lost views over it. Never again:

- Run `qa_audio_gate.py` (this folder) on the FINAL file before any upload:
  `python3 qa_audio_gate.py FINAL.mp4 --expect <the approved source/narration audio> --block <recent narrations/other productions' audio files or folder>`
- The gate checks: audible sound at start/middle/end; identity correlation ≥ 0.90 with the expected audio; contamination correlation < 0.05 against every blocked file. Any FAIL = do not upload; fix and re-run.
- NEVER use a shared project slot file (anything like `public/audio.mp3`) as a music bed or source for another production. Music beds come only from a dedicated music library of verified instrumental files.
- For narrated videos, the whisper-vs-script transcript check stays mandatory as well — the gate proves the audio is the right file, the transcript proves the right words.

## Alternatives for better results

- Add spoken narration when the video has a message to deliver, because narration gives the sound a clear purpose.

- Choose a music track before editing, so the edit is built around sound rather than added at the end.

- Ask for a new export with sound when a delivered file arrives silent, rather than trying to repair a post after publication.
