# Netlify Deployment Guide - NUVIEW Strategic Pipeline

## Overview

This guide provides complete instructions for deploying the NUVIEW Strategic Pipeline to Netlify with automated deployments from the main branch.

## Prerequisites

1. A Netlify account (free tier is sufficient)
2. GitHub repository access
3. Admin permissions on the repository

## Initial Setup

### Step 1: Connect Repository to Netlify

1. **Log in to Netlify**: Go to [https://app.netlify.com](https://app.netlify.com)

2. **Create New Site**:
   - Click "Add new site" → "Import an existing project"
   - Choose "GitHub" as your Git provider
   - Authorize Netlify to access your GitHub account if prompted

3. **Select Repository**:
   - Find and select `JacobThielNUVIEW/nuview-strategic-pipeline`
   - Click to configure

4. **Configure Build Settings**:
   - **Branch to deploy**: `main`
   - **Build command**: (leave empty - static site)
   - **Publish directory**: `.` (root directory)
   - Click "Deploy site"

### Step 2: Domain Configuration

The site is configured to use the Netlify subdomain:

**Primary Domain**: `salesnuviewspace.netlify.app`

This domain:
- Is automatically provisioned by Netlify
- Has HTTPS enabled via Netlify's SSL certificate
- Updates automatically on every push to main branch
- Requires no additional DNS configuration

**Alternative Access**: The site is also available via GitHub Pages at `jacobthielnuview.github.io/nuview-strategic-pipeline`

### Step 3: Configure Environment Variables

1. **Go to Site Settings** → **Environment variables**
2. **Add the following variables**:
   - `NUVIEW_SCRAPE_TOKEN`: Your secure token for triggering scrapes
   - Any other secrets your workflows need

## Automated Deployments

### How It Works

1. **On Every Push to Main**:
   - Netlify automatically detects the push
   - Deploys the entire repository (static files)
   - Updates the live site within 30-60 seconds

2. **Deploy Previews**:
   - Pull requests automatically get preview URLs
   - Test changes before merging to main
   - Preview URLs are in the format: `deploy-preview-[pr-number]--your-site.netlify.app`

3. **Branch Deploys**:
   - Configure specific branches for automatic deployment
   - Useful for staging environments

### Deployment Triggers

The site will automatically deploy when:
- Code is pushed to the main branch
- Data files are updated (via daily scrape workflow)
- Manual deployment is triggered from Netlify dashboard

## Configuration Files

### netlify.toml

The `netlify.toml` file in the repository root configures:
- Build settings
- Redirect rules for clean URLs
- Security headers (CSP, X-Frame-Options, etc.)
- Cache control policies
- Asset optimization (minification, compression)

### _redirects

The `_redirects` file provides fallback redirect rules:
- Root redirects to dashboard
- Clean URL shortcuts for common pages
- Legacy URL redirects

## Integration with GitHub Actions

Your existing GitHub Actions workflows continue to work alongside Netlify:

### Daily Ops Workflow
- Scrapes data at 3 AM UTC
- Validates and pushes to main branch
- **Triggers automatic Netlify deployment**

### Backup Workflow
- Creates daily backups
- Pushes to repository
- Netlify ignores backup files (no redeploy needed)

### Deploy Pages Workflow (GitHub Pages)
- Can run in parallel with Netlify
- Useful for redundancy
- Or disable if only using Netlify

## Performance Optimizations

### Enabled by Default

1. **Asset Compression**:
   - Brotli and gzip compression for all text files
   - Automatic image optimization

2. **Caching**:
   - Static assets: 1 year cache
   - HTML files: revalidate on every request
   - Data JSON files: 5-minute cache with revalidation

3. **CDN**:
   - Global CDN for fast worldwide access
   - Edge caching reduces latency

4. **Security Headers**:
   - Content Security Policy (CSP)
   - XSS Protection
   - Frame Options
   - HTTPS enforcement

## Monitoring and Analytics

### Built-in Netlify Analytics

1. **Go to Site** → **Analytics**
2. View:
   - Page views
   - Unique visitors
   - Top pages
   - Traffic sources
   - Bandwidth usage

### Deploy Notifications

Configure notifications for:
- Successful deployments
- Failed deployments
- Deploy previews ready

**Setup**:
1. Go to **Site Settings** → **Build & deploy** → **Deploy notifications**
2. Add notifications via:
   - Email
   - Slack
   - Webhook
   - GitHub commit status

## Troubleshooting

### Common Issues

#### 1. Site Not Deploying

**Check**:
- Build logs in Netlify dashboard
- Ensure main branch is being monitored
- Verify no build errors in logs

**Fix**:
- Trigger manual deploy from Netlify dashboard
- Check GitHub webhook is active

#### 2. 404 Errors

**Check**:
- Redirects in `netlify.toml` and `_redirects`
- Publish directory is set to `.` (root)

**Fix**:
- Verify file paths are correct
- Check redirect syntax

#### 3. Assets Not Loading

**Check**:
- Browser console for CSP errors
- Network tab for 404s
- Asset paths in HTML files

**Fix**:
- Update CSP in netlify.toml if needed
- Verify relative paths in HTML

#### 4. Custom Domain Not Working

**Check**:
- DNS propagation (can take up to 48 hours)
- DNS records match Netlify requirements
- HTTPS provisioning status

**Fix**:
- Use `dig` or online DNS tools to verify
- Renew SSL certificate in Netlify if needed

## Manual Deployment

To deploy manually:

1. **Via Netlify Dashboard**:
   - Go to **Deploys**
   - Click **Trigger deploy** → **Deploy site**

2. **Via Netlify CLI**:
   ```bash
   npm install -g netlify-cli
   netlify login
   netlify deploy --prod
   ```

## Rollback

To rollback to a previous version:

1. Go to **Deploys** in Netlify dashboard
2. Find the deploy you want to restore
3. Click **...** → **Publish deploy**
4. Confirm the rollback

## Security Best Practices

1. **Never commit secrets** to the repository
2. **Use environment variables** for sensitive data
3. **Enable branch protection** on main branch
4. **Review deploy previews** before merging PRs
5. **Monitor deploy logs** for suspicious activity
6. **Regularly update dependencies** (though this is a static site)

## Cost Considerations

### Free Tier Includes:
- 100 GB bandwidth/month
- Unlimited sites
- HTTPS included
- Deploy previews
- Basic analytics

### Paid Tiers:
- Increased bandwidth (starting at $19/mo for 400 GB)
- Advanced analytics
- Team collaboration features
- Priority support

**Note**: For NUVIEW's use case, the free tier should be more than sufficient.

## Maintenance

### Monthly Tasks
- [ ] Review Netlify analytics
- [ ] Check deploy success rate
- [ ] Verify automated workflows still triggering deploys
- [ ] Review bandwidth usage

### Quarterly Tasks
- [ ] Review and update security headers
- [ ] Test all redirect rules
- [ ] Verify custom domain SSL certificate
- [ ] Review performance metrics

## Support

### Netlify Resources
- Documentation: [https://docs.netlify.com](https://docs.netlify.com)
- Community Forum: [https://answers.netlify.com](https://answers.netlify.com)
- Status Page: [https://www.netlifystatus.com](https://www.netlifystatus.com)

### NUVIEW Internal Support
- Create GitHub issue in this repository
- Contact the development team
- Review workflow logs in GitHub Actions

## Comparison: Netlify vs GitHub Pages

| Feature | Netlify | GitHub Pages |
|---------|---------|--------------|
| **Custom Domain** | ✅ Full support | ✅ Limited support |
| **HTTPS** | ✅ Auto SSL | ✅ Auto SSL |
| **Build Time** | ⚡ 30-60 seconds | 🐌 1-5 minutes |
| **CDN** | ✅ Global | ✅ Limited |
| **Redirects** | ✅ Advanced | ❌ Limited |
| **Headers** | ✅ Full control | ❌ No control |
| **Preview Deploys** | ✅ Yes | ❌ No |
| **Analytics** | ✅ Built-in | ❌ Separate tool |
| **Cost** | 💰 Free tier ample | 💰 Free |

## Conclusion

Netlify provides a robust, fast, and feature-rich platform for deploying the NUVIEW Strategic Pipeline. The automated deployment from the main branch ensures that every data update and code change is immediately reflected on the live site.

For questions or issues, please create an issue in the repository or contact the development team.

---

**Last Updated**: November 2024  
**Version**: 1.0  
**Maintained by**: NUVIEW Team
