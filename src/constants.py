# Offgriders.py
MICRO_GRID_DESIGN_LOGFILE_LOG = "micro_grid_design_logfile.log"
DISPLAY_EXPERIMENT = "display_experiment"
PERFORM_MULTICRITERIA_ANALYSIS = "perform_multicriteria_analysis"
OUTPUT_FILE = "output_file"

# Default input file
INPUT_TEMPLATE_EXCEL_XLSX = "inputs/input_data.xlsx"

# A1_GENERAL_FUNCTIONS
CAPACITY_PV_KWP = "capacity_pv_kWp"
CAPACITY_WIND_KW = "capacity_wind_kW"
CAPACITY_STORAGE_KWH = "capacity_storage_kWh"
POWER_STORAGE_KW = "power_storage_kW"
CAPACITY_GENSET_KW = "capacity_genset_kW"
CAPACITY_PCOUPLING_KW = "capacity_pcoupling_kW"
CAPACITY_RECTIFIER_AC_DC_KW = "capacity_rectifier_ac_dc_kW"
CAPACITY_INVERTER_DC_AC_KW = "capacity_inverter_dc_ac_kW"
DEMAND_PROFILE = "demand_profile"

# B_READ_FROM_FILES
SETTINGS = "settings"
INPUT_CONSTANT = "input_constant"
INPUT_SENSITIVITY = "input_sensitivity"
PROJECT_SITES = "project_sites"
CASE_DEFINITIONS = "case_definitions"
MULTICRITERIA_DATA = "multicriteria_data"
INPUT_FOLDER_TIMESERIES = "input_folder_timeseries"
TIMESERIES_FILE = "timeseries_file"
TITLE_GRID_AVAILABILITY = "title_grid_availability"
NECESSITY_FOR_BLACKOUT_TIMESERIES_GENERATION = (
    "necessity_for_blackout_timeseries_generation"
)
SETTING_VALUE = "setting_value"
UNIT = "Unit"
VALUE = "Value"
CASE_NAME = "case_name"
MAX_SHORTAGE = "max_shortage"
NUMBER_OF_EQUAL_GENERATORS = "number_of_equal_generators"
DIMENSIONS = "dimensions"
CRITERIA = "criteria"
PARAMETERS = "parameters"
TARIFF = "tariff"
TITLE_TIME = "title_time"
TITLE_DEMAND_AC = "title_demand_ac"
TITLE_DEMAND_DC = "title_demand_dc"
TITLE_PV = "title_pv"
TITLE_WIND = "title_wind"
DEMAND_AC = "demand_ac"
DEMAND_DC = "demand_dc"
PV_GENERATION_PER_KWP = "pv_generation_per_kWp"
WIND_GENERATION_PER_KW = "wind_generation_per_kW"
GRID_AVAILABILITY = "grid_availability"
OUTPUT_FOLDER = "output_folder"
RESTORE_OEMOF_IF_EXISTENT = "restore_oemof_if_existant"
RESTORE_BLACKOUTS_IF_EXISTENT = "restore_blackouts_if_existant"
SAVE_LP_FILE = "save_lp_file"
LP_FILE_FOR_ONLY_3_TIMESTEPS = "lp_file_for_only_3_timesteps"
SAVE_TO_CSV_FLOWS_STORAGE = "save_to_csv_flows_storage"
SAVE_TO_PNG_FLOWS_STORAGE = "save_to_png_flows_storage"
SAVE_TO_CSV_FLOWS_ELECTRICITY_MG = "save_to_csv_flows_electricity_mg"
SAVE_TO_PNG_FLOWS_ELECTRICITY_MG = "save_to_png_flows_electricity_mg"
EVALUATION_PERSPECTIVE = "evaluation_perspective"

DEFAULT = "default"
AC_SYSTEM = "AC_system"
DC_SYSTEM = "DC_system"
SEPARATOR = "seperator"
GRID_AVAILABILITY_CSV = "grid_availability.csv"

