from ttp import ttp

date_to_parse = """
interface Loopback0
 description Router-id-loopback
 ip address 192.168.0.113/24
 !
interface Vlan778
 description CPE_Acces_Vlan
 ip address 2002::fd37/124
 ip vrf CPE1

"""
ttp_template = """
interface {{ interface }}
 ip address {{ ip }}/{{ mask }}
 description {{ description }}
 ip vrf {{ vrf }}
"""


parser = ttp(data=date_to_parse, template=ttp_template)
parser.parse()

print("results")
results = parser.result(format="json")[0]
print(results)
