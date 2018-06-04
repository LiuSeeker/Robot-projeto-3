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
		self.list_dist = 0

	def dist(self, size_p, size_t):
		dist_origens = []
		for h in range(len(size_p)):
			if len(size_t) == len(size_p):
				if len(size_t) == 3:
					dist_origens.append(size_p[h]/2+size_t[h]/2)
				else:
					dist_origens.append(size_p[h]+size_t[h])

			elif len(size_t) > len(size_p) and len(size_p) == 1:
				for j in range(len(size_t)):
					if len(size_t) == 3:
						dist_origens.append(size_t[h]/2 +size_p[0])
					else:
						dist_origens.append(size_t[h]+size_p[0])


			elif len(size_t) > len(size_p) and len(size_p) == 2:
				if h == 0:
					if len(size_t) == 3:
						dist_origens.append(size_t[0]/2+size_p[h])
						dist_origens.append(size_t[1]/2+size_p[h])
					else:
						dist_origens.append(size_t[0]+size_p[h])
						dist_origens.append(size_t[1]+size_p[h])
				else:
					if len(size_t) == 3:
						dist_origens.append(size_t[2]/2+size_p[h])
					else:
						dist_origens.append(size_t[2]+size_p[h])


			elif len(size_t) < len(size_p) and len(size_t) == 1:
				if len(size_t) == 3:
					dist_origens.append(size_t[0]/2+size_p[h])
				else:
					dist_origens.append(size_t[0]+size_p[h])


			elif len(size_t) < len(size_p) and len(size_t) == 2:
				if h <= 1:
					if len(size_t) == 3:
						dist_origens.append(size_t[0]/2+size_p[h])
					else:
						dist_origens.append(size_t[0]+size_p[h])
				else:
					if len(size_t) == 3:
						dist_origens.append(size_t[1]/2+size_p[h])
					else:
						dist_origens.append(size_t[1]+size_p[h])

		self.list_dist = dist_origens

class Joint:
	def __init__(self, nome, tipo, parent, child):
		self.nome = nome
		self.tipo = tipo
		self.parent = parent
		self.child = child
		self.vel = 0
		self.force = 0


