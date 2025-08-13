from color_core import get_color_from_pair_number
from color_constants import MAJOR_COLORS, MINOR_COLORS

def generate_color_code_manual():
    manual_lines = []
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        manual_lines.append(f"{pair_number}: {major} {minor}")
    return "\n".join(manual_lines)

def print_color_code_manual():
    print("25-Pair Color Code Manual")
    print(generate_color_code_manual())
