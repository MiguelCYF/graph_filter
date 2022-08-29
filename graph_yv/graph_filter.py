import networkx as nx
import matplotlib.pyplot as plt


def filter_edges(edges, input_nodes, threshold):
    """
    找到和输入节点有 $threshold 个关联的节点，并输出它们之间的关系
    :param edges: [(n1,n2),(n1,n3)...]
    :param input_nodes: [n1,n2,n3...]
    :param threshold
    :return: edges:[(n5,n6),(n7,n8)...]
    """

    temp_to_nodes = set()
    for edge in edges:
        temp_to_nodes.add(edge[0])
        temp_to_nodes.add(edge[1])
    nodes = list(temp_to_nodes)

    graph = nx.Graph()
    graph.add_nodes_from(nodes)
    graph.add_edges_from(edges)

    final_edges = []
    # 执行算法
    for target_node in nodes:
        bfs = bfs_execute(target_node, graph)
        bfs_edge_arr = [i for i in bfs]

        if file_execute(bfs_edge_arr, target_node, input_nodes, threshold):
            for temp_edge in bfs_edge_arr:
                final_edges.append(temp_edge)

    draw(final_edges)

    result_arr = []
    for edge in final_edges:
        # 算法可能会改变边的方向，所以通过下面的判断，还原边的方向
        if edge in edges:
            result_arr.append({"src": edge[0], "desc": edge[1]})
        else:
            result_arr.append({"src": edge[1], "desc": edge[0]})

    return result_arr


def bfs_execute(node, graph):
    bfs = nx.bfs_predecessors(graph, node, False, 1)
    return bfs


def file_execute(bfs_edge_arr, target_node, input_nodes, threshold):
    """
    执行过滤逻辑
    :param bfs_edge_arr:
    :param target_node:
    :param input_nodes:
    :param threshold:
    :return:
    """
    cnt = 0
    threshold = int(threshold)

    if target_node not in input_nodes:
        for bfs_edge in bfs_edge_arr:
            if (bfs_edge[0] in input_nodes) or (bfs_edge[1] in input_nodes):
                cnt += 1

                if cnt >= threshold:
                    return True

    return False


def draw(input_edges):
    edges = []
    temp_to_nodes = set()

    for edge in input_edges:
        # 添加点
        temp_to_nodes.add(edge[0])
        temp_to_nodes.add(edge[1])

        # 添加边
        edges.append((edge[0], edge[1]))

    nodes = list(temp_to_nodes)

    graph = nx.Graph()

    for node in nodes:
        graph.add_node(node)

    graph.add_edges_from(edges)

    nx.draw(graph, with_labels=True, node_color='y', )
    plt.show()


if __name__ == '__main__':
    filter_edges()