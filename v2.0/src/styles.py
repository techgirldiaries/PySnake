"""
PySnake v2.0 - Aesthetic Colour Palette and Styling
Modern, creative colour scheme for enhanced visual experience

Structure:
- Theme-dependent Game Colours (change with themes)
- Theme-dependent UI Colours (change with themes)
- Static Colours (never change)
- Utility Functions (gradients, effects)
- Theme Manager (dynamic theme switching)
"""

# SECTION 1: THEME-DEPENDENT GAME COLOURS
# These colours change when you switch themes (Press T in menu)
# ---------------------------------------------------------------------------

# Game Background
DEEP_SPACE = (15, 15, 35)           # Main game background

# Player Entities
PLAYER_PRIMARY = (0, 255, 150)      # Player snake colour (teal-green)
AI_PRIMARY = (255, 100, 255)        # AI snake colour (magenta-pink)

# Game Objects
FOOD_RED = (255, 50, 80)            # Food colour (bright red-pink)
GRID_LINE = (40, 40, 60)            # Grid lines on game board

# Power-ups (Game Objects)
POWERUP_SPEED = (255, 220, 0)       # Speed boost (golden yellow)
POWERUP_INVINCIBLE = (50, 200, 255) # Invincibility (sky blue)
POWERUP_MULTIPLIER = (200, 50, 255) # Score multiplier (purple-pink)

#  ---------------------------------------------------------------------------
# SECTION 2: THEME-DEPENDENT UI COLOURS
# These UI colours also change with themes for cohesive look
#  ---------------------------------------------------------------------------

# Text Colours
TEXT_PRIMARY = (240, 240, 255)      # Main text (off-white)
TEXT_SECONDARY = (180, 180, 200)    # Secondary text (light grey)
TEXT_HIGHLIGHT = (0, 255, 200)      # Highlighted text (cyan-green)

# Accent & Status
ELECTRIC_CYAN = (0, 255, 255)       # Accent colour (title, highlights)
SUCCESS_GREEN = (0, 255, 150)       # Success messages
ERROR_RED = (255, 80, 100)          # Error messages
WARNING_AMBER = (255, 190, 50)      # Warning messages

# Menu & UI Backgrounds
MENU_BACKGROUND = (20, 20, 40)      # Menu background
BUTTON_NORMAL = (60, 60, 100)       # Button default state
BUTTON_HOVER = (80, 80, 130)        # Button hover state
BUTTON_ACTIVE = (100, 100, 160)     # Button active/pressed state
BORDER_BRIGHT = (100, 100, 150)     # UI borders

#  ---------------------------------------------------------------------------
# SECTION 3: STATIC COLOURS
# These colours remain constant across all themes
#  ---------------------------------------------------------------------------

# Fundamental Colours
BLACK = (0, 0, 0)                   # Pure black
MIDNIGHT_BLUE = (25, 25, 50)        # Gradient colour
DARK_CHARCOAL = (30, 30, 40)        # Overlay backgrounds
OVERLAY_DARK = (10, 10, 20)         # Very dark overlay

# Static Accent Colours (for effects that shouldn't change)
NEON_PINK = (255, 20, 147)          # Hot pink accent
LIME_GREEN = (50, 255, 50)          # Bright lime
SUNSET_ORANGE = (255, 140, 0)       # Warm orange
PURPLE_HAZE = (148, 0, 211)         # Deep purple
INFO_BLUE = (100, 150, 255)         # Information colour

# Derived Colours (calculated from theme colours)
PLAYER_GLOW = (0, 200, 120)         # Player glow effect
AI_GLOW = (200, 50, 200)            # AI glow effect
FOOD_GLOW = (255, 100, 130)         # Food glow effect
BORDER_DIM = (50, 50, 70)           # Dim borders

# Transparency Values (alpha channels)
ALPHA_HEAVY = 200       # 78% opacity
ALPHA_MEDIUM = 128      # 50% opacity
ALPHA_LIGHT = 80        # 31% opacity
ALPHA_SUBTLE = 40       # 16% opacity

#  ---------------------------------------------------------------------------
# SECTION 4: UTILITY FUNCTIONS
# Helper functions for colour manipulation and gradients
#  ---------------------------------------------------------------------------

def create_gradient(colour1, colour2, steps):
    """Create a smooth gradient between two colours
    
    Args:
        colour1: Starting RGB tuple
        colour2: Ending RGB tuple
        steps: Number of gradient steps
        
    Returns:
        List of RGB tuples forming a gradient
    """
    return [
        tuple(
            int(colour1[i] + (colour2[i] - colour1[i]) * (j / (steps - 1)))
            for i in range(3)
        )
        for j in range(steps)
    ]


