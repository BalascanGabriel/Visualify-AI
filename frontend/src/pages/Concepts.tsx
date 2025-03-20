
import { useEffect } from 'react';
import { motion } from 'framer-motion';
import { ArrowRight, Battery, ChevronRight, CircuitBoard, FileLock2, Zap, Lightbulb, Plug, Cable, Gauge, Sparkles } from 'lucide-react';

import Header from '@/components/Header';
import Footer from '@/components/Footer';
import ConceptCard from '@/components/ConceptCard';
import ElectricalVisualizer from '@/components/ElectricalVisualizer';

const Concepts = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const electricityConcepts = [
    {
      title: 'Circuits',
      description: 'Understand how electrical circuits work, from simple to complex, and how electrons flow through them.',
      icon: <CircuitBoard />,
      color: '#4896ef',
      link: '#circuits'
    },
    {
      title: 'Voltage & Current',
      description: 'Explore the relationship between voltage, current, and resistance in electrical systems.',
      icon: <Zap />,
      color: '#9d50ff',
      link: '#voltage-current'
    },
    {
      title: 'Components',
      description: 'Learn about resistors, capacitors, inductors, and other electrical components that make up circuits.',
      icon: <Plug />,
      color: '#50c9ff',
      link: '#components'
    },
    {
      title: 'Batteries & Power',
      description: 'Discover how batteries and power sources work to provide electrical energy.',
      icon: <Battery />,
      color: '#ff6b6b',
      link: '#batteries'
    },
    {
      title: 'Conductors & Insulators',
      description: 'Understand the differences between materials that conduct electricity and those that block it.',
      icon: <Cable />,
      color: '#4cd964',
      link: '#conductors'
    },
    {
      title: 'Measurement & Units',
      description: 'Learn about volts, amps, ohms, and other units used to measure electricity.',
      icon: <Gauge />,
      color: '#ffcc00',
      link: '#measurement'
    }
  ];

  const componentTypes = [
    {
      name: 'Resistors',
      description: 'Control the flow of current in a circuit by providing resistance.',
      color: '#4896ef'
    },
    {
      name: 'Capacitors',
      description: 'Store and release electrical energy in the form of an electric field.',
      color: '#9d50ff'
    },
    {
      name: 'Inductors',
      description: 'Store energy in a magnetic field when current flows through them.',
      color: '#ff6b6b'
    },
    {
      name: 'Transistors',
      description: 'Control the flow of current, acting as switches or amplifiers.',
      color: '#4cd964'
    }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-grow pt-20">
        {/* Hero Section */}
        <section className="py-20 relative bg-secondary/30">
          <div className="container mx-auto px-4 md:px-6 relative z-10">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="max-w-3xl mx-auto text-center"
            >
              <h1 className="text-4xl md:text-5xl font-bold mb-6">Electricity Concepts Visualized</h1>
              <p className="text-lg text-muted-foreground mb-8">
                Explore electrical concepts through interactive visualizations that make complex topics approachable and intuitive.
              </p>
              <div className="flex justify-center">
                <a 
                  href="#all-concepts"
                  className="inline-flex items-center gap-2 px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition-all font-medium"
                >
                  Browse Concepts
                  <ChevronRight className="w-4 h-4" />
                </a>
              </div>
            </motion.div>
          </div>
        </section>
        
        {/* All Concepts Section */}
        <section id="all-concepts" className="py-20">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div 
              className="text-center mb-16"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Key Electricity Concepts</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Each concept includes interactive visualizations and clear explanations
              </p>
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
              {electricityConcepts.map((concept, index) => (
                <ConceptCard
                  key={index}
                  title={concept.title}
                  description={concept.description}
                  icon={concept.icon}
                  color={concept.color}
                  link={concept.link}
                />
              ))}
            </div>
          </div>
        </section>
        
        {/* Circuits Section */}
        <section id="circuits" className="py-20 bg-secondary/30">
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col md:flex-row items-center gap-12">
              <div className="md:w-1/2">
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6 }}
                  viewport={{ once: true }}
                >
                  <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#4896ef]/10 mb-6">
                    <CircuitBoard className="w-4 h-4 text-[#4896ef]" />
                    <span className="text-sm font-medium text-[#4896ef]">Circuits</span>
                  </div>
                  <h2 className="text-3xl md:text-4xl font-bold mb-6">
                    Understanding Electrical Circuits
                  </h2>
                  <p className="text-muted-foreground mb-6">
                    An electrical circuit is a path that electrons follow from a power source through conductors and components, and back to the source. Circuits enable us to control electrical energy and put it to work.
                  </p>
                  <p className="text-muted-foreground mb-6">
                    There are two main types of circuits: series and parallel, each with different properties and applications.
                  </p>
                  <div className="space-y-3 mb-8">
                    <div className="flex items-start gap-3">
                      <div className="w-6 h-6 rounded-full bg-[#4896ef]/10 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <Sparkles className="w-3 h-3 text-[#4896ef]" />
                      </div>
                      <div>
                        <strong className="block text-foreground">Series Circuits</strong>
                        <span className="text-sm text-muted-foreground">Components connected in a single path, sharing the same current</span>
                      </div>
                    </div>
                    <div className="flex items-start gap-3">
                      <div className="w-6 h-6 rounded-full bg-[#4896ef]/10 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <Sparkles className="w-3 h-3 text-[#4896ef]" />
                      </div>
                      <div>
                        <strong className="block text-foreground">Parallel Circuits</strong>
                        <span className="text-sm text-muted-foreground">Components connected in multiple paths, sharing the same voltage</span>
                      </div>
                    </div>
                    <div className="flex items-start gap-3">
                      <div className="w-6 h-6 rounded-full bg-[#4896ef]/10 flex items-center justify-center flex-shrink-0 mt-0.5">
                        <Sparkles className="w-3 h-3 text-[#4896ef]" />
                      </div>
                      <div>
                        <strong className="block text-foreground">Closed vs. Open Circuits</strong>
                        <span className="text-sm text-muted-foreground">Closed circuits allow current to flow, while open circuits break the path</span>
                      </div>
                    </div>
                  </div>
                </motion.div>
              </div>
              
              <div className="md:w-1/2">
                <motion.div
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6 }}
                  viewport={{ once: true }}
                  className="aspect-square max-w-md mx-auto rounded-xl overflow-hidden border border-border shadow-xl bg-white"
                >
                  <ElectricalVisualizer type="circuit" />
                </motion.div>
              </div>
            </div>
            
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="mt-16"
            >
              <h3 className="text-2xl font-bold mb-6">Circuit Components</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {componentTypes.map((component, index) => (
                  <div 
                    key={index}
                    className="p-6 rounded-xl glass-card border border-border"
                  >
                    <h4 className="text-xl font-semibold mb-3" style={{ color: component.color }}>{component.name}</h4>
                    <p className="text-muted-foreground">{component.description}</p>
                  </div>
                ))}
              </div>
            </motion.div>
          </div>
        </section>
        
        {/* Voltage & Current Section */}
        <section id="voltage-current" className="py-20">
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col md:flex-row items-center gap-12">
              <div className="md:w-1/2 order-2 md:order-1">
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6 }}
                  viewport={{ once: true }}
                  className="aspect-square max-w-md mx-auto rounded-xl overflow-hidden border border-border shadow-xl bg-white"
                >
                  <ElectricalVisualizer type="electrons" />
                </motion.div>
              </div>
              
              <div className="md:w-1/2 order-1 md:order-2">
                <motion.div
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6 }}
                  viewport={{ once: true }}
                >
                  <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#9d50ff]/10 mb-6">
                    <Zap className="w-4 h-4 text-[#9d50ff]" />
                    <span className="text-sm font-medium text-[#9d50ff]">Voltage & Current</span>
                  </div>
                  <h2 className="text-3xl md:text-4xl font-bold mb-6">
                    Understanding Voltage, Current, and Resistance
                  </h2>
                  <p className="text-muted-foreground mb-6">
                    The flow of electricity is governed by three fundamental concepts: voltage, current, and resistance, which are related by Ohm's Law.
                  </p>
                  <div className="space-y-6 mb-8">
                    <div className="p-4 rounded-lg bg-secondary/50 border border-border">
                      <h4 className="font-medium mb-2">Voltage (V)</h4>
                      <p className="text-sm text-muted-foreground">The electrical pressure or force that pushes electrons through a circuit, measured in volts (V).</p>
                    </div>
                    <div className="p-4 rounded-lg bg-secondary/50 border border-border">
                      <h4 className="font-medium mb-2">Current (I)</h4>
                      <p className="text-sm text-muted-foreground">The flow of electrons through a conductor, measured in amperes or amps (A).</p>
                    </div>
                    <div className="p-4 rounded-lg bg-secondary/50 border border-border">
                      <h4 className="font-medium mb-2">Resistance (R)</h4>
                      <p className="text-sm text-muted-foreground">The opposition to current flow in a circuit, measured in ohms (Ω).</p>
                    </div>
                  </div>
                </motion.div>
              </div>
            </div>
          </div>
        </section>
        
        {/* Components Section */}
        <section id="components" className="py-20 bg-secondary/30">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="text-center mb-16 max-w-3xl mx-auto"
            >
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-[#50c9ff]/10 mb-6">
                <Plug className="w-4 h-4 text-[#50c9ff]" />
                <span className="text-sm font-medium text-[#50c9ff]">Electrical Components</span>
              </div>
              <h2 className="text-3xl md:text-4xl font-bold mb-6">
                Exploring Electrical Components
              </h2>
              <p className="text-muted-foreground">
                Electrical components are the building blocks of circuits, each with specific functions to control, store, or transform electrical energy.
              </p>
            </motion.div>
            
            <motion.div
              initial={{ opacity: 0, y: 30 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8 }}
              viewport={{ once: true }}
              className="relative h-80 md:h-96 mb-16 rounded-xl overflow-hidden border border-border shadow-xl"
            >
              <ElectricalVisualizer type="components" />
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.1 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card"
              >
                <h3 className="text-xl font-bold mb-4">Passive Components</h3>
                <p className="text-muted-foreground">
                  Components that don't generate energy or require a power source, such as resistors, capacitors, and inductors. They modify or store energy in a circuit.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.2 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card"
              >
                <h3 className="text-xl font-bold mb-4">Active Components</h3>
                <p className="text-muted-foreground">
                  Components that can control current flow and typically require a power source, such as transistors, diodes, and integrated circuits.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.3 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card"
              >
                <h3 className="text-xl font-bold mb-4">Electromechanical</h3>
                <p className="text-muted-foreground">
                  Components that combine electrical and mechanical functions, such as switches, relays, and motors, allowing physical control of electricity.
                </p>
              </motion.div>
            </div>
          </div>
        </section>
        
        {/* More Content CTA */}
        <section className="py-20 bg-gradient-to-br from-primary/5 to-accent/5">
          <div className="container mx-auto px-4 md:px-6 text-center">
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              whileInView={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="max-w-2xl mx-auto"
            >
              <FileLock2 className="w-12 h-12 mx-auto text-primary mb-6" />
              <h2 className="text-3xl md:text-4xl font-bold mb-6">
                More Concepts Coming Soon
              </h2>
              <p className="text-muted-foreground mb-8">
                We're continuously adding new electricity concepts and visualizations to help you understand the fascinating world of electrical science.
              </p>
              <a 
                href="#all-concepts"
                className="inline-flex items-center gap-2 px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition-all font-medium"
              >
                Browse Available Concepts
                <ArrowRight className="w-4 h-4" />
              </a>
            </motion.div>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default Concepts;
