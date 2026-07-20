<script>
  import { SvelteFlow, Controls, Panel, Background } from '@xyflow/svelte';
  import '@xyflow/svelte/dist/style.css';
  import { graphData } from '$lib/stores/graph';
  import dagre from '@dagrejs/dagre'; // npm install @dagrejs/dagre — auto-layout, since xyflow doesn't compute positions

  let nodes = [], edges = [];

  $: if ($graphData.nodes.length) {
    ({ nodes, edges } = layout($graphData.nodes, $graphData.edges));
  }

  function layout(rawNodes, rawEdges) {
    const g = new dagre.graphlib.Graph();
    g.setGraph({ rankdir: 'TB' });
    g.setDefaultEdgeLabel(() => ({}));
    rawNodes.forEach(n => g.setNode(n.id, { width: 120, height: 120 }));
    rawEdges.forEach(e => g.setEdge(e.source, e.target));
    dagre.layout(g);

    return {
      nodes: rawNodes.map(n => ({
        id: n.id,
        type: 'entity',
        data: { label: n.label },
        position: { x: g.node(n.id).x, y: g.node(n.id).y }
      })),
      edges: rawEdges.map(e => ({
        id: `${e.source}-${e.target}`,
        source: e.source,
        target: e.target,
        label: e.label,
        markerEnd: { type: 'arrowclosed' }
      }))
    };
  }

  function download() { /* svelteflow's toObject() + canvas export, or html-to-image on the pane element */ }
  function reset()    { nodes = layout($graphData.nodes, $graphData.edges).nodes; }
</script>

<SvelteFlow {nodes} {edges} fitView nodeTypes={{ entity: EntityNode }}>
  <Background />
  <Controls />
  <Panel position="top-right">
    <button on:click={download}><!-- download icon --></button>
    <button on:click={reset}><!-- reset icon --></button>
  </Panel>
</SvelteFlow>
