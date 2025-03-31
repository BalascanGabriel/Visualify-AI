// utils/mindmapUtils.js

let nodeId = 1;

function createNode(label, parent = null) {
  return {
    id: (nodeId++).toString(),
    label,
    parent
  };
}

function buildMindMap(structura) {
  const nodes = [];
  const links = [];

  for (const cap of structura) {
    const capNode = createNode(cap.capitol);
    nodes.push(capNode);

    for (const sub of cap.subcapitole) {
      const subNode = createNode(sub.subcapitol, capNode.id);
      nodes.push(subNode);
      links.push({ source: capNode.id, target: subNode.id });

      for (const concept of sub.concepte) {
        const conceptNode = createNode(concept, subNode.id);
        nodes.push(conceptNode);
        links.push({ source: subNode.id, target: conceptNode.id });
      }
    }
  }

  return { nodes, links };
}

module.exports = { buildMindMap };
