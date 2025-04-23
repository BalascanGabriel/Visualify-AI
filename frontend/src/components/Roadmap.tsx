// components/Roadmap.tsx
import React, { useState, useEffect, useRef } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

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
  const [conceptNode, setConceptNode] = useState<NodeType | null>(null);
  const cardsRef = useRef<HTMLDivElement[]>([]);

  useEffect(() => {
    cardsRef.current.forEach((el, i) => {
      if (el) {
        gsap.fromTo(
          el,
          { opacity: 0, y: 60 },
          {
            opacity: 1,
            y: 0,
            delay: i * 0.1,
            duration: 0.6,
            ease: 'power4.out',
            scrollTrigger: {
              trigger: el,
              start: 'top 80%',
              toggleActions: 'play none none none',
            },
          }
        );
      }
    });
  }, []);

  const rootNodes = nodesData.filter((n) => !nodesData.some((p) => p.id === n.parent));
  const getChildren = (parentId: string) => nodesData.filter((n) => n.parent === parentId);

  const renderItems = (parentId: string, level: number = 0) => {
    const children = getChildren(parentId);
    if (!children.length) return null;

    return (
      <ul className={`ml-${level * 2} mt-2 space-y-2 text-white/80`}>
        {children.map((child) => {
          const isConcept = !nodesData.some((n) => n.parent === child.id);
          return (
            <li key={child.id} className="relative group">
              <div
                className={`cursor-pointer pl-5 border-l-2 ${
                  level === 0
                    ? 'border-blue-400 text-white text-[16px] font-semibold'
                    : level === 1
                    ? 'border-cyan-400 text-cyan-200 text-[15px]'
                    : 'border-sky-300 text-sky-300 text-[14px]'
                } hover:underline transition duration-300 ease-in-out flex items-center gap-2`}
                onClick={() => {
                  if (isConcept) setConceptNode(child);
                  else setExpanded((prev) => ({ ...prev, [child.id]: !prev[child.id] }));
                }}
              >
                <span
                  className={`absolute left-0 top-1/2 transform -translate-y-1/2 w-2 h-2 rounded-full group-hover:scale-125 transition-transform duration-300 ${
                    level === 0 ? 'bg-blue-300' : level === 1 ? 'bg-cyan-300' : 'bg-sky-300'
                  }`}
                ></span>
                {child.label} {isConcept && <span className="ml-1">🎥</span>}
                {isConcept && (
                  <span className="ml-auto w-4 h-4 rounded-full border border-white/30 group-hover:border-white"></span>
                )}
              </div>
              {expanded[child.id] && renderItems(child.id, level + 1)}
            </li>
          );
        })}
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

  const rows = chunkArray(rootNodes, 3);

  return (
    <div className="bg-gradient-to-r from-[#0f172a] to-[#1e293b] min-h-screen py-20 px-6 overflow-x-hidden">
      <h2 className="text-4xl text-center font-bold text-white mb-12">Roadmap Generat</h2>
      <div className="space-y-48">
        {rows.map((row, rowIndex) => (
          <div key={rowIndex} className="flex gap-10 justify-center flex-wrap">
            {row.map((root, index) => (
              <div
                key={root.id}
                ref={(el) => {
                  if (el) cardsRef.current[index + rowIndex * 3] = el;
                }}
                className="relative bg-gradient-to-br from-blue-700 to-indigo-800 rounded-[2rem] shadow-xl p-6 w-[300px] border border-blue-400/30 flex-shrink-0 hover:shadow-blue-500/70 transition duration-500 transform hover:scale-[1.05] hover:rotate-[0.5deg] backdrop-blur-sm"
              >
                {index < row.length - 1 && (
                  <div className="absolute top-1/2 right-[-34px] transform -translate-y-1/2 z-0">
                    <svg width="64" height="24" viewBox="0 0 64 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M0 12 C 20 0, 44 24, 60 12" stroke="#67e8f9" strokeWidth="2" fill="none" />
                      <polygon points="60,12 54,8 54,16" fill="#67e8f9" />
                    </svg>
                  </div>
                )}
                {index === row.length - 1 && rowIndex < rows.length - 1 && (
                  <div className="absolute bottom-[-60px] left-[calc(100%/3)] transform -translate-x-1/2">
                    <svg width="64" height="64" viewBox="0 0 64 64" fill="none" xmlns="http://www.w3.org/2000/svg">
                      <path d="M12 0 C 0 20, 64 44, 48 60" stroke="#67e8f9" strokeWidth="2" fill="none" />
                      <polygon points="48,60 44,54 52,54" fill="#67e8f9" />
                    </svg>
                  </div>
                )}
                <h3 className="text-md font-bold text-white mb-4 relative z-10 leading-snug whitespace-normal">
                  {root.label}
                </h3>
                <div className="relative z-10">
                  {renderItems(root.id)}
                </div>
              </div>
            ))}
          </div>
        ))}
      </div>

      {conceptNode && (
        <div className="fixed top-0 left-0 w-full h-full flex items-center justify-center bg-black bg-opacity-50 z-50">
          <div className="bg-white p-6 rounded-xl shadow-xl max-w-md w-full relative">
            <button
              className="absolute top-2 right-2 text-gray-600 hover:text-black text-xl font-bold"
              onClick={() => setConceptNode(null)}
            >
              ×
            </button>
            <h2 className="text-xl font-bold mb-4">{conceptNode.label}</h2>
            <div className="bg-gray-200 rounded-lg h-64 flex items-center justify-center">
              <span className="text-gray-600">🎬 Video placeholder here</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Roadmap;
