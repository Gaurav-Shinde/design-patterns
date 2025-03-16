'''
Command Behavioral Pattern: encapsultates requests as objects for added business logic and multiple requests handling

Components:
- client
- invoker/sender
- reciever
- command and its implementation commands

Problem it solves:
If you are designing a text editor, having all command logic tied to a copy button subclass is bad for reuse.
Now if copying through other means, have to use copy button.
Instead adding another layer for business logic, being copy command, can be reused by other copying ways.
This abstraction layer with business logic is what command pattern adds.

Pros:
- SRP - decouple invoker and command objects
- OCP - create more commands to call since decoupled
- 
Cons:
- increase complexity by adding abstraction layer between 
- too many classes for each command

Usecases:
- queueing tasks, tracking operations history
- alternative for callbacks for parameterizing objects

Example:
You have a Smart devices controller for your home. 
You want to create a program that will queue each operation for each device.
But you want to have different business logic for each command too.
You decide to use the command pattern for program behavior structuring.
invoker: controller
abstraction layer: command classes (business logic)
reciever: smart devices operations

Output:
Home thermostat is at 70 degrees Farenheit
Home thermostat was 70 and current is set to 60 degrees Farenheit
kitchen_light light is turned off
bedroom_light light is turned on
Home thermostat is at 60 degrees Farenheit
'''
from abc import ABC, abstractmethod
import logging

# Light Device
class LightDevice:
    def __init__(self,name):
        self.name=name
    def turn_on(self):
        print(f"{self.name} light is turned on")
    def turn_off(self):
        print(f"{self.name} light is turned off")
        
# Thermostat Device
class ThermostatDevice:
    def __init__(self):
        self.temperature=70
    def get_thermostat(self):
        print(f"Home thermostat is at {self.temperature} degrees Farenheit")
    def set_thermostat(self,temperature):
        old_temperature = self.temperature
        self.temperature = temperature
        print(f"Home thermostat was {old_temperature} and current is set to {self.temperature} degrees Farenheit")

# Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    
# turn on light command
class TurnOnLightCommand(Command):
    def __init__(self,light: LightDevice):
        self.light = light
    def execute(self):
        self.light.turn_on()
        
# turn off light command
class TurnOffLightCommand(Command):
    def __init__(self, light: LightDevice):
        self.light = light
    def execute(self):
        self.light.turn_off()
        
# set thermostat command
class SetThermostatCommand(Command):
    def __init__(self, thermostat:ThermostatDevice, temperature: int):
        self.thermostat = thermostat
        self.temperature = temperature
    def execute(self):
        self.thermostat.set_thermostat(self.temperature)
# get thermostat command
class GetThermostatCommand(Command):
    def __init__(self, thermostat:ThermostatDevice):
        self.thermostat = thermostat
    def execute(self):
        self.thermostat.get_thermostat()

# remote controller for smart devices
class RemoteController:
    def __init__(self):
        self.commands_queue = []
    def append_command(self,command: Command):
        self.commands_queue.append(command)
    def execute_commands(self):
        for command in self.commands_queue:
            command.execute()
        self.commands_queue.clear()

# client code
def client_code():
    # devices
    kitchen_light = LightDevice("kitchen_light")
    bedroom_light = LightDevice("bedroom_light")
    thermostat = ThermostatDevice()
    # commands
    turn_off_kitchen_light = TurnOffLightCommand(kitchen_light)
    turn_on_bedroom_light = TurnOnLightCommand(bedroom_light)
    get_thermostat_temp = GetThermostatCommand(thermostat)
    set_thermostat_temp = SetThermostatCommand(thermostat,60)
    # controller
    remote_controller = RemoteController()
    
    # add commands to queue
    remote_controller.append_command(get_thermostat_temp)
    remote_controller.append_command(set_thermostat_temp)
    remote_controller.append_command(turn_off_kitchen_light)
    remote_controller.append_command(turn_on_bedroom_light)
    remote_controller.append_command(get_thermostat_temp)
    
    # execute commands
    remote_controller.execute_commands()
    
if __name__ == "__main__":
    client_code()
    
