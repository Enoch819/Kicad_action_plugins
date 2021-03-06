#  action_net2net_min_distance.py
#
# Copyright (C) 2018 Mitja Nemec
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import wx
import pcbnew
import net2net_distance
import logging
import os
import sys

SCALE = 1000000.0


class Net2NedDistance(pcbnew.ActionPlugin):
    """
    A script to delete selection
    How to use:
    - move to GAL
    - select two pads
    - call the plugin
    """

    def defaults(self):
        self.name = "Net2Net distance"
        self.category = "Measure distance"
        self.description = "Measure minimum distance between two selected nets"

    def Run(self):
        # load board
        board = pcbnew.GetBoard()

        # get user units
        if pcbnew.GetUserUnits() == 1:
            user_units = 'mm'
        else:
            user_units = 'in'

        # go to the project folder - so that log will be in proper place
        os.chdir(os.path.dirname(os.path.abspath(board.GetFileName())))

        # set up logger
        logging.basicConfig(level=logging.DEBUG,
                            filename="net2et distance.log",
                            filemode='w',
                            format='%(asctime)s %(name)s %(lineno)d:%(message)s',
                            datefmt='%m-%d %H:%M:%S',
                            disable_existing_loggers=False)
        logger = logging.getLogger(__name__)
        logger.info("Action plugin Net2net distance started")

        stdout_logger = logging.getLogger('STDOUT')
        sl_out = StreamToLogger(stdout_logger, logging.INFO)
        sys.stdout = sl_out

        stderr_logger = logging.getLogger('STDERR')
        sl_err = StreamToLogger(stderr_logger, logging.ERROR)
        sys.stderr = sl_err

        _pcbnew_frame = \
            filter(lambda w: w.GetTitle().lower().startswith('pcbnew'),
                   wx.GetTopLevelWindows()
                   )[0]

        # get all pads
        modules = board.GetModules()

        pads = []
        for mod in modules:
            # get their pads
            module_pads = mod.PadsList()
            # get net
            for pad in module_pads:
                pads.append(pad)

        # get list of all selected pads
        selected_pads = []
        for pad in pads:
            if pad.IsSelected():
                selected_pads.append(pad)

        # check the nets on all the pads
        nets = []
        for pad in selected_pads:
            nets.append(pad.GetNetname())

        # if two pads are selected
        if len(selected_pads) != 2:
            # if more or less than one show only a messagebox
            caption = 'Net2Net Distance'
            message = "You have to select two and only two pads"
            dlg = wx.MessageDialog(_pcbnew_frame, message, caption, wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy()
            return

        # and if they are on the same net
        if nets[0] == nets[1]:
            caption = 'Net2Net Distance'
            message = "The selected pads are on the same net"
            dlg = wx.MessageDialog(_pcbnew_frame, message, caption, wx.OK | wx.ICON_INFORMATION)
            dlg.ShowModal()
            dlg.Destroy() 
            return

        try:
            dis, loc = net2net_distance.get_min_distance(board, selected_pads[0], selected_pads[1])
        except Exception:
            logger.exception("Fatal error when replicating")
            raise

        caption = 'Net2Net Track Distance'
        if user_units == 'mm':
            message = "Distance between pads is " + "%.3f" % (dis/SCALE) + " mm"
        else:
            message = "Distance between pads is " + "%.4f" % (dis/(SCALE*25.4)) + " in"
        dlg = wx.MessageDialog(_pcbnew_frame, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()


class StreamToLogger(object):
    """
    Fake file-like stream object that redirects writes to a logger instance.
    """
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())