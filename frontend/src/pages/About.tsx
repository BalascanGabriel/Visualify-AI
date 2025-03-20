
import { useEffect } from 'react';
import { motion } from 'framer-motion';
import { Brain, Laptop, LineChart, Mail, MessageCircle, ShieldCheck, SmilePlus, Target, UsersRound } from 'lucide-react';

import Header from '@/components/Header';
import Footer from '@/components/Footer';
import AIVisualizer from '@/components/AIVisualizer';

const About = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const missionItems = [
    {
      icon: <Target />,
      title: 'Simplify AI Learning',
      description: 'Making complex AI concepts accessible to everyone through visual learning.'
    },
    {
      icon: <UsersRound />,
      title: 'Bridge Knowledge Gaps',
      description: 'Creating resources that help people of all backgrounds understand AI technology.'
    },
    {
      icon: <SmilePlus />,
      title: 'Inspire Innovation',
      description: 'Encouraging the next generation of AI developers and enthusiasts.'
    }
  ];

  const teamMembers = [
    {
      name: 'Pop Mihai',
      role: 'Visual Designer (just student)',
      image: 'https://images.unsplash.com/photo-1689019764274-64ba1b0adcdb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
      name: 'Georgescu Alexandru',
      role: 'AI Developer (just student)',
      image: 'https://images.unsplash.com/photo-1689019764274-64ba1b0adcdb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
      name: 'Vascuta Denis',
      role: 'Interactive Developer (just student)',
      image: 'https://images.unsplash.com/photo-1689019764274-64ba1b0adcdb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
    },
    {
      name: 'Balascan Gabriel',
      role: 'AI Developer',
      image: 'https://images.unsplash.com/photo-1689019764274-64ba1b0adcdb?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
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
              <h1 className="text-4xl md:text-5xl font-bold mb-6">About AI Visualizer</h1>
              <p className="text-lg text-muted-foreground mb-8">
                Dedicated to making artificial intelligence concepts more accessible and understandable through visual learning.
              </p>
            </motion.div>
          </div>
        </section>
        
        {/* Our Mission Section */}
        <section className="py-20">
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col md:flex-row items-center gap-12">
              <div className="md:w-1/2">
                <motion.div
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  transition={{ duration: 0.6 }}
                  viewport={{ once: true }}
                >
                  <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 mb-6">
                    <Brain className="w-4 h-4 text-primary" />
                    <span className="text-sm font-medium text-primary">Our Mission</span>
                  </div>
                  <h2 className="text-3xl md:text-4xl font-bold mb-6">
                    Visualizing the Future of AI Learning
                  </h2>
                  <p className="text-muted-foreground mb-8">
                    AI Visualizer was created with a simple but powerful mission: to make artificial intelligence concepts accessible to everyone through visual learning. We believe that understanding AI shouldn't require a computer science degree, but should be approachable for curious minds from all backgrounds.
                  </p>
                  
                  <div className="space-y-6">
                    {missionItems.map((item, index) => (
                      <div key={index} className="flex items-start gap-4">
                        <div className="w-10 h-10 rounded-lg flex items-center justify-center bg-primary/10 flex-shrink-0">
                          <div className="text-primary w-5 h-5">
                            {item.icon}
                          </div>
                        </div>
                        <div>
                          <h3 className="font-semibold text-lg mb-1">{item.title}</h3>
                          <p className="text-muted-foreground">{item.description}</p>
                        </div>
                      </div>
                    ))}
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
                  <AIVisualizer type="neural-network" />
                </motion.div>
              </div>
            </div>
          </div>
        </section>
        
        {/* Our Values Section */}
        <section className="py-20 bg-secondary/30">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="text-center mb-16"
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-6">Our Core Values</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Principles that guide our approach to teaching and visualizing AI concepts
              </p>
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.1 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card text-center"
              >
                <div className="w-12 h-12 rounded-full bg-[#4896ef]/10 flex items-center justify-center mx-auto mb-4">
                  <LineChart className="w-6 h-6 text-[#4896ef]" />
                </div>
                <h3 className="text-xl font-bold mb-3">Clarity & Simplicity</h3>
                <p className="text-muted-foreground">
                  We break down complex concepts into clear, understandable visuals that focus on essential components without oversimplifying.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card text-center"
              >
                <div className="w-12 h-12 rounded-full bg-[#9d50ff]/10 flex items-center justify-center mx-auto mb-4">
                  <Laptop className="w-6 h-6 text-[#9d50ff]" />
                </div>
                <h3 className="text-xl font-bold mb-3">Interactive Learning</h3>
                <p className="text-muted-foreground">
                  We believe in learning by doing, which is why our visualizations encourage exploration and experimentation.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.3 }}
                viewport={{ once: true }}
                className="p-6 rounded-xl glass-card text-center"
              >
                <div className="w-12 h-12 rounded-full bg-[#50c9ff]/10 flex items-center justify-center mx-auto mb-4">
                  <ShieldCheck className="w-6 h-6 text-[#50c9ff]" />
                </div>
                <h3 className="text-xl font-bold mb-3">Technical Accuracy</h3>
                <p className="text-muted-foreground">
                  We ensure our visualizations are not just accessible but also technically sound and representative of real AI principles.
                </p>
              </motion.div>
            </div>
          </div>
        </section>
        
        {/* Team Section */}
        <section className="py-20">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="text-center mb-16"
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-6">Meet Our Team</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Passionate experts combining AI knowledge with visual design excellence
              </p>
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
              {teamMembers.map((member, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  className="text-center"
                >
                  <div className="mb-4 w-32 h-32 mx-auto relative">
                    <div className="absolute inset-0 rounded-full bg-gradient-to-br from-primary to-accent animate-pulse-slow"></div>
                    <img 
                      src={member.image} 
                      alt={member.name} 
                      className="w-28 h-28 object-cover rounded-full mx-auto relative z-10 border-4 border-background"
                    />
                  </div>
                  <h3 className="text-xl font-bold">{member.name}</h3>
                  <p className="text-muted-foreground">{member.role}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
        
        {/* Contact Section */}
        <section className="py-20 bg-gradient-to-br from-primary/5 to-accent/5">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="max-w-3xl mx-auto text-center"
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-6">Get In Touch</h2>
              <p className="text-muted-foreground mb-12">
                Have questions, feedback, or ideas for new AI visualizations? We'd love to hear from you!
              </p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div className="p-6 rounded-xl glass-card text-center">
                  <div className="w-12 h-12 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
                    <Mail className="w-6 h-6 text-primary" />
                  </div>
                  <h3 className="text-xl font-bold mb-3">Email Us</h3>
                  <p className="text-muted-foreground mb-4">
                    For general inquiries and questions
                  </p>
                  <a 
                    href="mailto:contact@aivisualizer.com" 
                    className="text-primary hover:underline"
                  >
                    contact@visualify.com
                  </a>
                </div>
                
                <div className="p-6 rounded-xl glass-card text-center">
                  <div className="w-12 h-12 rounded-full bg-accent/10 flex items-center justify-center mx-auto mb-4">
                    <MessageCircle className="w-6 h-6 text-accent" />
                  </div>
                  <h3 className="text-xl font-bold mb-3">Live Chat</h3>
                  <p className="text-muted-foreground mb-4">
                    Chat with our team in real-time
                  </p>
                  <button 
                    className="text-accent hover:underline"
                  >
                    Start a conversation
                  </button>
                </div>
              </div>
            </motion.div>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default About;
