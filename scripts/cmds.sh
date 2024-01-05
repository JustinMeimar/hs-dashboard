sudo -i -u postgres

psql -U postgres -d nginx_logs


(env) ➜  logs psql -U justin -d nginx_logs


\c nginx_logs   # connect to database

\dt             # list tables

\d logs         # list schema 

\l              # list databases

\du             # list users
