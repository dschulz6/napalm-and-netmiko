import jinja2

advertised_routes  = ["10.10.10.0 255.255.255.0", "10.10.20.0 255.255.255.0", "10.10.30.0 255.255.255.0"]
bgp_vars = {
    "local_as": "10",
	"peer1_ip": "172.16.0.2",
	"peer1_as": "20",
	"advertised_routes": advertised_routes,
}


template_file = 'ios_bgp.j2'
with open(template_file) as f:
	bgp_template = f.read()

template = jinja2.Template(bgp_template)
print(template.render(bgp_vars))
