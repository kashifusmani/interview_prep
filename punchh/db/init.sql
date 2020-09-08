CREATE TABLE IF NOT EXISTS email_campaigns (
  id SERIAL PRIMARY KEY,
  business_id INT NOT NULL,
  campaign_date DATE NOT NULL,
  email VARCHAR NOT NULL,
  event VARCHAR NOT NULL,
  campaign_name VARCHAR NOT NULL,
  sg_event_id VARCHAR NOT NULL,
  sg_message_id VARCHAR NOT NULL,
  email_timestamp TIMESTAMP NOT NULL
)