INPUT_TEMPLATE_EXCEL_XLSX = "inputs/input_data.xlsx"

OEMOF_FOLDER = "/oemof"
INPUTS_FOLDER = "/inputs"
ELECTRICITY_MG_FOLDER = "/electricity_mg"
STORAGE_FOLDER = "/storage"
LP_FILES_FOLDER = "/lp_files"

# C_SENSITIVITY_EXPERIMENTS
BLACKOUT_DURATION = "blackout_duration"
BLACKOUT_DURATION_STD_DEVIATION = "blackout_duration_std_deviation"
BLACKOUT_FREQUENCY = "blackout_frequency"
BLACKOUT_FREQUENCY_STD_DEVIATION = "blackout_frequency_std_deviation"
SENSITIVITY_ALL_COMBINATIONS = "sensitivity_all_combinations"
DEMAND_AC_SCALING_FACTOR = "demand_ac_scaling_factor"
DEMAND_DC_SCALING_FACTOR = "demand_dc_scaling_factor"
STORAGE_SOC_INITIAL = "storage_soc_initial"
TOTAL_NUMBER_OF_EXPERIMENTS = "total_number_of_experiments"
PROJECT_SITE_NAME = "project_site_name"
EXPERIMENT_NAME = "experiment_name"
MIN = "Min"
MAX = "Max"
STEP = "Step"
COMBUSTION_VALUE_FUEL = "combustion_value_fuel"
DISTRIBUTION_GRID_COST_INVESTMENT = "distribution_grid_cost_investment"
DISTRIBUTION_GRID_COST_OPEX = "distribution_grid_cost_opex"
DISTRIBUTION_GRID_LIFETIME = "distribution_grid_lifetime"
GENSET_BATCH = "genset_batch"
GENSET_COST_INVESTMENT = "genset_cost_investment"
GENSET_COST_OPEX = "genset_cost_opex"
GENSET_COST_VAR = "genset_cost_var"
GENSET_EFFICIENCY = "genset_efficiency"
GENSET_LIFETIME = "genset_lifetime"
GENSET_MAX_LOADING = "genset_max_loading"
GENSET_MIN_LOADING = "genset_min_loading"
GENSET_OVERSIZE_FACTOR = "genset_oversize_factor"
INVERTER_DC_AC_BATCH = "inverter_dc_ac_batch"
INVERTER_DC_AC_COST_INVESTMENT = "inverter_dc_ac_cost_investment"
INVERTER_DC_AC_COST_OPEX = "inverter_dc_ac_cost_opex"
INVERTER_DC_AC_COST_VAR = "inverter_dc_ac_cost_var"
INVERTER_DC_AC_EFFICIENCY = "inverter_dc_ac_efficiency"
INVERTER_DC_AC_LIFETIME = "inverter_dc_ac_lifetime"
MAINGRID_DISTANCE = "maingrid_distance"
MAINGRID_ELECTRICITY_PRICE = "maingrid_electricity_price"
MAINGRID_EXTENSION_COST_INVESTMENT = "maingrid_extension_cost_investment"
MAINGRID_EXTENSION_COST_OPEX = "maingrid_extension_cost_opex"
MAINGRID_EXTENSION_LIFETIME = "maingrid_extension_lifetime"
MAINGRID_FEEDIN_TARIFF = "maingrid_feedin_tariff"
MAINGRID_RENEWABLE_SHARE = "maingrid_renewable_share"
MIN_RENEWABLE_SHARE = "min_renewable_share"
PCOUPLING_BATCH = "pcoupling_batch"
PCOUPLING_COST_INVESTMENT = "pcoupling_cost_investment"
PCOUPLING_COST_OPEX = "pcoupling_cost_opex"
PCOUPLING_COST_VAR = "pcoupling_cost_var"
PCOUPLING_EFFICIENCY = "pcoupling_efficiency"
PCOUPLING_LIFETIME = "pcoupling_lifetime"
PCOUPLING_OVERSIZE_FACTOR = "pcoupling_oversize_factor"
PRICE_FUEL = "price_fuel"
PROJECT_COST_INVESTMENT = "project_cost_investment"
PROJECT_COST_OPEX = "project_cost_opex"
PROJECT_LIFETIME = "project_lifetime"
PV_BATCH = "pv_batch"
PV_COST_INVESTMENT = "pv_cost_investment"
PV_COST_OPEX = "pv_cost_opex"
PV_COST_VAR = "pv_cost_var"
PV_LIFETIME = "pv_lifetime"
RECTIFIER_AC_DC_BATCH = "rectifier_ac_dc_batch"
RECTIFIER_AC_DC_COST_INVESTMENT = "rectifier_ac_dc_cost_investment"
RECTIFIER_AC_DC_COST_OPEX = "rectifier_ac_dc_cost_opex"
RECTIFIER_AC_DC_COST_VAR = "rectifier_ac_dc_cost_var"
RECTIFIER_AC_DC_EFFICIENCY = "rectifier_ac_dc_efficiency"
RECTIFIER_AC_DC_LIFETIME = "rectifier_ac_dc_lifetime"
SHORTAGE_MAX_ALLOWED = "shortage_max_allowed"
SHORTAGE_MAX_TIMESTEP = "shortage_max_timestep"
SHORTAGE_PENALTY_COST = "shortage_penalty_costs"
SHORTAGE_LIMIT = "stability_limit"
SHORTAGE_BATCH_CAPACITY = "storage_batch_capacity"
SHORTAGE_BATCH_POWER = "storage_batch_power"
SHORTAGE_CAPACITY_COST_INVESTMENT = "storage_capacity_cost_investment"
SHORTAGE_CAPACITY_COST_OPEX = "storage_capacity_cost_opex"
STORAGE_CAPACITY_LIFETIME = "storage_capacity_lifetime"
STORAGE_COST_VAR = "storage_cost_var"
STORAGE_CRATE_CHARGE = "storage_Crate_charge"
STORAGE_CRATE_DISCHARGE = "storage_Crate_discharge"
STORAGE_EFFICIENCY_CHARGE = "storage_efficiency_charge"
STORAGE_EFFICIENCY_DISCHARGE = "storage_efficiency_discharge"
STORAGE_LOSS_TIMESTEP = "storage_loss_timestep"
STORAGE_POWER_COST_INVESTMENT = "storage_power_cost_investment"
STORAGE_POWER_COST_OPEX = "storage_power_cost_opex"
STORAGE_POWER_LIFETIME = "storage_power_lifetime"
STORAGE_SOC_MAX = "storage_soc_max"
STORAGE_SOC_MIN = "storage_soc_min"
TAX = "tax"
WACC = "wacc"
WHITE_NOISE_DEMAND = "white_noise_demand"
WHITE_NOISE_PV = "white_noise_pv"
WHITE_NOISE_WIND = "white_noise_wind"
WIND_BATCH = "wind_batch"
WIND_COST_INVESTMENT = "wind_cost_investment"
WIND_COST_OPEX = "wind_cost_opex"
WIND_COST_VAR = "wind_cost_var"
WIND_LIFETIME = "wind_lifetime"
FUEL_PRICE = "fuel_price"
FUEL_PRICE_CHANGE_ANNUAL = "fuel_price_change_annual"
CASE = "case"
RESULTS_DEMAND_CHARACTERISTICS = "results_demand_characteristics"
RESULTS_BLACKOUT_CHARACTERISTICS = "results_blackout_characteristics"
CAPACITY_INVERTER_KW = "capacity_inverter_kW"
LCOE = "lcoe"
ANNUITY = "annuity"
NPV = "npv"
SUPPLY_RELIABILITY_KWH = "supply_reliability_kWh"
RES_SHARE = "res_share"
AUTONOMY_FACTOR = "autonomy_factor"
TOTAL_DEMAND_ANNUAL_KWH = "total_demand_annual_kWh"
DEMAND_PEAK_KW = "demand_peak_kW"
TOTAL_DEMAND_SUPPLIED_ANNUAL_KWH = "total_demand_supplied_annual_kWh"
TOTAL_DEMAND_SHORTAGE_ANNUAL_KWH = "total_demand_shortage_annual_kWh"
NATIONAL_GRID_RELIABILITY_H = "national_grid_reliability_h"
NATIONAL_GRID_TOTAL_BLACKOUT_DURATION = "national_grid_total_blackout_duration"
NATIONAL_GRID_NUMBER_OF_BLACKOUTS = "national_grid_number_of_blackouts"
TOTAL_PV_GENERATION_KWH = "total_pv_generation_kWh"
TOTAL_WIND_GENERATION_KWH = "total_wind_generation_kWh"
TOTAL_GENSET_GENERATION_KWH = "total_genset_generation_kWh"
CONSUMPTION_FUEL_ANNUAL_L = "consumption_fuel_annual_l"
CONSUMPTION_MAIN_GRID_MG_SIDE_ANNUAL_KWH = "consumption_main_grid_mg_side_annual_kWh"
GENSET_HOURS_OF_OPERATION = "generator_operation_hours"
FEEDIN_MAIN_GRID_MG_SIDE_ANNUAL_KWH = "feedin_main_grid_mg_side_annual_kWh"
RESULTS_ANNUITIES = "results_annuities"
ANNUITY_PV = "annuity_pv"
ANNUITY_STORAGE = "annuity_storage"
ANNUITY_RECTIFIER_AC_DC = "annuity_rectifier_ac_dc"
ANNUITY_INVERTER_DC_AC = "annuity_inverter_dc_ac"
ANNUITY_WIND = "annuity_wind"
ANNUITY_GENSET = "annuity_genset"
ANNUITY_PCOUPLING = "annuity_pcoupling"
ANNUITY_DISTRIBUTION_GRID = "annuity_distribution_grid"
ANNUITY_PROJECT = "annuity_project"
ANNUITY_MAINGRID_EXTENSION = "annuity_maingrid_extension"
EXPENDITURES_FUEL_ANNUAL = "expenditures_fuel_annual"
EXPENDITURES_MAIN_GRID_CONSUMPTION_ANNUAL = "expenditures_main_grid_consumption_annual"
EXPENDITURES_SHORTAGE_ANNUAL = "expenditures_shortage_annual"
REVENUE_MAIN_GRID_FEEDIN_ANNUAL = "revenue_main_grid_feedin_annual"
RESULTS_COSTS = "results_costs"
COSTS_PV = "costs_pv"
COSTS_STORAGE = "costs_storage"
COSTS_RECTIFIER_AC_DC = "costs_rectifier_ac_dc"
COSTS_INVERTER_DC_AC = "costs_inverter_dc_ac"
COSTS_WIND = "costs_wind"
COSTS_GENSET = "costs_genset"
COSTS_PCOUPLING = "costs_pcoupling"
COSTS_DISTRIBUTION_GRID = "costs_distribution_grid"
COSTS_PROJECT = "costs_project"
FIRST_INVESTMENT = "first_investment"
OPERATION_MAINTAINANCE_EXPENDITURES = "operation_maintainance_expenditures"
COSTS_MAINGRID_EXTENSION = "costs_maingrid_extension"
EXPENDITURES_FUEL_TOTAL = "expenditures_fuel_total"
EXPENDITURES_MAIN_GRID_CONSUMPTION_TOTAL = "expenditures_main_grid_consumption_total"
EXPENDITURES_SHORTAGE_TOTAL = "expenditures_shortage_total"
REVENUE_MAIN_GRID_FEEDIN_TOTAL = "revenue_main_grid_feedin_total"
OBJECTIVE_VALUE = "objective_value"
SIMULATION_TIME = "simulation_time"
EVALUATION_TIME = "evaluation_time"
FILENAME = "filename"
COMMENTS = "comments"
CO2_EMISSIONS_KGC02EQ = "co2_emissions_kgCO2eq"
TOTAL_EXCESS_ANNUAL_KWH = "total_excess_annual_kWh"

