from lib_inpaint_background.globals import BackgroundGlobals
from lib_inpaint_background.webui_callbacks import setup_script_callbacks


setup_script_callbacks(BackgroundGlobals.is_extension_enabled)