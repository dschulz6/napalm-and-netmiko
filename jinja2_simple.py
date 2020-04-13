import jinja2

bgp_vars = {
	"peer1_ip": "172.16.0.2",
	"peer1_as": "20",
	"advertised_route1": "10.10.10.0/24",
	"advertised_route2": "10.10.20.0/24",
	"advertised_route3": "10.10.30.0/24",
}

bgp_template = '''
router bgp 10
network {{ advertised_route1 }}
network {{ advertised_route2 }}
network {{ advertised_route3 }}
neighbor {{ peer1_ip }} remote-as {{ peer1_as }}
update-source loopback0
ebgp-multihop 1

'''

t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))