SENSITIVITY_EXPERIMENTS_CSV = "sensitivity_experiments.csv"
SIMULATION_EXPERIMENTS_CSV = "simulation_experiments.csv"

# D0_process_input
PERFORM_SIMULATION = "perform_simulation"
BASED_ON_CASE = "based_on_case"
ANNUITY_FACTOR = "annuity_factor"
CRF = "crf"
PV = "pv"
WIND = "wind"
GENSET = "genset"
STORAGE_CAPACITY = "storage_capacity"
STORAGE_POWER = "storage_power"
PCOUPLING = "pcoupling"
MAINGRID_EXTENSION = "maingrid_extension"
DISTRIBUTION_GRID = "distribution_grid"
RECTIFIER_AC_DC = "rectifier_ac_dc"
INVERTER_DC_AC = "inverter_dc_ac"
PROJECT = "project"
EVALUATED_DAYS = "evaluated_days"
TIME_END = "time_end"
TIME_START = "time_start"
DATE_TIME_INDEX = "date_time_index"
TIME_FREQUENCY = "time_frequency"
FILE_INDEX = "file_index"
DEMAND_PROFILE_AC = "demand_profile_ac"
DEMAND_PROFILE_DC = "demand_profile_dc"
ACCUMULATED_PROFILE_AC_SIDE = "accumulated_profile_ac_side"
ACCUMULATED_PROFILE_DC_SIDE = "accumulated_profile_dc_side"
TOTAL_DEMAND_AC = "total_demand_ac"
PEAK_DEMAND_AC = "peak_demand_ac"
TOTAL_DEMAND_DC = "total_demand_dc"
PEAK_DEMAND_DC = "peak_demand_dc"
PEAK_PV_GENERATION_PER_KWP = "peak_pv_generation_per_kWp"
PEAK_WIND_GENERATION_PER_KW = "peak_wind_generation_per_kW"
MEAN_DEMAND_AC = "mean_demand_ac"
MEAN_DEMAND_DC = "mean_demand_dc"
PEAK_MEAN_DEMAND_RATIO_AC = "peak/mean_demand_ratio_ac"
PEAK_MEAN_DEMAND_RATIO_DC = "peak/mean_demand_ratio_dc"
ABS_PEAK_DEMAND_AC_SIDE = "abs_peak_demand_ac_side"

