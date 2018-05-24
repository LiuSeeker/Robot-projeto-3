from xml.etree.ElementTree import parse, Element, SubElement, Comment, tostring, ElementTree
from random import randint, uniform, choice


class Link:
	def __init__(self, nome, tipo, dimensoes):
		self.nome = nome
		self.tipo = tipo
		self.dimensoes = dimensoes
		self.peca_x = True
		self.peca_mx = True
		self.peca_y = True
		self.peca_my = True
		self.peca_z = True
		self.peca_mz = True

def cria_carro():
	global dic_links
	#n_pneus = randint(3,6)
	#n_pecas = randint(2,5)
	n_pecas = 4

	shapes = ["box", "cylinder", "sphere"]

	root = Element("robot", {'name': 'nome_robo'})

	link_principal = SubElement(root, "link", {'name': 'link_principal'})

	inertial_p = SubElement(link_principal, "inertial")
	mass_p = SubElement(inertial_p, "mass", {'value': '5'})
	inertia_p = SubElement(inertial_p, "inertia", {'ixx': '1.0', 'ixy': '0.0', 'ixz': '0.0', 'iyy': '1.0', 'iyz': '0.0','izz': '1.0'})

	randshape = shapes[randint(0,2)]

	collision_p = SubElement(link_principal, "collision")
	origin_p_c = SubElement(collision_p, "origin", {'xyz': '0 0 0'})
	geometry_p_c = SubElement(collision_p, "geometry")


	if randshape == "box":
		size_list = [round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1)]
		size_list_str = []
		for size in size_list:
			size_list_str.append(str(size))
		shape_p_c = SubElement(geometry_p_c, randshape, {'size': ' '.join(size_list_str)})
	if randshape == "cylinder":
		size_list = [round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1)]
		size_list_str = []
		for size in size_list:
			size_list_str.append(str(size))
		shape_p_c = SubElement(geometry_p_c, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
	if randshape == "sphere":
		size_list = [round(uniform(0.3,1.5),1)]
		size_list_str = []
		for size in size_list:
			size_list_str.append(str(size))
		shape_p_c = SubElement(geometry_p_c, randshape, {'radius': ''.join(size_list_str)})

	sizes_link_p = size_list
	sizes_link_str_p = size_list_str

	visual_p = SubElement(link_principal, "visual")
	origin_p_v = SubElement(visual_p, "origin", {'xyz': '0 0 0'})
	geometry_p_v = SubElement(visual_p, "geometry")

	if randshape == "box":
		shape_p_v = SubElement(geometry_p_v, randshape, {'size': ' '.join(size_list_str)})
	if randshape == "cylinder":
		shape_p_v = SubElement(geometry_p_v, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
	if randshape == "sphere":
		shape_p_v = SubElement(geometry_p_v, randshape, {'radius': ''.join(size_list_str)})

	dic_links = {"link_principal": Link("link_principal", randshape, sizes_link_p)}

	########
	for i in range(n_pecas-1):
		nome_link = 'link' + str(i+1)
		link = SubElement(root, "link", {'name': nome_link})

		inertial_l = SubElement(link, "inertial")
		mass_l = SubElement(inertial_l, "mass", {'value': '5'})
		inertia_l = SubElement(inertial_l, "inertia", {'ixx': '1.0', 'ixy': '0.0', 'ixz': '0.0', 'iyy': '1.0', 'iyz': '0.0','izz': '1.0'})

		randshape = shapes[randint(0,2)]

		collision_l = SubElement(link, "collision")
		origin_l_c = SubElement(collision_l, "origin", {'xyz': '0 0 0'})
		geometry_l_c = SubElement(collision_l, "geometry")

		if randshape == "box":
			size_list = [round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1)]
			size_list_str = []
			for size in size_list:
				size_list_str.append(str(size))
			shape_l_c = SubElement(geometry_l_c, randshape, {'size': ' '.join(size_list_str)})
		elif randshape == "cylinder":
			size_list = [round(uniform(0.3,1.5),1), round(uniform(0.3,1.5),1)]
			size_list_str = []
			for size in size_list:
				size_list_str.append(str(size))
			shape_l_c = SubElement(geometry_l_c, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
		elif randshape == "sphere":
			size_list = [round(uniform(0.3,1.5),1)]
			size_list_str = []
			for size in size_list:
				size_list_str.append(str(size))
			shape_l_c = SubElement(geometry_l_c, randshape, {'radius': ''.join(size_list_str)})

		sizes_link_t = size_list
		sizes_link_str_t = size_list_str

		visual_l = SubElement(link, "visual")
		origin_l_v = SubElement(visual_l, "origin", {'xyz': '0 0 0'})
		geometry_l_v = SubElement(visual_l, "geometry")

		if randshape == "box":
			shape_l_v = SubElement(geometry_l_v, randshape, {'size': ' '.join(size_list_str)})
		elif randshape == "cylinder":
			shape_l_v = SubElement(geometry_l_v, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
		elif randshape == "sphere":
			shape_l_v = SubElement(geometry_l_v, randshape, {'radius': ''.join(size_list_str)})

		dic_link_t = {i: Link(nome_link, randshape, sizes_link_t)}
		dic_links.update(dic_link_t)

		#######

		nome_joint = 'joint' + str(i+1)
		
		loop_key = True
		while loop_key:
			lista_keys = list(dic_links.keys())
			rand_key = lista_keys[randint(0, len(lista_keys)-2)]
			if dic_links[rand_key].peca_x or dic_links[rand_key].peca_mx or dic_links[rand_key].peca_y or dic_links[rand_key].peca_my or dic_links[rand_key].peca_z or dic_links[rand_key].peca_mz:
				loop_key = False
			else:
				loop_key = True

		link_parente = dic_links[rand_key].nome
		list_sizes = dic_links[rand_key].dimensoes

		print(list_sizes, sizes_link_t)

		dist_origens = []
		for h in range(len(list_sizes)):
			if len(sizes_link_t) == len(list_sizes):
				if len(sizes_link_t) == 3:
					dist_origens.append(list_sizes[h]/2+sizes_link_t[h]/2)
				else:
					dist_origens.append(list_sizes[h]+sizes_link_t[h])

			elif len(sizes_link_t) > len(list_sizes) and len(list_sizes) == 1:
				for j in range(len(sizes_link_t)):
					if len(sizes_link_t) == 3:
						dist_origens.append(sizes_link_t[h]/2 +list_sizes[0])
					else:
						dist_origens.append(sizes_link_t[h]+list_sizes[0])


			elif len(sizes_link_t) > len(list_sizes) and len(list_sizes) == 2:
				if h == 0:
					if len(sizes_link_t) == 3:
						dist_origens.append(sizes_link_t[0]/2+list_sizes[h])
						dist_origens.append(sizes_link_t[1]/2+list_sizes[h])
					else:
						dist_origens.append(sizes_link_t[0]+list_sizes[h])
						dist_origens.append(sizes_link_t[1]+list_sizes[h])
				else:
					if len(sizes_link_t) == 3:
						dist_origens.append(sizes_link_t[2]/2+list_sizes[h])
					else:
						dist_origens.append(sizes_link_t[2]+list_sizes[h])


			elif len(sizes_link_t) < len(list_sizes) and len(sizes_link_t) == 1:
				if len(sizes_link_t) == 3:
					dist_origens.append(sizes_link_t[0]/2+list_sizes[h])
				else:
					dist_origens.append(sizes_link_t[0]+list_sizes[h])


			elif len(sizes_link_t) < len(list_sizes) and len(sizes_link_t) == 2:
				if h <= 1:
					if len(sizes_link_t) == 3:
						dist_origens.append(sizes_link_t[0]/2+list_sizes[h])
					else:
						dist_origens.append(sizes_link_t[0]+list_sizes[h])
				else:
					if len(sizes_link_t) == 3:
						dist_origens.append(sizes_link_t[1]/2+list_sizes[h])
					else:
						dist_origens.append(sizes_link_t[1]+list_sizes[h])

		loop_lado = True
		while loop_lado:
			rand_lado = randint(0, len(list_sizes)-1)
			rand_lado2 = randint(0,1)

			if rand_lado == 0:
				rand_dist = round(uniform(list_sizes[0],dist_origens[0]),1)
				if rand_lado2 == 0 and dic_links[rand_key].peca_x:
					size_list_j = [str(rand_dist), '0', '0']
					dic_links[rand_key].peca_x = False
					dic_links[i].peca_mx = False
					loop_lado = False

				elif rand_lado2 == 1 and dic_links[rand_key].peca_mx:
					size_list_j = ["-"+str(rand_dist), '0', '0']
					dic_links[rand_key].peca_mx = False
					dic_links[i].peca_x = False
					loop_lado = False

			if rand_lado == 1:
				if len(dist_origens) == 1:
					rand_dist = round(uniform(list_sizes[1],dist_origens[0]),1)
				else:
					rand_dist = round(uniform(list_sizes[1],dist_origens[1]),1)
				if rand_lado2 == 0 and dic_links[rand_key].peca_y:
					size_list_j = ['0', str(rand_dist), '0']
					dic_links[rand_key].peca_y = False
					dic_links[i].peca_my = False
					loop_lado = False

				elif rand_lado2 == 1 and dic_links[rand_key].peca_my:
					size_list_j = ['0', "-"+str(rand_dist), '0']
					dic_links[rand_key].peca_my = False
					dic_links[i].peca_y = False
					loop_lado = False

			if rand_lado == 2:
				if len(dist_origens) == 2:
					rand_dist = round(uniform(list_sizes[2],dist_origens[1]),1)
				elif len(dist_origens) == 1:
					rand_dist = round(uniform(list_sizes[2],dist_origens[0]),1)
				else:
					rand_dist = round(uniform(list_sizes[2],dist_origens[2]),1)

				if rand_lado2 == 0 and dic_links[rand_key].peca_z:
					size_list_j = ['0', '0', str(rand_dist)]
					dic_links[rand_key].peca_z = False
					dic_links[i].peca_mz = False
					loop_lado = False

				elif rand_lado2 == 1 and dic_links[rand_key].peca_mz:
					size_list_j = ['0', '0', "-"+str(rand_dist)]
					dic_links[rand_key].peca_mz = False
					dic_links[i].peca_z = False
					loop_lado = False

		joint_types = ["fixed", "continuous", "continuous"]

		joint = SubElement(root, "joint", {'name': nome_joint, 'type': choice(joint_types)})
		origin_j = SubElement(joint, "origin", {'xyz': ' '.join(size_list_j)})
		parent_j = SubElement(joint, "parent", {'link': link_parente})
		parent_j = SubElement(joint, "child", {'link': nome_link})

		###################

	return root

tree = ElementTree(cria_carro())
tree.write("oba.urdf")

#print(dic_links[0].link)