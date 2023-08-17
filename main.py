from factory import *


def add_basic_components(f):
    copper_plate = Component('copper_plate')
    iron_plate = Component('iron_plate')
    copper_cable = Component('copper_cable')
    electronic_circuit = Component('electronic_circuit', inputs=[{'iron_plate': 1, 'copper_cable': 3}],
                                   machine='assembly_table_1')
    f.add_component(copper_plate)
    f.add_component(iron_plate)
    f.add_component(copper_cable)
    f.add_component(electronic_circuit)
    pass


def add_basic_machines(f):
    assembly_table_1 = Machine('assembly_table_1')
    f.add_machine(assembly_table_1)
    pass


def create_basic_factory():
    logging.basicConfig(level=logging.INFO)
    f = Factory()
    add_basic_machines(f)
    add_basic_components(f)
    # make if components are in inventory
    assembly_table_1 = f.machines['assembly_table_1']
    assembly_table_1.make(f.inventory, 'electronic_circuit')
    return f


factory = create_basic_factory()
# todo: get rpi and create ros nodes for machines
# todo a user panel for monitoring & worker panel for working
# todo: mimic launch files on local pc? Need launch file from command line (powershell or bash)
