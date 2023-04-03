from manim import *
from math import ceil

n = 10
part_size = 3
colors = [BLUE, GREEN, RED, YELLOW]

class MatrixAnimation(Scene):
    def construct(self):
        # Define the matrix
        elements = [i for i in range(1, n+1)]
        m = Matrix([elements])
        
        # Define the matrix elements as a VGroup
        matrix_elements = VGroup()
        matrix_elements.add(m)
        # Position the matrix elements
        matrix_elements.arrange_in_grid(rows=1, buff=0.5)
        
        # Add the matrix elements to the scene and animate them
        self.play(Create(matrix_elements, lag_ratio=0.2))
        self.wait(1)
        
        self.play(
            matrix_elements.animate.shift(2 * UP)
        )
        partition_add_text = Text(f"Particionamos el arreglo en subarreglos de tamaño {3}", font_size=0.4 * DEFAULT_FONT_SIZE)
        self.play(FadeIn(partition_add_text))
        self.wait(2)
        self.play(FadeOut(partition_add_text))
        groups = []
        for i in range(1, n+1, part_size):
            m_i = Matrix([[j for j in range(i, min(i + part_size, n + 1))]])
            m_i.set_row_colors(colors[i%len(colors)])
            g_i = VGroup(m_i)
            g_i.arrange_in_grid(rows=1, buff=0.5)
            groups.append(g_i)
        partitions = VGroup()
        [partitions.add(p) for p in groups]
        partitions.arrange_in_grid(rows=1, cols=ceil(n / part_size))
        self.add(partitions)
        self.play(Create(partitions))
        self.play(
            FadeOut(matrix_elements),
            partitions.animate.shift(2 * UP)
        )
        partition_sum_text = Text(f"Ahora, sumemos cada particion en paralelo", font_size=0.4 * DEFAULT_FONT_SIZE)
        partition_sum_text.shift(DOWN)
        self.play(FadeIn(partition_sum_text))
        self.wait(2)
        self.play(FadeOut(partition_sum_text))
        sum_groups = []
        for i in range(0, n, part_size):
            m_i = Matrix([[sum(elements[i:min(i + part_size, len(elements))])]])
            m_i.set_row_colors(colors[(i+1)%len(colors)])
            g_i = VGroup(m_i)
            g_i.align_to(groups[len(sum_groups)], UP)
            sum_groups.append(g_i)
        self.wait(1)
        sums = VGroup()
        [sums.add(s) for s in sum_groups]
        sums.arrange_in_grid(rows=1, cols=len(sum_groups), buff=0.5)
        sums.move_to(ORIGIN)
        self.play(
            FadeIn(sums)
        )
        self.wait(2)
        self.play(
            FadeOut(partitions),
            sums.animate.shift(UP)
        )
        result_text = Text(f"Finalmente, vamos a sumar el resultado de cada particion en el hilo principal para obtener el resultado final", font_size=0.4 * DEFAULT_FONT_SIZE)
        self.play(FadeIn(result_text))
        res = Matrix([[sum(elements)]])
        res_group = VGroup(res)
        self.wait(2)
        self.play(FadeOut(result_text))
        self.play(
            FadeIn(res_group)
        )
        self.wait(1)
        final = VGroup()
        final.add(matrix_elements)
        final.add(partitions)
        final.add(sums)
        final.add(res_group)
        final.arrange_in_grid(rows=4, cols=1)
        self.play(
            Create(final)
        )
        self.wait(5)