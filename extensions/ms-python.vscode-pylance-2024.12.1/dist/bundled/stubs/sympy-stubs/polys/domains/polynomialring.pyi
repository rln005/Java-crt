from typing import Any, Literal

from sympy.polys.domains.compositedomain import CompositeDomain
from sympy.polys.domains.ring import Ring
from sympy.polys.rings import PolyElement
from sympy.utilities import public

class PolynomialRing(Ring, CompositeDomain):
    is_Poly = ...
    has_assoc_Ring = ...
    has_assoc_Field = ...
    def __init__(self, domain_or_ring, symbols=..., order=...) -> None: ...
    def new(self, element) -> PolyElement: ...
    @property
    def zero(self): ...
    @property
    def one(self): ...
    @property
    def order(self): ...
    def __str__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def is_unit(self, a) -> Literal[False]: ...
    def canonical_unit(self, a): ...
    def to_sympy(self, a): ...
    def from_sympy(self, a): ...
    def from_ZZ(K1, a, K0): ...
    def from_ZZ_python(K1, a, K0): ...
    def from_QQ(K1, a, K0): ...
    def from_QQ_python(K1, a, K0): ...
    def from_ZZ_gmpy(K1, a, K0): ...
    def from_QQ_gmpy(K1, a, K0): ...
    def from_GaussianIntegerRing(K1, a, K0): ...
    def from_GaussianRationalField(K1, a, K0): ...
    def from_RealField(K1, a, K0): ...
    def from_ComplexField(K1, a, K0): ...
    def from_AlgebraicField(K1, a, K0) -> PolyElement | None: ...
    def from_PolynomialRing(K1, a, K0) -> None: ...
    def from_FractionField(K1, a, K0) -> None: ...
    def from_GlobalPolynomialRing(K1, a, K0) -> None: ...
    def get_field(self) -> Any: ...
    def is_positive(self, a): ...
    def is_negative(self, a): ...
    def is_nonpositive(self, a): ...
    def is_nonnegative(self, a): ...
    def gcdex(self, a, b): ...
    def gcd(self, a, b): ...
    def lcm(self, a, b): ...
    def factorial(self, a): ...