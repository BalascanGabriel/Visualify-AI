
import { useEffect, useRef } from 'react';

interface Node {
  x: number;
  y: number;
  radius: number;
  color: string;
  vx: number;
  vy: number;
  type?: string;
}

interface Edge {
  from: number;
  to: number;
  width: number;
  alpha: number;
  current?: number;
}

interface ElectricalVisualizerProps {
  type?: 'circuit' | 'electrons' | 'components';
  className?: string;
}

const ElectricalVisualizer = ({ type = 'circuit', className = '' }: ElectricalVisualizerProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const nodes: Node[] = useRef<Node[]>([]).current;
  const edges: Edge[] = useRef<Edge[]>([]).current;
  const animationRef = useRef<number>();
  const timeRef = useRef<number>(0);

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
    if (type === 'circuit') {
      initializeCircuit();
    } else if (type === 'electrons') {
      initializeElectrons();
    } else {
      initializeComponents();
    }
    
    // Animation loop
    const animate = (timestamp: number) => {
      timeRef.current = timestamp;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw edges (wires)
      for (const edge of edges) {
        const fromNode = nodes[edge.from];
        const toNode = nodes[edge.to];
        
        // Basic wire
        ctx.beginPath();
        ctx.strokeStyle = `rgba(120, 185, 250, ${edge.alpha})`;
        ctx.lineWidth = edge.width;
        ctx.moveTo(fromNode.x, fromNode.y);
        ctx.lineTo(toNode.x, toNode.y);
        ctx.stroke();
        
        // Animate current if applicable
        if (type === 'circuit' && edge.current && edge.current > 0) {
          const dx = toNode.x - fromNode.x;
          const dy = toNode.y - fromNode.y;
          const distance = Math.sqrt(dx * dx + dy * dy);
          const numParticles = Math.floor(distance / 15);
          
          for (let i = 0; i < numParticles; i++) {
            const t = ((timestamp / 500) + (i / numParticles)) % 1;
            const particleX = fromNode.x + dx * t;
            const particleY = fromNode.y + dy * t;
            
            ctx.beginPath();
            ctx.fillStyle = 'rgba(255, 255, 160, 0.8)';
            ctx.arc(particleX, particleY, 3, 1, Math.PI * 2);
            ctx.fill();
          }
        }
      }
      
      // Draw and update nodes (components/electrons)
      for (let i = 0; i < nodes.length; i++) {
        const node = nodes[i];
        
        // Update position for electrons
        if (type === 'electrons' || (type === 'circuit' && node.type === 'electron')) {
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
        
        // Draw node based on type
        if (node.type === 'resistor') {
          // Draw resistor
          ctx.beginPath();
          ctx.fillStyle = node.color;
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 3;
          
          // Draw rectangle
          ctx.fillRect(node.x - 20, node.y - 10, 40, 20);
          ctx.strokeRect(node.x - 20, node.y - 10, 50, 20);
          
          // Draw zigzag pattern inside
          ctx.beginPath();
          ctx.moveTo(node.x - 15, node.y);
          for (let j = 0; j < 5; j++) {
            const xOffset = j * 6;
            ctx.lineTo(node.x - 15 + xOffset, node.y + (j % 2 === 0 ? -5 : 5));
          }
          ctx.stroke();
        } else if (node.type === 'battery') {
          // Draw battery
          ctx.beginPath();
          ctx.fillStyle = node.color;
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 2;
          
          // Main rectangle
          ctx.fillRect(node.x - 20, node.y - 15, 40, 30);
          ctx.strokeRect(node.x - 20, node.y - 15, 40, 30);
          
          // Positive terminal
          ctx.beginPath();
          ctx.fillStyle = '#444';
          ctx.fillRect(node.x + 5, node.y - 5, 10, 2);
          ctx.fillRect(node.x + 10, node.y - 10, 2, 20);
          
          // Negative terminal
          ctx.fillRect(node.x - 15, node.y - 5, 10, 2);
        } else if (node.type === 'bulb') {
          // Draw light bulb
          ctx.beginPath();
          ctx.fillStyle = 'rgba(255, 255, 160, 0.8)';
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 2;
          
          // Bulb circle
          ctx.arc(node.x, node.y - 5, 15, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();
          
          // Bulb base
          ctx.beginPath();
          ctx.fillStyle = '#aaa';
          ctx.fillRect(node.x - 8, node.y + 10, 16, 10);
          ctx.strokeRect(node.x - 8, node.y + 10, 16, 10);
          
          // Filament
          ctx.beginPath();
          ctx.strokeStyle = '#888';
          ctx.moveTo(node.x - 5, node.y);
          ctx.lineTo(node.x, node.y - 5);
          ctx.lineTo(node.x + 5, node.y);
          ctx.stroke();
          
          // Glow effect
          if (type === 'circuit') {
            const gradient = ctx.createRadialGradient(node.x, node.y - 5, 5, node.x, node.y - 5, 25);
            gradient.addColorStop(0, 'rgba(255, 255, 200, 0.8)');
            gradient.addColorStop(1, 'rgba(255, 255, 100, 0)');
            
            ctx.beginPath();
            ctx.fillStyle = gradient;
            ctx.arc(node.x, node.y - 5, 25, 0, Math.PI * 2);
            ctx.fill();
          }
        } else if (node.type === 'switch') {
          // Draw switch
          ctx.beginPath();
          ctx.fillStyle = '#ddd';
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 2;
          
          // Base
          ctx.fillRect(node.x - 20, node.y - 5, 40, 10);
          ctx.strokeRect(node.x - 20, node.y - 5, 40, 10);
          
          // Switch toggle (randomly toggle)
          const switchOn = Math.sin(timestamp / 2000) > 0;
          ctx.beginPath();
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 2;
          ctx.moveTo(node.x - 15, node.y);
          if (switchOn) {
            ctx.lineTo(node.x + 15, node.y);
          } else {
            ctx.lineTo(node.x + 5, node.y - 10);
          }
          ctx.stroke();
          
          // Switch knob
          ctx.beginPath();
          ctx.fillStyle = switchOn ? '#4CAF50' : '#F44336';
          ctx.arc(node.x - 15, node.y, 5, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();
        } else if (node.type === 'capacitor') {
          // Draw capacitor
          ctx.beginPath();
          ctx.strokeStyle = '#444';
          ctx.lineWidth = 2;
          
          // Two parallel plates
          ctx.moveTo(node.x - 15, node.y - 15);
          ctx.lineTo(node.x - 15, node.y + 15);
          ctx.moveTo(node.x + 15, node.y - 15);
          ctx.lineTo(node.x + 15, node.y + 15);
          ctx.stroke();
          
          // Draw charging state (pulse animation)
          const chargeLevel = Math.sin(timestamp / 1000) * 0.5 + 0.5;
          ctx.fillStyle = `rgba(120, 185, 250, ${chargeLevel})`;
          ctx.fillRect(node.x - 14, node.y - 14, 13, 28);
          ctx.fillRect(node.x + 2, node.y - 14, 13, 28);
        } else {
          // Draw regular node (electron)
          ctx.beginPath();
          ctx.fillStyle = node.color;
          ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
          ctx.fill();
          
          // For electrons, add a minus sign
          if (node.type === 'electron') {
            ctx.beginPath();
            ctx.strokeStyle = 'white';
            ctx.lineWidth = 1.5;
            ctx.moveTo(node.x - 3, node.y);
            ctx.lineTo(node.x + 3, node.y);
            ctx.stroke();
          }
        }
      }
      
      animationRef.current = requestAnimationFrame(animate);
    };
    
    animationRef.current = requestAnimationFrame(animate);
    
    return () => {
      window.removeEventListener('resize', resizeCanvas);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [type]);
  
  // Initialize nodes and edges for circuit visualization
  const initializeCircuit = () => {
    nodes.length = 0;
    edges.length = 0;
    
    // Create basic circuit with battery, resistor, bulb, and wires
    nodes.push(
      // Battery
      {
        x: canvasRef.current!.clientWidth * 0.2,
        y: canvasRef.current!.clientHeight * 0.5,
        radius: 20,
        color: '#ffcc66',
        vx: 0,
        vy: 0,
        type: 'battery'
      },
      // Resistor
      {
        x: canvasRef.current!.clientWidth * 0.4,
        y: canvasRef.current!.clientHeight * 0.3,
        radius: 15,
        color: '#aaddff',
        vx: 0,
        vy: 0,
        type: 'resistor'
      },
      // Bulb
      {
        x: canvasRef.current!.clientWidth * 0.6,
        y: canvasRef.current!.clientHeight * 0.3,
        radius: 15,
        color: '#ffff99',
        vx: 0,
        vy: 0,
        type: 'bulb'
      },
      // Switch
      {
        x: canvasRef.current!.clientWidth * 0.8,
        y: canvasRef.current!.clientHeight * 0.5,
        radius: 15,
        color: '#dddddd',
        vx: 0,
        vy: 0,
        type: 'switch'
      }
    );
    
    // Add electrons
    for (let i = 0; i < 15; i++) {
      const angle = (i / 15) * Math.PI * 2;
      const radius = Math.min(canvasRef.current!.clientWidth, canvasRef.current!.clientHeight) * 0.3;
      const x = canvasRef.current!.clientWidth / 2 + Math.cos(angle) * radius;
      const y = canvasRef.current!.clientHeight / 2 + Math.sin(angle) * radius;
      
      nodes.push({
        x,
        y,
        radius: 4,
        color: '#4488ff',
        vx: Math.cos(angle) * 0.5,
        vy: Math.sin(angle) * 0.5,
        type: 'electron'
      });
    }
    
    // Connect components with wires
    edges.push(
      {
        from: 0, // Battery
        to: 1,   // Resistor
        width: 3,
        alpha: 0.8,
        current: 1
      },
      {
        from: 1, // Resistor
        to: 2,   // Bulb
        width: 3,
        alpha: 0.8,
        current: 0.8
      },
      {
        from: 2, // Bulb
        to: 3,   // Switch
        width: 4,
        alpha: 0.8,
        current: 0.6
      },
      {
        from: 3, // Switch
        to: 0,   // Battery
        width: 3,
        alpha: 1,
        current: 1
      }
    );
  };
  
  // Initialize nodes for electrons visualization
  const initializeElectrons = () => {
    nodes.length = 0;
    edges.length = 0;
    
    const numNodes = 40;
    const width = canvasRef.current!.clientWidth;
    const height = canvasRef.current!.clientHeight;
    
    // Create nodes (electrons)
    for (let i = 0; i < numNodes; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        radius: Math.random() * 4 + 3,
        color: `rgba(68, 136, 255, ${Math.random() * 0.5 + 0.5})`,
        vx: (Math.random() - 0.5) * 1.5,
        vy: (Math.random() - 0.5) * 1.5,
        type: 'electron'
      });
    }
    
    // Create some connecting edges
    for (let i = 0; i < numNodes; i++) {
      for (let j = i + 1; j < numNodes; j++) {
        if (Math.random() < 0.03) {
          edges.push({
            from: i,
            to: j,
            width: Math.random() * 1 + 0.5,
            alpha: Math.random() * 0.3 + 0.1
          });
        }
      }
    }
  };
  
  // Initialize nodes for components visualization
  const initializeComponents = () => {
    nodes.length = 0;
    edges.length = 0;
    
    const width = canvasRef.current!.clientWidth;
    const height = canvasRef.current!.clientHeight;
    
    // Create component nodes in a grid
    const components = [
      { type: 'battery', color: '#ffcc66' },
      { type: 'resistor', color: '#aaddff' },
      { type: 'bulb', color: '#ffff99' },
      { type: 'switch', color: '#dddddd' },
      { type: 'capacitor', color: '#bbffbb' }
    ];
    
    const cols = 3;
    const rows = 2;
    const marginX = width * 0.15;
    const marginY = height * 0.2;
    const spacingX = (width - marginX * 2) / (cols - 1);
    const spacingY = (height - marginY * 2) / (rows - 1);
    
    let index = 0;
    for (let row = 0; row < rows; row++) {
      for (let col = 0; col < cols; col++) {
        if (index < components.length) {
          const x = marginX + col * spacingX;
          const y = marginY + row * spacingY;
          
          nodes.push({
            x,
            y,
            radius: 20,
            color: components[index].color,
            vx: 0,
            vy: 0,
            type: components[index].type
          });
          
          index++;
        }
      }
    }
  };

  return (
    <canvas 
      ref={canvasRef} 
      className={`w-full h-full ${className}`}
    />
  );
};

export default ElectricalVisualizer;
