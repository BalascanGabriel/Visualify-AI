// Clean, organized, collapsible mindmap with custom clickable nodes + visual ties between chapters
import React, { useEffect, useRef, useState, useCallback, memo } from 'react';
import ReactFlow, {
  Background,
  Controls,
  Node,
  Edge,
  useReactFlow,
  ReactFlowProvider,
  Handle,
  Position,
  NodeProps
} from 'react-flow-renderer';

// Types
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

const palette = [
  '#ffd6e0', '#cdeac0', '#f2c6b4', '#b5ead7', '#e0bbf9',
  '#f9c6c9', '#fbe7c6', '#e2f0cb', '#c6def1', '#d0f4de'
];

// Custom node component
const CollapsibleNode = memo(({ id, data }: NodeProps) => {
  return (
    <div onClick={() => data.onClick(id)} style={data.style}>
      <Handle type="target" position={Position.Left} />
      <div>{data.label}</div>
      <Handle type="source" position={Position.Right} />
    </div>
  );
});

const MindmapContent: React.FC<MindmapProps> = ({ nodesData, linksData }) => {
  const { fitView } = useReactFlow();
  const initialized = useRef(false);

  const getInitialVisible = () => {
    const chapters = nodesData.filter(n => n.parent === null).map(n => n.id);
    const subchapters = nodesData.filter(n => nodesData.find(ch => ch.id === n.parent && ch.parent === null)).map(n => n.id);
    return [...chapters, ...subchapters];
  };

  const [visibleNodes, setVisibleNodes] = useState<string[]>(getInitialVisible);

  const getAllDescendants = (id: string): string[] => {
    const children = nodesData.filter(n => n.parent === id);
    return children.reduce((acc, curr) => [...acc, curr.id, ...getAllDescendants(curr.id)], []);
  };

  const toggleChildren = useCallback((nodeId: string) => {
    const children = nodesData.filter(n => n.parent === nodeId);
    const areVisible = children.every(c => visibleNodes.includes(c.id));
    const toChange = getAllDescendants(nodeId);

    setVisibleNodes(prev =>
      areVisible ? prev.filter(id => !toChange.includes(id)) : [...new Set([...prev, ...toChange])]
    );
  }, [nodesData, visibleNodes]);

  const layoutNodes = (): Record<string, { x: number; y: number }> => {
    const positions: Record<string, { x: number; y: number }> = {};
    const rootNodes = nodesData.filter(n => n.parent === null);
    const verticalGap = 120;
    const horizontalGap = 220;
    let globalY = 0;

    const layoutSubtree = (node: NodeType, depth: number, order: number) => {
      const x = depth * horizontalGap;
      const y = globalY;
      positions[node.id] = { x, y };
      globalY += verticalGap;

      const children = nodesData.filter(n => n.parent === node.id && visibleNodes.includes(n.id));
      children.forEach((child, i) => layoutSubtree(child, depth + 1, i));
    };

    rootNodes.forEach((root, i) => layoutSubtree(root, 0, i));
    return positions;
  };

  const positions = layoutNodes();

  const nodes: Node[] = nodesData
    .filter(node => visibleNodes.includes(node.id))
    .map((node, index) => ({
      id: node.id,
      type: 'collapsible',
      data: {
        label: node.label,
        onClick: toggleChildren,
        style: {
          background: node.parent === null
            ? 'linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%)'
            : palette[index % palette.length],
          color: node.parent === null ? '#fff' : '#333',
          border: '1px solid #ccc',
          borderRadius: 12,
          padding: 10,
          fontSize: 14,
          boxShadow: '0 4px 14px rgba(0,0,0,0.1)',
          minWidth: 150,
          textAlign: 'center',
          cursor: 'pointer'
        }
      },
      position: positions[node.id],
      draggable: false
    }));

  // Normal mindmap edges
  const mainEdges: Edge[] = linksData.filter(
    link => visibleNodes.includes(link.source) && visibleNodes.includes(link.target)
  ).map(link => ({
    id: `${link.source}-${link.target}`,
    source: link.source,
    target: link.target,
    animated: true,
    style: { stroke: '#9999ff', strokeWidth: 2 },
  }));

  // Connect top-level chapters visually
  const chapterNodes = nodesData.filter(n => n.parent === null && visibleNodes.includes(n.id));
  const tieEdges: Edge[] = chapterNodes.slice(1).map((node, index) => ({
    id: `tie-${chapterNodes[index].id}-${node.id}`,
    source: chapterNodes[index].id,
    target: node.id,
    animated: false,
    style: {
      stroke: '#aaa',
      strokeWidth: 1.5,
      strokeDasharray: '4 2',
    },
  }));

  const edges: Edge[] = [...mainEdges, ...tieEdges];

  useEffect(() => {
    if (!initialized.current) {
      fitView({ padding: 0.2 });
      initialized.current = true;
    }
  }, [fitView]);

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={{ collapsible: CollapsibleNode }}
        fitView
        panOnScroll
        zoomOnScroll
        zoomOnPinch
      >
        <Background color="#f0f4f8" gap={20} />
        <Controls />
      </ReactFlow>
    </div>
  );
};

const Mindmap: React.FC<MindmapProps> = (props) => (
  <ReactFlowProvider>
    <MindmapContent {...props} />
  </ReactFlowProvider>
);

export default Mindmap;