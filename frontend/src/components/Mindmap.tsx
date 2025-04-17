// components/Mindmap.tsx
import React from 'react';
import ReactFlow, { Background, Controls, Node, Edge } from 'react-flow-renderer';

type NodeType = {
  id: string;
  label: string;
  parent: string | null;
};

type LinkType = {
  source: string;
  target: string;
};

type MindmapProps = {
  nodesData: NodeType[];
  linksData: LinkType[];
};

const Mindmap: React.FC<MindmapProps> = ({ nodesData, linksData }) => {
  // Convertim datele în format compatibil cu react-flow
  const nodes: Node[] = nodesData.map((node, index) => ({
    id: node.id,
    data: { label: node.label },
    position: { x: Math.random() * 1000, y: index * 80 },
  }));

  const edges: Edge[] = linksData.map((link) => ({
    id: `${link.source}-${link.target}`,
    source: link.source,
    target: link.target,
    animated: true,
  }));

  return (
    <div style={{ width: '100%', height: '120vh' }}>
      <ReactFlow nodes={nodes} edges={edges} fitView>
        <Background />
        <Controls />
      </ReactFlow>
    </div>
  );
};

export default Mindmap;
