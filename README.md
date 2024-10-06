# Requirements
## Environment variable named **dynatrace_dsn**
Example: Driver={ODBC Driver 17 for SQL Server};Server=tcp:**yourserver**.database.windows.net,1433;Database=**yourdatabase**;Uid=yourlogin;Pwd=**yourpassword**;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;
## Table "ram_monitoring" 
```sql
CREATE TABLE ram_monitoring (
    created_at DATETIME,
    total_memory DECIMAL(10,2),
    available_memory DECIMAL(10,2),
    used_memory DECIMAL(10,2),
    memory_percentage DECIMAL(10,2)
);
```
## ODBC Driver 17 for SQL Server
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16#download-for-windows