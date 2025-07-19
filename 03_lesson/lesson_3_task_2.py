from smartphone import Smartphone

catalog = [
    Smartphone("LG", "K90", "+79134556622"),
    Smartphone("Xiaomi", "K60", "+79956651213"),
    Smartphone("Apple", "16 Pro", "+79132290091"),
    Smartphone("Sony", "W578", "+79132223344"),
    Smartphone("Blackberry", "RT77", "+79145664433")
    ]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")
