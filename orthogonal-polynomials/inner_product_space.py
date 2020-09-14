from sympy import simplify, sqrt

class InnerProductSpace:
    def inner(self, f, g):
        pass

    def norm(self, f):
        return sqrt(self.inner(f, f))

    def normalize(self, f):
        return f / self.norm(f)

    def orthonormalize(self, basis):
        orth_basis = []
        for v in basis:
            subtracted = [self.inner(v, e) * e for e in orth_basis]
            e = self.normalize(v - sum(subtracted))
            orth_basis.append(simplify(e))
        return orth_basis

    def approximate(self, func, basis):
        orth_basis = self.orthonormalize(basis)
        expr = sum([(self.inner(func, e) * e) for e in orth_basis])
        return simplify(expr)
