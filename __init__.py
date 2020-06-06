# -*- coding: utf-8 -*-
import logging
from . import controllers, models
from odoo import api, SUPERUSER_ID


_logger = logging.getLogger(__name__)
_handler = logging.FileHandler('/Users/tamnguyen/Programming/Odoo/local/log')
_logger.addHandler(_handler)


def _register_hook(cr, registry):
    _logger.info("-------CONFIGURING THE APPLICATION-----------")
    config_data = {
        'group_discount_per_so_line': True,
        'group_warning_account': True,
    }
    env = api.Environment(cr, SUPERUSER_ID,{})
    config_rec = env['res.config.settings'].create(config_data)
    config_rec.execute()
    _logger.info("-------END CONFIGURATION----------------------")

