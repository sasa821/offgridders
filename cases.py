'''
Overlying script for tool for the analysis of possible
operational modes of micro grids interconnecting with an unreliable national grid
'''

import os
import pandas

from oemof.tools import logger
import logging
# Logging
#logger.define_logging(logfile='main_tool.log',
#                      screen_level=logging.INFO,
#                      file_level=logging.DEBUG)

from oemof_functions import generatemodel

class cases():
    ###############################################################################
    # Basecase
    ###############################################################################
    def base(demand_profile, pv_generation):
        '''
        Case: micro grid with fixed capacities = dispatch analysis

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        from config import allow_shortage
        case_name = "mg_fix"
        micro_grid_system = generatemodel.initialize_model()
        generatemodel.textblock_fix()
        micro_grid_system, bus_fuel, bus_electricity_mg = generatemodel.bus_basic(micro_grid_system)
        micro_grid_system, bus_fuel = generatemodel.fuel(micro_grid_system, bus_fuel)
        if allow_shortage == True: micro_grid_system = generatemodel.shortage(micro_grid_system, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.demand(micro_grid_system, bus_electricity_mg, demand_profile)
        micro_grid_system, bus_electricity_mg = generatemodel.excess(micro_grid_system, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.pv_fix(micro_grid_system, bus_electricity_mg, pv_generation)
        micro_grid_system, bus_fuel, bus_electricity_mg = generatemodel.transformer_fix(micro_grid_system, bus_fuel, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.storage_fix(micro_grid_system, bus_electricity_mg)
        micro_grid_system = generatemodel.simulate(micro_grid_system)
        generatemodel.store_results(micro_grid_system, case_name)
        #micro_grid_system = generatemodel.load_results()
        generatemodel.process(micro_grid_system, case_name, get_el_bus=False)
        logging.info(' ')
        return logging.debug('            Simulation of case "base" complete.')

    ###############################################################################
    # Optimization of off-grid micro grid
    ###############################################################################

    def mg_oem(demand_profile, pv_generation):
        '''
        Case: micro grid with variable capacities = OEM

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     var cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     var cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     var cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        from config import allow_shortage
        case_name = "mg_oem"
        micro_grid_system = generatemodel.initialize_model()
        generatemodel.textblock_oem()
        micro_grid_system, bus_fuel, bus_electricity_mg = generatemodel.bus_basic(micro_grid_system)
        micro_grid_system, bus_fuel = generatemodel.fuel(micro_grid_system, bus_fuel)
        if allow_shortage == True: micro_grid_system, bus_electricity_mg = generatemodel.shortage(micro_grid_system, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.demand(micro_grid_system, bus_electricity_mg, demand_profile)
        micro_grid_system, bus_electricity_mg = generatemodel.excess(micro_grid_system, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.pv_oem(micro_grid_system, bus_electricity_mg, pv_generation)
        micro_grid_system, bus_fuel, bus_electricity_mg = generatemodel.transformer_oem(micro_grid_system, bus_fuel, bus_electricity_mg)
        micro_grid_system, bus_electricity_mg = generatemodel.storage_oem(micro_grid_system, bus_electricity_mg)
        micro_grid_system = generatemodel.simulate(micro_grid_system)
        generatemodel.store_results(micro_grid_system, case_name)
        #micro_grid_system = generatemodel.load_results()
        electricity_bus = generatemodel.process(micro_grid_system, case_name, get_el_bus=True)
        oem_results = generatemodel.process_oem(electricity_bus, case_name)
        logging.info(' ')
        return oem_results

    ###############################################################################
    # Dispatch with MG as sunk costs
    ###############################################################################
    def buyoff():
        '''
        Case: Buyoff of micro grid with fixed capacities after x years = dispatch analysis for evaluation of costs p.a????

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        logging.debug('            Simulation of case "buyoff" complete.')
        return

    ###############################################################################
    # Dispatch at parallel operation (mg as backup)
    ###############################################################################
    def parallel():
        '''
        Case: micro grid parallel operation with grid extension ... how? another bus for grid electricity, and consumers
        or algorithms decide, which supply is chosen? or 50% of consumers stay with mg? or mg only provides during blackout times?

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        logging.debug('            Simulation of case "parallel" complete.')
        return

    ###############################################################################
    # Dispatch with national grid as backup
    ###############################################################################
    def backupgrid():
        '''
        Case: micro grid with fixed capacities provides during blackout times

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        logging.debug('            Simulation of case "backupgrid" complete.')
        return

    ###############################################################################
    # Dispatch at buy from and sell to grid
    ###############################################################################
    def buysell():
        '''
        Case: micro grid connected to national grid and can feed in and out at will
        only buy from grid, when chaper than own production??

                        input/output    bus_fuel        bus_electricity      bus_electricity_ng
                            |               |               |                         |
                            |               |               |                         |
        source: pv          |------------------------------>|     fix cap             |
                            |               |               |                         |
        source: fossil_fuel |-------------->|               |                         |
                            |               |               |                         |
        trafo: generator    |<--------------|               |     fix cap             |
                            |------------------------------>|                         |
                            |               |               |                         |
        storage: battery    |<------------------------------|     fix cap             |
                            |------------------------------>|                         |
                            |               |               |                         |
        sink: demand        |<------------------------------|     fix                 |
                            |               |               |                         |
        sink: excess        |<------------------------------|     var                 |
                            |               |               |                         |
        sink: shortage      |<------------------------------|     var                 |
                            |               |               |                         |
        source: ng          |               |               |<------------------------| var
        sink: ng            |               |               |------------------------>|
        '''
        logging.debug('            Simulation of case "buysell" complete.')
        return

    ###############################################################################
    # Optimal adapted MG design and dispatch
    ###############################################################################
    def adapted():
        '''
        Case: micro grid is optimized for additional cacities (lower capacities) with grid interconnection

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        logging.debug('            Simulation of case "adapted" complete.')
        return

    ###############################################################################
    # Optimal mix and dispatch at interconnected state
    ###############################################################################
    def oem_interconnected():
        '''
        Case: micro grid is optimized with grid interconnection

                        input/output    bus_fuel        bus_electricity
                            |               |               |
                            |               |               |
        source: pv          |------------------------------>|     fix cap
                            |               |               |
        source: fossil_fuel |-------------->|               |
                            |               |               |
        trafo: generator    |<--------------|               |     fix cap
                            |------------------------------>|
                            |               |               |
        storage: battery    |<------------------------------|     fix cap
                            |------------------------------>|
                            |               |               |
        sink: demand        |<------------------------------|     fix
                            |               |               |
        sink: excess        |<------------------------------|     var
                            |               |               |
        sink: shortage      |<------------------------------|     var
                            |               |               |
        '''
        logging.debug('            Simulation of case "oem_interconnected" complete.')
        return

    