def get_glow_color(base_colour, intensity=0.5):
    """Get a glowing version of a colour by increasing brightness
    
    Args:
        base_colour: Base RGB tuple
        intensity: Glow intensity (0.0 to 1.0)
        
    Returns:
        Brighter RGB tuple
    """
    return tuple(min(255, int(c + (255 - c) * intensity)) for c in base_colour)


def get_dim_color(base_colour, factor=0.6):
    """Get a dimmer version of a colour
    
    Args:
        base_colour: Base RGB tuple
        factor: Dimming factor (0.0 = black, 1.0 = original)
        
    Returns:
        Dimmer RGB tuple
    """
    return tuple(int(c * factor) for c in base_colour)


def get_snake_segment_color(base_colour, segment_index, total_segments, invincible=False):
    """Get colour for a snake segment with fade effect from head to tail
    
    Args:
        base_colour: Snake's primary colour
        segment_index: Position in snake (0 = head)
        total_segments: Total length of snake
        invincible: Whether snake has invincibility power-up
        
    Returns:
        RGB tuple for this segment
    """
    if invincible:
        # Invincible: bright cyan pulse effect
        fade_factor = max(0.4, 1.0 - (segment_index / total_segments) * 0.6)
        return tuple(int(c * fade_factor + ELECTRIC_CYAN[i] * (1 - fade_factor)) 
                    for i, c in enumerate(base_colour))
    else:
        # Normal: fade from head to tail
        fade_factor = max(0.3, 1.0 - (segment_index / max(1, total_segments)) * 0.7)
        return tuple(int(c * fade_factor) for c in base_colour)


#  ---------------------------------------------------------------------------
# SECTION 5: PRE-CALCULATED GRADIENTS
# Commonly used gradients (recalculate when theme changes)
#  ---------------------------------------------------------------------------

# Background gradient (top to bottom)
BACKGROUND_GRADIENT = create_gradient(DEEP_SPACE, MIDNIGHT_BLUE, 10)

# Player snake gradient (head to tail)
PLAYER_GRADIENT = create_gradient(PLAYER_PRIMARY, PLAYER_GLOW, 20)

# AI snake gradient (head to tail)
AI_GRADIENT = create_gradient(AI_PRIMARY, AI_GLOW, 20)


#  ---------------------------------------------------------------------------
# SECTION 6: UI ELEMENT STYLE DEFINITIONS
# Complete style specifications for UI components
#  ---------------------------------------------------------------------------

# Button style definitions (uses theme colours dynamically)
BUTTON_STYLE = {
    'padding': 15,
    'border_radius': 8,
    'border_width': 2,
    'text_color': TEXT_PRIMARY,
    'bg_color': BUTTON_NORMAL,
    'hover_color': BUTTON_HOVER,
    'active_color': BUTTON_ACTIVE,
    'border_color': BORDER_BRIGHT
}

# Title style (uses theme accent colours)
TITLE_STYLE = {
    'color': ELECTRIC_CYAN,
    'shadow_color': NEON_PINK,        # Static pink shadow
    'shadow_offset': (3, 3)
}

# Score display style (uses player/AI colours from theme)
SCORE_STYLE = {
    'player_color': PLAYER_PRIMARY,
    'ai_color': AI_PRIMARY,
    'bg_color': (0, 0, 0, 180),      # Semi-transparent black
    'border_color': ELECTRIC_CYAN
}

# Pulsing effect colours for power-ups
PULSE_COLORS = {
    'speed': [POWERUP_SPEED, get_glow_color(POWERUP_SPEED, 0.3)],
    'invincible': [POWERUP_INVINCIBLE, get_glow_color(POWERUP_INVINCIBLE, 0.3)],
    'multiplier': [POWERUP_MULTIPLIER, get_glow_color(POWERUP_MULTIPLIER, 0.3)]
}

# Particle effect colours (static - always colourful)
PARTICLE_COLORS = [
    ELECTRIC_CYAN,
    NEON_PINK,
    LIME_GREEN,
    POWERUP_SPEED
]

#  ---------------------------------------------------------------------------
# SECTION 7: THEME MANAGER - DYNAMIC THEME SWITCHING
# Manages theme switching for BOTH game elements AND UI elements
# Press 'T' in main menu to cycle through themes
#  ---------------------------------------------------------------------------