SUFFIX_COST_INVESTMENT = "_cost_investment"
SUFFIX_LIFETIME = "_lifetime"
SUFFIX_COST_OPEX = "_cost_opex"
SUFFIX_COST_ANNUITY = "_cost_annuity"
SUFFIX_COST_CAPEX = "_cost_capex"


# E_blackouts_central_grid
TIMESTEP = "timestep"
MAX_DATE_TIME_INDEX = "max_date_time_index"
GRID_TOTAL_BLACKOUT_DURATION = "grid_total_blackout_duration"
GRID_NUMBER_OF_BLACKOUTS = "grid_number_of_blackouts"
GRID_RELIABILITY = "grid_reliability"
MAX_EVALUATED_DAYS = "max_evaluated_days"

GRID_AVAILABILITY_CSV = "grid_availability.csv"

# F_case_definitions
PEAK_DEMAND = "peak_demand"
GENSET_WITH_MINIMAL_LOADING = "genset_with_minimal_loading"
CAPACITY_PCC_CONSUMPTION_KW = "capacity_pcc_consumption_kW"
CAPACITY_PCC_FEEDING_KW = "capacity_pcc_feedin_kW"
STORAGE_FIXED_CAPACITY = "storage_fixed_capacity"
STORAGE_FIXED_POWER = "storage_fixed_power"
GENSET_FIXED_CAPACITY = "genset_fixed_capacity"
PV_FIXED_CAPACITY = "pv_fixed_capacity"
PCC_CONSUMPTION_FIXED_CAPACITY = "pcc_consumption_fixed_capacity"
PCC_FEEDIN_FIXED_CAPACITY = "pcc_feedin_fixed_capacity"
WIND_FIXED_CAPACITY = "wind_fixed_capacity"
RECTIFIER_AC_DC_FIXED_CAPACITY = "rectifier_ac_dc_fixed_capacity"
INVERTER_DC_AC_FIXED_CAPACITY = "inverter_dc_ac_fixed_capacity"
ALLOW_SHORTAGE = "allow_shortage"
STABILITY_CONSTRAINT = "stability_constraint"
RENEWABLE_CONSTRAINT = "renewable_constraint"
RENEWABLE_SHARE_CONSTRAINT = "renewable_share_constraint"
EVALUATION_PERSPECTIVE = EVALUATION_PERSPECTIVE
FORCE_CHARGE_FROM_MAINGRID = "force_charge_from_maingrid"
DISCHARGE_ONLY_WHEN_BLACKOUT = "discharge_only_when_blackout"
ENABLE_INVERTER_ONLY_AT_BLACKOUT = "enable_inverter_only_at_backout"
OEM = "oem"

