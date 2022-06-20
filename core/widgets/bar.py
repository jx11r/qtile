from importlib import import_module

BAR: str = 'rounded'

def config() -> tuple[list, dict]:
    try:
        module = import_module(f'core.widgets.{BAR}')
        module.bar.update(
            { 'widgets': module.widgets }
        )
    except ImportError:
        return [], {}

    return module.tags, module.bar
