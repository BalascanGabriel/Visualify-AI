
import { useEffect, useRef, useState } from 'react';
import { ArrowRight, Zap } from 'lucide-react';
import { NavLink } from 'react-router-dom';

const HeroParticle = ({ delay = 0 }: { delay?: number }) => {
  return (
    <div 
      className="absolute rounded-full bg-primary/20 animate-pulse-slow" 
      style={{
        width: `${Math.random() * 30 + 10}px`,
        height: `${Math.random() * 30 + 10}px`,
        top: `${Math.random() * 80 + 10}%`,
        left: `${Math.random() * 80 + 10}%`,
        animationDelay: `${delay}s`,
        opacity: Math.random() * 0.7 + 0.3,
      }}
    />
  );
};

const Hero = () => {
  const [isVisible, setIsVisible] = useState(false);
  const heroRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    setIsVisible(true);
    
    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsVisible(entry.isIntersecting);
      },
      { threshold: 0.1 }
    );
    
    if (heroRef.current) {
      observer.observe(heroRef.current);
    }
    
    return () => {
      if (heroRef.current) {
        observer.unobserve(heroRef.current);
      }
    };
  }, []);

  return (
    <div 
      ref={heroRef}
      className="relative min-h-[90vh] flex flex-col items-center justify-center overflow-hidden"
    >
      {/* Animated background particles */}
      <div className="absolute inset-0 overflow-hidden">
        {Array.from({ length: 10 }).map((_, i) => (
          <HeroParticle key={i} delay={i * 0.5} />
        ))}
      </div>
      
      {/* Gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-background/0 via-background/50 to-background" />
      
      <div className="container mx-auto px-4 relative z-10 text-center max-w-4xl">
        <div className={`transition-all duration-1000 ${isVisible ? 'opacity-100' : 'opacity-0 transform translate-y-10'}`}>
          <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-secondary mb-6 animate-fade-in-down">
            <Zap className="w-4 h-4 text-primary" />
            <span className="text-sm font-medium">Visualizing Electricity Concepts</span>
          </div>
        </div>
        
        <h1 
          className={`text-4xl md:text-6xl lg:text-7xl font-bold mb-6 transition-all duration-1000 delay-300 ${
            isVisible ? 'opacity-100' : 'opacity-0 transform translate-y-10'
          }`}
        >
          Learn Electricity Through <span className="text-gradient">Visual Understanding</span>
        </h1>
        
        <p 
          className={`text-lg md:text-xl text-muted-foreground mb-10 max-w-2xl mx-auto transition-all duration-1000 delay-500 ${
            isVisible ? 'opacity-100' : 'opacity-0 transform translate-y-10'
          }`}
        >
          Explore electricity concepts through beautiful interactive visualizations. Understand circuits, current, voltage, and electrical components with clarity and ease.
        </p>
        
        <div 
          className={`flex flex-col sm:flex-row gap-4 justify-center transition-all duration-1000 delay-700 ${
            isVisible ? 'opacity-100' : 'opacity-0 transform translate-y-10'
          }`}
        >
          <NavLink 
            to="/concepts" 
            className="inline-flex items-center gap-2 px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition-all font-medium"
          >
            Explore Concepts
            <ArrowRight className="w-4 h-4" />
          </NavLink>
          <NavLink 
            to="/about" 
            className="inline-flex items-center gap-2 px-6 py-3 bg-secondary text-foreground rounded-lg hover:bg-secondary/80 transition-all font-medium"
          >
            Learn More
          </NavLink>
        </div>
      </div>
      
      {/* Bottom wave decoration */}
      <div className="absolute bottom-0 left-0 right-0 h-24 bg-gradient-to-t from-background to-transparent" />
    </div>
  );
};

export default Hero;
