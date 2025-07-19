from adress import Address
from mailing import Mailing

to_addr = Address("630075", "Новосибирск", "Дуси Ковальчук", "378", "3")
from_addr = Address("456633", "Казань", "Ленина", "234", "89")

mail = Mailing(to_addr, from_addr, 256, "LN99900012345")

from_address_str = (f"{mail.from_address.index}, {mail.from_address.city},"
                   f"{mail.from_address.street}, {mail.from_address.house} - "
                   f"{mail.from_address.apartment}")

to_address_str = (f"{mail.to_address.index}, {mail.to_address.city}, "
                 f"{mail.to_address.street}, {mail.to_address.house} - "
                 f"{mail.to_address.apartment}")

print(f"Отправление {mail.track} из {from_address_str} в {to_address_str}. "
      f"Стоимость {mail.cost} рублей.")
