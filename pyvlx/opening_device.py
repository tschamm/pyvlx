"""Module for window openers."""
from .node import Node
from .command_send import CommandSend
from .position import Position
from .exception import PyVLXException


class OpeningDevice(Node):
    """Meta class for opening device with one main parameter for position."""

    async def set_position_percent(self, position_percent):
        """Set window to desired position."""
        command_send = CommandSend(pyvlx=self.pyvlx, node_id=self.node_id, position=Position(position_percent=position_percent))
        await command_send.do_api_call()
        if not command_send.success:
            raise PyVLXException("Unable to send command")

    async def open(self):
        """Open window."""
        await self.set_position_percent(0)

    async def close(self):
        """Close window."""
        await self.set_position_percent(100)


class Window(OpeningDevice):
    """Window object."""

    # pylint: disable=too-many-arguments
    def __init__(self, pyvlx, node_id, name, rain_sensor=False):
        """Initialize Window class."""
        super().__init__(pyvlx=pyvlx, node_id=node_id, name=name)
        self.rain_sensor = rain_sensor

    def __str__(self):
        """Return object as readable string."""
        return '<{} name="{}" ' \
            'node_id="{}" rain_sensor={}/>' \
            .format(
                type(self).__name__,
                self.name,
                self.node_id, self.rain_sensor)


class Blind(OpeningDevice):
    """Blind objects."""

    pass


class RollerShutter(OpeningDevice):
    """RollerShutter object."""

    pass