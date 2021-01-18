class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)

        overlap = 0
        if A <= E <= G <= C:
            if F <= B <= D <= H:
                overlap = (G - E) * (D - B)
            if F <= B <= H <= D:
                overlap = (G - E) * (H - B)
            if B <= F <= H <= D:
                overlap = (G - E) * (H - F)
            if B <= F <= D <= H:
                overlap = (G - E) * (D - F)

        if E <= A <= C <= G:
            if F <= B <= D <= H:
                overlap = (C - A) * (D - B)
            if F <= B <= H <= D:
                overlap = (C - A) * (H - B)
            if B <= F <= H <= D:
                overlap = (C - A) * (H - F)
            if B <= F <= D <= H:
                overlap = (C - A) * (D - F)

        if A <= E <= C <= G:
            if F <= B <= D <= H:
                overlap = (C - E) * (D - B)
            if F <= B <= H <= D:
                overlap = (C - E) * (H - B)
            if B <= F <= H <= D:
                overlap = (C - E) * (H - F)
            if B <= F <= D <= H:
                overlap = (C - E) * (D - F)

        if E <= A <= G <= C:
            if F <= B <= D <= H:
                overlap = (G - A) * (D - B)
            if F <= B <= H <= D:
                overlap = (G - A) * (H - B)
            if B <= F <= H <= D:
                overlap = (G - A) * (H - F)
            if B <= F <= D <= H:
                overlap = (G - A) * (D - F)
        return s1 + s2 - overlap
