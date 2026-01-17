import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import time

# -------------------------------
# APPROXIMATE VERTEX COVER (2-Approx)
# -------------------------------
def approximate_vertex_cover(G):
    cover = set()
    edges = list(G.edges())

    while edges:
        u, v = edges.pop()
        cover.add(u)
        cover.add(v)

        # remove all edges incident to u or v
        edges = [(x, y) for (x, y) in edges if x not in (u, v) and y not in (u, v)]

    return cover


# -------------------------------
# STREAMLIT UI
# -------------------------------
st.set_page_config(page_title="Approximate Vertex Cover – CCP", layout="wide")

st.title("🔐 Approximate Vertex Cover for Network Security Monitoring")
st.markdown("""
**Design and Analysis of Algorithms – CCP**

This application demonstrates a **polynomial-time approximation algorithm**
for the **Vertex Cover problem**, which is **NP-Hard**.
""")

# -------------------------------
# INPUTS
# -------------------------------
st.sidebar.header("Graph Configuration")

num_vertices = st.sidebar.slider("Number of Devices (Vertices)", 5, 100, 20)
num_edges = st.sidebar.slider("Number of Communication Links (Edges)", 5, 300, 40)
seed = st.sidebar.number_input("Random Seed", value=42)

generate = st.sidebar.button("Generate Network & Solve")

# -------------------------------
# MAIN LOGIC
# -------------------------------
if generate:
    random.seed(seed)
    G = nx.gnm_random_graph(num_vertices, num_edges, seed=seed)

    st.subheader("📊 Network Statistics")
    st.write(f"**Total Devices:** {G.number_of_nodes()}")
    st.write(f"**Total Links:** {G.number_of_edges()}")

    # Run Approximation Algorithm
    start = time.time()
    vertex_cover = approximate_vertex_cover(G)
    end = time.time()

    st.subheader("✅ Approximate Vertex Cover Result")
    st.write(f"**Selected Devices:** {len(vertex_cover)}")
    st.write(f"**Execution Time:** {end - start:.4f} seconds")

    st.markdown("""
    🔹 This is a **2-Approximation Algorithm**  
    🔹 Guaranteed solution ≤ **2 × Optimal Vertex Cover**  
    🔹 Runs in **polynomial time**
    """)

    # -------------------------------
    # VISUALIZATION
    # -------------------------------
    st.subheader("📌 Network Visualization")

    pos = nx.spring_layout(G, seed=seed)

    plt.figure(figsize=(10, 8))

    # Nodes
    nx.draw_networkx_nodes(
        G, pos,
        node_color=["red" if n in vertex_cover else "lightblue" for n in G.nodes()],
        node_size=500
    )

    # Edges
    nx.draw_networkx_edges(G, pos, alpha=0.6)

    # Labels
    nx.draw_networkx_labels(G, pos, font_size=8)

    st.pyplot(plt)

    st.markdown("""
    **🔴 Red Nodes** → Selected for monitoring (Vertex Cover)  
    **🔵 Blue Nodes** → Not selected
    """)

# -------------------------------
# THEORY SECTION
# -------------------------------
st.subheader("📘 Why Approximation?")
st.markdown("""
- Vertex Cover is an **NP-Hard problem**
- Exact solutions are impractical for large networks
- Approximation ensures:
  - Fast execution
  - Near-optimal solutions
  - Scalability to thousands of devices
""")

st.subheader("🎯 CCP Outcomes Achieved")
st.markdown("""
✔ Graph modeling  
✔ Approximation algorithm  
✔ Large-scale simulation  
✔ Visualization for validation  
✔ Efficient resource allocation
""")
