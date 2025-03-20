
import { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { ArrowLeft, ArrowRight, BookOpen } from 'lucide-react';

import Header from '@/components/Header';
import Footer from '@/components/Footer';
import { Button } from '@/components/ui/button';
import AIVisualizer from '@/components/AIVisualizer';

// Define the correct type for visualizerType to match AIVisualizer's type prop
type VisualizerType = 'neural-network' | 'connections' | 'particles';

// Mock lesson data - in a real app, this would come from the backend
const mockLessons = [
  {
    id: "ch1",
    title: "What is Machine Learning?",
    content: `
      <h2>Introduction to Machine Learning</h2>
      <p>Machine Learning is a subset of artificial intelligence that focuses on developing systems that can learn from and make decisions based on data.</p>
      <p>Unlike traditional programming where explicit instructions are provided, machine learning algorithms build a model based on sample data, known as training data, to make predictions or decisions without being explicitly programmed to do so.</p>
      <h3>Key Concepts</h3>
      <ul>
        <li><strong>Training:</strong> The process of teaching a model using data</li>
        <li><strong>Features:</strong> The input variables used by the model</li>
        <li><strong>Labels:</strong> The output or target variables the model tries to predict</li>
        <li><strong>Inference:</strong> Using the trained model to make predictions</li>
      </ul>
    `,
    visualizerType: "neural-network" as VisualizerType,
    nextChapter: "ch2",
    prevChapter: null
  },
  {
    id: "ch2",
    title: "Supervised vs Unsupervised Learning",
    content: `
      <h2>Types of Machine Learning</h2>
      <p>Machine learning can be categorized into several types based on how algorithms learn and make predictions.</p>
      <h3>Supervised Learning</h3>
      <p>In supervised learning, the algorithm is trained on labeled data, meaning that each training example has an input-output pair. The goal is to learn a mapping function that can predict the output for new, unseen inputs.</p>
      <h3>Unsupervised Learning</h3>
      <p>In unsupervised learning, the algorithm is given data without explicit instructions on what to do with it. The goal is to model the underlying structure or distribution of the data to learn more about it.</p>
      <h3>Key Differences</h3>
      <ul>
        <li><strong>Data:</strong> Supervised uses labeled data; unsupervised uses unlabeled data</li>
        <li><strong>Goal:</strong> Supervised predicts outputs; unsupervised finds patterns</li>
        <li><strong>Applications:</strong> Supervised for classification and regression; unsupervised for clustering and dimensionality reduction</li>
      </ul>
    `,
    visualizerType: "connections" as VisualizerType,
    nextChapter: "ch3",
    prevChapter: "ch1"
  },
  {
    id: "ch3",
    title: "Neural Networks Fundamentals",
    content: `
      <h2>Neural Network Basics</h2>
      <p>Neural networks are computing systems inspired by the biological neural networks that constitute animal brains. They are a series of algorithms that endeavors to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates.</p>
      <h3>Components of a Neural Network</h3>
      <ul>
        <li><strong>Neurons:</strong> The basic computational unit</li>
        <li><strong>Weights:</strong> Parameters that transform input data within the network</li>
        <li><strong>Activation Functions:</strong> Determine the output of a neural network node</li>
        <li><strong>Layers:</strong> Groups of neurons that process specific features</li>
      </ul>
      <h3>Types of Layers</h3>
      <ul>
        <li><strong>Input Layer:</strong> Receives the raw data</li>
        <li><strong>Hidden Layers:</strong> Perform computations and transfer information</li>
        <li><strong>Output Layer:</strong> Produces the final result</li>
      </ul>
    `,
    visualizerType: "neural-network" as VisualizerType,
    nextChapter: "ch4",
    prevChapter: "ch2"
  },
  {
    id: "ch4",
    title: "Training Models: Best Practices",
    content: `
      <h2>Training Neural Networks</h2>
      <p>Training a neural network involves adjusting its parameters (weights and biases) to minimize the difference between its predictions and the actual outputs.</p>
      <h3>Key Steps in Training</h3>
      <ol>
        <li><strong>Data Preparation:</strong> Cleaning, normalizing, and splitting data</li>
        <li><strong>Model Architecture:</strong> Designing the network structure</li>
        <li><strong>Forward Propagation:</strong> Computing predictions</li>
        <li><strong>Loss Calculation:</strong> Measuring prediction error</li>
        <li><strong>Backpropagation:</strong> Computing gradients</li>
        <li><strong>Parameter Update:</strong> Adjusting weights and biases</li>
      </ol>
      <h3>Common Challenges</h3>
      <ul>
        <li><strong>Overfitting:</strong> When the model learns noise in the training data</li>
        <li><strong>Underfitting:</strong> When the model is too simple to capture patterns</li>
        <li><strong>Vanishing/Exploding Gradients:</strong> Issues with gradient propagation</li>
      </ul>
    `,
    visualizerType: "particles" as VisualizerType,
    nextChapter: "ch5",
    prevChapter: "ch3"
  },
  {
    id: "ch5",
    title: "Evaluating Model Performance",
    content: `
      <h2>Model Evaluation</h2>
      <p>Evaluating a machine learning model is crucial to understand its performance and how well it generalizes to unseen data.</p>
      <h3>Common Evaluation Metrics</h3>
      <h4>For Classification</h4>
      <ul>
        <li><strong>Accuracy:</strong> Proportion of correct predictions</li>
        <li><strong>Precision:</strong> Proportion of positive identifications that were actually correct</li>
        <li><strong>Recall:</strong> Proportion of actual positives that were identified correctly</li>
        <li><strong>F1 Score:</strong> Harmonic mean of precision and recall</li>
      </ul>
      <h4>For Regression</h4>
      <ul>
        <li><strong>Mean Absolute Error (MAE):</strong> Average absolute difference between predictions and actual values</li>
        <li><strong>Mean Squared Error (MSE):</strong> Average squared difference between predictions and actual values</li>
        <li><strong>R-squared:</strong> Proportion of variance in the dependent variable explained by the model</li>
      </ul>
    `,
    visualizerType: "neural-network" as VisualizerType,
    nextChapter: null,
    prevChapter: "ch4"
  }
];

const LessonPage = () => {
  const { chapterId } = useParams<{ chapterId: string }>();
  const [lesson, setLesson] = useState<typeof mockLessons[0] | null>(null);
  
  useEffect(() => {
    // In a real app, fetch the lesson data from your backend
    const currentLesson = mockLessons.find(l => l.id === chapterId);
    if (currentLesson) {
      setLesson(currentLesson);
      window.scrollTo(0, 0);
    }
  }, [chapterId]);
  
  if (!lesson) {
    return (
      <div className="min-h-screen flex flex-col">
        <Header />
        <main className="flex-grow pt-20 flex items-center justify-center">
          <div className="text-center">
            <h2 className="text-2xl font-bold mb-4">Loading lesson...</h2>
            <p className="text-muted-foreground">Please wait while we prepare your visual learning experience.</p>
          </div>
        </main>
        <Footer />
      </div>
    );
  }
  
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-grow pt-20">
        <div className="container mx-auto px-4 md:px-6 py-12">
          <div className="mb-6">
            <Link 
              to="/learn" 
              className="inline-flex items-center gap-2 text-sm font-medium hover:text-primary transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Back to Curriculum
            </Link>
          </div>
          
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ duration: 0.5 }}
            className="max-w-4xl mx-auto"
          >
            <div className="mb-8">
              <h1 className="text-3xl md:text-4xl font-bold mb-4">{lesson.title}</h1>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-5 gap-8 mb-12">
              <div className="col-span-3">
                <div 
                  className="prose prose-stone dark:prose-invert max-w-none"
                  dangerouslySetInnerHTML={{ __html: lesson.content }}
                />
              </div>
              
              <div className="col-span-2">
                <div className="sticky top-24">
                  <div className="aspect-square rounded-xl overflow-hidden border shadow-lg mb-4">
                    <AIVisualizer type={lesson.visualizerType as 'neural-network' | 'connections' | 'particles'} />
                  </div>
                  <p className="text-sm text-center text-muted-foreground italic">
                    "One picture is worth a thousand words"
                  </p>
                </div>
              </div>
            </div>
            
            <div className="flex justify-between items-center pt-6 border-t">
              {lesson.prevChapter ? (
                <Link to={`/learn/${lesson.prevChapter}`}>
                  <Button variant="outline" className="flex items-center gap-2">
                    <ArrowLeft className="w-4 h-4" />
                    Previous Chapter
                  </Button>
                </Link>
              ) : (
                <div></div>
              )}
              
              {lesson.nextChapter ? (
                <Link to={`/learn/${lesson.nextChapter}`}>
                  <Button className="bg-primary text-white hover:bg-primary/90 flex items-center gap-2">
                    Next Chapter
                    <ArrowRight className="w-4 h-4" />
                  </Button>
                </Link>
              ) : (
                <Link to="/learn">
                  <Button className="bg-primary text-white hover:bg-primary/90 flex items-center gap-2">
                    <BookOpen className="w-4 h-4" />
                    Complete Course
                  </Button>
                </Link>
              )}
            </div>
          </motion.div>
        </div>
      </main>
      
      <Footer />
    </div>
  );
};

export default LessonPage;
