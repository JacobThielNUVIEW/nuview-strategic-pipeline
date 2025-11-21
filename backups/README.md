# Automated Backups

This directory contains automated backups of the data files from the NUVIEW Strategic Pipeline.

## Backup Schedule

- Backups run daily at 4:00 AM UTC
- Retention period: 30 days
- Automatic cleanup of old backups

## Backup Contents

Each backup archive contains:
- `data/opportunities.json` - Scraped opportunities
- `data/forecast.json` - Market forecast data
- `data/processed/` - Processed data files
- `backup_metadata.json` - Backup metadata (date, git commit, etc.)

## File Naming Convention

Backups are named: `YYYY-MM-DD.tar.gz`

Example: `2024-11-20.tar.gz`

## Restoring from Backup

To restore data from a backup:

```bash
# Extract the backup archive
tar -xzf backups/2024-11-20.tar.gz -C /tmp/

# Copy files back to data directory
cp -r /tmp/2024-11-20/data/* data/
```

## Manual Backup

To create a manual backup:

```bash
# Trigger the backup workflow
gh workflow run backup.yml
```

Or go to: https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline/actions/workflows/backup.yml

## Backup Verification

Backups are automatically verified after creation to ensure integrity. Check the workflow logs for verification results.

---

**Note**: Backups are stored in the repository to ensure they're version-controlled and accessible. Large repositories may need to consider external backup storage.
