# PySnake v2.0 - Troubleshooting Guide 🔧

Comprehensive solutions for common issues and problems.

---

## 🚨 Installation Issues

### Python Not Found

**Problem**: `'python' is not recognised as an internal or external command`

**Solutions**:

1. Install Python 3.7+ from [python.org](https://www.python.org/)
2. During installation, check "Add Python to PATH"
3. Restart terminal/command prompt after installation
4. Try `python3` instead of `python` on macOS/Linux
5. Verify installation: `python --version`

### Pygame Installation Failed

**Problem**: `pip install pygame` fails or shows errors

**Solutions**:

**Windows**:

```bash
python -m pip install --upgrade pip
python -m pip install pygame
```

**macOS**:

```bash
pip3 install pygame
# If that fails, try:
brew install python3
pip3 install pygame
```

**Linux (Ubuntu/Debian)**:

```bash
sudo apt-get update
sudo apt-get install python3-pygame
# Or:
pip3 install pygame
```

### Requirements.txt Errors

**Problem**: `pip install -r requirements.txt` fails

**Solutions**:

1. Update pip: `python -m pip install --upgrade pip`
2. Install manually: `pip install pygame`
3. Check Python version: `python --version` (needs 3.7+)
4. Use virtual environment:

```bash
   python -m venv venv
# Windows:
   venv\Scripts\activate

# macOS/Linux:
   source venv/bin/activate
   pip install -r requirements.txt
```

## 🎮 Game Launch Issues

### Game Won't Start

**Problem**: Double-clicking or running `python play.py` does nothing

**Solutions**:

1. Open terminal/command prompt in `v2.0/` directory
2. Run: `python play.py`
3. Check for error messages in console
4. Verify you're in correct directory: `cd path/to/PySnake/v2.0`
5. Try: `python src/snake_pygame.py` as alternative

### Module Not Found Errors

**Problem**: `ModuleNotFoundError: No module named 'pygame'`

**Solution**:

```bash
pip install pygame
# Verify installation:
python -c "import pygame; print(pygame.version.ver)"
```

**Problem**: `ModuleNotFoundError: No module named 'config'`

**Solution**: You're running from wrong directory. Navigate to `v2.0/` folder:

```bash
cd path/to/PySnake/v2.0
python play.py
```

### Import Errors in src/

**Problem**: `ImportError: cannot import name 'X' from 'Y'`

**Solutions**:

1. Clear Python cache:

```bash
# Windows:
   cd v2.0
   Remove-Item -Recurse -Force src\__pycache__
   Remove-Item -Recurse -Force __pycache__

# macOS/Linux:
   cd v2.0
   rm -rf src/__pycache__
   rm -rf __pycache__
```

2. Restart Python interpreter

3. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

## 🖥️ Display Issues

### Window Too Small/Large

**Problem**: Game window doesn't fit screen properly

**Solutions**:

1. Game is designed for 800×600 resolution
2. Check monitor resolution: needs at least 800×600
3. Adjust Windows display scaling to 100%
4. Modify `config.py` to change window size (advanced)

### Graphics Glitching

**Problem**: Visual artifacts, flickering, or corrupted graphics

**Solutions**:

1. Update graphics drivers
2. Close other graphics-intensive applications
3. Try windowed mode instead of fullscreen
4. Reduce screen recording software if running
5. Update Pygame: `pip install --upgrade pygame`

### Black Screen on Launch

**Problem**: Window opens but stays black

**Solutions**:

1. Wait 5-10 seconds (first launch can be slow)
2. Press keys to ensure window is focused
3. Check GPU drivers are up to date
4. Try different Python version if using very old/new version
5. Reinstall Pygame: `pip uninstall pygame` then `pip install pygame`

## 🎵 Audio Issues

### No Sound Effects

**Problem**: Game runs but no audio plays

**Solution**: This is **completely normal**! Sound files are optional.

To **enable audio**:

1. Create `assets/sounds/` directory
2. Add `.wav` files:
   - `eat.wav` - Food collection sound
   - `game_over.wav` - Death sound
   - `power_up.wav` - Power-up collection sound
3. Restart game

**Free sound resources**:

- [Freesound.org](https://freesound.org/)
- [OpenGameArt.org](https://opengameart.org/)
- [ZapSplat](https://www.zapsplat.com/)

### Sound Is Corrupted/Distorted

**Problem**: Audio plays but sounds wrong

**Solutions**:

1. Ensure audio files are `.wav` format (not `.mp3` or `.ogg`)
2. Use 16-bit PCM WAV files
3. Sample rate should be 22050 Hz or 44100 Hz
4. File size should be under 1 MB each
5. Test files in media player before adding to game

## 🎮 Gameplay Issues

### Controls Not Responding

**Problem**: Arrow keys or WASD don't move snake

**Solutions**:

1. Click on game window to ensure it has focus
2. Check keyboard layout is standard (not Dvorak, etc.)
3. Try alternative keys (arrows if WASD doesn't work, vice versa)
4. Close other applications that might intercept keyboard
5. Restart game

### Snake Moves Too Fast/Slow

**Problem**: Speed doesn't feel right

**Solutions**:

1. Change difficulty in main menu (1=Easy, 2=Medium, 3=Hard)
2. Speed naturally increases as snake grows longer
3. Speed Boost power-up temporarily increases speed
4. Check system performance (close background apps)
5. Verify 60 FPS target is being met (check console output)

### Game Freezes/Crashes

**Problem**: Game stops responding or crashes unexpectedly

**Solutions**:

1. Check Python version: `python --version` (needs 3.7-3.11)
2. Update Pygame: `pip install --upgrade pygame`
3. Close other applications (free up RAM)
4. Check console for error messages
5. Restart computer if problem persists

### AI Snake Not Moving

**Problem**: In AI Opponent mode, AI snake doesn't move or behaves strangely

**Solutions**:

1. This is rare - usually indicates AI got trapped
2. Restart the game
3. Try different difficulty level
4. Report bug on GitHub if it persists

## 💾 Data Issues

### High Score Not Saving

**Problem**: High score resets when restarting game

**Solutions**:

1. Check write permissions in `v2.0/` directory
2. Verify `db/` folder exists (auto-created on first run)
3. Check `db/highscores.json` file exists
4. On Windows: Run as Administrator if permission errors
5. On macOS/Linux: Check file permissions:

```bash
   ls -la db/
   # Should show read/write permissions
```

### High Score File Corrupted

**Problem**: `Error loading high scores` message

**Solutions**:

1. Delete `db/highscores.json`
2. Game will recreate it on next run
3. Your high scores will reset (unavoidable)

**Alternative**: Manually repair JSON file:

```json
{
  "single_player": 0,
  "ai_opponent_player": 0,
  "ai_opponent_ai": 0
}
```

### Database Folder Missing

**Problem**: `db/` folder doesn't exist

**Solution**: Game creates it automatically on first run. If not:

```bash
# Windows:
   mkdir db

# macOS/Linux:
   mkdir db
```


## 🎨 Theme Issues

### Theme Not Changing

**Problem**: Pressing T doesn't switch themes

**Solutions**:

1. **Must be in main menu** (not in-game or settings)
2. Ensure you're pressing 'T' (not 't' if Caps Lock interferes)
3. Wait a moment after pressing - change should be immediate
4. Try restarting game if persists

### Theme Colors Look Wrong

**Problem**: Colors appear incorrect or washed out

**Solutions**:

1. Check monitor colour calibration
2. Adjust monitor brightness/contrast
3. Try different theme (Press T)
4. Update graphics drivers
5. Verify Pygame version: `pip show pygame`

## ⚡ Performance Issues

### Low Frame Rate / Lag

**Problem**: Game runs slowly or choppy

**Solutions**:

1. Close background applications
2. Update graphics drivers
3. Check CPU usage (Task Manager / Activity Monitor)
4. Reduce screen resolution
5. Disable screen recording software
6. Try Easy difficulty (fewer calculations)

### High CPU Usage

**Problem**: Game uses too much CPU

**Solutions**:

1. This is normal for Pygame (60 FPS rendering)
2. Close other applications
3. Reduce unnecessary system processes
4. On laptops: Ensure plugged into power
5. Check for system updates

## 🌐 Platform-Specific Issues

### Windows Issues

**Problem**: DLL errors or missing files

**Solutions**:

1. Install Visual C++ Redistributable
2. Update Windows
3. Install DirectX End-User Runtime
4. Reinstall Python and Pygame

### macOS Issues

**Problem**: "Python quit unexpectedly" error

**Solutions**:

1. Use Python from python.org (not system Python)
2. Grant accessibility permissions: System Preferences → Security & Privacy → Accessibility
3. Try: `pip3 install --upgrade pygame`

### Linux Issues

**Problem**: SDL/graphics library errors

**Solutions**:

```bash
# Ubuntu/Debian:
   sudo apt-get install python3-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev

# Fedora:
   sudo dnf install python3-devel SDL2-devel SDL2_image-devel SDL2_mixer-devel SDL2_ttf-devel
```

## 🔍 Debug Mode

### Enable Debug Output

To see detailed error messages:

**Option 1**: Run from terminal

```bash
   cd v2.0
   python play.py
```

Watch console for error messages.

**Option 2**: Check Python exceptions
Add to `src/game.py` in `__main__` section:

```python
import traceback
try:
    # existing code
except Exception as e:
    traceback.print_exc()
    input("Press Enter to exit...")
```

## 📝 Reporting Bugs

If none of these solutions work:

### Before Reporting

1. Check console for error messages
2. Note exactly what you did before error occurred
3. Test with fresh installation
4. Check if others have the same issue on GitHub

### Report on GitHub

Include:

- Python version: `python --version`
- Pygame version: `pip show pygame`
- Operating system and version
- Exact error message (full traceback)
- Steps to reproduce the issue
- Screenshots if relevant

**GitHub Issues**: [github.com/techgirldiaries/PySnake/issues](https://github.com/techgirldiaries/PySnake/issues)

## 🆘 Still Need Help?

1. Check [README.md](README.md) for basic setup
2. Read [docs/QUICKSTART.md](docs/QUICKSTART.md) for detailed installation
3. Review [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for technical details
4. Search GitHub Issues for similar problems
5. Create new issue on GitHub with details

---

**Most issues are solved by ensuring Pygame is installed correctly!**

```bash
pip install pygame
python play.py
```

Good luck! 🐍🎮