class ThemeManager:
    """Manages dynamic theme switching with complete colour palettes
    
    Themes affect:
    - Game elements (snakes, food, power-ups, background, grid)
    - UI elements (text, buttons, menus, accents)
    - Gradients and effects are recalculated for new theme
    """
    
    def __init__(self):
        """Initialise theme manager with default Cyberpunk theme"""
        from config import Theme
        self.Theme = Theme
        self.current_theme = Theme.CYBERPUNK
        
        # Define all themes with COMPLETE colour palettes (game + UI)
        self.themes = {
            Theme.CYBERPUNK: {
                'name': 'Cyberpunk',
                # Game colours
                'background': (15, 15, 35),
                'player': (0, 255, 150),
                'ai': (255, 100, 255),
                'food': (255, 50, 80),
                'powerup_speed': (255, 220, 0),
                'powerup_invincible': (50, 200, 255),
                'powerup_multiplier': (200, 50, 255),
                'grid': (40, 40, 60),
                # UI colours
                'text_primary': (240, 240, 255),
                'text_secondary': (180, 180, 200),
                'text_highlight': (0, 255, 200),
                'accent': (0, 255, 255),
                'success': (0, 255, 150),
                'error': (255, 80, 100),
                'warning': (255, 190, 50),
                'menu_bg': (20, 20, 40),
                'button_normal': (60, 60, 100),
                'button_hover': (80, 80, 130),
                'button_active': (100, 100, 160),
                'border': (100, 100, 150)
            },
            Theme.RETRO: {
                'name': 'Retro Arcade',
                # Game colours
                'background': (0, 0, 0),
                'player': (0, 255, 0),
                'ai': (255, 0, 255),
                'food': (255, 0, 0),
                'powerup_speed': (255, 255, 0),
                'powerup_invincible': (0, 255, 255),
                'powerup_multiplier': (255, 128, 0),
                'grid': (30, 30, 30),
                # UI colours
                'text_primary': (255, 255, 255),
                'text_secondary': (200, 200, 200),
                'text_highlight': (255, 255, 0),
                'accent': (255, 255, 0),
                'success': (0, 255, 0),
                'error': (255, 0, 0),
                'warning': (255, 255, 0),
                'menu_bg': (10, 10, 10),
                'button_normal': (50, 50, 50),
                'button_hover': (80, 80, 80),
                'button_active': (110, 110, 110),
                'border': (150, 150, 150)
            },
            Theme.OCEAN: {
                'name': 'Ocean',
                # Game colours
                'background': (10, 30, 60),
                'player': (0, 200, 255),
                'ai': (255, 150, 50),
                'food': (255, 100, 200),
                'powerup_speed': (255, 215, 0),
                'powerup_invincible': (135, 206, 250),
                'powerup_multiplier': (147, 112, 219),
                'grid': (20, 50, 80),
                # UI colours
                'text_primary': (200, 240, 255),
                'text_secondary': (150, 200, 230),
                'text_highlight': (100, 255, 255),
                'accent': (100, 255, 255),
                'success': (0, 255, 200),
                'error': (255, 100, 150),
                'warning': (255, 200, 100),
                'menu_bg': (15, 40, 70),
                'button_normal': (40, 70, 110),
                'button_hover': (60, 90, 130),
                'button_active': (80, 110, 150),
                'border': (120, 180, 220)
            },
            Theme.FOREST: {
                'name': 'Forest',
                # Game colours
                'background': (15, 40, 25),
                'player': (100, 255, 100),
                'ai': (200, 100, 50),
                'food': (255, 50, 50),
                'powerup_speed': (200, 180, 50),
                'powerup_invincible': (100, 150, 200),
                'powerup_multiplier': (180, 150, 200),
                'grid': (30, 60, 40),
                # UI colours
                'text_primary': (220, 255, 220),
                'text_secondary': (180, 220, 180),
                'text_highlight': (150, 255, 150),
                'accent': (150, 255, 150),
                'success': (100, 255, 100),
                'error': (255, 100, 100),
                'warning': (200, 180, 50),
                'menu_bg': (20, 50, 30),
                'button_normal': (40, 80, 50),
                'button_hover': (60, 100, 70),
                'button_active': (80, 120, 90),
                'border': (120, 180, 140)
            }
        }
    
    def cycle_theme(self):
        """Cycle to the next theme in sequence"""
        themes_list = list(self.Theme)
        current_index = themes_list.index(self.current_theme)
        next_index = (current_index + 1) % len(themes_list)
        self.current_theme = themes_list[next_index]
        self.apply_theme()
    
    def set_theme(self, theme):
        """Set a specific theme by Theme enum value
        
        Args:
            theme: Theme enum value (e.g., Theme.CYBERPUNK)
        """
        if theme in self.themes:
            self.current_theme = theme
            self.apply_theme()
    
    def apply_theme(self):
        """Apply current theme to ALL global colour variables
        
        Updates both game colours AND UI colours for complete theme switching
        Also recalculates gradients and UI style definitions
        """
        global DEEP_SPACE, PLAYER_PRIMARY, AI_PRIMARY, FOOD_RED
        global POWERUP_SPEED, POWERUP_INVINCIBLE, POWERUP_MULTIPLIER, GRID_LINE
        global TEXT_PRIMARY, TEXT_SECONDARY, TEXT_HIGHLIGHT, ELECTRIC_CYAN
        global SUCCESS_GREEN, ERROR_RED, WARNING_AMBER
        global MENU_BACKGROUND, BUTTON_NORMAL, BUTTON_HOVER, BUTTON_ACTIVE, BORDER_BRIGHT
        global PLAYER_GLOW, AI_GLOW, FOOD_GLOW
        global BACKGROUND_GRADIENT, PLAYER_GRADIENT, AI_GRADIENT
        global BUTTON_STYLE, TITLE_STYLE, SCORE_STYLE, PULSE_COLORS
        
        palette = self.themes[self.current_theme]
        
        # Update game colours
        DEEP_SPACE = palette['background']
        PLAYER_PRIMARY = palette['player']
        AI_PRIMARY = palette['ai']
        FOOD_RED = palette['food']
        POWERUP_SPEED = palette['powerup_speed']
        POWERUP_INVINCIBLE = palette['powerup_invincible']
        POWERUP_MULTIPLIER = palette['powerup_multiplier']
        GRID_LINE = palette['grid']
        
        # Update UI colours
        TEXT_PRIMARY = palette['text_primary']
        TEXT_SECONDARY = palette['text_secondary']
        TEXT_HIGHLIGHT = palette['text_highlight']
        ELECTRIC_CYAN = palette['accent']
        SUCCESS_GREEN = palette['success']
        ERROR_RED = palette['error']
        WARNING_AMBER = palette['warning']
        MENU_BACKGROUND = palette['menu_bg']
        BUTTON_NORMAL = palette['button_normal']
        BUTTON_HOVER = palette['button_hover']
        BUTTON_ACTIVE = palette['button_active']
        BORDER_BRIGHT = palette['border']
        
        # Recalculate derived colours (glows)
        PLAYER_GLOW = get_dim_color(PLAYER_PRIMARY, 0.7)
        AI_GLOW = get_dim_color(AI_PRIMARY, 0.7)
        FOOD_GLOW = get_glow_color(FOOD_RED, 0.3)
        
        # Recalculate gradients
        BACKGROUND_GRADIENT = create_gradient(DEEP_SPACE, MIDNIGHT_BLUE, 10)
        PLAYER_GRADIENT = create_gradient(PLAYER_PRIMARY, PLAYER_GLOW, 20)
        AI_GRADIENT = create_gradient(AI_PRIMARY, AI_GLOW, 20)
        
        # Update UI style dictionaries
        BUTTON_STYLE.update({
            'text_color': TEXT_PRIMARY,
            'bg_color': BUTTON_NORMAL,
            'hover_color': BUTTON_HOVER,
            'active_color': BUTTON_ACTIVE,
            'border_color': BORDER_BRIGHT
        })
        
        TITLE_STYLE.update({
            'color': ELECTRIC_CYAN
        })
        
        SCORE_STYLE.update({
            'player_color': PLAYER_PRIMARY,
            'ai_color': AI_PRIMARY,
            'border_color': ELECTRIC_CYAN
        })
        
        # Update pulse colours for power-ups
        PULSE_COLORS.update({
            'speed': [POWERUP_SPEED, get_glow_color(POWERUP_SPEED, 0.3)],
            'invincible': [POWERUP_INVINCIBLE, get_glow_color(POWERUP_INVINCIBLE, 0.3)],
            'multiplier': [POWERUP_MULTIPLIER, get_glow_color(POWERUP_MULTIPLIER, 0.3)]
        })
    
    def get_theme_name(self):
        """Get the display name of the current theme
        
        Returns:
            String name of theme (e.g., 'Cyberpunk', 'Ocean')
        """
        return self.themes[self.current_theme]['name']
    
    def get_colours(self):
        """Get complete colour palette for current theme
        
        Returns:
            Dictionary with all colour values for current theme
        """
        return self.themes[self.current_theme]
    
    def get_theme_list(self):
        """Get list of all available theme names
        
        Returns:
            List of theme name strings
        """
        return [self.themes[theme]['name'] for theme in self.Theme]


#  ---------------------------------------------------------------------------
# CREATE GLOBAL THEME MANAGER INSTANCE
# Import this instance to access theme switching functionality
#  ---------------------------------------------------------------------------

theme_manager = ThemeManager()