# G0_oemof_simulate
MAIN = "main"
META = "meta"
OBJECTIVE = "objective"
SOLVER = "solver"
TIME = "Time"
BUS_ELECTRICITY_AC = "bus_electricity_ac"
BUS_ELECTRICITY_DC = "bus_electricity_dc"
SHARE_BACKUP = "share_backup"
SHARE_USAGE = "share_usage"
SHARE_HYBRID = "share_hybrid"
BUS_FUEL = "bus_fuel"

PREFIX_RESULTS = "results_"
SAVE_OEMOFRESULTS = "save_oemofresults"

# G1_oemof_create_model
SOLVER_VERBOSE = "solver_verbose"
CMDLINE_OPTION = "cmdline_option"
CMDLINE_OPTION_VALUE = "cmdline_option_value"
SYMBOLIC_SOLVER_LABELS = "symbolic_solver_labels"
OEMOF = "/oemof"

# G2a_oemof_busses_and_components
SOURCE_FUEL = "source_fuel"
SOURCE_SHORTAGE = "source_shortage"
BUS_ELECTRICITY_NG_CONSUMPTION = "bus_electricity_ng_consumption"
SOURCE_MAINGRID_CONSUMPTION = "source_maingrid_consumption"
SINK_MAINGRID_CONSUMPTION_SYMBOLIC = "sink_maingrid_consumption_symbolic"
SOURCE_PV = "source_pv"
PV_COST_ANNUITY = "pv_cost_annuity"
SOURCE_WIND = "source_wind"
TRANSFORMER_RECTIFIER = "transformer_rectifier"
RECTIFIER_AC_DC_COST_ANNUITY = "rectifier_ac_dc_cost_annuity"
TRANSFORMER_INVERTER_DC_AC = "transformer_inverter_dc_ac"
INVERTER_DC_AC_COST_ANNUITY = "inverter_dc_ac_cost_annuity"
TRANSFORMER_GENSET_ = "transformer_genset_"
GENSET_COST_ANNUITY = "genset_cost_annuity"
TRANSFORMER_PCC_FEEDIN = "transformer_pcc_feedin"
PCOUPLING_COST_ANNUITY = "pcoupling_cost_annuity"
TRANSFORMER_PCC_CONSUMPTION = "transformer_pcc_consumption"
GENERIC_STORAGE = "generic_storage"
STORAGE_CAPACITY_COST_ANNUITY = "storage_capacity_cost_annuity"
STORAGE_POWER_COST_ANNUITY = "storage_power_cost_annuity"
SINK_EXCESS = "sink_excess"
DISTRIBUTION_GRID_EFFICIENCY = "distribution_grid_efficiency"
SINK_DEMAND_AC = "sink_demand_ac"
SINK_DEMAND_DC = "sink_demand_dc"
SINK_MAINGRID_FEEDIN = "sink_maingrid_feedin"
SINK_MAINGRID_FEEDIN_SYMBOLIC = "source_maingrid_feedin_symbolic"