def cria_urdf():
	global dic_links
	global dic_joints
	dic_joints = {}
	#n_pneus = randint(3,6)
	n_pecas = randint(2,5)
	#n_pecas = 3

	shapes = ["box", "cylinder", "sphere"] # Tipos de shapes do link

	root = Element("robot", {'name': 'nome_robo'})

	link_principal = SubElement(root, "link", {'name': 'link_principal'})

	inertial_p = SubElement(link_principal, "inertial")
	mass_p = SubElement(inertial_p, "mass", {'value': '5'})
	inertia_p = SubElement(inertial_p, "inertia", {'ixx': '1.0', 'ixy': '0.0', 'ixz': '0.0', 'iyy': '1.0', 'iyz': '0.0','izz': '1.0'})

	randshape = shapes[randint(0,2)] # Escolhe shape

	collision_p = SubElement(link_principal, "collision")
	origin_p_c = SubElement(collision_p, "origin", {'xyz': '0 0 1'})
	geometry_p_c = SubElement(collision_p, "geometry")


	# Define as dimensões baseadas no shape
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

	# Lista das dimensões do link
	sizes_link_p = size_list
	sizes_link_str_p = size_list_str

	visual_p = SubElement(link_principal, "visual")
	origin_p_v = SubElement(visual_p, "origin", {'xyz': '0 0 1'})
	geometry_p_v = SubElement(visual_p, "geometry")

	if randshape == "box":
		shape_p_v = SubElement(geometry_p_v, randshape, {'size': ' '.join(size_list_str)})
	if randshape == "cylinder":
		shape_p_v = SubElement(geometry_p_v, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
	if randshape == "sphere":
		shape_p_v = SubElement(geometry_p_v, randshape, {'radius': ''.join(size_list_str)})

	# Adiciona o link ao dicionario
	dic_links = {"link_principal": Link("link_principal", randshape, sizes_link_p)}

	########

	for i in range(n_pecas-1):
		nome_link = 'link' + str(i+1)
		link = SubElement(root, "link", {'name': nome_link})

		inertial_l = SubElement(link, "inertial")
		mass_l = SubElement(inertial_l, "mass", {'value': '5'})
		inertia_l = SubElement(inertial_l, "inertia", {'ixx': '1.0', 'ixy': '0.0', 'ixz': '0.0', 'iyy': '1.0', 'iyz': '0.0','izz': '1.0'})

		randshape = shapes[randint(0,2)] # Escolhe shape

		collision_l = SubElement(link, "collision")
		origin_l_c = SubElement(collision_l, "origin", {'xyz': '0 0 1'})
		geometry_l_c = SubElement(collision_l, "geometry")

		# Define as dimensões baseadas no shape
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

		# Lista das dimensões do link
		sizes_link_t = size_list
		sizes_link_str_t = size_list_str

		visual_l = SubElement(link, "visual")
		origin_l_v = SubElement(visual_l, "origin", {'xyz': '0 0 1'})
		geometry_l_v = SubElement(visual_l, "geometry")

		if randshape == "box":
			shape_l_v = SubElement(geometry_l_v, randshape, {'size': ' '.join(size_list_str)})
		elif randshape == "cylinder":
			shape_l_v = SubElement(geometry_l_v, randshape, {'radius': size_list_str[0], 'length': size_list_str[1]})
		elif randshape == "sphere":
			shape_l_v = SubElement(geometry_l_v, randshape, {'radius': ''.join(size_list_str)})

		# Adiciona o link ao dicionario
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


		dic_links[i].dist(list_sizes, sizes_link_t)
		

		loop_lado = True
		while loop_lado:
			rand_lado = randint(0,2)

			rand_lado2 = randint(0,1)

			if rand_lado == 0:
				rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[0]),1)
				if rand_lado2 == 0 and dic_links[rand_key].peca_x:
					size_list_j = [str(rand_dist), '0', '1']
					dic_links[rand_key].peca_x = False
					dic_links[i].peca_mx = False
					loop_lado = False

				elif rand_lado2 == 1 and dic_links[rand_key].peca_mx:
					size_list_j = ["-"+str(rand_dist), '0', '1']
					dic_links[rand_key].peca_mx = False
					dic_links[i].peca_x = False
					loop_lado = False

			if rand_lado == 1:
				if len(dic_links[i].list_dist) == 1 and len(list_sizes) == 1:
					rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[0]),1)
				elif len(dic_links[i].list_dist) == 1:
					rand_dist = round(uniform(list_sizes[1],dic_links[i].list_dist[0]),1)
				elif len(list_sizes) == 1:
					rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[1]),1)
				else:
					rand_dist = round(uniform(list_sizes[1],dic_links[i].list_dist[1]),1)
				if rand_lado2 == 0 and dic_links[rand_key].peca_y:
					size_list_j = ['0', str(rand_dist), '1']
					dic_links[rand_key].peca_y = False
					dic_links[i].peca_my = False
					loop_lado = False

				elif rand_lado2 == 1 and dic_links[rand_key].peca_my:
					size_list_j = ['0', "-"+str(rand_dist), '1']
					dic_links[rand_key].peca_my = False
					dic_links[i].peca_y = False
					loop_lado = False

			if rand_lado == 2:
				if len(dic_links[i].list_dist) == 1 and len(list_sizes) == 1:
					rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[0]),1)
				elif len(dic_links[i].list_dist) == 2 and len(list_sizes) == 1:
					rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[1]),1)
				elif len(dic_links[i].list_dist) == 3 and len(list_sizes) == 1:
					rand_dist = round(uniform(list_sizes[0],dic_links[i].list_dist[2]),1)
				elif len(dic_links[i].list_dist) == 1 and len(list_sizes) == 2:
					rand_dist = round(uniform(list_sizes[1],dic_links[i].list_dist[0]),1)
				elif len(dic_links[i].list_dist) == 2 and len(list_sizes) == 2:
					rand_dist = round(uniform(list_sizes[1],dic_links[i].list_dist[1]),1)
				elif len(dic_links[i].list_dist) == 3 and len(list_sizes) == 2:
					rand_dist = round(uniform(list_sizes[1],dic_links[i].list_dist[2]),1)
				elif len(dic_links[i].list_dist) == 2 and len(list_sizes) == 3:
					rand_dist = round(uniform(list_sizes[2],dic_links[i].list_dist[1]),1)
				elif len(dic_links[i].list_dist) == 1 and len(list_sizes) == 3:
					rand_dist = round(uniform(list_sizes[2],dic_links[i].list_dist[0]),1)
				else:
					rand_dist = round(uniform(list_sizes[2],dic_links[i].list_dist[2]),1)

				if rand_lado2 == 0 and dic_links[rand_key].peca_z:
					size_list_j = ['0', '0', str(rand_dist+1)]
					dic_links[rand_key].peca_z = False
					dic_links[i].peca_mz = False
					loop_lado = False

		joint_types = ["fixed", "continuous", "continuous"]

		rand_type = choice(joint_types)

		joint = SubElement(root, "joint", {'name': nome_joint, 'type': rand_type})
		origin_j = SubElement(joint, "origin", {'xyz': ' '.join(size_list_j)})
		parent_j = SubElement(joint, "parent", {'link': link_parente})
		parent_j = SubElement(joint, "child", {'link': nome_link})

		dic_joint_t = {i: Joint(nome_joint, rand_type, link_parente, nome_link)}
		dic_joints.update(dic_joint_t)

		###################

	return root


def escreve_urdf():
	tree = ElementTree(cria_urdf())
	tree.write("oba.urdf")

#print(dic_links, dic_joints)