# Strategic Pipeline Dashboard

## Overview

The Strategic Pipeline Dashboard is a modern, interactive dashboard for viewing and managing NUVIEW's business development opportunities. It features a dark SpaceX-inspired theme with advanced data visualization and filtering capabilities.

## Features

### 1. Executive Summary
- **Total Opportunities**: Count of all active opportunities
- **New Today**: Opportunities added in the last 24 hours
- **High Value**: Opportunities valued over $10M
- **Closing Soon**: Opportunities with deadlines within 90 days

### 2. Interactive Data Table
- **Tabulator Integration**: Advanced data table with:
  - Pagination (25/50/100/All records per page)
  - Sortable columns
  - Responsive collapse for mobile devices
  - Click rows to view detailed information
  - CSV export functionality

### 3. Pipeline Visualization
- **Drawflow Diagram**: Visual representation of the automated pipeline
  - Daily trigger at 3 AM UTC via GitHub Actions
  - 34 global data sources
  - Raw data collection and storage
  - Quality control validation (100% pass required)
  - Program generation
  - Automated deployment to GitHub Pages
  - Daily backup at 4 AM UTC

### 4. Detail Panel
- **Slide-over Panel**: Click any opportunity row to view:
  - Full title and description
  - Agency information with links
  - Value and funding details
  - Deadline and urgency
  - Next action items
  - Direct links to source and agency websites

### 5. Collapsible Sidebar
- **Navigation**: Quick access to all dashboard sections
- **Collapse Toggle**: Minimize sidebar to maximize content area
- **Last Refresh**: Shows when data was last updated

## Data Source

The dashboard loads data from `/data/opportunities.json`, which contains:
- Opportunity metadata (title, agency, value, etc.)
- Timeline information (deadline, days until, urgency)
- Links to sources and agency websites
- Category and pillar classifications

## Technologies Used

- **Bootstrap 5.3.3**: Responsive framework and UI components
- **Bootstrap Icons 1.11.3**: Icon set for UI elements
- **Tabulator 6.2.5**: Advanced data table library
- **Drawflow 0.2.1**: Node-based visual workflow editor
- **Vanilla JavaScript**: No framework dependencies for core logic

## Browser Compatibility

The dashboard works best in modern browsers:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Usage

### Accessing the Dashboard
Navigate to: `dashboard/strategic-pipeline.html`

### Navigation
Use the sidebar to jump to different sections:
- Executive Summary
- All Opportunities (data table)
- Space Systems
- DaaS / Geoint
- Funding & Grants
- Forecast Calendar
- Pipeline Matrix
- How It Works (pipeline diagram)

### Viewing Details
Click any row in the opportunities table to open the detail panel on the right side.

### Exporting Data
Click the "Export CSV" button above the opportunities table to download the data.

### Collapsing Sidebar
Click the menu icon (☰) in the top-left to collapse/expand the sidebar.

## Customization

### Theme Colors
The dashboard uses a dark theme with these primary colors:
- Background: `#0f172a` to `#1e293b` (gradient)
- Accent: `#ef4444` (NUVIEW red)
- Text: `#e2e8f0` (light gray)
- Borders: `#334155` (medium gray)

### Data Refresh
The dashboard automatically loads the latest data from `opportunities.json` on page load. The "Last refresh" timestamp in the sidebar shows when the data was last updated.

## Future Enhancements

Potential improvements for future versions:
- Real-time data updates via WebSocket
- Advanced filtering and search
- Custom views and saved filters
- Chart visualizations for trends
- Integration with CRM systems
- User authentication and personalization

## Security Considerations

### CDN Resources
The dashboard loads external libraries from CDN providers. For production deployment:

1. **Add SRI (Subresource Integrity) hashes** to all CDN resources
2. Example:
   ```html
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" 
         rel="stylesheet"
         integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH"
         crossorigin="anonymous"/>
   ```
3. Generate hashes using: `openssl dgst -sha384 -binary <file> | openssl base64 -A`

### XSS Protection
- All user-provided data is HTML-escaped before rendering
- Uses dedicated `escapeHtml()` function to sanitize strings
- Prevents script injection through opportunity titles, descriptions, etc.

### External Links
- All external links include `rel="noopener noreferrer"` attributes
- Prevents opened pages from accessing window.opener
- Protects against tabnabbing attacks

### Data Validation
- All numeric values are validated before display
- Date parsing includes validation checks
- Error messages are specific to the failure type
- URL validation before rendering links

## Support

For issues or questions about the Strategic Pipeline Dashboard, contact the NUVIEW development team.