# G2b
STORAGE_CAPACITY_MIN = "storage_capacity_min"
DEMAND = "Demand"
STORED_CAPACITY = "Stored capacity"
GRID_AVAILABILITY = "Grid availability"
DEMAND_SHORTAGE = "Demand shortage"
CONSUMPTION_MAIN_GRID_MG_SIDE = "Consumption from main grid (MG side)"
FEED_INTO_MAIN_GRID_MG_SIDE = "Feed into main grid (MG side)"
GENSET_GENERATION = "Genset generation"
STORAGE_DISCHARGE = "Storage discharge"
STORAGE_CHARGE_DC = "Storage charge DC"
STORAGE_DISCHARGE_DC = "Storage discharge DC"
INVERTER_INPUT = "Inverter input"

# G3
SEQUENCES = "sequences"
FLOW = "flow"
TOTAL_DEMAND_SHORTAGE_AC_ANNUAL_KWH = "total_demand_shortage_ac_annual_kWh"
DEMAND_SHORTAGE_AC = "Demand shortage AC"
TOTAL_DEMAND_SHORTAGE_DC_ANNUAL_KWH = "total_demand_shortage_dc_annual_kWh"
DEMAND_SHORTAGE_DC = "Demand shortage DC"
DEMAND_SUPPLIED = "Demand supplied"
TOTAL_DEMAND_EXCESS_AC_ANNUAL_KWH = "total_demand_excess_ac_annual_kWh"
EXCESS_GENERATION_AC = "Excess generation AC"
TOTAL_DEMAND_EXCESS_DC_ANNUAL_KWH = "total_demand_excess_dc_annual_kWh"
EXCESS_GENERATION_DC = "Excess generation DC"
TOTAL_DEMAND_EXCESS_ANNUAL_KWH = "total_demand_excess_annual_kWh"
EXCESS_GENERATION = "Excess generation"
PV_GENERATION_DC = "PV generation DC"
PV_GENERATION_AC = "PV generation AC"
PV_GENERATION = "PV generation"
SCALARS = "scalars"
INVEST = "invest"
RECTIFIER_OUTPUT = "Rectifier output"
RECTIFIER_INPUT = "Rectifier input"
TOTAL_RECTIFIER_AC_DC_THROUGHPUT_KWH = "total_rectifier_ac_dc_throughput_kWh"
INVERTER_OUTPUT = "Inverter output"
TOTAL_INVERTER_DC_AC_THROUGHPUT_KWH = "total_inverter_dc_ac_throughput_kWh"
WIND_GENERATION = "Wind generation"
TRANSFORMER_GENSET_1 = "transformer_genset_1"
GENSET_1_GENERATION = "Genset 1 generation"
CONSUMPTION_FUEL_ANNUAL_KWH = "consumption_fuel_annual_kWh"
CAPACITY = "capacity"
TOTAL_STORAGE_THOUGHPUT_KWH = "total_storage_throughput_kWh"
STORAGE_CHARGE_AC = "Storage charge AC"
STORAGE_DISCHARGE_AC = "Storage discharge AC"
STORAGE_CHARGE = "Storage charge"
STORAGE_SOC = "Storage SOC"
CONSUMPTION_MAIN_GRID_UTILITY_SIDE_ANNUAL_KWH = (
    "consumption_main_grid_utility_side_annual_kWh"
)

