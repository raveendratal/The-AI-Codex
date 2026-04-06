# Cluster Sizing Guide

## Workload-Based Recommendations

| Workload Type | Instance Type | Workers | Autoscale |
|---------------|---------------|---------|----------|
| Interactive / EDA | Memory-optimized (r5) | 2-4 | Yes |
| ETL / Batch | Compute-optimized (c5) | 4-16 | Yes |
| ML Training | GPU (p3/g4) | 2-8 | Yes |
| Streaming | General purpose (m5) | 2-8 | Yes |
| Ad-hoc SQL | Serverless SQL Warehouse | N/A | Auto |

## Spot Instance Strategy
- Use Spot for workers (up to 90% savings)
- Keep driver on On-Demand
- Set fallback to On-Demand for time-critical jobs
- Use diversified instance pools

## SQL Warehouse Sizing
| Size | Cluster Count | Concurrent Queries | Use Case |
|------|---------------|--------------------|---------|
| 2X-Small | 1 | 10 | Dev / Testing |
| Small | 1 | 10 | Light BI |
| Medium | 1 | 10 | Production BI |
| Large | 1-3 | 30 | Heavy analytics |

## Auto-Termination Settings
- Interactive clusters: 30-60 min
- Job clusters: terminate after job
- SQL warehouses: 10-15 min

## Monthly Cost Estimation Formula
```
Monthly Cost = (DBU Price × DBUs/hour × Hours/day × Days/month × Workers)
             + (EC2 Price × Hours/day × Days/month × Workers)
```
