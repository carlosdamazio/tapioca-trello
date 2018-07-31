# -*- coding: utf-8 -*-

from .action import ACTION_MAPPING
from .batch import BATCH_MAPPING
from .board import BOARD_MAPPING
from .card import CARD_MAPPING
from .checklist import CHECKLIST_MAPPING

RESOURCE_MAPPING = {}
RESOURCE_MAPPING.update(ACTION_MAPPING)
RESOURCE_MAPPING.update(BATCH_MAPPING)
RESOURCE_MAPPING.update(BOARD_MAPPING)
RESOURCE_MAPPING.update(CARD_MAPPING)
RESOURCE_MAPPING.update(CHECKLIST_MAPPING)
