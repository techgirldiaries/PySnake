# Assets Folder

This folder is for optional game assets like sound effects and music.

## Sound Effects

The game looks for these sound files in the `sounds/` subfolder:

### Required Files (Optional)

- `eat.wav` - Sound when snake eats food
- `game_over.wav` - Sound when game ends
- `power_up.wav` - Sound when collecting power-ups

**Note**: The game works perfectly WITHOUT these files. They're completely optional!

## Where to Get Free Sound Effects

### Recommended Sites (All Free)

1. **Freesound.org** - <https://freesound.org/>
   - Search for: "eat", "bite", "game over", "power up", "arcade"
   - Large collection of CC-licensed sounds

2. **OpenGameArt.org** - <https://opengameart.org/>
   - Game-focused sound effects
   - Many retro/arcade sounds

3. **ZapSplat** - <https://www.zapsplat.com/>
   - Free for indie games
   - High quality sounds

4. **Mixkit** - <https://mixkit.co/free-sound-effects/>
   - Modern sound effects
   - No attribution required

## Tips for Choosing Sounds

### For `eat.wav`

- Keep it short (< 0.5 seconds)
- Something satisfying like "crunch", "chomp", "pop"
- Not too loud or jarring

### For `game_over.wav`

- 1-2 seconds max
- Descending tones or "buzzer" effects work well
- Should feel final but not too harsh

### For `power_up.wav`

- Bright, ascending tones
- 0.5-1 second duration
- Should feel rewarding and magical

## Format Requirements

- **Format**: WAV (`.wav`)
- **Sample Rate**: 44100 Hz recommended
- **Bit Depth**: 16-bit recommended
- **Channels**: Mono or Stereo both work

## Converting Audio Files

If you have MP3 or OGG files, convert them to WAV:

### Using Online Tools

- <https://cloudconvert.com/mp3-to-wav>
- <https://convertio.co/mp3-wav/>

### Using FFmpeg (Command Line)

```bash
ffmpeg -i input.mp3 output.wav
```

## Example Search Terms

When searching for sounds, try these keywords:

- "8-bit eat"
- "arcade bite"
- "retro game over"
- "pixel power up"
- "coin collect"
- "arcade beep"
- "game success"

## Testing Your Sounds

1. Place `.wav` files in `v2.0/assets/sounds/`
2. Run the game
3. Enable sounds in Settings (S from main menu)
4. Play to hear your sounds!

---

**Remember**: The game is fully functional without any sound files. Add them only if you want audio enhancement!
