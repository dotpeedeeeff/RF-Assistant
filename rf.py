import math

def resonant_frequency_calc(inductance: float, capacitance: float) -> float:
    """
    Resonant frequency calculator.
    Returns result scaled to kHz.
    """
    frequency = 1 / ((2 * math.pi) * (math.sqrt(inductance * capacitance)))
    frequency = round(frequency, 0)
    frequency = frequency / 1000
    frequency = int(frequency)
    frequency = str(frequency) + " kHz"
    return frequency


def convert_to_farads(user_capacitance: float, capacitance_suffix: str) -> float:
    """"
    Converters capacitance value with SI suffix to Farads.
    """
    si_c_suffixes = {
        "pF": 1E-12,
        "nF": 1E-9,
        "uF": 1E-6
    }

    farad_capacitance = user_capacitance * (si_c_suffixes[capacitance_suffix])
    return farad_capacitance


def convert_to_henries(user_inductance: float, inductance_suffix: str) -> float:
    """
    Converts inductance value with SI suffix to Henries.
    """
    si_l_suffixes = {
        "uH": 1E-6,
        "mH": 1E-3
    }
    henry_inductance = user_inductance * (si_l_suffixes[inductance_suffix])
    return henry_inductance


def generate_capacitance_array(start_capacitance: int, stop_capacitance: int, capacitance_step: int) -> list:
    """
    Generate array of capacitances from start, stop and step inputs.
    """
    stepped_capacitance_array = []
    current_capacitance = start_capacitance    
    
    if capacitance_step == 0:
        return [start_capacitance]
    
    if stop_capacitance < start_capacitance:
        return [start_capacitance]

    while current_capacitance < stop_capacitance:

        stepped_capacitance_array.append(current_capacitance)
        current_capacitance += capacitance_step

    if not stepped_capacitance_array or stepped_capacitance_array[-1] != stop_capacitance:
        stepped_capacitance_array.append(stop_capacitance)

    return stepped_capacitance_array


def generate_frequency_array(stepped_capacitance_array: float, henry_inductance: float, capacitance_suffix: str) -> list:
    frequency_output_array = []
    for i in range(len(stepped_capacitance_array)):
        """
        Calculate frequency for each capacitance value in array.
        """       
        current_capacitance_iteration = stepped_capacitance_array[i]
        current_capacitance_iteration = convert_to_farads(current_capacitance_iteration, capacitance_suffix)
        current_frequency_iteration = resonant_frequency_calc(henry_inductance, current_capacitance_iteration)
        frequency_output_array.append(current_frequency_iteration)
    return frequency_output_array


def prepare_final_output(stepped_capacitance_array, frequency_output_array, capacitance_suffix):
    final_array_out = []
    for i in range(len(stepped_capacitance_array)):
        # Prepare final string for rendering
        final_iter = str(stepped_capacitance_array[i]) + " " + capacitance_suffix + " " + (frequency_output_array[i])
        final_array_out.append(final_iter)
    return final_array_out


def final_frequency_calculcator(user_inductance, inductance_suffix, start_capacitance, stop_capacitance, capacitance_step, capacitance_suffix):
    # main function to output frequency array
    henry_inductance = convert_to_henries(user_inductance, inductance_suffix)
    stepped_capacitance_array = generate_capacitance_array(start_capacitance, stop_capacitance, capacitance_step)
    frequency_output_arr = generate_frequency_array(stepped_capacitance_array, henry_inductance, capacitance_suffix)
    final_array_out = prepare_final_output(stepped_capacitance_array, frequency_output_arr, capacitance_suffix)
    return final_array_out


def capacitive_reactance_calculator(user_capacitance: float, capacitance_suffix: str, frequency: float):
    farad_capacitance = convert_to_farads(user_capacitance, capacitance_suffix)
    herz_frequency = frequency * 1000
    capacitive_reactance = 1 / (2 * math.pi * herz_frequency * farad_capacitance)
    capacitive_reactance = round(capacitive_reactance, 1)
    return capacitive_reactance