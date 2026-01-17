import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import time
import random

# -------------------------------------------------
# 2-Approximation Vertex Cover Algorithm
# -------------------------------------------------
def vertex_cover_approx(edges):
    """
    Implements 2-Approximation Vertex Cover Algorithm
    Time Complexity: O(E)
    """
    cover = set()
    edges_set = set(edges)

    while edges_set:
        (u, v) = edges_set.pop()
        cover.add(u)
        cover.add(v)
        edges_set = {e for e in edges_set if u not in e and v not in e}

    return cover


# -------------------------------------------------
# Graph Visualization
# -------------------------------------------------
def draw_graph(edges, cover=None):
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G, seed=42)

    fig, ax = plt.subplots(figsize=(8, 6))

    node_colors = [
        "red" if cover and node in cover else "lightblue"
        for node in G.nodes()
    ]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    ax.set_title("Network Graph Visualization")
    ax.axis("off")
    return fig


# -------------------------------------------------
# Streamlit App Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Approximate Vertex Cover – CCP",
    layout="wide"
)

st.title("🔐 Network Security Monitoring")
st.subheader("Approximate Vertex Cover using 2-Approximation Algorithm")

st.markdown("""
This application demonstrates an **approximate solution** to the  
**Vertex Cover problem**,_ATTACHMENT833

- Vertex Cover is **NP-Hard**
- Exact solutions are infeasible for large networks
- A **2-Approximation algorithm** is used for efficiency
""")

# -------------------------------------------------
# Session State
# -------------------------------------------------
if "edges" not in st.session_state:
    st.session_state.edges = []

# -------------------------------------------------
# Sidebar – Graph Configuration
# -------------------------------------------------
with st.sidebar:
    st.header("Graph Configuration")

    n = st.slider("Number of Devices (Vertices)", 5, 200, 20)
    m = st.slider("Number of Communication Links (Edges)", 5, 500, 40)
    seed = st.number_input("Random Seed", value=42)

    if st.button("Generate Network & Solve"):
        random.seed(seed)
        G = nx.gnm_random_graph(n, m, seed=seed)
        st.session_state.edges = list(G.edges())

    st.markdown("---")
    st.header("Manual Edge Entry")

    col1, col2 = st.columns(2)
    u = col1.text_input("Node U")
    v = col2.text_input("Node V")

    if st.button("Add Edge"):
        if u and v:
            st.session_state.edges.append((u, v))
            st.success(f"Added edge ({u}, {v})")
        else:
            st.warning("Enter both nodes")

    if st.button("Clear All Edges"):
        st.session_state.edges = []
        st.success("All edges cleared")


# -------------------------------------------------
# Main Content
# -------------------------------------------------
st.header("📊 Current Network")

if not st.session_state.edges:
    st.info("No network created yet.")
else:
    st.write(f"**Total Edges:** {len(st.session_state.edges)}")

    fig = draw_graph(st.session_state.edges)
    st.pyplot(fig)

    # -------------------------------------------------
    # Run Algorithm
    # -------------------------------------------------
