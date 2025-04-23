// Clean, collapsible mindmap with concept video popup support
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
import './Mindmap.css'; // We'll style the modal here

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
    <div
      onClick={(e) => {
        e.stopPropagation();
        data.onClick(id, data.isConcept);
      }}
      style={data.style}
    >
      <Handle type="target" position={Position.Left} />
      <div>{data.label} {data.isConcept && '🎥'}</div>
      <Handle type="source" position={Position.Right} />
    </div>
  );
});

const MindmapContent: React.FC<MindmapProps> = ({ nodesData, linksData }) => {
  const { fitView } = useReactFlow();
  const initialized = useRef(false);

  const [visibleNodes, setVisibleNodes] = useState<string[]>([]);
  const [conceptNode, setConceptNode] = useState<NodeType | null>(null);

  useEffect(() => {
    const chapters = nodesData.filter(n => n.parent === null).map(n => n.id);
    const subchapters = nodesData.filter(n => nodesData.find(ch => ch.id === n.parent && ch.parent === null)).map(n => n.id);
    setVisibleNodes([...chapters, ...subchapters]);
  }, [nodesData]);

  const getAllDescendants = (id: string): string[] => {
    const children = nodesData.filter(n => n.parent === id);
    return children.reduce((acc, curr) => [...acc, curr.id, ...getAllDescendants(curr.id)], []);
  };

  const toggleChildren = useCallback((nodeId: string, isConcept: boolean) => {
    if (isConcept) {
      const node = nodesData.find(n => n.id === nodeId) || null;
      setConceptNode(node);
      return;
    }

    const children = nodesData.filter(n => n.parent === nodeId);
    const areVisible = children.every(c => visibleNodes.includes(c.id));
    const toChange = getAllDescendants(nodeId);

    setVisibleNodes(prev =>
      areVisible ? prev.filter(id => !toChange.includes(id)) : [...new Set([...prev, ...toChange])]
    );
  }, [nodesData, visibleNodes]);

  const layoutNodes = (): Record<string, { x: number; y: number }> => {
    const pos: Record<string, { x: number; y: number }> = {};
    const rootNodes = nodesData.filter(n => n.parent === null);
    const verticalGap = 120;
    const horizontalGap = 220;
    let globalY = 0;

    const layoutSubtree = (node: NodeType, depth: number, order: number) => {
      const x = depth * horizontalGap;
      const y = globalY;
      pos[node.id] = { x, y };
      globalY += verticalGap;

      const children = nodesData.filter(n => n.parent === node.id && visibleNodes.includes(n.id));
      children.forEach((child, i) => layoutSubtree(child, depth + 1, i));
    };

    rootNodes.forEach((root, i) => layoutSubtree(root, 0, i));
    return pos;
  };

  const positions = layoutNodes();

  const nodes: Node[] = nodesData
    .filter(node => visibleNodes.includes(node.id))
    .map((node, index) => {
      const isConcept = !nodesData.some(n => n.parent === node.id);
      return {
        id: node.id,
        type: 'collapsible',
        data: {
          label: node.label,
          onClick: toggleChildren,
          isConcept,
          style: {
            background: node.parent === null
              ? 'linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%)'
              : isConcept
                ? '#ffe5b4' // Light orange for concept nodes
                : palette[index % palette.length],
            color: '#333',
            border: '1px solid #ccc',
            borderRadius: 12,
            padding: 10,
            fontSize: 30,
            boxShadow: '0 4px 14px rgba(0,0,0,0.1)',
            minWidth: 150,
            textAlign: 'center',
            cursor: 'pointer'
          }
        },
        position: positions[node.id],
        draggable: false
      };
    });

  const mainEdges: Edge[] = linksData.filter(
    link => visibleNodes.includes(link.source) && visibleNodes.includes(link.target)
  ).map(link => ({
    id: `${link.source}-${link.target}`,
    source: link.source,
    target: link.target,
    animated: true,
    style: { stroke: '#9999ff', strokeWidth: 2 },
  }));

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

      {conceptNode && (
        <div className="mindmap-modal">
          <div className="mindmap-modal-content">
            <button className="mindmap-modal-close" onClick={() => setConceptNode(null)}>
              ×
            </button>
            <h2>{conceptNode.label}</h2>
            <p>🎬 Here will be the video rendered from Manim for this concept.</p>
            <div className="video-placeholder">[VIDEO PLACEHOLDER]</div>
          </div>
        </div>
      )}
    </div>
  );
};

const Mindmap: React.FC<MindmapProps> = (props) => (
  <ReactFlowProvider>
    <MindmapContent {...props} />
  </ReactFlowProvider>
);

export default Mindmap;
