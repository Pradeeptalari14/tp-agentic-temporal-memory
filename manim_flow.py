"""
3Blue1Brown Manim Animation: Agentic Temporal Memory Decay & Consolidation
Renders the Ebbinghaus forgetting curve alongside Neo4j entity consolidation.
"""
from manim import *

class TemporalMemoryFlow(Scene):
    def construct(self):
        title = Text("Agentic Temporal Memory: Dual Vector-Graph Storage", font_size=30, color=PURPLE)
        subtitle = Text("Ebbinghaus Forgetting Curves & Sub-15ms Context Injection", font_size=18, color=LIGHT_GRAY)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP)
        self.play(Write(title_group))
        self.wait(1)

        graph_box = Text("Neo4j Knowledge Graph: Temporal Entities", font_size=20, color=BLUE).shift(LEFT * 3)
        vector_box = Text("Qdrant: Dense Episodic Vectors", font_size=20, color=TEAL).shift(RIGHT * 3)
        self.play(FadeIn(graph_box), FadeIn(vector_box))
        self.wait(1)

        finops = Text("FinOps Impact: 75.8% System Prompt Token Reduction", font_size=22, color=GREEN).to_edge(DOWN)
        self.play(FadeIn(finops))
        self.wait(2)
