#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Node based auto rigger
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from Qt.QtCore import *

from tpQtLib.core import base

from PyFlow.Core.GraphManager import GraphManagerSingleton
from PyFlow.UI.Widgets.BlueprintCanvas import BlueprintCanvasWidget

import tpRigToolkit


class RigNodeTool(tpRigToolkit.Tool, object):
    def __init__(self, config):
        super(RigNodeTool, self).__init__(config=config)

    def ui(self):
        super(RigNodeTool, self).ui()

        rig_node_widget = RigNodeWidget()
        self.main_layout.addWidget(rig_node_widget)


class RigNodeWidget(base.BaseWidget, object):

    newFileExecuted = Signal(bool)          # BlueprintCanvasWidget needs this signal to work
    fileBeenLoaded = Signal()               # BlueprintCanvasWidget needs this signal to work

    def __init__(self, parent=None):
        super(RigNodeWidget, self).__init__(parent=parent)

    def ui(self):
        super(RigNodeWidget, self).ui()

        self._graph_manager = GraphManagerSingleton()
        self._canvas_widget = BlueprintCanvasWidget(self._graph_manager.get(), self)
        self._canvas_widget.setObjectName('canvasWidget')

        self.main_layout.addWidget(self._canvas_widget)

    def onRequestFillProperties(self, properties_fill_delegate):
        """
        Implements onRequestFillProperties. This function MUST be implemented for PyFlow to work.
        :param properties_fill_delegate:
        """

        pass

    def onRequestClearProperties(self):
        """
        Implements onRequestClearProperties. This function MUST be implemented for PyFlow to work.
        :param properties_fill_delegate:
        """

        pass