BUS_ELECTRICITY_NG_FEEDIN = "bus_electricity_ng_feedin"
FEEDIN_MAIN_GRID_UTILITY_SIDE_ANNUAL_KWH = "feedin_main_grid_utility_side_annual_kWh"
TOTAL_PCOUPLING_THROUGHPUT_KWH = "total_pcoupling_throughput_kWh"
DEMAND_AC = "Demand AC"
DEMAND_DC = "Demand DC"

# G3a
WIND_COST_ANNUITY = "wind_cost_annuity"
MAINGRID_EXTENSION_COST_ANNUITY = "maingrid_extension_cost_annuity"
STORAGE = "storage"
FUEL_CO2_EMISSION_FACTOR = "fuel_co2_emission_factor"
MAINGRID_CO2_EMISSION_FACTOR = "maingrid_co2_emission_factor"
INCLUDE_SHORTAGE_PENALTY_COSTS_IN_LCOE = "include_shortage_penalty_costs_in_lcoe"

PREFIX_ANNUITY = "annuity_"
PREFIX_CAPACITY = "capacity_"
PREFIX_OM_VAR = "om_var_"
PREFIX_TOTAL = "total_"
PREFIX_COSTS = "costs_"

SUFFIX_COST_VAR = "_cost_var"
SUFFIX_KW = "_kW"
SUFFIX_GENERATION_KWH = "_generation_kWh"
SUFFIX_THROUGHPUT_KWH = "_throughput_kWh"

