# Cursor GitHub Access Token Setup

**Date**: 2025-01-24  
**Issue**: Access Denied - No GitHub access token found with access to repository `mlesnews/lumina-ai`  
**Solution**: Create and configure GitHub Personal Access Token (PAT)

---

## Problem

Cursor Cloud Agents feature requires GitHub access to clone repositories. You're seeing:
```
Access Denied: No GitHub access token found with access to repository mlesnews/lumina-ai
```

---

## Solution: Create GitHub Personal Access Token

### Step 1: Create GitHub Personal Access Token (PAT)

1. Go to [GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)](https://github.com/settings/tokens?type=beta)
   - Or: GitHub → Your Profile → Settings → Developer settings → Personal access tokens → Tokens (classic)

2. Click **Generate new token** → **Generate new token (classic)**

3. Configure the token:
   - **Note**: `Cursor Cloud Agents - lumina-ai`
   - **Expiration**: Choose expiration (90 days, 1 year, or no expiration)
   - **Scopes**: Select the following permissions:
     - ✅ **repo** (Full control of private repositories)
       - This includes: `repo:status`, `repo_deployment`, `public_repo`, `repo:invite`, `security_events`
     - ✅ **read:org** (Read org and team membership, read org projects) - *Optional but recommended*
     - ✅ **read:user** (Read user profile data) - *Optional but recommended*

4. Click **Generate token**

5. **⚠️ IMPORTANT**: Copy the token immediately - you won't be able to see it again!
   - The token will look like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

### Step 2: Add Token to Cursor Settings

1. Open **Cursor Settings** (File → Preferences → Settings, or `Ctrl+,`)

2. Search for "GitHub" or navigate to **Personal Configuration → GitHub Access**

3. Enter your GitHub Personal Access Token in the token field

4. Click **Save** or **Apply**

5. Click **Refresh** or restart Cursor to test the connection

---

### Step 3: Verify Access

1. In Cursor Settings → Personal Configuration → GitHub Access
2. The error should disappear
3. You should see your GitHub username or repository access confirmed

---

## Alternative: Store Token Securely in Azure Key Vault

### Store Token in Key Vault:

```powershell
az keyvault secret set `
    --vault-name jarvis-lumina `
    --name github-personal-access-token `
    --value "ghp_YOUR_TOKEN_HERE"
```

### Retrieve Token (if needed):

```powershell
az keyvault secret show `
    --vault-name jarvis-lumina `
    --name github-personal-access-token `
    --query "value" -o tsv
```

**Note**: Cursor may not directly read from Key Vault, but you can:
1. Retrieve the token from Key Vault
2. Copy it
3. Paste into Cursor Settings

---

## Token Permissions Explained

### Required Permission: `repo`

The `repo` scope provides:
- ✅ Read/write access to code, commit statuses, repository projects, collaborators
- ✅ Read/write access to organization membership, and organization projects
- ✅ Read/write access to repository hooks

This is sufficient for Cursor Cloud Agents to:
- Clone your repository (`mlesnews/lumina-ai`)
- Access repository contents
- Create branches/commits (if needed)

### Optional Permissions:

- **read:org**: Read organization membership (if your repo is in an org)
- **read:user**: Read your GitHub profile information

---

## Security Best Practices

1. **Use Fine-Grained Tokens (if available)**:
   - GitHub now supports fine-grained personal access tokens
   - Can restrict to specific repositories
   - More secure than classic tokens

2. **Set Expiration**:
   - Don't create tokens with no expiration
   - Use 90 days or 1 year, then rotate

3. **Use Minimum Required Permissions**:
   - Only grant `repo` scope (required)
   - Avoid granting unnecessary scopes

4. **Rotate Tokens Regularly**:
   - Create new token before old one expires
   - Update in Cursor settings
   - Revoke old token

5. **Never Commit Tokens**:
   - Never commit tokens to version control
   - Use environment variables or secure storage
   - Use Azure Key Vault for storage

6. **Monitor Token Usage**:
   - Check GitHub Settings → Developer settings → Personal access tokens
   - Review "Last used" dates
   - Revoke unused tokens

---

## Troubleshooting

### Issue: Token still shows "Access Denied"

**Solutions**:
1. Verify the token hasn't expired
2. Check that `repo` scope is selected
3. Verify the token has access to the specific repository (`mlesnews/lumina-ai`)
4. If repository is private, ensure token has `repo` scope
5. Try generating a new token and re-entering it

### Issue: "Repository not found"

**Solutions**:
1. Verify repository name is correct: `mlesnews/lumina-ai`
2. Check repository exists and is accessible
3. If private repo, ensure token has `repo` scope
4. Verify your GitHub username is `mlesnews`

### Issue: Token works but expires

**Solutions**:
1. Create a new token before expiration
2. Update token in Cursor Settings
3. Consider using fine-grained token with longer expiration
4. Set calendar reminder to rotate token

### Issue: "Invalid token format"

**Solutions**:
1. Ensure you copied the entire token (starts with `ghp_`)
2. Don't include extra spaces or newlines
3. Paste token directly (don't edit it)
4. Try copying token again from GitHub

---

## Fine-Grained Token Alternative (Recommended)

If available, use Fine-Grained Personal Access Tokens for better security:

1. Go to [GitHub Settings → Developer settings → Personal access tokens → Fine-grained tokens](https://github.com/settings/tokens?type=beta)

2. Click **Generate new token**

3. Configure:
   - **Token name**: `Cursor Cloud Agents`
   - **Expiration**: Set appropriate expiration
   - **Repository access**: Select "Only select repositories" → Choose `mlesnews/lumina-ai`
   - **Repository permissions**:
     - Contents: Read and write
     - Metadata: Read-only
     - Pull requests: Read and write (if needed)

4. Generate and copy token

5. Add to Cursor Settings (same as classic token)

---

## Environment Variables (Alternative Method)

Some applications can read from environment variables. If Cursor supports this:

**Windows PowerShell:**
```powershell
$env:GITHUB_TOKEN = "ghp_YOUR_TOKEN_HERE"
```

**Linux/Mac:**
```bash
export GITHUB_TOKEN="ghp_YOUR_TOKEN_HERE"
```

Then restart Cursor. (Note: This may not be supported by Cursor - check Cursor documentation)

---

## Repository Access Verification

To verify your token has access to the repository:

### Using GitHub CLI (if installed):

```bash
gh auth login --with-token < token.txt
gh repo view mlesnews/lumina-ai
```

### Using curl:

```bash
curl -H "Authorization: token ghp_YOUR_TOKEN" https://api.github.com/repos/mlesnews/lumina-ai
```

Should return repository information if token is valid.

---

## Quick Reference

### Token Creation URL:
https://github.com/settings/tokens/new

### Required Scopes:
- ✅ **repo** (Full control of private repositories)

### Token Format:
`ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

### Repository:
`mlesnews/lumina-ai`

### Cursor Settings Location:
Settings → Personal Configuration → GitHub Access

---

## References

- **GitHub Token Settings**: https://github.com/settings/tokens
- **GitHub Token Docs**: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
- **Cursor Docs**: https://cursor.com/docs
- **Repository**: https://github.com/mlesnews/lumina-ai

---

**Last Updated**: 2025-01-24  
**Maintained By**: @JARVIS @MARVIN