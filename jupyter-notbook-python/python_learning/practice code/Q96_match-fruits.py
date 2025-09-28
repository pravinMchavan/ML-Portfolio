# Match a fruit name to its category (e.g., "apple" → "Fruit", "carrot" → "Vegetable") and print it.

def check(item):
    match item.lower():
        case "apple"|"banana" | "grape":
            print("fruit")
        case "carrate" | "potato" | "onion":
            print("vagitable")
        case "almond" | "walnut":
            print("nut")
        case _:
            print("unknown catorgery")
check("grapes")