# G3b
CONSUMPTION_FROM_MAIN_GRID = "Consumption from main grid"
FEED_INTO_MAIN_GRID = "Feed into main grid"
EXCESS_ELECTRICITY = "Excess electricity"
CAPACITY_PCC = "capacity pcc"

# G4
DISPLAY_META = "display_meta"
DISPLAY_MAIN = "display_main"
DISPLAY_INVEST = "display_invest"

SUFFIX_GRAPH = "_graph"
BASE_OEM = "base_oem"
BASE_OEM_WITH_MIN_LOADING = "base_oem_with_min_loading"
SUFFIX_ELECTRICITY_MG_CSV = "_electricity_mg.csv"
SUFFIX_ELECTRICITY_MG_PNG = "_electricity_mg.png"
SUFFIX_ELECTRICITY_MG_4DAYS_PNG = "_electricity_mg_4days.png"
SUFFIX_STORAGE_CSV = "_storage.csv"
SUFFIX_STORAGE_PNG = "_storage.png"
SUFFIX_STORAGE_4DAYS_PNG = "_storage_4days.png"

# H0
CAPACITIES = "capacities"
EVALUATIONS = "evaluations"
NORMALIZED_EVALUATIONS = "normalized_evaluations"
GLOBAL_LS = "global_Ls"
LOCAL_LS = "local_Ls"
LEVELS = "levels"
PREVIOUS_LEVEL = "previous_level"
CHANGES = "changes"
ANALYSE = "analyse"
WEIGHT = "weight"
ABREV = "Abrev"
DIESEL = "diesel"
MAINGRID = "maingrid"
PLOT = "plot"
PARAMETER = "parameter"
SHOW = "show"

DIMENSIONS_W = "Dimensions"  # dimension_weights
LOCAL = "local"

# H1
ECONOMIC = "economic"
TECHNICAL = "technical"
SOCIOINSTITUTIONAL = "socioinstitutional"
ENVIRONMENTAL = "environmental"
ENVIRONMENTAL_W = "Environmental"
CASES_AND_EXPERIMENTS = "cases and experiments"
EVALUATION = "evaluation"

EC1 = "EC1"
EC2 = "EC2"

T1 = "T1"
T2 = "T2"
T3 = "T3"
T4 = "T4"

S1 = "S1"
S2 = "S2"
S3 = "S3"

EN1 = "EN1"
EN2 = "EN2"
EN3 = "EN3"

WEIGHTS = "Weights"
L1 = "L1"
LINF = "Linf"
MCA_PLOTS = "/mca_plots"
GLOBAL = "global"
PREFIX_CASE = "case_"
PATH_MCA_EVALUATIONS_XLSX = "MCA_evaluations.xlsx"
