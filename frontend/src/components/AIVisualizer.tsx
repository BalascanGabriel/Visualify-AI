import { useEffect, useRef } from "react";
import gsap from "gsap";

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
  type?: "neural-network" | "connections" | "particles";
  className?: string;
}

const AIVisualizer = ({ type = "neural-network", className = "" }: AIVisualizerProps) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const nodes: Node[] = useRef<Node[]>([]).current;
  const edges: Edge[] = useRef<Edge[]>([]).current;
  const animationRef = useRef<number>();
  const tiltRef = useRef({ x: 0, y: 0 });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const resizeCanvas = () => {
      const dpr = window.devicePixelRatio || 1;
      canvas.width = canvas.clientWidth * dpr;
      canvas.height = canvas.clientHeight * dpr;
      ctx.scale(dpr, dpr);
    };

    window.addEventListener("resize", resizeCanvas);
    resizeCanvas();

    if (type === "neural-network") {
      initializeNeuralNetwork();
    } else if (type === "connections") {
      initializeConnections();
    }

    animateWithGSAP();
    animateCanvas();

    const handleMouseMove = (e: MouseEvent) => {
      const rect = canvas.getBoundingClientRect();
      const x = (e.clientX - rect.left - rect.width / 2) / rect.width;
      const y = (e.clientY - rect.top - rect.height / 2) / rect.height;
      gsap.to(tiltRef.current, { x, y, duration: 0.6, ease: "power3.out" });
    };

    canvas.addEventListener("mousemove", handleMouseMove);

    return () => {
      window.removeEventListener("resize", resizeCanvas);
      canvas.removeEventListener("mousemove", handleMouseMove);
      if (animationRef.current) cancelAnimationFrame(animationRef.current);
    };
  }, [type]);

  const animateWithGSAP = () => {
    nodes.forEach((node) => {
      gsap.to(node, {
        x: `+=${Math.random() * 100 - 50}`,
        y: `+=${Math.random() * 100 - 50}`,
        duration: 1.8,
        repeat: -1,
        yoyo: true,
        ease: "sine.inOut",
      });
    });

    gsap.to(edges, {
      alpha: 0.9,
      duration: 1.2,
      repeat: -1,
      yoyo: true,
      ease: "power1.inOut",
      stagger: 0.02,
    });
  };

  const animateCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const draw = () => {
      ctx.fillStyle = "#FFFFFF";
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.save();

      const tiltX = tiltRef.current.x * 20;
      const tiltY = tiltRef.current.y * 20;
      ctx.translate(canvas.width / 2, canvas.height / 2);
      ctx.rotate((-tiltX * Math.PI) / 180);
      ctx.rotate((tiltY * Math.PI) / 180);
      ctx.translate(-canvas.width / 2, -canvas.height / 2);

      edges.forEach((edge) => {
        const fromNode = nodes[edge.from];
        const toNode = nodes[edge.to];

        ctx.beginPath();
        ctx.strokeStyle = `rgba(50, 50, 50, ${edge.alpha})`;
        ctx.lineWidth = edge.width;
        ctx.moveTo(fromNode.x, fromNode.y);
        ctx.lineTo(toNode.x, toNode.y);
        ctx.stroke();
      });

      nodes.forEach((node) => {
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
    nodes.length = 0;
    edges.length = 0;

    const layers = 4;
    const nodesPerLayer = [5, 7, 7, 2];
    const canvasWidth = canvasRef.current!.clientWidth;
    const canvasHeight = canvasRef.current!.clientHeight;

    nodesPerLayer.forEach((numNodes, layer) => {
      const xPos = ((layer + 1) / (layers + 1)) * canvasWidth;

      for (let i = 0; i < numNodes; i++) {
        const yPos = ((i + 1) / (numNodes + 1)) * canvasHeight;
        nodes.push({
          x: xPos,
          y: yPos,
          radius: 10,
          color: layer === 0 ? "#FF6B6B" : layer === layers - 1 ? "#6B47FF" : "#6BCB77",
          vx: 0,
          vy: 0,
        });

        if (layer > 0) {
          const prevLayerOffset = nodesPerLayer.slice(0, layer).reduce((sum, n) => sum + n, 0);
          for (let j = prevLayerOffset - nodesPerLayer[layer - 1]; j < prevLayerOffset; j++) {
            edges.push({ from: j, to: nodes.length - 1, width: 2.5, alpha: 0.5 });
          }
        }
      }
    });
  };

  const initializeConnections = () => {
    // similar logic
  };

  return <canvas ref={canvasRef} className={`w-full h-full ${className}`} />;
};

export default AIVisualizer;
