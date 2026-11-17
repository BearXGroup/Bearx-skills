# Popular pronunciation in narration

## Find the terms that TTS reads wrong

- Scan the narration script before generating audio and mark every technical term, acronym, foreign word, and proper name whose written form can mislead the voice.

- Find the popular spoken form for each marked term in the reference video or material the user named, or ask the user for it when no reference names it.

- Never guess a popular form, and never let the voice read a marked term as written when the popular form is known to differ.

## Respell the TTS input and listen

- Put the respelled form only in the text file you send to the voice tool, and keep the correct written form in the on-screen text, the captions, and the published script.

- Generate the audio with `python3 ~/workspace/custom-connectors/custom.elevenlabs/bin/elevenlabs.py say <voice_id> <text-file> <output.mp3>` and the CA bundle from the ElevenLabs connector doc.

- Listen to every respelled term in the finished audio before announcing the video ready.

- Fix the respelling and regenerate when the voice still says the written form, and repeat the listen check until the popular form is heard.

- Save each working respelling beside the script so the next video in the same series reuses it instead of rediscovering it.

- Keep a word-for-word reading exact and tell the user when a term may sound wrong instead of respelling it.

## Use the spelling the user gave aloud

- When the user spells a name letter by letter, use exactly that spelling in every later message, file name, title, caption, and TTS input.

- When dictation or a transcript shows a lookalike word for a name the user already spelled, check it against the spelled form before using it anywhere.

- Correct every earlier use once the right spelling is known, including file names and TTS inputs that already carry the wrong form.

## Available connectors

- [ElevenLabs](~/workspace/custom-connectors/custom.elevenlabs/CONNECTOR.md) for generating narration with the chosen voice.

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Keep one respelling list per series so the same term is spoken the same way in every episode.

- When a term has no settled popular form, use the written form and tell the user instead of inventing a pronunciation.
