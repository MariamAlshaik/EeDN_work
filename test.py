import networkx as nx
import pylab as plt
import json
from networkx.readwrite import json_graph


class SetEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def serialize_graph(graph):
    json_data = json_graph.node_link_data(graph)
    serial_data = json.dumps(json_data, separators=(',', ':'), indent = 4, cls = SetEncoder)
    return serial_data
