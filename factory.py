import numpy as np
import logging


class Overlord:
    """ Decide how to Move Components to different Machines around the Factory """
    def __init__(self):
        pass


class FactoryJob:
    """ move a component to a machine """
    def __init__(self):
        self.to_make = None     #
        self.holding = None
        self.reward = None


class Factory:
    def __init__(self):
        self.layout = np.zeros([200, 100])  # 20m x 10m in 10cm squares
        self.movers = []
        self.machines = dict()
        self.inventory = dict()

    def add_machine(self, machine):
        # add to layout
        self.machines[machine.name] = machine
        logging.info(f'adding machine {machine.name}')

    def add_component(self, component):
        self.inventory[component.name] = component
        logging.info(f'adding component {component.name}')

    def add_mover(self, mover):
        self.movers.append(mover)

    def show(self):
        logging.info(f'len(self.machines) machines')
        logging.info(f'len(self.inventory) inventory')
        return self.layout


# class Mover:
#     """ Transport (Human, arms, conveyor, robot) """
#     def __init__(self):
#         self.arms = None


class Machine:
    def __init__(self, _name):
        self.name = _name
        self.dimensions = None
        self.backlog = []
        self.status = ""
        self.schedule = None

    def start(self):
        self.status = "Working"
        logging.info(f'starting machine {self.name}')

    def loop(self):
        while True:
            time.pause(1)

    def stop(self):
        self.status = "Idle"
        logging.info(f'stopping machine {self.name}')

    def make(self, inventory, name):
        # check recipe for machine
        if name not in inventory:
            logging.info(f'{name} not made by this machine')
            return None

        target = inventory[name]
        # check we have the parts needed in stock
        # for component in self.recipes[name].inputs:
        #     if component.amount > inventory[name].amount:
        #         logging.warning(f'Not enough {component.name} in stock to make {name}')
        #         return None

        # remove components from inventory
        # connect to and start machine
        # set status
        self.start()

    def check_status(self, name, inventory):
        # if machine has finished, set to idle and output component
        self.stop()
        inventory[name].amount += 1
        pass


class Component:
    def __init__(self, _name, inputs=None, machine=None):
        self.name = _name
        self.inputs = inputs
        self.machine = machine
        self.amount = None
        self.unit = None
