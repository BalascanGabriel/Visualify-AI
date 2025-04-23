// components/Roadmap.tsx
import React, { useState } from 'react';

interface NodeType {
  id: string;
  label: string;
  parent: string | null;
}

interface LinkType {
  source: string;
  target: string;
}

interface RoadmapProps {
  nodesData: NodeType[];
  linksData: LinkType[];
}

const Roadmap = ({ nodesData, linksData }: RoadmapProps) => {
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});

  const rootNodes = nodesData.filter((n) => !nodesData.some((p) => p.id === n.parent));
  const getChildren = (parentId: string) => nodesData.filter((n) => n.parent === parentId);

  const renderItems = (parentId: string, level: number = 0) => {
    const children = getChildren(parentId);
    if (!children.length) return null;

    return (
      <ul className={`ml-${level * 2} mt-2 space-y-2 text-white/80`}>
        {children.map((child) => (
          <li key={child.id} className="relative">
            <div
              className={`cursor-pointer pl-4 border-l-2 ${level === 0 ? 'border-blue-400 text-white font-semibold' : level === 1 ? 'border-cyan-400 text-cyan-200' : 'border-sky-300 text-sky-300'} hover:underline`}
              onClick={() => setExpanded((prev) => ({ ...prev, [child.id]: !prev[child.id] }))}
            >
              <span className={`absolute left-0 top-1/2 transform -translate-y-1/2 w-2 h-2 rounded-full ${level === 0 ? 'bg-blue-300' : level === 1 ? 'bg-cyan-300' : 'bg-sky-300'}`}></span>
              {child.label}
            </div>
            {expanded[child.id] && renderItems(child.id, level + 1)}
          </li>
        ))}
      </ul>
    );
  };

  const chunkArray = (arr: NodeType[], size: number) => {
    const result = [];
    for (let i = 0; i < arr.length; i += size) {
      result.push(arr.slice(i, i + size));
    }
    return result;
  };

  const rows = chunkArray(rootNodes, 4); // 4 carduri pe rănd

  return (
    <div className="bg-gradient-to-r from-[#0f172a] to-[#1e293b] min-h-screen py-20 px-6 overflow-x-auto">
      <h2 className="text-4xl text-center font-bold text-white mb-12">Roadmap Generat</h2>
      <div className="space-y-20"> {/* spațiu mai mare între rânduri */}
        {rows.map((row, rowIndex) => (
          <div key={rowIndex} className="flex gap-8 justify-center flex-wrap">
            {row.map((root, index) => (
              <div
                key={root.id}
                className="relative bg-[#0f172a] rounded-2xl shadow-xl p-6 w-[280px] border border-sky-700/40 flex-shrink-0"
              >
                {/* Săgeată între carduri */}
                {index < row.length - 1 && (
                  <div className="absolute top-1/2 right-[-32px] transform -translate-y-1/2 z-0">
                    <svg width="64" height="24" viewBox="0 0 64 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M0 12 C 20 0, 44 24, 60 12" stroke="#38bdf8" strokeWidth="2" fill="none" />
                      <polygon points="60,12 54,8 54,16" fill="#38bdf8" />
                    </svg>
                  </div>
                )}
                {/* Săgeată între rânduri */}
                {index === row.length - 1 && rowIndex < rows.length - 1 && (
                  <div className="absolute bottom-[-30px] left-1/2 transform -translate-x-1/2">
                    <svg width="24" height="64" viewBox="0 0 24 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 0 C 0 20, 24 44, 12 60" stroke="#38bdf8" strokeWidth="2" fill="none" />
                      <polygon points="12,60 8,54 16,54" fill="#38bdf8" />
                    </svg>
                  </div>
                )}
                <h3 className="text-lg font-semibold text-white mb-4 relative z-10 whitespace-normal leading-snug">{root.label}</h3>
                <div className="relative z-10">
                  {renderItems(root.id)}
                </div>
              </div>
            ))}
          </div>
        ))}
      </div>
    </div>
  );
};

export default Roadmap;
