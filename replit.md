# Jovian Careers Website

## Overview
A Flask-based careers website for Jovian, showcasing open job positions. The site features a modern, responsive design with a clean interface for browsing available positions.

## Project Structure
```
jovian-careers-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── home.html         # Main homepage template
└── static/               # Static assets directory
```

## Technology Stack
- **Framework**: Flask 3.0.0
- **Language**: Python 3.11
- **Server**: Gunicorn (for production)
- **Template Engine**: Jinja2

## Features
- Responsive homepage with gradient banner
- Job listings with details (title, location, salary)
- REST API endpoint for job data (`/api/jobs`)
- Modern, accessible UI design

## Development
- The app runs on `0.0.0.0:5000` for development
- Debug mode is enabled in development
- Workflow is configured to auto-start the Flask development server

## API Endpoints
- `GET /` - Homepage with job listings
- `GET /api/jobs` - JSON API endpoint returning all jobs

## Recent Changes
- **2025-11-06**: Initial project setup
  - Created Flask application structure
  - Added job listings for Data Analyst, Data Scientist, Frontend Engineer, and Backend Engineer
  - Designed responsive homepage template
  - Configured development workflow
