import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def vertex_cover_approx(edges):
    """
    Implements 2-Approximation Vertex Cover Algorithm
    """
    cover = set()
    edges_set = set(edges)
    while edges_set:
        (u, v) = edges_set.pop()
        cover.add(u)
        cover.add(v)
        edges_set = {e for e in edges_set if u not in e and v not in e}
    return cover


def draw_graph(edges, cover=None):
    """
    Draws the graph using networkx and matplotlib.
    Highlights the vertex cover nodes if provided.
    """
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)

    fig, ax = plt.subplots(figsize=(8, 6))

    node_colors = (
        ['red' if node in cover else 'lightblue' for node in G.nodes()]
        if cover else 'lightblue'
    )

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500, ax=ax)
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    return fig


# Streamlit app
st.set_page_config(page_title="Network Security Monitoring", layout="wide")

# 🔹 ADDED TEXT (ONLY THIS)
st.markdown("""
## 🔐 Network Security Monitoring
### Approximate Vertex Cover using 2-Approximation Algorithm

This application demonstrates an **approximate solution** to the  
**Vertex Cover problem**.

- Vertex Cover is **NP-Hard**
- Exact solutions are infeasible for large networks
- A **2-Approximation algorithm** is used for efficiency
""")

# Initialize session state
if 'edges' not in st.session_state:
    st.session_state.edges = []

# Sidebar for adding edges
with st.sidebar:
    st.header("Add Connection")
    col1, col2 = st.columns(2)
    u = col1.text_input("Node U", key="u_input")
    v = col2.text_input("Node V", key="v_input")

    if st.button("Add Edge"):
        if u and v:
            st.session_state.edges.append((u, v))
            st.success(f"Added edge: ({u}, {v})")
        else:
            st.warning("Please enter both nodes.")

    if st.button("Clear All Edges"):
        st.session_state.edges = []
        st.success("Cleared all edges.")

# Main content
st.title("Network Security Monitoring")
st.subheader("Approximate Vertex Cover (2-Approximation)")

# Display current network
st.header("Current Network Connections")
if st.session_state.edges:
    for edge in st.session_state.edges:
        st.write(edge)
else:
    st.info("No connections added yet.")

# Visualize graph
if st.session_state.edges:
    st.header("Network Visualization")
    fig = draw_graph(st.session_state.edges)
    st.pyplot(fig)

# Run algorithm
if st.button("Run Vertex Cover Algorithm", type="primary"):
    if st.session_state.edges:
        cover = vertex_cover_approx(st.session_state.edges)
        st.header("Selected Monitoring Devices (Vertex Cover)")
        st.write(cover)
        st.write(f"Total devices selected: {len(cover)}")

        st.header("Visualization with Vertex Cover Highlighted")
        fig_cover = draw_graph(st.session_state.edges, cover)
        st.pyplot(fig_cover)
    else:
        st.warning("Please add some connections first.")

# Footer
st.markdown("---")
st.caption("Built with Streamlit for modern UI/UX. Design and Analysis of Algorithms - CCP")
