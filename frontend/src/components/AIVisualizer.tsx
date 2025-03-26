import { useEffect, useRef } from 'react';
import gsap from 'gsap';

interface Particle {
  x: number;
  y: number;
  alpha: number;
  radius: number;
  vx: number;
  vy: number;
}

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

interface Orbital {
  nodeIndex: number;
  angle: number;
  radius: number;
  speed: number;
  size: number;
  color: string;
  isStatic?: boolean;
  spark?: number;
  exploded?: boolean;
}

interface AIVisualizerProps {
  type?: 'neural-network' | 'connections' | 'particles';
  className?: string;
}

const AIVisualizer = ({ type = 'neural-network', className = '' }: AIVisualizerProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const nodes = useRef<Node[]>([]);
  const edges = useRef<Edge[]>([]);
  const orbitals = useRef<Orbital[]>([]);
  const particles = useRef<Particle[]>([]);
  const animationRef = useRef<number>();
  const tiltRef = useRef({ x: 0, y: 0 });
  const pan = useRef({ x: 0, y: 0 });
  const isDragging = useRef(false);
  const dragOrbital = useRef<number | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const resizeCanvas = () => {
      const dpr = window.devicePixelRatio || 1;
      canvas.width = canvas.clientWidth * dpr;
      canvas.height = canvas.clientHeight * dpr;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(dpr, dpr);
    };

    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    nodes.current = [];
    edges.current = [];
    orbitals.current = [];
    particles.current = [];

    if (type === "neural-network") {
      initializeNeuralNetwork();
    }

    animateWithGSAP();
    animateCanvas();

    const handleMouseMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      gsap.to(tiltRef.current, {
        x: (x - rect.width / 2) / rect.width,
        y: (y - rect.height / 2) / rect.height,
        duration: 0.4,
        ease: "power2.out"
      });

      if (isDragging.current && dragOrbital.current !== null) {
        const orbital = orbitals.current[dragOrbital.current];
        const node = nodes.current[orbital.nodeIndex];
        const dx = x - node.x;
        const dy = y - node.y;
        orbital.radius = Math.sqrt(dx * dx + dy * dy);
        orbital.angle = Math.atan2(dy, dx);
        orbital.isStatic = true;
      }
    };

    const handleMouseDown = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      orbitals.current.forEach((orbital, index) => {
        const node = nodes.current[orbital.nodeIndex];
        const ox = node.x + Math.cos(orbital.angle) * orbital.radius;
        const oy = node.y + Math.sin(orbital.angle) * orbital.radius;
        const dx = ox - x;
        const dy = oy - y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < orbital.size * 5) {
          dragOrbital.current = index;
          isDragging.current = true;
          orbital.isStatic = true;
          orbital.color = "#FFD700";
          orbital.spark = 1;
          orbital.exploded = true;

          for (let i = 0; i < 12; i++) {
            const angle = (Math.PI * 2 * i) / 12;
            particles.current.push({
              x: ox,
              y: oy,
              alpha: 1,
              radius: 1 + Math.random() * 2,
              vx: Math.cos(angle) * 2,
              vy: Math.sin(angle) * 2
            });
          }
        }
      });
    };

    const handleMouseUp = () => {
      isDragging.current = false;
      if (dragOrbital.current !== null) {
        orbitals.current[dragOrbital.current].isStatic = false;
        dragOrbital.current = null;
      }
    };

    const handleClick = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      nodes.current.forEach((node) => {
        const dx = node.x - x;
        const dy = node.y - y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < node.radius * 2) {
          gsap.to(node, {
            radius: node.radius + 10,
            duration: 0.3,
            yoyo: true,
            repeat: 1,
            ease: "power2.inOut"
          });
        }
      });
    };

    canvas.addEventListener("mousemove", handleMouseMove);
    canvas.addEventListener("mousedown", handleMouseDown);
    canvas.addEventListener("mouseup", handleMouseUp);
    canvas.addEventListener("click", handleClick);

    return () => {
      window.removeEventListener("resize", resizeCanvas);
      canvas.removeEventListener("mousemove", handleMouseMove);
      canvas.removeEventListener("mousedown", handleMouseDown);
      canvas.removeEventListener("mouseup", handleMouseUp);
      canvas.removeEventListener("click", handleClick);
      if (animationRef.current) cancelAnimationFrame(animationRef.current);
    };
  }, [type]);

  const animateWithGSAP = () => {
    nodes.current.forEach((node) => {
      gsap.to(node, {
        x: node.x + Math.random() * 60 - 30,
        y: node.y + Math.random() * 60 - 30,
        duration: 1 + Math.random() * 1.5,
        repeat: -1,
        yoyo: true,
        ease: "sine.inOut"
      });
    });
    gsap.to(edges.current, {
      alpha: 0.9,
      duration: 1,
      repeat: -1,
      yoyo: true,
      ease: "power1.inOut"
    });
  };

  const animateCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas?.getContext("2d");
    if (!canvas || !ctx) return;

    const draw = () => {
      const width = canvas.clientWidth;
      const height = canvas.clientHeight;
      ctx.clearRect(0, 0, width, height);

      ctx.save();
      ctx.translate(pan.current.x, pan.current.y);

      edges.current.forEach((edge) => {
        const from = nodes.current[edge.from];
        const to = nodes.current[edge.to];
        ctx.beginPath();
        ctx.strokeStyle = `rgba(3, 97, 163, ${edge.alpha})`;
        ctx.lineWidth = edge.width;
        ctx.moveTo(from.x, from.y);
        ctx.lineTo(to.x, to.y);
        ctx.stroke();
      });

      particles.current = particles.current.filter(p => p.alpha > 0);
      particles.current.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        p.alpha -= 0.02;
        ctx.beginPath();
        ctx.fillStyle = `rgba(${Math.floor(Math.random()*200)}, ${Math.floor(Math.random()*200)}, ${Math.floor(Math.random()*200)}, ${p.alpha})`;
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fill();
      });

      orbitals.current.forEach((orbital) => {
        const node = nodes.current[orbital.nodeIndex];
        if (!orbital.isStatic) orbital.angle += orbital.speed;
        const ox = node.x + Math.cos(orbital.angle) * orbital.radius;
        const oy = node.y + Math.sin(orbital.angle) * orbital.radius;

        if (orbital.spark && orbital.spark > 0) {
          ctx.fillStyle = "#FF69B4";
          ctx.beginPath();
          ctx.arc(ox, oy, orbital.size * 2.5 * orbital.spark, 0, Math.PI * 2);
          ctx.fill();
          orbital.spark -= 0.05;
          if (orbital.spark <= 0) orbital.spark = 0;
        }

        ctx.beginPath();
        ctx.fillStyle = orbital.color || "#ffffff";
        ctx.arc(ox, oy, orbital.size, 0, Math.PI * 2);
        ctx.fill();
      });

      nodes.current.forEach((node) => {
        const glow = ctx.createRadialGradient(node.x, node.y, 0, node.x, node.y, node.radius * 3.5);
        glow.addColorStop(0, `${node.color}AA`);
        glow.addColorStop(1, "transparent");
        ctx.fillStyle = glow;
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius * 2.5, 0, Math.PI * 2);
        ctx.fill();

        ctx.beginPath();
        ctx.fillStyle = node.color;
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fill();
      });

      ctx.restore();
      animationRef.current = requestAnimationFrame(draw);
    };

    draw();
  };

  const initializeNeuralNetwork = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const width = canvas.clientWidth;
    const height = canvas.clientHeight;

    const layers = 4;
    const nodesPerLayer = [4, 6, 6, 2];
    let nodeIndex = 0;

    nodesPerLayer.forEach((count, layer) => {
      const x = ((layer + 1) / (layers + 1)) * width;
      for (let i = 0; i < count; i++) {
        const y = ((i + 1) / (count + 1)) * height;
        const color = layer === 0 ? "#FF6B6B" : layer === layers - 1 ? "#6B47FF" : "#00FFC6";
        const node: Node = {
          x,
          y,
          radius: 8,
          color,
          vx: 0,
          vy: 0
        };
        nodes.current.push(node);

        for (let j = 0; j < 2; j++) {
          orbitals.current.push({
            nodeIndex,
            angle: Math.random() * Math.PI * 2,
            radius: 10 + Math.random() * 10,
            speed: 0.005 + Math.random() * 0.005,
            size: 2.5,
            color: "#7777FF",
            spark: 0
          });
        }

        if (layer > 0) {
          const prevTotal = nodesPerLayer.slice(0, layer).reduce((sum, n) => sum + n, 0);
          const prevCount = nodesPerLayer[layer - 1];
          for (let j = 0; j < prevCount; j++) {
            edges.current.push({
              from: prevTotal - prevCount + j,
              to: nodeIndex,
              width: 1.9,
              alpha: 0.7
            });
          }
        }
        nodeIndex++;
      }
    });
  };

  return (
    <canvas
      ref={canvasRef}
      className={`w-full h-full ${className}`}
      style={{ backgroundColor: "transparent", cursor: "grab" }}
    />
  );
};

export default AIVisualizer;