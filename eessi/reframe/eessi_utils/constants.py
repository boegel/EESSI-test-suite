"""
Constants for ReFrame tests
"""
DEVICES = {
    'GPU': 'gpu',
    'CPU': 'cpu',
}

TAGS = {
    'CI': 'CI',
}

FEATURES = {
    'GPU': 'gpu',
    'CPU': 'cpu',
}

SCALES = {
        # required keys:
        # - num_nodes
        # - either node_part or (num_cpus_per_node and num_gpus_per_node)
        '1_core': {'num_nodes': 1, 'num_cpus_per_node': 1, 'num_gpus_per_node': 1},
        '2_cores': {'num_nodes': 1, 'num_cpus_per_node': 2, 'num_gpus_per_node': 1},
        '4_cores': {'num_nodes': 1, 'num_cpus_per_node': 4, 'num_gpus_per_node': 1},
        '1_8_node': {'num_nodes': 1, 'node_part': 8},  # 1/8 node
        '1_4_node': {'num_nodes': 1, 'node_part': 4},  # 1/4 node
        '1_2_node': {'num_nodes': 1, 'node_part': 2},  # 1/2 node
        '1_node': {'num_nodes': 1, 'node_part': 1},
        '2_nodes': {'num_nodes': 2, 'node_part': 1},
        '4_nodes': {'num_nodes': 4, 'node_part': 1},
        '8_nodes': {'num_nodes': 8, 'node_part': 1},
        '16_nodes': {'num_nodes': 16, 'node_part': 1},
}
