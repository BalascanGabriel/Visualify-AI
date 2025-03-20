
import { ArrowRight, BookOpen, Brain, Lightbulb, Upload, Eye, Sparkles } from 'lucide-react';
import { useEffect } from 'react';
import { motion } from 'framer-motion';
import { NavLink } from 'react-router-dom';

import Header from '@/components/Header';
import Hero from '@/components/Hero';
import Footer from '@/components/Footer';
import AIVisualizer from '@/components/AIVisualizer';

const Index = () => {
  useEffect(() => {
    window.scrollTo(0, 0);
  }, []);

  const features = [
    {
      title: 'Visual Learning',
      description: 'Complex concepts transformed into intuitive visual representations for faster comprehension.',
      icon: <Eye />,
      color: '#4896ef'
    },
    {
      title: 'Personalized Curriculum',
      description: 'AI-generated learning plans tailored to your goals, schedule, and learning style.',
      icon: <Brain />,
      color: '#9d50ff'
    },
    {
      title: 'Any Subject Matter',
      description: 'From technical subjects to creative arts, our AI can visualize any topic for enhanced learning.',
      icon: <BookOpen />,
      color: '#50c9ff'
    }
  ];

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-grow">
        {/* Hero Section */}
        <section className="py-20 md:py-32 relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-b from-secondary/30 to-transparent -z-10"></div>
          
          <div className="container mx-auto px-4 md:px-6">
            <div className="flex flex-col md:flex-row items-center gap-8 md:gap-16">
              <div className="md:w-1/2 text-center md:text-left">
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6 }}
                >
                  <h1 className="text-4xl md:text-6xl font-bold mb-6 leading-tight">
                    Learn Anything <span className="text-primary">Visually</span> with AI
                  </h1>
                  <p className="text-lg md:text-xl text-muted-foreground mb-8">
                    Upload your study materials and let our AI transform them into visual learning experiences.
                    <span className="block mt-2 italic font-medium">"One picture is worth a thousand words"</span>
                  </p>
                  <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
                    <NavLink to="/learn">
                      <button className="px-6 py-3 bg-primary text-white rounded-lg hover:bg-primary/90 transition-all font-medium w-full sm:w-auto flex items-center justify-center gap-2">
                        Start Learning
                        <ArrowRight className="w-4 h-4" />
                      </button>
                    </NavLink>
                    <NavLink to="/about">
                      <button className="px-6 py-3 bg-secondary text-foreground rounded-lg hover:bg-secondary/80 transition-all font-medium w-full sm:w-auto">
                        About Visualify
                      </button>
                    </NavLink>
                  </div>
                </motion.div>
              </div>
              
              <div className="md:w-1/2">
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ duration: 0.8 }}
                  className="relative"
                >
                  <div className="aspect-square max-w-md mx-auto">
                    <AIVisualizer type="neural-network" />
                  </div>
                  <div className="absolute -bottom-4 -right-4 bg-white dark:bg-slate-800 px-4 py-2 rounded-lg shadow-lg">
                  </div>
                </motion.div>
              </div>
            </div>
          </div>
        </section>
        
        {/* How It Works Section */}
        <section className="py-20 bg-gradient-to-b from-white to-secondary/10 dark:from-background dark:to-secondary/10">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div 
              className="text-center mb-16"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-4">How Visualify Works</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Transform your learning experience in three simple steps
              </p>
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.1 }}
                viewport={{ once: true }}
                className="text-center"
              >
                <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
                  <Upload className="w-7 h-7 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-2">1. Upload Materials</h3>
                <p className="text-muted-foreground">
                  Simply upload your PDF study materials or textbooks to our platform.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
                viewport={{ once: true }}
                className="text-center"
              >
                <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
                  <Brain className="w-7 h-7 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-2">2. AI Processing</h3>
                <p className="text-muted-foreground">
                  Our AI analyzes the content and creates visual learning materials and a personalized curriculum.
                </p>
              </motion.div>
              
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.3 }}
                viewport={{ once: true }}
                className="text-center"
              >
                <div className="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center mx-auto mb-4">
                  <BookOpen className="w-7 h-7 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-2">3. Start Learning</h3>
                <p className="text-muted-foreground">
                  Follow your personalized learning plan with visual aids that make complex concepts easy to understand.
                </p>
              </motion.div>
            </div>
          </div>
        </section>
        
        {/* Features Section */}
        <section className="py-20">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div 
              className="text-center mb-16"
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
            >
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Features That Make Learning Better</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Our AI-powered visual learning platform is designed to transform the way you learn
              </p>
            </motion.div>
            
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {features.map((feature, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  viewport={{ once: true }}
                  className="p-6 rounded-xl border bg-white/50 dark:bg-slate-900/50 hover:shadow-md transition-all"
                >
                  <div 
                    className="w-12 h-12 rounded-lg flex items-center justify-center mb-4"
                    style={{ backgroundColor: `${feature.color}10` }}
                  >
                    <div style={{ color: feature.color }} className="w-6 h-6">
                      {feature.icon}
                    </div>
                  </div>
                  <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
                  <p className="text-muted-foreground">{feature.description}</p>
                </motion.div>
              ))}
            </div>
          </div>
        </section>
        
        {/* CTA Section */}
        <section className="py-20 bg-gradient-to-r from-primary/10 to-accent/10">
          <div className="container mx-auto px-4 md:px-6">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              viewport={{ once: true }}
              className="max-w-3xl mx-auto text-center"
            >
              <div className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-primary/10 mb-6">
                <Sparkles className="w-4 h-4 text-primary" />
                <span className="text-sm font-medium text-primary">Start Your Visual Learning Journey</span>
              </div>
              <h2 className="text-3xl md:text-4xl font-bold mb-6">
                Ready to Transform How You Learn?
              </h2>
              <p className="text-lg text-muted-foreground mb-8">
                Join thousands of learners who have accelerated their understanding through visual AI learning.
              </p>
              <NavLink to="/learn">
                <button className="px-8 py-4 bg-primary text-white rounded-lg hover:bg-primary/90 transition-all font-medium text-lg flex items-center gap-2 mx-auto">
                  Try Visualify Now
                  <ArrowRight className="w-5 h-5" />
                </button>
              </NavLink>
            </motion.div>
          </div>
        </section>
      </main>
      
      <Footer />
    </div>
  );
};

export default Index;
