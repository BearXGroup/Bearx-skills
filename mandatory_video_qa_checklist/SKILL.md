# Mandatory video QA checklist

## Check audio with numbers

- Run the audio gate on the final file before any upload with `python3 ~/workspace/custom-skills/video_sound_preflight/qa_audio_gate.py <final> --expect <approved audio> --block <recent narrations>`.

- Require identity of at least 0.90 with the expected audio and contamination below 0.05 against blocked audio and audible sound at the start and in the middle and at the end.

- Measure pause noise in the final mix and compare it with the pure narration.

- Reject the file when pauses sit above minus 55 dB RMS or when the mix carries clearly more high frequency energy above 10 kHz than the pure narration.

- Check that the voice starts at least 0.45 seconds after the video starts while movement is already running.

- Use only a verified instrumental library track and never use narration or a shared project slot file as a music bed.

- Keep music at 8 percent or less under narration, with 8 to 10 percent allowed for La Fora BR.

- Rotate the track on every video and repeat a track only after about one week.

- Compare a whisper transcript of the final audio with the script and reject any large divergence.

## Check editing direction and density

- Sample frames across the whole video and confirm that no stretch passes 8 seconds with the same still image or scene.

- Count distinct visual elements and require at least 6 elements in a Short of about 55 seconds, with 7 to 9 elements as the ideal.

- Use real photos or images of the theme as the dominant visual and reject any long stretch that is only text slides.

- Apply HDR to SDR tone mapping to iPhone HDR footage before any other filter and check that skin and colors stay natural.

- Confirm that karaoke captions never cover text in graphic scenes and that large words fit the width with margin.

## Check SEO and hook

- Research what is trending in the niche before locking the theme and never choose a theme by guesswork.

- Put the main keyword at the start of the title with a benefit or curiosity and keep the title within 100 characters on YouTube.

- Put the keyword in the first lines of the description, list sources by name only with no links, put hashtags at the end, and prepare tags for the Studio.

- Use a short description of up to 70 characters with at most 4 hashtags and no closing slogan for FORTE packages that Alexandre uploads.

- Open with a direct pain or question in the first sentence and let every line imply that the next line matters more.

- Show a strong moving photo of the pain in the first frame with no logo or intro before it.

- Put large hook text on screen from the first second and state clearly what comes next.

- Close with an opinion or experience question and pin that question as the first comment on YouTube, with a different question for each video.

## Check the thumbnail and the live post

- Make one impactful thumbnail per video with a strong theme image and large legible text on a phone screen.

- Never repeat a background between videos or between parts of one episode.

- Apply the thumbnail as the custom thumbnail and check it live after publishing.

- Report the measured result for all five blocks and attach the finished file when you announce a video as ready.

- Treat any failed block as a stop, fix the file, and run the full checklist again before uploading.

## Available connectors

- [Instagram](/opt/hatch/connectors/instagram/CONNECTOR.md) for publishing reels and checking the live post.

- [Facebook](/opt/hatch/connectors/facebook_cli/CONNECTOR.md) for publishing Page video posts and checking the live post.

- [vidIQ](/opt/hatch/connectors/vidiq_mcp/CONNECTOR.md) for researching YouTube keywords, trends, and retention.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Rebuild with a clean library track instead of trying to remove hiss from an uploaded video, because YouTube cannot swap the file and its editor cannot remove hiss.

- Publish the corrected version as a new upload when the defective version already went live, and add new information so the new upload stands as a different video.

- Prefer real photos from the day over extra slides when a long video starts to feel slide heavy.
