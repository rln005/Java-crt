from networkx.utils.backends import _dispatchable

@_dispatchable
def tensor_product(G, H): ...
@_dispatchable
def cartesian_product(G, H): ...
@_dispatchable
def lexicographic_product(G, H): ...
@_dispatchable
def strong_product(G, H): ...
@_dispatchable
def power(G, k): ...
@_dispatchable
def rooted_product(G, H, root): ...
@_dispatchable
def corona_product(G, H): ...