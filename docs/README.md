# Renesis AI Assistant Documentation

This directory contains the complete documentation for the Renesis AI Assistant project. The documentation is built using modern web technologies with a sleek, responsive design.

## 📚 Documentation Structure

```
docs/
├── index.md                 # Main documentation homepage
├── installation.md          # Installation and setup guide
├── configuration.md         # Configuration reference
├── usage.md                 # User guide and how-to
├── architecture.md          # System architecture overview
├── api-reference.md         # API documentation
├── troubleshooting.md       # Common issues and solutions
├── faq.md                   # Frequently asked questions
├── contributing.md          # Contributing guidelines
├── requirements.txt         # Documentation dependencies
├── stylesheets/
│   └── extra.css           # Custom CSS styles
├── javascripts/
│   └── mathjax.js          # MathJax configuration
└── README.md               # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Local Development

1. **Install documentation dependencies**:
   ```bash
   pip install -r docs/requirements.txt
   ```

2. **Start the development server**:
   ```bash
   python -m http.server 8000
   ```

3. **Open your browser** and navigate to `http://localhost:8000`

4. **Edit documentation** - changes will be automatically reloaded

### Building for Production

1. **Build the static site**:
   ```bash
   npm run build
   ```

2. **The built site** will be in the `site/` directory

3. **Deploy** the contents of `site/` to your web server

## 🛠️ Development Workflow

### Making Changes

1. **Edit Markdown files** in the `docs/` directory
2. **Preview changes** using the local development server
3. **Test the build** using the build command
4. **Commit your changes** following our [contributing guidelines](contributing.md)

### Adding New Pages

1. **Create a new Markdown file** in the `docs/` directory
2. **Add the page to navigation** in the site configuration:
   ```yaml
   nav:
     - Home: index.md
     - Your New Page: your-new-page.md
   ```
3. **Link to the page** from other relevant documentation

### Styling and Customization

- **Custom CSS**: Edit `docs/stylesheets/extra.css`
- **Custom JavaScript**: Edit `docs/javascripts/mathjax.js` or add new files
- **Theme configuration**: Modify the site configuration

## 📝 Writing Guidelines

### Markdown Best Practices

- Use **clear, descriptive headings**
- Include a **table of contents** for long pages
- Use **code blocks** with language specification:
  ```python
  def example_function():
      return "Hello, World!"
  ```
- Add **admonitions** for important information:
  ```markdown
  !!! note "Important"
      This is an important note.
  
  !!! warning "Caution"
      This requires careful attention.
  
  !!! tip "Pro Tip"
      This is a helpful tip.
  ```

### Content Structure

1. **Start with an overview** of what the page covers
2. **Use numbered lists** for step-by-step instructions
3. **Include examples** for code and configuration
4. **Add cross-references** to related documentation
5. **End with next steps** or related resources

### Code Documentation

- **Include complete examples** that users can copy and run
- **Explain parameters** and return values
- **Show error handling** where appropriate
- **Use consistent formatting** for code blocks

### API Documentation

- **Document all public methods** and classes
- **Include parameter types** and descriptions
- **Show example requests and responses**
- **Document error codes** and messages

## 🎨 Styling Features

### Available Components

#### Status Badges
```html
<span class="status-badge success">Success</span>
<span class="status-badge warning">Warning</span>
<span class="status-badge error">Error</span>
<span class="status-badge info">Info</span>
```

#### Feature Cards
```html
<div class="feature-grid">
  <div class="feature-card">
    <div class="icon">🚀</div>
    <h3>Feature Title</h3>
    <p>Feature description goes here.</p>
  </div>
</div>
```

#### Button Links
```html
<a href="/path/to/page" class="button">Primary Button</a>
<a href="/path/to/page" class="button secondary">Secondary Button</a>
```

#### API Method Documentation
```html
<div class="api-method">
  <div class="method-name">process_query</div>
  <div class="method-signature">
    process_query(query: str, user_id: str) -> QueryResponse
  </div>
  <p>Method description goes here.</p>
</div>
```

### Mathematical Expressions

MathJax is configured for mathematical notation:

- **Inline math**: `\(E = mc^2\)`
- **Block math**: 
  ```
  \[
  \text{similarity} = \frac{\vec{a} \cdot \vec{b}}{||\vec{a}|| \cdot ||\vec{b}||}
  \]
  ```

### Dark Mode Support

The documentation automatically supports dark mode with:
- **Automatic theme detection**
- **Manual theme toggle**
- **Consistent styling** across themes
- **Proper contrast ratios** for accessibility

## 🔧 Configuration

### Site Configuration

The main configuration manages the site structure:

```yaml
site_name: Renesis AI Assistant Documentation
theme:
  name: readthedocs
  features:
    - search
    - navigation
```

### Plugin Configuration

- **Search**: Enhanced search with highlighting
- **Minify**: Optimizes HTML, CSS, and JS
- **Git info**: Shows last modified dates
- **Redirects**: Handles URL redirects

