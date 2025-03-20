
import { useState } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight } from 'lucide-react';
import { NavLink } from 'react-router-dom';

export interface ConceptCardProps {
  title: string;
  description: string;
  icon: React.ReactNode;
  color: string;
  link: string;
}

const ConceptCard = ({ title, description, icon, color, link }: ConceptCardProps) => {
  const [isHovered, setIsHovered] = useState(false);
  
  return (
    <motion.div
      className="relative overflow-hidden rounded-xl glass-card group"
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
      viewport={{ once: true, margin: "-50px" }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
    >
      <div className="p-6 h-full flex flex-col">
        <div 
          className="w-12 h-12 rounded-lg flex items-center justify-center mb-4"
          style={{ backgroundColor: `${color}15` }}
        >
          <div className="text-[color] w-6 h-6" style={{ color }}>
            {icon}
          </div>
        </div>
        
        <h3 className="text-xl font-bold mb-3">{title}</h3>
        <p className="text-muted-foreground mb-6 flex-grow">{description}</p>
        
        <NavLink 
          to={link}
          className="inline-flex items-center gap-2 text-sm font-medium mt-auto group-hover:text-primary transition-colors"
        >
          Learn more
          <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
        </NavLink>
      </div>
      
      {/* Animated border */}
      <motion.div 
        className="absolute bottom-0 left-0 h-1"
        style={{ backgroundColor: color }}
        initial={{ width: 0 }}
        animate={{ width: isHovered ? '100%' : '0%' }}
        transition={{ duration: 0.3 }}
      />
    </motion.div>
  );
};

export default ConceptCard;
