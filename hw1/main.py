import ast
import inspect
import networkx as nx


class Walker(ast.NodeVisitor):
    def __init__(self):
        self.stack = []
        self.graph = nx.Graph()

    def generic_visit(self, stmt):
        node_name = str(stmt)
        parent_name = None
        if self.stack:
            parent_name = self.stack[-1]
        self.stack.append(node_name)
        
        node_type = str(type(stmt))[13:-2]
        #print(stmt)
        if hasattr(stmt, "name"):
            label = node_type + ' ' + stmt.name
        elif hasattr(stmt, "id"):
            label = node_type + ' ' + stmt.id
        else:
            label = node_type
            
        self.graph.add_node(node_name, label=label)
        if parent_name:
            self.graph.add_edge(node_name, parent_name)

        super(self.__class__, self).generic_visit(stmt)
        self.stack.pop()
        

if __name__ == '__main__':
    ast_object = ast.parse(open('fib.py', 'r').read())
    walker = Walker()
    walker.visit(ast_object)
    img = nx.drawing.nx_pydot.to_pydot(walker.graph)
    img.write_png('artifacts/graph.png')
