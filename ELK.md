# ELK Stack Overview

## ELK Component(s)
- Elastic Search
- Kibana
- ES Fleet Server

## Setup Guide
- Elastic Cloud
- Elastic On-prem

### Elastic Search

**Download:**

```bash
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-[CURRENTVERSION]-linux-x86_64.tar.gz
tar -xzf elasticsearch-[CURRENTVERSION]-linux-x86_64.tar.gz
cd elasticsearch-[CURRENTVERSION]/
```

**Start Elastic Search:**

```bash
./bin/elasticsearch
```

**Enrollment Output:**

```
✅ Elasticsearch security features have been automatically configured!
✅ Authentication is enabled and cluster connections are encrypted.

ℹ️  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  <YOUR ELASTIC PW>

ℹ️  HTTP CA certificate SHA-256 fingerprint:
  <YOUR CERT HASH>

ℹ️  Configure Kibana to use this cluster:
• Run Kibana and click the configuration link in the terminal when Kibana starts.
• Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  <YOUR ENROLLMENT TOKEN>

ℹ️  Configure other nodes to join this cluster:
• On this node:
  ⁃ Create an enrollment token with `bin/elasticsearch-create-enrollment-token -s node`.
  ⁃ Uncomment the transport.host setting at the end of config/elasticsearch.yml.
  ⁃ Restart Elasticsearch.
• On other nodes:
  ⁃ Start Elasticsearch with `bin/elasticsearch --enrollment-token <token>`, using the enrollment token that you generated.
```

### Kibana

**Download:**
```bash
curl -O https://artifacts.elastic.co/downloads/kibana/kibana-[CURRENTVERSION]-linux-x86_64.tar.gz
tar -xzf kibana-[CURRENTVERSION]-linux-x86_64.tar.gz
cd kibana-[CURRENTVERSION]/
```

**Startup:**

```bash
./bin/kibana
```

Modify `kibana.yml`:
```
server.host "localhost" => server.host "MachineIP"
```
#### Enable Security
**Kibana Encryption Keys**

```bash
./bin/kibana-encryption-keys generate
```

**Keys**
- Add these to `kibana-[CURRENTVERSION]/config/kibama.yml` at the bottom.
```yml
xpack.encryptedSavedObjects.encryptionKey: <YOURKEY>
xpack.reporting.encryptionKey: <YOURKEY>
xpack.security.encryptionKey: <YOURKEY>
```

**This guide does not include the steps to implement enterprise self-sign certificates. That process can be found on elastics site, as well a more detailed installation guide [here.](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)**

## Fleet Server

Fleet requires another server independent of the rest of the ELK stack, assuming ELK is not being ran in a cluster. The Fleet server will communicate with the ELK stack via `https://<FLEETIP>:8220`, in this implementation we are using the default self-signed certificate generated from the fleet server installer.

- Visit: http://<ELKIP>:5601/app/fleet/settings
  - Click `Add Fleet Server`
  - Fleet Server Hosts `Add new Fleet Server Hosts`
    - This option may not be given instead it will just present a Name and URL field.
  - Name - Whatever name you want to give the fleet server `ELK-Fleet01`
  - URL - `https://<FLEETIP>:8220`
  - Click continue, you will then be given the command to download and install the elastic agent on the fleet server. Once complete and the connection has been confirmed the server will populate under the agents section assigned the default fleet policy containing the `Fleet Server` integration, this policy must contain that integration otherwise the service will stop working properly and require manual removal.

**Manual Removal** - 
```bash
# Reset agent policy
curl -u 'USER:PASSWORD' --request POST \
  --url http://ELKIP:5601/internal/fleet/reset_preconfigured_agent_policies/policy-elastic-agent-on-cloud \
  --header 'content-type: application/json' \
  --header 'kbn-xsrf: xyz' \
  --header 'elastic-api-version: 1'

# Manually unenroll elastic agent from ELK.
curl -u 'USER:PASWORD' --request POST \
  --url http://ELKIP:5601/api/fleet/agents/AGENTID/unenroll \
  --header 'content-type: application/json' \
  --header 'kbn-xsrf: xx' \
  --data-raw '{"force":true,"revoke":true}' \
  --compressed
```

[Elastic Agents are stuck in Updating or Offline](https://www.elastic.co/guide/en/fleet/current/fleet-troubleshooting.html#agents-in-cloud-stuck-at-updating)


## Integrations
- AlienVaultOTX
- MISP Threat Sharing
- OpenCTI
  - Abuseipdb
  - GreyNoise
  - Virustotal
  - 
## Testing

