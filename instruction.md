Analyze the Apache-style access log at `/app/access.log` and write the result to
`/app/report.json`.

Success criteria:

1. `/app/report.json` is a valid JSON object containing exactly these keys:
   `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the integer count of nonblank log entries. For the
   provided log, it must be `6`.
3. `unique_ips` is the integer count of distinct client IP addresses from the
   first token of each log entry. For the provided log, it must be `3`.
4. `top_path` is the most frequently requested path from the quoted HTTP request
   field. For the provided log, it must be `"/index.html"`.
