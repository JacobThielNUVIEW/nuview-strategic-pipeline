# NUVIEW Pipeline Matrix - Documentation

## Overview

The **NUVIEW Pipeline Matrix** is an interactive, executive-level visualization of the data processing pipeline. It provides real-time status updates, animated flow indicators, and detailed information about each stage of the NUVIEW intelligence pipeline.

## Features

### 🎨 Visual Design
- **NUVIEW-branded colors**: Uses official palette (Red #E41C24/#EE3338, Deep Black, Dark Gray, Crisp White)
- **Animated SVG nodes**: Gradient-filled pipeline stages with pulsing status indicators
- **Flow arrows**: Animated connection arrows showing data flow between stages
- **Hover effects**: Interactive tooltips with detailed stage descriptions
- **Responsive layout**: Optimized for desktop, tablet, and mobile devices

### 📊 Live Data Integration
- Pulls real-time data from:
  - `../data/opportunities.json` - Opportunity pipeline data
  - `../data/processed/qc_report.json` - Quality control reports
- Automatic fallback to demo data if files are missing
- Auto-refreshes every 30 seconds
- Displays current pipeline status, last run time, and QC metrics

### 🎯 Pipeline Stages

#### 1. SCRAPE 🕷️
- **Script**: `scrape_all.py`
- **Function**: Automated daily collection of federal and commercial LiDAR opportunities
- **Sources**: SAM.gov, NASA, ESA, and other agencies
- **Schedule**: Runs via GitHub Actions at 3:00 AM UTC

#### 2. QC ✅
- **Script**: `qc_validator.py`
- **Function**: Validates data integrity and quality
- **Checks**: Required fields, proper formatting, data completeness
- **Output**: Quality reports with error and warning counts

#### 3. MATRIX 📊
- **File**: `priority_matrix.csv`
- **Function**: Processes and prioritizes opportunities
- **Categorization**: DaaS, R&D, and Platform opportunities
- **Scoring**: Urgency and priority score calculations

#### 4. MERGE 🔗
- **Process**: `data_integration`
- **Function**: Merges data from multiple sources
- **Sources**: Opportunities, forecast, global tracker
- **Output**: Unified, consistent datasets

#### 5. DASHBOARD 📈
- **File**: `index.html`
- **Function**: Presents data through interactive dashboards
- **Views**: Main dashboard, pipeline view, global tracker
- **Updates**: Real-time with latest data

### 📱 Responsive Design

The pipeline matrix automatically adapts to different screen sizes:
- **Desktop (>1200px)**: 5-column grid layout with full SVG arrows
- **Tablet (768px-1200px)**: 3-column grid layout
- **Mobile (<768px)**: Single-column stacked layout

## Installation & Usage

### Standalone Access

Simply open the file in a web browser:
```bash
# Local development
python -m http.server 8000
# Then navigate to: http://localhost:8000/dashboard/pipeline_matrix.html
```

### Embedding in Dashboard

#### Option 1: Iframe Embed
Add this HTML to any page:
```html
<iframe src="dashboard/pipeline_matrix.html" 
        width="100%" 
        height="800px" 
        frameborder="0"
        style="border-radius: 12px;">
</iframe>
```

#### Option 2: Direct Link
Add a navigation link:
```html
<a href="dashboard/pipeline_matrix.html" class="pipeline-matrix-link">
    <i class="bi bi-diagram-3"></i> View Pipeline Matrix →
</a>
```

#### Option 3: Sidebar Navigation
The matrix is already integrated into the main dashboard sidebar:
```html
<a href="pipeline_matrix.html">
    <i class="bi bi-diagram-3"></i> Pipeline Matrix
</a>
```

## Data Requirements

### Required Files

1. **opportunities.json** (`../data/opportunities.json`)
   ```json
   {
     "meta": {
       "market_val": "14.13",
       "cagr": "19.43",
       "updated": "2025-11-20T20:55:20Z",
       "totalCount": 4
     },
     "opportunities": [...]
   }
   ```

2. **qc_report.json** (`../data/processed/qc_report.json`)
   ```json
   {
     "timestamp": "2025-11-20T21:13:49Z",
     "qc_status": "PASS",
     "qc_percentage": 100,
     "total_errors": 0,
     "total_warnings": 2,
     "summary": "QC PASSED with 0 errors and 2 warnings"
   }
   ```

### Fallback Behavior

If data files are missing or fail to load:
- Automatically switches to demo data
- Shows placeholder values
- Continues to function normally
- Console warnings indicate demo mode

## Status Indicators

The pipeline matrix uses color-coded status indicators:

| Status | Color | Animation | Meaning |
|--------|-------|-----------|---------|
| **Operational** | Red (#EE3338) | Pulsing | Stage is running normally |
| **Idle** | Light Gray (#666666) | None | Stage is inactive/waiting |
| **Loading** | Light Gray (#666666) | Spinning | Stage is processing |
| **Fail** | Red (#E41C24) | Blinking | Stage has errors |

## Interactivity

### Hover Effects
- **Node Hover**: Shows detailed tooltip with stage description
- **Visual Feedback**: Node lifts with glow effect
- **Smooth Transitions**: CSS animations for polished feel

### Click Events
Currently, nodes are clickable but don't navigate. Future enhancements could:
- Open detailed logs for each stage
- Navigate to stage-specific dashboards
- Display historical performance data

## Performance

- **Load Time**: <2 seconds (depends on data file sizes)
- **Auto-Refresh**: Every 30 seconds (configurable)
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **No External Dependencies**: Standalone HTML/CSS/JS (except fonts)

## Customization

### Changing Colors
Edit the CSS variables in the `<style>` section:
```css
:root {
    --nuview-red-primary: #E41C24;
    --nuview-red-bright: #EE3338;
    --nuview-black: #000000;
    --nuview-dark-gray: #1a1a1a;
    /* ... more colors ... */
}
```

### Modifying Node Information
Edit the `nodeDescriptions` object in JavaScript:
```javascript
const nodeDescriptions = {
    scrape: {
        title: 'Your Custom Title',
        content: 'Your custom description'
    },
    // ... more nodes ...
};
```

### Adjusting Refresh Rate
Change the interval in JavaScript (currently 30 seconds):
```javascript
// Auto-refresh data every 30 seconds
setInterval(() => {
    loadPipelineData();
}, 30000); // Change to desired milliseconds
```

## Troubleshooting

### Data Not Loading
1. Check browser console for error messages
2. Verify data files exist at correct paths
3. Ensure proper JSON formatting
4. Check CORS settings if hosting on different domain

### Arrows Not Appearing
1. Ensure SVG is not blocked by content security policy
2. Check browser support for SVG
3. Verify window has loaded before drawing arrows
4. Try resizing browser window to trigger redraw

### Mobile Layout Issues
1. Clear browser cache
2. Test in different mobile browsers
3. Check viewport meta tag is present
4. Verify responsive CSS media queries

## Future Enhancements

Potential improvements for future versions:

1. **Historical Data**: Show trend graphs for each stage
2. **Performance Metrics**: Display processing times and throughput
3. **Alert System**: Real-time notifications for failures
4. **Drill-Down Views**: Click nodes to see detailed logs
5. **Comparison Mode**: Compare current vs. previous runs
6. **Export Functionality**: Download pipeline reports as PDF
7. **Dark/Light Themes**: Toggle between color schemes
8. **Custom Workflows**: Drag-and-drop to build custom pipelines

## Support

For questions, issues, or feature requests:
- **Internal**: Contact the NUVIEW development team
- **Documentation**: Refer to main README.md in repository root
- **Updates**: Check repository for latest version

## Version History

- **v1.0.0** (Nov 2025): Initial release
  - Interactive node-based visualization
  - Live data integration
  - Responsive design
  - NUVIEW brand styling
  - Embedded documentation

## License

Proprietary - NUVIEW Space Technologies, Inc.

---

**Last Updated**: November 2025  
**Maintained By**: NUVIEW Development Team  
**Status**: Production Ready
