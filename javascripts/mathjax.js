// MathJax configuration for Renesis AI Assistant Documentation

window.MathJax = {
  tex: {
    inlineMath: [['\\(', '\\)']],
    displayMath: [['\\[', '\\]']],
    processEscapes: true,
    processEnvironments: true,
    packages: {
      '[+]': ['ams', 'newcommand', 'configmacros']
    },
    macros: {
      // Custom macros for AI/ML notation
      RR: '{\\mathbb{R}}',
      NN: '{\\mathbb{N}}',
      ZZ: '{\\mathbb{Z}}',
      QQ: '{\\mathbb{Q}}',
      CC: '{\\mathbb{C}}',
      
      // Vector notation
      vec: ['{\\mathbf{#1}}', 1],
      mat: ['{\\mathbf{#1}}', 1],
      
      // Machine learning specific
      argmax: '{\\operatorname{argmax}}',
      argmin: '{\\operatorname{argmin}}',
      softmax: '{\\operatorname{softmax}}',
      sigmoid: '{\\operatorname{sigmoid}}',
      
      // Probability and statistics
      Prob: ['{\\mathbb{P}\\left(#1\\right)}', 1],
      Exp: ['{\\mathbb{E}\\left[#1\\right]}', 1],
      Var: ['{\\operatorname{Var}\\left(#1\\right)}', 1],
      Cov: ['{\\operatorname{Cov}\\left(#1\\right)}', 1],
      
      // Common functions
      loss: '{\\mathcal{L}}',
      data: '{\\mathcal{D}}',
      model: '{\\mathcal{M}}',
      
      // Embedding and similarity
      embed: ['{\\text{embed}\\left(#1\\right)}', 1],
      sim: ['{\\text{sim}\\left(#1, #2\\right)}', 2],
      cosine: ['{\\text{cosine}\\left(#1, #2\\right)}', 2]
    }
  },
  options: {
    ignoreHtmlClass: 'tex2jax_ignore',
    processHtmlClass: 'tex2jax_process',
    renderActions: {
      addMenu: [0, '', '']
    }
  },
  loader: {
    load: ['[tex]/ams', '[tex]/newcommand', '[tex]/configmacros']
  },
  startup: {
    ready: function() {
      console.log('MathJax is loaded and ready for Renesis AI Assistant docs');
      MathJax.startup.defaultReady();
    }
  }
};

// Additional configuration for better integration with documentation theme
document.addEventListener('DOMContentLoaded', function() {
  // Add MathJax processing to dynamically loaded content
  const observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {
      if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
        // Check if MathJax is available and process new content
        if (window.MathJax && window.MathJax.typesetPromise) {
          window.MathJax.typesetPromise(mutation.addedNodes).catch(function(err) {
            console.warn('MathJax typeset failed:', err);
          });
        }
      }
    });
  });
  
  // Observe the main content area for changes
  const contentArea = document.querySelector('.md-content');
  if (contentArea) {
    observer.observe(contentArea, {
      childList: true,
      subtree: true
    });
  }
});

// Handle theme changes (light/dark mode)
document.addEventListener('DOMContentLoaded', function() {
  const themeToggle = document.querySelector('[data-md-component="palette"]');
  if (themeToggle) {
    themeToggle.addEventListener('change', function() {
      // Re-render MathJax content when theme changes
      setTimeout(function() {
        if (window.MathJax && window.MathJax.typesetPromise) {
          window.MathJax.typesetPromise().catch(function(err) {
            console.warn('MathJax re-render failed:', err);
          });
        }
      }, 100);
    });
  }
});

// Custom styling for MathJax in dark mode
function updateMathJaxForTheme() {
  const isDarkMode = document.body.getAttribute('data-md-color-scheme') === 'slate';
  
  if (isDarkMode) {
    // Apply dark mode styles to MathJax elements
    const style = document.createElement('style');
    style.id = 'mathjax-dark-mode';
    style.textContent = `
      .MathJax {
        color: #e0e0e0 !important;
      }
      .MathJax_Display {
        color: #e0e0e0 !important;
      }
      mjx-container[jax="CHTML"] {
        color: #e0e0e0 !important;
      }
    `;
    
    // Remove existing dark mode styles
    const existingStyle = document.getElementById('mathjax-dark-mode');
    if (existingStyle) {
      existingStyle.remove();
    }
    
    document.head.appendChild(style);
  } else {
    // Remove dark mode styles
    const existingStyle = document.getElementById('mathjax-dark-mode');
    if (existingStyle) {
      existingStyle.remove();
    }
  }
}

// Apply theme-specific styling when page loads
document.addEventListener('DOMContentLoaded', updateMathJaxForTheme);

// Monitor theme changes
const themeObserver = new MutationObserver(function(mutations) {
  mutations.forEach(function(mutation) {
    if (mutation.type === 'attributes' && mutation.attributeName === 'data-md-color-scheme') {
      updateMathJaxForTheme();
    }
  });
});

// Start observing theme changes
if (document.body) {
  themeObserver.observe(document.body, {
    attributes: true,
    attributeFilter: ['data-md-color-scheme']
  });
}