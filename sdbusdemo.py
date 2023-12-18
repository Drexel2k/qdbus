from sdbus import (DbusInterfaceCommonAsync, dbus_signal_async, sd_bus_open_system)

from asyncio import new_event_loop


service = "org.freedesktop.NetworkManager"
#service of qspotify, instance number changes on every launch of qspotify
#service="org.mpris.MediaPlayer2.spotifyd.instance7453"
path = "/org/freedesktop/NetworkManager"
#path="/org/mpris/MediaPlayer2"
iface = "org.freedesktop.DBus.Properties"

class DBusInterface(
    DbusInterfaceCommonAsync,
    interface_name=iface
):

    @dbus_signal_async(
        signal_signature='sa{sv}as'
    )
    def PropertiesChanged(self) -> (str, dict, list):
        pass


example_object = DBusInterface.new_proxy(service, path, bus=sd_bus_open_system())


async def dbuspropertieschange() -> None:
    # Use async for loop to print clock signals we receive
    async for x in example_object.PropertiesChanged:
        print(f'{x} ')

loop = new_event_loop()

# Always binds your tasks to a variable
task_clock = loop.create_task(dbuspropertieschange())

loop.run_forever()