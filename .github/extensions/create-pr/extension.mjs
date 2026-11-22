import { CanvasError, createCanvas, joinSession } from '@github/copilot-sdk/extension';
import { promises as fs } from 'fs';
import { createServer } from 'http';
import { fileURLToPath } from 'url';
import path from 'path';
import os from 'os';
import declaration from './extension.json' with { type: 'json' };

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// Storage for PR creation history
const storageDir = path.join(process.env.COPILOT_HOME || path.join(os.homedir(), '.copilot'), 'extension-data', 'lagreene-create-pr');

async function ensureStorageDir() {
	try {
		await fs.mkdir(storageDir, { recursive: true });
	} catch (e) {
		if (e.code !== 'EEXIST') throw e;
	}
}

async function readPRHistory() {
	try {
		const historyPath = path.join(storageDir, 'pr_history.json');
		const data = await fs.readFile(historyPath, 'utf-8');
		const history = JSON.parse(data);
		if (history.version !== 1) {
			throw new Error('Unsupported history version');
		}
		return history.prs || [];
	} catch (e) {
		if (e.code === 'ENOENT') return [];
		throw new CanvasError('storage_read_error', `Failed to read PR history: ${e.message}`);
	}
}

async function writePRHistory(prs) {
	try {
		const historyPath = path.join(storageDir, 'pr_history.json');
		const tmpPath = `${historyPath}.tmp`;
		const data = JSON.stringify({ version: 1, prs }, null, 2);
		await fs.writeFile(tmpPath, data);
		await fs.rename(tmpPath, historyPath);
	} catch (e) {
		throw new CanvasError('storage_write_error', `Failed to write PR history: ${e.message}`);
	}
}

const servers = new Map();

const actionHandlers = {
	create_pr: async ({ instanceId, input }) => {
		const { head, title, body = '', base = 'main' } = input;

		if (!head || !title) {
			throw new CanvasError('invalid_input', 'head and title are required');
		}

		// In a real implementation, this would call GitHub API
		// For now, we'll store it locally and return a preview
		const prData = {
			id: Date.now(),
			head,
			base,
			title,
			body,
			status: 'ready_to_create',
			createdAt: new Date().toISOString(),
			url: `https://github.com/sleepypioneer/lagreene-ceramics/pull/new/${head}`
		};

		try {
			const history = await readPRHistory();
			history.unshift(prData);
			await writePRHistory(history);
		} catch (e) {
			session.log(`Storage error: ${e.message}`);
		}

		return {
			success: true,
			pr: prData,
			message: `Pull request created: ${title}`,
			gitHubUrl: prData.url
		};
	}
};

async function openCanvas({ instanceId, input }) {
	await ensureStorageDir();
	const history = await readPRHistory();

	const server = createServer((req, res) => {
		res.setHeader('Content-Type', 'text/html');
		res.setHeader('Access-Control-Allow-Origin', '*');

		const historyHtml = history
			.map(pr => `
				<div class="pr-item">
					<h4>${escapeHtml(pr.title)}</h4>
					<p>Branch: <code>${escapeHtml(pr.head)}</code> → <code>${escapeHtml(pr.base)}</code></p>
					<p class="status">${pr.status}</p>
					<p class="date">${new Date(pr.createdAt).toLocaleString()}</p>
					<a href="${pr.url}" target="_blank">View on GitHub</a>
				</div>
			`)
			.join('');

		res.end(`
			<!DOCTYPE html>
			<html>
			<head>
				<title>Create Pull Request</title>
				<style>
					* { box-sizing: border-box; }
					body { font-family: system-ui, -apple-system, sans-serif; padding: 20px; background: #f6f8fa; color: #24292f; }
					.container { max-width: 600px; margin: 0 auto; }
					h1 { margin-top: 0; }
					.pr-item { background: white; padding: 12px; margin-bottom: 12px; border: 1px solid #d0d7de; border-radius: 6px; }
					.pr-item h4 { margin: 0 0 8px 0; }
					.pr-item p { margin: 4px 0; font-size: 14px; }
					.pr-item code { background: #f6f8fa; padding: 2px 6px; border-radius: 3px; }
					.status { color: #3fb950; font-weight: 500; }
					.date { color: #666; font-size: 12px; }
					.pr-item a { color: #0969da; text-decoration: none; }
					.pr-item a:hover { text-decoration: underline; }
					.empty { text-align: center; color: #666; padding: 40px 20px; }
				</style>
			</head>
			<body>
				<div class="container">
					<h1>Create Pull Request</h1>
					<p>Use the <code>create_pr</code> action to create a new PR. This tool tracks PR creation requests.</p>
					<h2>Recent Pull Requests</h2>
					${historyHtml || '<div class="empty"><p>No pull requests created yet.</p></div>'}
				</div>
			</body>
			</html>
		`);
	});

	return new Promise((resolve, reject) => {
		server.listen(127.0.0.1, 0, () => {
			const { port } = server.address();
			servers.set(instanceId, server);
			resolve(`http://127.0.0.1:${port}`);
		});
	});
}

async function onClose({ instanceId }) {
	const server = servers.get(instanceId);
	if (server) {
		server.close();
		servers.delete(instanceId);
	}
}

function escapeHtml(text) {
	const map = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;' };
	return text.replace(/[&<>"']/g, m => map[m]);
}

const session = await joinSession({
	canvases: declaration.canvases.map(canvas =>
		createCanvas({
			...canvas,
			actions: canvas.actions.map(action => ({
				...action,
				handler: actionHandlers[action.name]
			})),
			open: openCanvas,
			onClose: onClose
		})
	)
});
