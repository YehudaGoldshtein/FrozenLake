

def val_to_sign(val):
    switcher = {
        "up": "\u2191",
        "down": "\u2193",
        "left": "\u2190",
        "right": "\u2192",
        "stay": "\u25A1",
    }
    return switcher.get(val, " ")


def draw_policy(policy):
    new_map = "_" * (len(policy[0]) * 2 + 3) + "\n"
    for i in range(len(policy)):
        new_map += "| "
        for j in range(len(policy[i])):
            new_map += val_to_sign(policy[i][j]) + " "
        new_map += "|"
        new_map += "\n"

    new_map += "\u203E" * (len(policy[0]) * 2 + 3)
    return new_map

def draw_value(value_map):
    new_map = "_" * (len(value_map[0]) * 2 + 3) + "\n"
    for i in range(len(value_map)):
        new_map += "| "
        for j in range(len(value_map[i])):
            new_map += str(value_map[i][j]) + " "
        new_map += "|"
        new_map += "\n"

    new_map += "\u203E" * (len(value_map[0]) * 2 + 3)
    return new_map
