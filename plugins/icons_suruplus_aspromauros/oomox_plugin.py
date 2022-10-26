# -*- coding: utf-8 -*-
import os

from oomox_gui.config import FALLBACK_COLOR
from oomox_gui.export_common import CommonIconThemeExportDialog
from oomox_gui.plugin_api import OomoxIconsPlugin
from oomox_gui.i18n import translate
from oomox_gui.color import mix_theme_colors


PLUGIN_DIR = os.path.dirname(os.path.realpath(__file__))


class SuruPlusIconsExportDialog(CommonIconThemeExportDialog):

    timeout = 300
    config_name = 'icons_suruplus_aspromauros'

    def do_export(self):
        export_path = os.path.expanduser(
            self.option_widgets[self.OPTIONS.DEFAULT_PATH].get_text()
        )

        self.command = [
            "bash",
            os.path.join(PLUGIN_DIR, "change_color.sh"),
            "-o", self.theme_name,
            "--destdir", export_path,
            self.temp_theme_path,
        ]
        super().do_export()


class Plugin(OomoxIconsPlugin):
    name = 'suruplus_aspromauros_icons'
    display_name = 'Suru++ Asprómauros'
    about_text = translate(
        'These aspromautic or monochromatic icons are based on '
        'Suru++ 30 Dark icons. It is flat, minimalist and designed '
        'for full dark environments.'
    )
    about_links = [
        {
            'name': translate('Homepage'),
            'url': 'https://github.com/gusbemacbe/suru-plus-aspromauros',
        },
    ]

    export_dialog = SuruPlusIconsExportDialog
    preview_svg_dir = os.path.join(PLUGIN_DIR, "icon_previews/")

    theme_model_icons = [
        {
            'key': 'ICONS_SYMBOLIC_ACTION',
            'type': 'color',
            'fallback_function': lambda colors: mix_theme_colors(
                colors['MENU_FG'], colors['BTN_FG'],
                0.66
            ),
            'display_name': translate('Actions Icons'),
            'value_filter': {
                'SURUPLUS_GRADIENT_ENABLED': False,
            },
        },
        {
            'key': 'ICONS_SYMBOLIC_PANEL',
            'type': 'color',
            'fallback_key': 'FG',
            'display_name': translate('Panel Icons'),
        },
        {
            'key': 'SURUPLUS_GRADIENT_ENABLED',
            'type': 'bool',
            'fallback_value': False,
            'reload_options': True,
            'display_name': translate('Enable Gradients'),
        },
        {
            'key': 'SURUPLUS_GRADIENT1',
            'type': 'color',
            'fallback_key': 'ICONS_SYMBOLIC_ACTION',
            'display_name': translate('Gradient Start Color'),
            'value_filter': {
                'SURUPLUS_GRADIENT_ENABLED': True,
            },
        },
        {
            'key': 'SURUPLUS_GRADIENT2',
            'type': 'color',
            'fallback_key': 'SEL_BG',
            'display_name': translate('Gradient End Color'),
            'value_filter': {
                'SURUPLUS_GRADIENT_ENABLED': True,
            },
        },
    ]

    def preview_transform_function(self, svg_template, colorscheme):
        icon_preview = svg_template.replace(
            "%SYMBOLIC_ACTION%", colorscheme["ICONS_SYMBOLIC_ACTION"] or FALLBACK_COLOR
        ).replace(
            "%SYMBOLIC_PANEL%", colorscheme["ICONS_SYMBOLIC_PANEL"] or FALLBACK_COLOR
        )
        if colorscheme['SURUPLUS_GRADIENT_ENABLED'] and 'arrongin' in svg_template:
            icon_preview = icon_preview.replace(
                "currentColor", "url(#arrongin)"
            ).replace(
                "%GRADIENT1%", colorscheme["SURUPLUS_GRADIENT1"] or FALLBACK_COLOR
            ).replace(
                "%GRADIENT2%", colorscheme["SURUPLUS_GRADIENT2"] or FALLBACK_COLOR
            )
        return icon_preview
