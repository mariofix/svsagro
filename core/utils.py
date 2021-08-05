from django.apps import apps
from os.path import isfile


def get_menus() -> list:
    modulos = []
    for app in apps.get_app_configs():
        try:
            if app.is_module:
                app_menu = f"{app.name}/templates/{app.name}/menu.html"
                if isfile(app_menu):
                    modulos.append({"name": app.name, "menu": f"{app.name}/menu.html"})
        except AttributeError:
            pass

    return modulos
