# Delta Sharing Quick Reference

## Sharing Checklist
- [ ] Identify tables to share
- [ ] Define partition filters (if applicable)
- [ ] Create share object
- [ ] Add tables with appropriate options
- [ ] Create recipient
- [ ] Grant access
- [ ] Share activation link (open sharing)
- [ ] Document in governance registry

## Share Management Commands
```sql
-- List all shares
SHOW SHARES;

-- Describe share contents
DESCRIBE SHARE sales_share;

-- Remove table from share
ALTER SHARE sales_share REMOVE TABLE main.gold.sales;

-- Drop share
DROP SHARE sales_share;

-- Revoke access
REVOKE SELECT ON SHARE sales_share FROM RECIPIENT partner;

-- Drop recipient
DROP RECIPIENT external_partner;
```

## Monitoring Shared Data
```sql
-- Check recipient access status
SELECT * FROM system.access.audit
WHERE action_name LIKE '%share%'
  AND event_time >= current_date() - INTERVAL 7 DAY;
```

## Security Considerations
- Shares are read-only for recipients
- Recipients cannot modify source data
- Activation links expire (configurable)
- IP access lists can restrict recipient access
- All access is logged in audit tables
