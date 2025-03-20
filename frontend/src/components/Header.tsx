
import { useState, useEffect } from 'react';
import { NavLink } from 'react-router-dom';
import { Zap, Menu, X } from 'lucide-react';
import logo from './logo.png'

const Header = () => {
  const [scrolled, setScrolled] = useState(false);
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY > 20) {
        setScrolled(true);
      } else {
        setScrolled(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  return (
    <header 
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        scrolled ? 'py-3 bg-white/80 dark:bg-slate-900/80 backdrop-blur-md shadow-sm' : 'py-5 bg-transparent'
      }`}
    >
      <div className="container mx-auto px-4 md:px-6 flex items-center justify-between">
        <NavLink 
          to="/" 
          className="flex items-center gap-2 font-display font-bold text-xl transition-all"
        >
          <img src={logo} alt={'logo'} className="w-7 h-6 text-primary" />
          <span className="text-gradient">Visualify</span>
        </NavLink>
        
        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-6">
          <NavLink 
            to="/" 
            className={({ isActive }) => 
              `font-medium transition-all hover:text-primary ${isActive ? 'text-primary' : ''}`
            }
          >
            Home
          </NavLink>
          <NavLink 
            to="/learn" 
            className={({ isActive }) => 
              `font-medium transition-all hover:text-primary ${isActive ? 'text-primary' : ''}`
            }
          >
            Learn
          </NavLink>
          <NavLink 
            to="/about" 
            className={({ isActive }) => 
              `font-medium transition-all hover:text-primary ${isActive ? 'text-primary' : ''}`
            }
          >
            About
          </NavLink>
        </nav>

        {/* Mobile Menu Button */}
        <button 
          className="md:hidden text-foreground"
          onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
          aria-label="Toggle menu"
        >
          {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
        </button>
      </div>

      {/* Mobile Menu */}
      <div 
        className={`fixed inset-0 z-40 bg-background pt-20 px-4 transition-transform duration-300 transform ${
          mobileMenuOpen ? 'translate-x-0' : 'translate-x-full'
        } md:hidden`}
      >
        <nav className="flex flex-col gap-4">
          <NavLink 
            to="/" 
            className={({ isActive }) => 
              `py-3 px-4 font-medium text-lg rounded-md transition-all ${
                isActive ? 'bg-secondary text-primary' : 'hover:bg-secondary/50'
              }`
            }
            onClick={() => setMobileMenuOpen(false)}
          >
            Home
          </NavLink>
          <NavLink 
            to="/learn" 
            className={({ isActive }) => 
              `py-3 px-4 font-medium text-lg rounded-md transition-all ${
                isActive ? 'bg-secondary text-primary' : 'hover:bg-secondary/50'
              }`
            }
            onClick={() => setMobileMenuOpen(false)}
          >
            Learn
          </NavLink>
          <NavLink 
            to="/about" 
            className={({ isActive }) => 
              `py-3 px-4 font-medium text-lg rounded-md transition-all ${
                isActive ? 'bg-secondary text-primary' : 'hover:bg-secondary/50'
              }`
            }
            onClick={() => setMobileMenuOpen(false)}
          >
            About
          </NavLink>
        </nav>
      </div>
    </header>
  );
};

export default Header;
