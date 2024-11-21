
# Configure a Bitbucket Webhook to Trigger a FOSSA CLI Scan

This guide walks you through the steps to configure a Bitbucket webhook that triggers a FOSSA CLI scan on specific events like pull requests or pushes.

---

## **Step 1: Set Up the FOSSA CLI in Your Environment**
1. **Install the FOSSA CLI**:
   - Download the CLI from the [FOSSA GitHub repository](https://github.com/fossas/fossa-cli).
   - Ensure the `FOSSA_API_KEY` environment variable is set with your FOSSA API key.

   ```bash
   export FOSSA_API_KEY=<your_fossa_api_key>
   ```

2. **Test the CLI**:
   Run the following command in your local repository to ensure it works:
   ```bash
   fossa analyze
   ```

---

## **Step 2: Set Up a Webhook in Bitbucket**
1. Navigate to your repository in Bitbucket.
2. Go to **Repository Settings** > **Webhooks**.
3. Click **Add webhook**.
4. Fill in the webhook details:
   - **Title**: `FOSSA CLI Trigger`
   - **URL**: The endpoint of your webhook listener (e.g., CI/CD service or custom server).
   - **Events**: Choose events such as:
     - `Pull request created`
     - `Pull request updated`
     - `Push`
5. Save the webhook.

---

## **Step 3: Create a Webhook Listener**
You need a listener to process webhook events and trigger the FOSSA CLI scan.

### Example: Node.js Listener
Create a simple Node.js server to handle the webhook:

```javascript
const express = require('express');
const { exec } = require('child_process');
const app = express();

app.use(express.json());

app.post('/webhook', (req, res) => {
    console.log('Webhook received:', req.body);

    // Trigger FOSSA CLI scan
    exec('fossa analyze', (error, stdout, stderr) => {
        if (error) {
            console.error(\`Error executing FOSSA CLI: \${error.message}\`);
            res.status(500).send('FOSSA scan failed.');
            return;
        }
        console.log(\`FOSSA output: \${stdout}\`);
        console.error(\`FOSSA errors: \${stderr}\`);
        res.status(200).send('FOSSA scan completed.');
    });
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(\`Webhook listener running on port \${PORT}\`);
});
```

1. Save this script as `webhook.js`.
2. Run it using `node webhook.js`.
3. Expose it to the internet using tools like [ngrok](https://ngrok.com/).

---

## **Step 4: Secure the Webhook**
1. Add a secret token to the webhook in Bitbucket.
2. Validate the token in your listener:

   ```javascript
   const SECRET_TOKEN = 'your-secret-token';

   app.post('/webhook', (req, res) => {
       const token = req.headers['x-event-key']; // Replace with appropriate Bitbucket header
       if (token !== SECRET_TOKEN) {
           return res.status(403).send('Forbidden: Invalid token');
       }

       // Proceed with FOSSA CLI trigger
   });
   ```

---

## **Step 5: Automate in CI/CD**
You can use a CI/CD system like Jenkins or GitHub Actions to listen for webhook events and trigger the FOSSA CLI scan.

### Example with Jenkins
1. Configure Jenkins to trigger on the webhook event.
2. Add a pipeline step to execute `fossa analyze`.

---

## **Step 6: Test the Webhook**
1. Trigger an event in Bitbucket (e.g., create a pull request).
2. Verify the webhook listener receives the event and executes the `fossa analyze` command.

---

This setup will automate FOSSA CLI scans for your repository, ensuring up-to-date analysis on every pull request or push event.