### Extension Configuration

- **PyMdown Extensions**: Enhanced Markdown features
- **Code highlighting**: Syntax highlighting for code blocks
- **Admonitions**: Callout boxes for notes and warnings
- **Tables**: Enhanced table formatting
- **Task lists**: Checkbox lists
- **Emoji**: Emoji support

## 🚀 Deployment

### GitHub Pages (Automatic)

The documentation is automatically deployed to GitHub Pages when:
- Changes are pushed to the `main` branch
- Changes are made to documentation files
- The GitHub Actions workflow completes successfully

### Manual Deployment

1. **Build the documentation**:
   ```bash
   npm run build
   ```

2. **Deploy to GitHub Pages**:
   ```bash
   npm run deploy
   ```

3. **Deploy to custom server**:
   ```bash
   # Copy the site/ directory to your web server
   rsync -av site/ user@server:/path/to/webroot/
   ```

### Docker Deployment

```dockerfile
FROM nginx:alpine
COPY site/ /usr/share/nginx/html/
EXPOSE 80
```

```bash
# Build the documentation
npm run build

# Build Docker image
docker build -t gutless-docs .

# Run container
docker run -p 8080:80 gutless-docs
```

## 🧪 Testing

### Local Testing

```bash
# Test build
npm run build --strict

# Test serve
npm run serve --strict

# Check for broken links
pip install linkchecker
linkchecker http://localhost:8000/
```

### Automated Testing

The GitHub Actions workflow includes:
- **Build testing**: Ensures documentation builds without errors
- **Link checking**: Validates internal and external links
- **Accessibility testing**: Checks for accessibility issues
- **Performance testing**: Runs Lighthouse audits
- **Spell checking**: Validates spelling and grammar
- **Markdown linting**: Ensures consistent formatting

## 📊 Analytics and Monitoring

### Google Analytics

To enable Google Analytics:

1. **Get a Google Analytics tracking ID**
2. **Update site configuration**:
   ```yaml
   extra:
     analytics:
       provider: google
       property: G-XXXXXXXXXX
   ```

### Performance Monitoring

- **Lighthouse CI**: Automated performance audits
- **Core Web Vitals**: Monitoring user experience metrics
- **Uptime monitoring**: Server availability checks

## 🔍 Search Configuration

### Search Features

- **Full-text search**: Searches all content
- **Search highlighting**: Highlights search terms
- **Search suggestions**: Provides search suggestions
- **Keyboard shortcuts**: `S` to focus search

### Search Optimization

- **Use descriptive headings** for better search results
- **Include relevant keywords** in content
- **Structure content logically** with proper hierarchy
- **Use meta descriptions** for pages

## 🌐 Internationalization

### Adding Languages

1. **Create language-specific directories**:
   ```
   docs/
   ├── en/
   │   ├── index.md
   │   └── ...
   └── es/
       ├── index.md
       └── ...
   ```

2. **Configure language selection** in the site configuration
3. **Update navigation** for each language
4. **Add language switcher** to theme

## 🔧 Troubleshooting

### Common Issues

#### Build Errors

```bash
# Clear cache and rebuild
rm -rf site/
npm run build --clean
```

#### Serve Issues

```bash
# Check for port conflicts
lsof -i :8000

# Use different port
npm run serve -- --port 8001
```

#### Plugin Errors

```bash
# Update dependencies
pip install --upgrade -r docs/requirements.txt

# Check plugin compatibility
npm --version
```

### Getting Help

- **Check the project documentation**
- **Review the styling guide**
- **Search project issues on GitHub**
- **Ask in project discussions**

## 📈 Best Practices

### Performance

- **Optimize images** before adding to documentation
- **Use appropriate image formats** (WebP, SVG when possible)
- **Minimize external dependencies**
- **Enable compression** in web server configuration

### Accessibility

- **Use semantic HTML** in custom components
- **Provide alt text** for images
- **Ensure proper heading hierarchy**
- **Test with screen readers**
- **Maintain good color contrast**

### SEO

- **Use descriptive page titles**
- **Include meta descriptions**
- **Structure content with proper headings**
- **Use internal linking**
- **Optimize for relevant keywords**

### Maintenance

- **Regular dependency updates**
- **Monitor for broken links**
- **Review and update content regularly**
- **Archive outdated information**
- **Maintain consistent style and tone**

## 🤝 Contributing

We welcome contributions to the documentation! Please see our [Contributing Guide](contributing.md) for detailed information on:

- **How to contribute**
- **Style guidelines**
- **Review process**
- **Code of conduct**

### Quick Contribution Steps

1. **Fork the repository**
2. **Create a feature branch**
3. **Make your changes**
4. **Test locally**
5. **Submit a pull request**

## 📞 Support

For documentation-related questions:

- **Create an issue** in the GitHub repository
- **Start a discussion** in GitHub Discussions
- **Contact the maintainers** directly

For general project support, see the main [README](../README.md).

---

*This documentation is continuously improved. Last updated: December 2024*