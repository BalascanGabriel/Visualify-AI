import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface NodeData {
  id: string;
  label: string;
  parent: string | null;
}

interface MindmapData {
  nodes: NodeData[];
}

interface Props {
  data: MindmapData;
}

const Mindmap: React.FC<Props> = ({ data }) => {
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  const toggleNode = (id: string) => {
    setExpanded(prev => ({ ...prev, [id]: !prev[id] }));
  };

  const renderTree = (parentId: string | null, depth = 0): JSX.Element[] => {
    const children = data.nodes.filter(n => n.parent === parentId);

    return children.map((node, index) => (
      <div key={node.id} className={`ml-${depth * 4} mb-2`}>
        <motion.div
          initial={{ opacity: 0, y: -10 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: 10 }}
          className="flex items-center gap-2 cursor-pointer"
          onClick={() => toggleNode(node.id)}
        >
          {data.nodes.some(n => n.parent === node.id) && (
            <span className="text-blue-500">{expanded[node.id] ? '▼' : '▶'}</span>
          )}
          <span className="text-gray-800 font-medium">{node.label}</span>
        </motion.div>

        <AnimatePresence>
          {expanded[node.id] && (
            <motion.div
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: 'auto' }}
              exit={{ opacity: 0, height: 0 }}
              className="ml-4 border-l-2 border-blue-300 pl-4"
            >
              {renderTree(node.id, depth + 1)}
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    ));
  };

  return (
    <div className="w-full max-w-4xl mx-auto p-4 rounded-xl bg-white shadow-xl">
      <h2 className="text-2xl font-bold mb-4 text-blue-700">Mindmap</h2>
      <div>{renderTree(null)}</div>
    </div>
  );
};

export default Mindmap;
