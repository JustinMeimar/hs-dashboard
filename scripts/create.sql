DROP TABLE IF EXISTS logs;

CREATE TABLE logs (
    ip VARCHAR(255),
    datetime TIMESTAMP WITHOUT TIME ZONE,
    request_method VARCHAR(50),
    path TEXT,
    status INTEGER,
    size INTEGER,
    referrer TEXT,
    user_agent TEXT,
    PRIMARY KEY (ip, datetime) 
);