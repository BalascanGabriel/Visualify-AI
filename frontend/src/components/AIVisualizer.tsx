
import { useEffect, useRef } from 'react';

interface Node {
  x: number;
  y: number;
  radius: number;
  color: string;
  vx: number;
  vy: number;
}

interface Edge {
  from: number;
  to: number;
  width: number;
  alpha: number;
}

interface AIVisualizerProps {
  type?: 'neural-network' | 'connections' | 'particles';
  className?: string;
}

const AIVisualizer = ({ type = 'neural-network', className = '' }: AIVisualizerProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const nodes: Node[] = useRef<Node[]>([]).current;
  const edges: Edge[] = useRef<Edge[]>([]).current;
  const animationRef = useRef<number>();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    
    // Set canvas dimensions
    const resizeCanvas = () => {
      const dpr = window.devicePixelRatio || 1;
      canvas.width = canvas.clientWidth * dpr;
      canvas.height = canvas.clientHeight * dpr;
      ctx.scale(dpr, dpr);
    };
    
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    // Initialize nodes and edges based on visualization type
    if (type === 'neural-network') {
      initializeNeuralNetwork();
    } else if (type === 'connections') {
      initializeConnections();
    } else {
      initializeParticles();
    }
    
    // Animation loop
    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw edges
      for (const edge of edges) {
        const fromNode = nodes[edge.from];
        const toNode = nodes[edge.to];
        
        ctx.beginPath();
        ctx.strokeStyle = `rgba(100, 149, 237, ${edge.alpha})`;
        ctx.lineWidth = edge.width;
        ctx.moveTo(fromNode.x, fromNode.y);
        ctx.lineTo(toNode.x, toNode.y);
        ctx.stroke();
      }
      
      // Draw and update nodes
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        
        // Update position
        if (type !== 'neural-network') {
          node.x += node.vx;
          node.y += node.vy;
          
          // Boundary checks
          if (node.x < node.radius || node.x > canvas.clientWidth - node.radius) {
            node.vx *= -1;
          }
          
          if (node.y < node.radius || node.y > canvas.clientHeight - node.radius) {
            node.vy *= -1;
          }
        }
        
        // Draw node
        ctx.beginPath();
        ctx.fillStyle = node.color;
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fill();
      }
      
      animationRef.current = requestAnimationFrame(animate);
    };
    
    animate();
    
    return () => {
      window.removeEventListener('resize', resizeCanvas);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [type]);
  
  // Initialize nodes and edges for neural network visualization
  const initializeNeuralNetwork = () => {
    nodes.length = 0;
    edges.length = 0;
    
    const layers = 4;
    const nodesPerLayer = [4, 6, 6, 2];
    let nodeIndex = 0;
    
    // Create nodes
    for (let layer = 0; layer < layers; layer++) {
      const numNodes = nodesPerLayer[layer];
      const xPos = (layer + 1) * (canvasRef.current!.clientWidth / (layers + 1));
      
      for (let i = 0; i < numNodes; i++) {
        const yPos = ((i + 1) * canvasRef.current!.clientHeight) / (numNodes + 1);
        nodes.push({
          x: xPos,
          y: yPos,
          radius: 6,
          color: layer === 0 ? 'rgba(64, 156, 255, 0.8)' : 
                 layer === layers - 1 ? 'rgba(157, 80, 255, 0.8)' : 
                 'rgba(100, 180, 255, 0.6)',
          vx: 0,
          vy: 0
        });
        
        // Connect to previous layer
        if (layer > 0) {
          const prevLayerStart = nodeIndex - nodesPerLayer[layer - 1];
          for (let j = prevLayerStart; j < nodeIndex; j++) {
            edges.push({
              from: j,
              to: nodeIndex + i,
              width: Math.random() * 1.5 + 0.5,
              alpha: Math.random() * 0.4 + 0.1
            });
          }
        }
      }
      
      nodeIndex += numNodes;
    }
  };
  
  // Initialize nodes and edges for connection visualization
  const initializeConnections = () => {
    nodes.length = 0;
    edges.length = 0;
    
    const numNodes = 20;
    const width = canvasRef.current!.clientWidth;
    const height = canvasRef.current!.clientHeight;
    
    // Create nodes
    for (let i = 0; i < numNodes; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 4 + 2,
        color: `rgba(${Math.floor(Math.random() * 100 + 100)}, ${Math.floor(Math.random() * 100 + 100)}, 255, 0.7)`,
        vx: (Math.random() - 0.5) * 1,
        vy: (Math.random() - 0.5) * 1
      });
    }
    
    // Create edges
    for (let i = 0; i < numNodes; i++) {
      const numConnections = Math.floor(Math.random() * 3) + 1;
      for (let j = 0; j < numConnections; j++) {
        const toNode = (i + j + 1) % numNodes;
        edges.push({
          from: i,
          to: toNode,
          width: Math.random() + 0.5,
          alpha: Math.random() * 0.3 + 0.1
        });
      }
    }
  };
  
  // Initialize nodes for particle visualization
  const initializeParticles = () => {
    nodes.length = 0;
    edges.length = 0;
    
    const numNodes = 30;
    const width = canvasRef.current!.clientWidth;
    const height = canvasRef.current!.clientHeight;
    
    // Create nodes
    for (let i = 0; i < numNodes; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 5 + 1,
        color: `rgba(${Math.floor(Math.random() * 100 + 150)}, ${Math.floor(Math.random() * 50 + 100)}, 255, ${Math.random() * 0.5 + 0.3})`,
        vx: (Math.random() - 0.5) * 2,
        vy: (Math.random() - 0.5) * 2
      });
    }
  };

  return (
    <canvas 
      ref={canvasRef} 
      className={`w-full h-full ${className}`}
    />
  );
};

export default AIVisualizer;
